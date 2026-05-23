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
    paths: list[Path] = []
    for pattern in ("**/*.html", "template-servico.html"):
        paths.extend(ROOT.glob(pattern))
    paths.extend(ROOT.glob("scripts/*.py"))
    paths.append(ROOT / "scripts" / "index.template.html")
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return sorted(unique)


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
