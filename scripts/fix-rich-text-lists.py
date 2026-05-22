#!/usr/bin/env python3
"""Convert service-rich-text paragraphs under 'O que fazemos' into ul/li lists."""
import re
import glob

H2_OQUE = re.compile(
    r"(<h2>O que fazemos[^<]*</h2>)(.*?)(<h2>Zonas de Atendimento)",
    re.S,
)
P_TAG = re.compile(r"<p>(.*?)</p>", re.S)
UL_TAG = re.compile(r"<ul(?![^>]*service-zones)[^>]*>(.*?)</ul>", re.S)
LI_TAG = re.compile(r"<li>(.*?)</li>", re.S)


def split_paragraph_to_items(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    # Multiple sentences → one bullet each
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÀÃÕÇ])", text)
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) > 1:
        return parts
    return [text]


def section_to_list_html(section: str) -> str:
    items: list[str] = []

    for p_inner in P_TAG.findall(section):
        items.extend(split_paragraph_to_items(p_inner))

    for ul_inner in UL_TAG.findall(section):
        for li_inner in LI_TAG.findall(ul_inner):
            items.append(li_inner.strip())

    if not items:
        return section

    lis = "\n".join(f"                    <li>{item}</li>" for item in items)
    return f"\n                <ul>\n{lis}\n                </ul>\n"


def fix_file(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        html = f.read()

    def replacer(m: re.Match) -> str:
        h2_open, section, h2_zonas = m.group(1), m.group(2), m.group(3)
        if not P_TAG.search(section) and not UL_TAG.search(section):
            return m.group(0)
        new_section = section_to_list_html(section)
        return h2_open + new_section + "\n                " + h2_zonas

    new_html, count = H2_OQUE.subn(replacer, html)
    if count == 0:
        return False
    if new_html == html:
        return False
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_html)
    return True


def main():
    fixed = []
    for path in sorted(glob.glob("servico-*.html")):
        if fix_file(path):
            fixed.append(path)
    print(f"Fixed {len(fixed)} files:")
    for p in fixed:
        print(f"  - {p}")


if __name__ == "__main__":
    main()
