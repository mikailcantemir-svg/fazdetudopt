#!/usr/bin/env python3
"""Apply unique service-rich-text content to all servico-*.html files."""
import re
from pathlib import Path

from service_rich_content import SERVICE_BODIES

ROOT = Path(__file__).resolve().parent.parent
PATTERN = re.compile(
    r'(<div class="service-rich-text">)(.*?)(</div>\s*\n\s*<div class="service-cta-box">)',
    re.DOTALL,
)


def main():
    updated = []
    missing = []
    for slug, body in SERVICE_BODIES.items():
        path = ROOT / slug
        if not path.exists():
            missing.append(slug)
            continue
        html = path.read_text(encoding="utf-8")
        new_html, n = PATTERN.subn(r"\1" + body + r"\n            \3", html, count=1)
        if n != 1:
            print(f"WARN: could not patch {slug}")
            continue
        path.write_text(new_html, encoding="utf-8", newline="\n")
        updated.append(slug)
    print(f"Updated {len(updated)} files")
    if missing:
        print("Missing:", missing)


if __name__ == "__main__":
    main()
