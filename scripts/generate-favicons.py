#!/usr/bin/env python3
"""Generate favicon.ico and PNG icons from logo.png (white bg, readable in light/dark SERP)."""

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
WHITE = (255, 255, 255, 255)
# Mascot scale inside square canvas (breathing room for 16px favicon)
CONTENT_SCALE = 0.86
# Pixels this dark are treated as logo black background (not character)
BG_THRESHOLD = 58


def is_background_pixel(r: int, g: int, b: int, a: int) -> bool:
    if a < 40:
        return True
    return max(r, g, b) < BG_THRESHOLD


def remove_black_background(img: Image.Image) -> Image.Image:
    """Replace near-black backdrop with white so favicon is not a black blob."""
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if is_background_pixel(r, g, b, a):
                px[x, y] = WHITE
    return img


def crop_square(img: Image.Image) -> Image.Image:
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))


def on_white_canvas(img: Image.Image) -> Image.Image:
    """Center mascot on opaque white square (Google light + dark UI)."""
    side = img.size[0]
    inner = max(1, int(side * CONTENT_SCALE))
    resized = img.resize((inner, inner), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (side, side), WHITE)
    offset = (side - inner) // 2
    canvas.paste(resized, (offset, offset), resized)
    return canvas.convert("RGB")


def render_size(img: Image.Image, size: int) -> Image.Image:
    return img.resize((size, size), Image.Resampling.LANCZOS)


def prepare_source() -> Image.Image:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing source image: {SOURCE}")
    with Image.open(SOURCE) as raw:
        img = remove_black_background(raw.convert("RGBA"))
        img = crop_square(img)
        return on_white_canvas(img)


def main() -> None:
    base = prepare_source()

    for name, size in OUTPUTS.items():
        render_size(base, size).save(ROOT / name, format="PNG", optimize=True)
        print(f"wrote {name} ({size}x{size}, white background)")

    ico_images = [render_size(base, s) for s in ICO_SIZES]
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
