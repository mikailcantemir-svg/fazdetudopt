#!/usr/bin/env python3
"""Extract images from AC article DOCX and save as WebP."""
from __future__ import annotations

import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DOCX = Path(
    r"C:\Users\mikai\Desktop\Artigos"
    r"\Ar Condicionado Lisboa Instalar, Limpar e Manter o Split.docx"
)
OUT = ROOT / "images" / "artigos" / "ar-condicionado"

MAPPING = {
    "word/media/image1.jpeg": "ar-condicionado-lisboa-split-sala.webp",
    "word/media/image2.jpeg": "limpeza-filtros-ar-condicionado-split.webp",
    "word/media/image3.jpeg": "manutencao-ar-condicionado-checklist.webp",
}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(DOCX) as z:
        for src, dest_name in MAPPING.items():
            data = z.read(src)
            tmp = OUT / dest_name.replace(".webp", ".jpg")
            tmp.write_bytes(data)
            img = Image.open(tmp)
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")
            out = OUT / dest_name
            img.save(out, "WEBP", quality=82, method=6)
            tmp.unlink()
            print(f"{dest_name}: {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
