# Video

Blender-rendered explainer, built headless from `scene.py`. No .blend to
maintain — the scene is the code, so it is diffable and re-renders
identically (fixed random seed).

## Render

```bash
BLENDER=/Applications/Blender.app/Contents/MacOS/Blender

# single frame, for checking a beat
"$BLENDER" -b -P video/scene.py -- --still 165 --out "$PWD/video/check"

# full sequence -> PNG frames
"$BLENDER" -b -P video/scene.py -- --frames 210 --out "$PWD/video/frames/f"

# encode
ffmpeg -y -framerate 30 -i video/frames/f%04d.png \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart video/anti-slop.mp4
```

1080×1920, 30fps, 7s. Renders in ~25s on an M-series laptop.

## Notes

- Flat 2D under an orthographic camera: every object is a plane with an
  emission shader. No lights, no shadows, no denoising.
- `view_transform = "Standard"`. AgX is a filmic tone map and turns flat
  emission to mud — near-black arrives as mid-grey.
- Colours are authored as sRGB hex and converted to linear at the
  boundary by `srgb()`. Emission inputs are linear.
- Nothing is parented. Animated parent transforms kept desynchronising
  cards from their own contents; absolute positions with scale-only
  entrances removed the whole class of bug.
- PNG sequence rather than direct video: this Blender build has no
  FFmpeg writer, and frames survive a crash anyway.

## Sound

Not included. Audio licensing is worth checking yourself rather than
inheriting — see the notes in the handover.
