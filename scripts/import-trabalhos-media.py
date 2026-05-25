#!/usr/bin/env python3
"""Copy and optimize trabalhos media from the user's photos folder (one-off)."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(r"C:\Users\mikai\Documents\fotos website")
IMG_OUT = ROOT / "images" / "trabalhos"
VID_OUT = ROOT / "videos" / "trabalhos"
MAX_WIDTH = 1200
WEBP_QUALITY = 82

# (source image, webp name, mp4 name, source video) — 4 pairs = 8 files
JOBS = [
    (
        "WhatsApp Image 2026-05-25 at 14.19.41 (2).jpeg",
        "reparacao-casa-banho-lisboa-01.webp",
        "reparacao-casa-banho-lisboa-01.mp4",
        "WhatsApp Video 2026-05-25 at 14.19.41.mp4",
    ),
    (
        "WhatsApp Image 2026-05-25 at 14.19.40 (3).jpeg",
        "pintura-interior-lisboa-01.webp",
        "pintura-interior-lisboa-01.mp4",
        "WhatsApp Video 2026-05-25 at 14.16.22 (1).mp4",
    ),
    (
        "WhatsApp Image 2026-05-25 at 14.16.21.jpeg",
        "trabalhos-exteriores-jardim-01.webp",
        "trabalhos-exteriores-jardim-01.mp4",
        "WhatsApp Video 2026-05-25 at 14.16.22 (3).mp4",
    ),
    (
        "WhatsApp Image 2026-05-25 at 14.16.22.jpeg",
        "manutencao-interior-lisboa-01.webp",
        "manutencao-interior-lisboa-01.mp4",
        "WhatsApp Video 2026-05-25 at 14.16.22 (2).mp4",
    ),
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
    try:
        from PIL import Image  # noqa: F401
    except ImportError as e:
        raise SystemExit("Install Pillow: pip install Pillow") from e

    IMG_OUT.mkdir(parents=True, exist_ok=True)
    VID_OUT.mkdir(parents=True, exist_ok=True)

    print("=== Imagens (origem -> destino) ===")
    dims: dict[str, tuple[int, int]] = {}
    for src_name, webp_name, _vid_name, _vid_src in JOBS:
        src = SRC / src_name
        dst = IMG_OUT / webp_name
        if not src.is_file():
            raise SystemExit(f"Missing source image: {src}")
        w, h = optimize_image(src, dst)
        dims[webp_name] = (w, h)
        print(f"  {src_name}")
        print(f"    -> {dst.relative_to(ROOT)} ({w}x{h}, {dst.stat().st_size:,} B)")

    print("\n=== Videos (origem -> destino) ===")
    for _img_src, _webp, mp4_name, vid_src_name in JOBS:
        src = SRC / vid_src_name
        dst = VID_OUT / mp4_name
        if not src.is_file():
            raise SystemExit(f"Missing source video: {src}")
        shutil.copy2(src, dst)
        mb = dst.stat().st_size / (1024 * 1024)
        flag = " WARNING: >10 MB" if mb > 10 else ""
        print(f"  {vid_src_name}")
        print(f"    -> {dst.relative_to(ROOT)} ({mb:.2f} MB){flag}")

    print("\n=== Dimensoes (home_page_i18n RECENT_WORK) ===")
    for webp_name, (w, h) in dims.items():
        print(f"  {webp_name}: width={w}, height={h}")


if __name__ == "__main__":
    main()
