"""Social preview card, 1280x640. Reuses the video's helpers.

The card has to carry the argument in one frame with no motion, so the
contrast is the point: slop on the left, system on the right, one rule
between them. Cropping a frame out of the vertical video loses exactly
that, which is why this is its own composition.

    blender -b -P video/social.py
"""

import math
import pathlib
import random
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import scene as S  # noqa: E402

import bpy  # noqa: E402

S.W, S.H = 1280, 640
random.seed(3)

S.wipe()
scn = bpy.context.scene
scn.render.resolution_x, scn.render.resolution_y = S.W, S.H
scn.frame_start = scn.frame_end = 1

world = bpy.data.worlds.new("w")
scn.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (1, 1, 1, 1)

bpy.ops.object.camera_add(location=(0, 0, 10))
cam = bpy.context.active_object
cam.data.type = "ORTHO"
cam.data.sensor_fit = "HORIZONTAL"
cam.data.ortho_scale = 11.0
scn.camera = cam

m_purple = S.flat_material("p", S.PURPLE)
m_purple_d = S.flat_material("pd", S.PURPLE_D)
m_grey = S.flat_material("g", S.GREY)
m_soft = S.flat_material("s", S.srgb("#c3c3cc"))
m_orange = S.flat_material("o", S.ORANGE)
m_ink = S.flat_material("i", S.INK)
m_paper = S.flat_material("w2", S.PAPER)

# ---- left: the pile ------------------------------------------------------
for i in range(16):
    ang = random.uniform(0, math.tau)
    rad = random.uniform(0.25, 1.0) ** 0.65
    x = -3.0 + math.cos(ang) * rad * 1.85
    y = -0.15 + math.sin(ang) * rad * 1.7
    m = m_purple if i % 2 else m_purple_d
    if random.random() < 0.35:
        S.blob(f"b{i}", x, y, random.uniform(0.28, 0.62), m)
    else:
        w = random.uniform(0.55, 1.25)
        h = w * random.uniform(0.45, 0.75)
        S.rect(f"c{i}", x, y, w, h, m, radius=0.08)
        for r in range(2):
            S.rect(f"l{i}_{r}", x - w / 2 + 0.16 + w * 0.16,
                   y + h / 2 - 0.14 - r * 0.14, w * (0.5 - r * 0.15), 0.045,
                   m_paper, z=0.02, radius=0.02)

# ---- right: the system ---------------------------------------------------
grid = [
    (3.0, 1.45, 3.5, 0.72),
    (2.13, 0.42, 1.72, 0.72), (3.87, 0.42, 1.72, 0.72),
    (2.42, -0.62, 2.3, 0.72), (4.31, -0.62, 0.9, 0.72),
    (3.0, -1.65, 3.5, 0.72),
]
for i, (x, y, w, h) in enumerate(grid):
    S.rect(f"q{i}", x, y, w, h, m_grey, radius=0.07)
    for r in range(2):
        S.rect(f"ql{i}_{r}", x - w / 2 + 0.22 + w * (0.2 - r * 0.06),
               y + h / 2 - 0.2 - r * 0.16, w * (0.42 - r * 0.13), 0.05,
               m_soft, z=0.03, radius=0.022)
    S.rect(f"qa{i}", x - w / 2 + 0.4, y - h / 2 + 0.18, 0.32, 0.08,
           m_orange, z=0.04, radius=0.032)

# ---- divider + wordmark --------------------------------------------------
S.rect("rule", 0, 0, 0.03, 3.9, m_ink, z=0.5)
S.text("t2", "every AI builds the same website", 0, 2.62, 0.26, m_soft)
S.text("t", "anti-slop-design", 0, -2.62, 0.34, m_ink)

S.render(scn, str(pathlib.Path(__file__).parent / "social"), still=1)
