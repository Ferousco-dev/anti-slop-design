"""
Build and render the anti-slop explainer, headless in Blender.

    blender -b -P video/scene.py -- --frames 300 --out video/out

Approach: flat 2D motion graphics, not 3D. Everything is a plane with an
emission shader under an orthographic camera, so there is no lighting to
fight, no shadows to denoise, and the render is fast and dead flat —
which is what the reference image is.

Matches the poster art: purple slop on the left, a gate, a clean orange
system on the right.
"""

import argparse
import math
import random
import sys

import bpy
from mathutils import Vector

# ----------------------------------------------------------------- config

W, H = 1080, 1920          # vertical, for TikTok
FPS = 30
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def srgb(*hexes):
    """sRGB hex -> linear. Emission inputs are linear, so authoring sRGB
    directly washes everything out; near-black arrives as mid-grey."""
    def chan(c):
        c /= 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    out = [tuple(chan(int(h.lstrip("#")[i:i + 2], 16)) for i in (0, 2, 4)) for h in hexes]
    return out[0] if len(out) == 1 else out


PURPLE = srgb("#8f56ff")
PURPLE_D = srgb("#6028cc")
ORANGE = srgb("#ff7327")
INK = srgb("#14141a")
PAPER = srgb("#ffffff")
GREY = srgb("#e9e9ee")

random.seed(7)  # deterministic: same render every run


# ------------------------------------------------------------- utilities


def wipe():
    bpy.ops.wm.read_factory_settings(use_empty=True)


def flat_material(name, rgb, alpha=1.0):
    """Emission-only material. No lighting model, so colour is exact."""
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    mat.blend_method = "BLEND"
    nt = mat.node_tree
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emit = nt.nodes.new("ShaderNodeEmission")
    emit.inputs["Color"].default_value = (*rgb, 1.0)
    emit.inputs["Strength"].default_value = 1.0
    if alpha >= 1.0:
        nt.links.new(emit.outputs["Emission"], out.inputs["Surface"])
    else:
        mix = nt.nodes.new("ShaderNodeMixShader")
        trans = nt.nodes.new("ShaderNodeBsdfTransparent")
        mix.inputs["Fac"].default_value = alpha
        nt.links.new(trans.outputs["BSDF"], mix.inputs[1])
        nt.links.new(emit.outputs["Emission"], mix.inputs[2])
        nt.links.new(mix.outputs["Shader"], out.inputs["Surface"])
    return mat


def rect(name, x, y, w, h, mat, z=0.0, radius=0.0):
    """A rounded rectangle as a plane. Radius via bevel modifier."""
    bpy.ops.mesh.primitive_plane_add(size=1, location=(x, y, z))
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = (w, h, 1)
    bpy.ops.object.transform_apply(scale=True)
    if radius > 0:
        bev = ob.modifiers.new("round", "BEVEL")
        bev.width = min(radius, w / 2, h / 2)
        bev.segments = 6
        bev.limit_method = "NONE"
    ob.data.materials.append(mat)
    return ob


def blob(name, x, y, r, mat, z=0.0):
    bpy.ops.mesh.primitive_circle_add(vertices=48, radius=r, fill_type="NGON",
                                      location=(x, y, z))
    ob = bpy.context.active_object
    ob.name = name
    ob.data.materials.append(mat)
    return ob


def key(ob, frame, loc=None, scale=None, rot=None):
    if loc is not None:
        ob.location = Vector(loc)
        ob.keyframe_insert("location", frame=frame)
    if scale is not None:
        s = (scale, scale, 1) if isinstance(scale, (int, float)) else scale
        ob.scale = s
        ob.keyframe_insert("scale", frame=frame)
    if rot is not None:
        ob.rotation_euler = (0, 0, rot)
        ob.keyframe_insert("rotation_euler", frame=frame)


def fcurves_of(ob):
    """Blender 4.4+ moved fcurves into slotted actions; 5.x removed
    Action.fcurves entirely. Handle both so this runs on either."""
    ad = getattr(ob, "animation_data", None)
    if not ad or not ad.action:
        return []
    act = ad.action
    if hasattr(act, "fcurves"):  # pre-4.4
        return list(act.fcurves)
    out = []
    slot = getattr(ad, "action_slot", None)
    for layer in act.layers:
        for strip in layer.strips:
            bag = strip.channelbag(slot) if slot else None
            if bag is None and getattr(strip, "channelbags", None):
                bag = strip.channelbags[0]
            if bag:
                out.extend(bag.fcurves)
    return out


def ease(ob, kind="EASE_OUT", back=False):
    for fc in fcurves_of(ob):
        for kp in fc.keyframe_points:
            kp.interpolation = "BACK" if back else "CUBIC"
            kp.easing = kind
            if back:
                kp.back = 1.2


