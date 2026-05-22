import re
import glob

for path in sorted(glob.glob("servico-*.html")):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    m = re.search(
        r'<div class="service-rich-text">(.*?)</div>\s*\n\s*<div class="service-cta-box">',
        html,
        re.S,
    )
    if not m:
        print(f"{path}: NO BLOCK")
        continue
    block = m.group(1)
    h2 = re.search(r"<h2>O que fazemos.*?</h2>(.*?)(?=<h2>Zonas)", block, re.S)
    if not h2:
        print(f"{path}: NO O QUE FAZEMOS")
        continue
    section = h2.group(1).strip()
    has_plain_ul = "<ul>" in section or bool(
        re.search(r'<ul(?![^>]*class="service-zones)', section)
    )
    ps = re.findall(r"<p>(.*?)</p>", section, re.S)
    print(f"{path}: paragraphs={len(ps)} plain_ul={has_plain_ul}")
