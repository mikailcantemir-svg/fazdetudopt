#!/usr/bin/env python3
"""Import TV wall-mount photos (15.28.09 batch) into instalacao-tv-parede-lisboa-*.webp."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r"C:\Users\mikai\Documents\fotos website")
OUT = ROOT / "images" / "trabalhos"
MAX_WIDTH = 1200
WEBP_QUALITY = 82

# Apenas fotos de instalação de TV (lote 15.28.09 / 15.28.10)
JOBS = [
    ("WhatsApp Image 2026-05-25 at 15.28.09 (4).jpeg", "instalacao-tv-parede-lisboa-01.webp"),
    ("WhatsApp Image 2026-05-25 at 15.28.09 (3).jpeg", "instalacao-tv-parede-lisboa-02.webp"),
    ("WhatsApp Image 2026-05-25 at 15.28.09 (2).jpeg", "instalacao-tv-parede-lisboa-03.webp"),
    ("WhatsApp Image 2026-05-25 at 15.28.09 (1).jpeg", "instalacao-tv-parede-lisboa-04.webp"),
    ("WhatsApp Image 2026-05-25 at 15.28.09.jpeg", "instalacao-tv-parede-lisboa-05.webp"),
    ("WhatsApp Image 2026-05-25 at 15.28.10 (1).jpeg", "instalacao-tv-parede-lisboa-06.webp"),
]


def optimize_image(src: Path, dst: Path) -> tuple[int, int]:
    from PIL import Image

    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        if w > MAX_WIDTH:
            nh = round(h * MAX_WIDTH / w)
            im = im.resize((MAX_WIDTH, nh), Image.Resampling.LANCZOS)
        w, h = im.size
        im.save(dst, "WEBP", quality=WEBP_QUALITY, method=6)
    return w, h


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    print("=== Instalacao TV (origem -> webp) ===")
    for src_name, webp_name in JOBS:
        src = SRC / src_name
        dst = OUT / webp_name
        if not src.is_file():
            raise SystemExit(f"Missing: {src}")
        w, h = optimize_image(src, dst)
        print(f"  {src_name}")
        print(f"    -> {dst.relative_to(ROOT)} ({w}x{h}, {dst.stat().st_size:,} B)")


if __name__ == "__main__":
    main()
