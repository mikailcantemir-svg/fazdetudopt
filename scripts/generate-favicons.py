#!/usr/bin/env python3
"""Generate favicon.ico and PNG icons from logo.png (white bg, tight crop, large mascot)."""

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
MASTER_SIZE = 512
# Mascot fills this fraction of the square (85–92%)
FILL_RATIO = 0.92
# Extra padding around detected content bbox before square fit
BBOX_PAD_RATIO = 0.08
BG_THRESHOLD = 58


def is_background_pixel(r: int, g: int, b: int, a: int) -> bool:
    if a < 40:
        return True
    if max(r, g, b) < BG_THRESHOLD:
        return True
    if min(r, g, b) > 245:
        return True
    return False


def remove_black_background(img: Image.Image) -> Image.Image:
    """Replace near-black backdrop with white."""
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if is_background_pixel(r, g, b, a) and max(r, g, b) < BG_THRESHOLD:
                px[x, y] = WHITE
    return img


def foreground_mask(img: Image.Image) -> Image.Image:
    """Binary mask: 255 = visible mascot / artwork."""
    mask = Image.new("L", img.size, 0)
    px = img.load()
    mpx = mask.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = px[x, y]
            if not is_background_pixel(r, g, b, a):
                mpx[x, y] = 255
    return mask


def expand_bbox(
    bbox: tuple[int, int, int, int],
    width: int,
    height: int,
    ratio: float,
) -> tuple[int, int, int, int]:
    left, upper, right, lower = bbox
    bw = right - left
    bh = lower - upper
    pad_x = int(bw * ratio / 2)
    pad_y = int(bh * ratio / 2)
    return (
        max(0, left - pad_x),
        max(0, upper - pad_y),
        min(width, right + pad_x),
        min(height, lower + pad_y),
    )


def crop_to_content(img: Image.Image) -> Image.Image:
    mask = foreground_mask(img)
    bbox = mask.getbbox()
    if bbox is None:
        raise SystemExit("No visible content found in logo.png")
    bbox = expand_bbox(bbox, img.width, img.height, BBOX_PAD_RATIO)
    return img.crop(bbox)


def fit_on_square_canvas(crop: Image.Image, side: int, fill: float) -> Image.Image:
    """Place cropped mascot on white square; longest side uses `fill` of canvas."""
    cw, ch = crop.size
    scale = (side * fill) / max(cw, ch)
    nw = max(1, int(round(cw * scale)))
    nh = max(1, int(round(ch * scale)))
    resized = crop.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (side, side), WHITE)
    ox = (side - nw) // 2
    oy = (side - nh) // 2
    canvas.paste(resized, (ox, oy), resized)
    return canvas.convert("RGB")


def render_size(img: Image.Image, size: int) -> Image.Image:
    return img.resize((size, size), Image.Resampling.LANCZOS)


def prepare_master() -> Image.Image:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing source image: {SOURCE}")
    with Image.open(SOURCE) as raw:
        img = remove_black_background(raw.convert("RGBA"))
        crop = crop_to_content(img)
        return fit_on_square_canvas(crop, MASTER_SIZE, FILL_RATIO)


def main() -> None:
    base = prepare_master()
    fill_pct = int(FILL_RATIO * 100)
    print(f"master {MASTER_SIZE}px, content fill ~{fill_pct}%, bbox pad {int(BBOX_PAD_RATIO * 100)}%")

    for name, size in OUTPUTS.items():
        render_size(base, size).save(ROOT / name, format="PNG", optimize=True)
        print(f"wrote {name} ({size}x{size})")

    ico_images = [render_size(base, s) for s in ICO_SIZES]
    ico_path = ROOT / "favicon.ico"
    ico_images[0].save(
        ico_path,
        format="ICO",
        sizes=[(s, s) for s in ICO_SIZES],
        append_images=ico_images[1:],
    )
    print(f"wrote favicon.ico ({', '.join(str(s) for s in ICO_SIZES)})")

    _refresh_gemini_bundle()


def _refresh_gemini_bundle() -> None:
    import importlib.util

    scripts = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "bundle_for_gemini",
        scripts / "bundle-for-gemini.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print("\n--- Gemini code bundle ---")
    mod.main()


if __name__ == "__main__":
    main()
