#!/usr/bin/env python3
"""
Convert .jpg, .jpeg and .png images to .webp (quality 80) using Pillow.

Scans the project root (logo.png, images/hero/, etc.) and writes a .webp file
next to each source image (e.g. logo.png -> logo.webp).

Usage:
    pip install pillow
    python scripts/optimize-images.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
EXTENSIONS = {".jpg", ".jpeg", ".png"}
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".cursor"}
WEBP_QUALITY = 80


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_images(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if should_skip(path):
            continue
        if path.suffix.lower() not in EXTENSIONS:
            continue
        yield path


def to_webp_path(source: Path) -> Path:
    return source.with_suffix(".webp")


def convert_image(source: Path) -> Path:
    out = to_webp_path(source)
    with Image.open(source) as img:
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
        elif img.mode != "RGB":
            img = img.convert("RGB")
        img.save(out, "WEBP", quality=WEBP_QUALITY, method=6)
    return out


def main() -> None:
    sources = list(iter_images(ROOT))
    if not sources:
        print("No images found.")
        return

    print(f"Found {len(sources)} image(s) under {ROOT}")
    for source in sources:
        rel = source.relative_to(ROOT)
        out = convert_image(source)
        before = source.stat().st_size
        after = out.stat().st_size
        pct = (1 - after / before) * 100 if before else 0
        print(f"  {rel} -> {out.name} ({before // 1024} KB -> {after // 1024} KB, {pct:.0f}% smaller)")
    print("Done.")


if __name__ == "__main__":
    main()
