#!/usr/bin/env python3
"""Add aria-hidden=\"true\" to decorative Font Awesome <i> icons."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ICON_RE = re.compile(
    r'<i\s+((?:(?!aria-hidden)[^>])*class="fa-(?:solid|brands|regular)\s[^"]+"(?:(?!aria-hidden)[^>]*)*)>',
    re.IGNORECASE,
)


def fix_content(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        attrs = match.group(1).strip()
        if "aria-hidden" in attrs:
            return match.group(0)
        count += 1
        return f'<i {attrs} aria-hidden="true">'

    return ICON_RE.sub(repl, text), count


def iter_targets() -> list[Path]:
    return sorted(
        p
        for p in ROOT.rglob("*.html")
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
    )


def main() -> None:
    total = 0
    for path in iter_targets():
        text = path.read_text(encoding="utf-8")
        updated, count = fix_content(text)
        if count:
            path.write_text(updated, encoding="utf-8")
            print(f"{path.relative_to(ROOT).as_posix()}: {count}")
            total += count
    print(f"Done. Updated {total} icon(s).")


if __name__ == "__main__":
    main()