def fade(ob, mat, f_in, f_out=None, hold=1.0):
    """Animate emission alpha via the material's mix factor."""
    nt = mat.node_tree
    mix = next((n for n in nt.nodes if n.type == "MIX_SHADER"), None)
    if mix is None:
        return
    inp = mix.inputs["Fac"]
    inp.default_value = 0.0
    inp.keyframe_insert("default_value", frame=f_in)
    inp.default_value = hold
    inp.keyframe_insert("default_value", frame=f_in + 8)
    if f_out:
        inp.keyframe_insert("default_value", frame=f_out)
        inp.default_value = 0.0
        inp.keyframe_insert("default_value", frame=f_out + 10)


def text(name, body, x, y, size, mat, align="CENTER", bold=True):
    bpy.ops.object.text_add(location=(x, y, 0.1))
    ob = bpy.context.active_object
    ob.name = name
    ob.data.body = body
    ob.data.size = size
    try:
        ob.data.font = bpy.data.fonts.load(FONT, check_existing=True)
    except Exception:
        pass  # fall back to Blender's built-in face
    ob.data.align_x = align
    ob.data.align_y = "CENTER"
    ob.data.extrude = 0
    ob.data.space_line = 0.85
    ob.data.materials.append(mat)
    return ob


# ---------------------------------------------------------------- scene


def build(total):
    wipe()
    scn = bpy.context.scene
    scn.render.resolution_x, scn.render.resolution_y = W, H
    scn.render.fps = FPS
    scn.frame_start, scn.frame_end = 1, total

    # Flat white world.
    world = bpy.data.worlds.new("w")
    scn.world = world
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)
    world.node_tree.nodes["Background"].inputs[1].default_value = 1.0

    bpy.ops.object.camera_add(location=(0, 0, 10))
    cam = bpy.context.active_object
    cam.data.type = "ORTHO"
    cam.data.sensor_fit = "VERTICAL"
    cam.data.ortho_scale = 11.5
    scn.camera = cam

    m_purple = flat_material("purple", PURPLE, 0.0)
    m_purple_d = flat_material("purple_d", PURPLE_D, 0.0)
    m_orange = flat_material("orange", ORANGE, 0.0)
    m_ink = flat_material("ink", INK, 0.0)
    m_grey = flat_material("grey", GREY, 0.0)
    m_ink_solid = flat_material("ink_s", INK)
    m_paper = flat_material("paper", PAPER, 0.0)
    m_ink_soft = flat_material("ink_soft", srgb("#c3c3cc"), 0.0)

    # ---- Act 1: the slop swarm ------------------------------------------
    # Purple cards and blobs crowding in from the left, overlapping,
    # arriving in a mess. This is the "every AI builds this" beat.
    slop = []
    for i in range(30):
        ang = random.uniform(0, math.tau)
        rad = random.uniform(0.3, 1.0) ** 0.6
        tx = math.cos(ang) * rad * 3.1
        # Clamped band: the headline owns the top, the payoff the bottom.
        ty = -0.35 + math.sin(ang) * rad * 2.6
        if random.random() < 0.4:
            ob = blob(f"blob{i}", tx, ty, random.uniform(0.35, 0.95),
                      m_purple if i % 2 else m_purple_d)
        else:
            w = random.uniform(0.7, 1.9)
            h = w * random.uniform(0.42, 0.78)
            m = m_purple if i % 2 else m_purple_d
            ob = rect(f"card{i}", tx, ty, w, h, m, radius=0.1)
            # Content lines, so it reads as an interface rather than a box.
            for r in range(random.randint(2, 3)):
                ln = rect(f"ln{i}_{r}", 0, h / 2 - 0.16 - r * 0.17,
                          w * random.uniform(0.32, 0.62), 0.055,
                          m_paper, z=0.02, radius=0.02)
                ln.parent = ob
        f = 6 + i * 2.2
        key(ob, f, loc=(tx - 7, ty, 0), scale=0.6)
        key(ob, f + 16, loc=(tx, ty, 0), scale=1.0)
        ease(ob, "EASE_OUT")
        slop.append(ob)

    fade(None, m_purple, 6, None, 0.92)
    fade(None, m_purple_d, 6, None, 0.92)
    fade(None, m_paper, 6, None, 0.55)

    hook = text("hook", "EVERY AI BUILDS\nTHE SAME SITE", 0, 3.9, 0.62, m_ink_solid)
    key(hook, 1, scale=0.0)
    key(hook, 2, scale=0.9)
    key(hook, 12, scale=1.0)
    ease(hook, "EASE_OUT", back=True)

    # ---- Act 2: the gate -------------------------------------------------
    gate_in = 78
    bars = []
    for i in range(9):
        x = -1.6 + i * 0.4
        b = rect(f"bar{i}", x, 0, 0.075, 2.6, m_ink_solid, z=0.3)
        key(b, 1, loc=(x, 9, 0.3))
        key(b, gate_in + i, loc=(x, 9, 0.3))
        key(b, gate_in + i + 12, loc=(x, 0, 0.3))
        ease(b, "EASE_OUT")
        bars.append(b)
    frame_l = rect("frame_l", -1.85, 0, 0.11, 2.9, m_ink_solid, z=0.3)
    frame_r = rect("frame_r", 1.85, 0, 0.11, 2.9, m_ink_solid, z=0.3)
    for b in (frame_l, frame_r):
        key(b, 1, loc=(b.location.x, 9, 0.3))
        key(b, gate_in, loc=(b.location.x, 9, 0.3))
        key(b, gate_in + 14, loc=(b.location.x, 0, 0.3))
        ease(b, "EASE_OUT")

    # Impact: the slop recoils off the gate.
    impact = gate_in + 16
    for ob in slop:
        base = ob.location.copy()
        key(ob, impact, loc=base)
        key(ob, impact + 7, loc=(base.x - 0.55, base.y, base.z))
        key(ob, impact + 26, loc=(base.x - 9, base.y * 1.3, base.z))
        ease(ob, "EASE_IN")

    fade(None, m_purple, 6, impact + 12, 0.92)
    fade(None, m_purple_d, 6, impact + 12, 0.92)
    fade(None, m_paper, 6, impact + 12, 0.55)

    key(hook, impact + 4, scale=1.0)
    key(hook, impact + 14, scale=0.0)
    ease(hook, "EASE_IN")

    # ---- Act 3: the clean system ----------------------------------------
    # Ordered cards, one accent colour, real hierarchy, arriving on a grid
    # instead of a pile.
    build_in = impact + 24
    clean = [
        (0.0, 1.85, 4.4, 1.0),
        (-1.5, 0.55, 1.32, 0.9), (0.0, 0.55, 1.32, 0.9), (1.5, 0.55, 1.32, 0.9),
        (-1.13, -0.78, 2.06, 0.9), (1.13, -0.78, 2.06, 0.9),
        (0.0, -2.05, 4.4, 1.0),
    ]
    for i, (x, y, w, h) in enumerate(clean):
        f = build_in + i * 4
        parts = [rect(f"clean{i}", x, y, w, h, m_grey, radius=0.09)]
        for r in range(2):
            parts.append(rect(
                f"cln{i}_{r}",
                x - w / 2 + 0.32 + w * (0.26 - r * 0.08),
                y + h / 2 - 0.28 - r * 0.20,
                w * (0.52 - r * 0.16), 0.07, m_ink_soft, z=0.04, radius=0.03))
        parts.append(rect(f"acc{i}", x - w / 2 + 0.53, y - h / 2 + 0.26,
                          0.42, 0.11, m_orange, z=0.05, radius=0.045))
        for part in parts:
            key(part, 1, scale=0.0)
            key(part, f - 1, scale=0.0)
            key(part, f, scale=0.9)
            key(part, f + 13, scale=1.0)
            ease(part, "EASE_OUT", back=True)

    fade(None, m_grey, build_in, None, 1.0)
    fade(None, m_ink_soft, build_in + 4, None, 1.0)
    fade(None, m_orange, build_in + 6, None, 1.0)

    payoff = text("payoff", "SO I WROTE A SKILL\nTHAT REFUSES TO", 0, -3.6, 0.55,
                  m_ink_solid)
    key(payoff, 1, scale=0.0)
    key(payoff, build_in + 17, scale=0.0)
    key(payoff, build_in + 18, scale=0.9)
    key(payoff, build_in + 30, scale=1.0)
    ease(payoff, "EASE_OUT", back=True)

    # Gate opens outward once the clean side has assembled.
    open_f = build_in + 34
    for i, b in enumerate(bars + [frame_l, frame_r]):
        key(b, open_f, loc=b.location)
        key(b, open_f + 18, loc=(b.location.x * 3.4, b.location.y, b.location.z))
        ease(b, "EASE_IN")

    return scn


