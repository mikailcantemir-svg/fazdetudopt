#!/usr/bin/env python3
"""Import lawn + irrigation photos/videos for recent-work gallery."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r"C:\Users\mikai\Documents\fotos website")
IMG_OUT = ROOT / "images" / "trabalhos"
VID_OUT = ROOT / "videos" / "trabalhos"
MAX_WIDTH = 1200
WEBP_QUALITY = 82

IMAGE_JOBS = [
    ("WhatsApp Image 2026-05-25 at 14.22.09 (9).jpeg", "relva-sistema-rega-lisboa-01.webp"),
    ("WhatsApp Image 2026-05-25 at 14.22.09 (11).jpeg", "relva-sistema-rega-lisboa-02.webp"),
    ("WhatsApp Image 2026-05-25 at 14.22.10 (2).jpeg", "relva-sistema-rega-lisboa-03.webp"),
    ("WhatsApp Image 2026-05-25 at 14.22.09 (10).jpeg", "relva-sistema-rega-lisboa-04.webp"),
    ("WhatsApp Image 2026-05-25 at 14.22.09 (12).jpeg", "relva-sistema-rega-lisboa-05.webp"),
    ("WhatsApp Image 2026-05-25 at 14.22.10.jpeg", "relva-sistema-rega-lisboa-06.webp"),
]

VIDEO_JOBS = [
    ("WhatsApp Video 2026-05-25 at 14.22.09 (1).mp4", "relva-sistema-rega-lisboa-01.mp4"),
    ("WhatsApp Video 2026-05-25 at 14.22.10 (2).mp4", "relva-sistema-rega-lisboa-02.mp4"),
    ("WhatsApp Video 2026-05-25 at 14.22.10 (3).mp4", "relva-sistema-rega-lisboa-03.mp4"),
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
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    VID_OUT.mkdir(parents=True, exist_ok=True)

    print("=== Imagens (origem -> webp) ===")
    for src_name, webp_name in IMAGE_JOBS:
        src = SRC / src_name
        dst = IMG_OUT / webp_name
        if not src.is_file():
            raise SystemExit(f"Missing: {src}")
        w, h = optimize_image(src, dst)
        print(f"  {src_name}")
        print(f"    -> {dst.relative_to(ROOT)} ({w}x{h}, {dst.stat().st_size:,} B)")

    print("\n=== Videos (origem -> mp4) ===")
    for src_name, mp4_name in VIDEO_JOBS:
        src = SRC / src_name
        dst = VID_OUT / mp4_name
        if not src.is_file():
            raise SystemExit(f"Missing: {src}")
        shutil.copy2(src, dst)
        mb = dst.stat().st_size / (1024 * 1024)
        flag = " WARNING: >10 MB" if mb > 10 else ""
        print(f"  {src_name}")
        print(f"    -> {dst.relative_to(ROOT)} ({mb:.2f} MB){flag}")


if __name__ == "__main__":
    main()
