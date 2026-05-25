#!/usr/bin/env python3
"""Generate favicon.ico and PNG icons from logo.png (square mascot, no extra assets)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "logo.png"
OUTPUTS = {
    "favicon-48x48.png": 48,
    "favicon-192x192.png": 192,
    "apple-touch-icon.png": 180,
}
ICO_SIZES = (16, 32, 48)


def square_icon(img: Image.Image, size: int) -> Image.Image:
    return img.resize((size, size), Image.Resampling.LANCZOS)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing source image: {SOURCE}")

    with Image.open(SOURCE) as raw:
        img = raw.convert("RGBA")
        w, h = img.size
        side = min(w, h)
        left = (w - side) // 2
        top = (h - side) // 2
        img = img.crop((left, top, left + side, top + side))

    for name, size in OUTPUTS.items():
        square_icon(img, size).save(ROOT / name, format="PNG", optimize=True)
        print(f"wrote {name} ({size}x{size})")

    ico_images = [square_icon(img, s) for s in ICO_SIZES]
    ico_path = ROOT / "favicon.ico"
    ico_images[0].save(
        ico_path,
        format="ICO",
        sizes=[(s, s) for s in ICO_SIZES],
        append_images=ico_images[1:],
    )
    print(f"wrote favicon.ico ({', '.join(str(s) for s in ICO_SIZES)})")


if __name__ == "__main__":
    main()