# --------------------------------------------------------------- render


def render(scn, out, still=None):
    try:
        scn.render.engine = "BLENDER_EEVEE_NEXT"
    except TypeError:
        scn.render.engine = "BLENDER_EEVEE"
    scn.render.film_transparent = False
    # Flat graphics want no tone mapping at all.
    scn.view_settings.view_transform = "Standard"
    scn.view_settings.look = "None"
    scn.display_settings.display_device = "sRGB"
    if hasattr(scn, "eevee"):
        scn.eevee.taa_render_samples = 16

    if still:
        scn.frame_set(still)
        scn.render.image_settings.file_format = "PNG"
        scn.render.filepath = out
        bpy.ops.render.render(write_still=True)
        return

    # This build has no FFmpeg writer, and a PNG sequence is the more
    # reliable path regardless: frames survive a crash, and encoding is
    # a separate, repeatable step.
    scn.render.image_settings.file_format = "PNG"
    scn.render.image_settings.color_mode = "RGB"
    scn.render.image_settings.compression = 15
    scn.render.filepath = out
    bpy.ops.render.render(animation=True)


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    ap = argparse.ArgumentParser()
    ap.add_argument("--frames", type=int, default=300)
    ap.add_argument("--out", default="//out")
    ap.add_argument("--still", type=int, default=0)
    a = ap.parse_args(argv)

    scene = build(a.frames)
    render(scene, a.out, still=a.still or None)
    print(f"done -> {a.out}")
