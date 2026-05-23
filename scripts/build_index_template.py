#!/usr/bin/env python3
"""One-off helper: build scripts/index.template.html from root index.html."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
idx = (ROOT / "index.html").read_text(encoding="utf-8")

idx = idx.replace(
    '<html lang="pt-PT">',
    '<html lang="{{HTML_LANG}}" data-page-lang="{{PAGE_LANG}}">',
)
idx = re.sub(r"    <title>.*?</title>", "    <title>{{PAGE_TITLE}}</title>", idx, count=1)
idx = re.sub(
    r'    <meta name="description" content=".*?">',
    '    <meta name="description" content="{{META_DESCRIPTION}}">',
    idx,
    count=1,
)
idx = re.sub(
    r'    <meta property="og:title" content=".*?">',
    '    <meta property="og:title" content="{{OG_TITLE}}">',
    idx,
    count=1,
)
idx = re.sub(
    r'    <meta property="og:description" content=".*?">',
    '    <meta property="og:description" content="{{OG_DESCRIPTION}}">',
    idx,
    count=1,
)
idx = re.sub(
    r'    <meta property="og:url" content=".*?">',
    '    <meta property="og:url" content="{{CANONICAL_URL}}">',
    idx,
    count=1,
)
idx = idx.replace(
    '    <meta property="og:image"',
    '    <meta property="og:locale" content="{{OG_LOCALE}}">\n    <meta property="og:image"',
)
idx = idx.replace(
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    '    <link rel="canonical" href="{{CANONICAL_URL}}">\n{{HREFLANG_BLOCK}}',
)
idx = re.sub(
    r'    <script type="application/ld\+json">.*?</script>',
    "    <script type=\"application/ld+json\">\n    {{JSON_LD}}\n    </script>",
    idx,
    count=1,
    flags=re.DOTALL,
)
idx = re.sub(
    r'                    <div class="lang-switcher" id="lang-switcher">.*?</div>\n                    </div>',
    "{{LANG_SWITCHER}}",
    idx,
    count=1,
    flags=re.DOTALL,
)
idx = re.sub(
    r'            <div class="services-modern-grid">.*?</div>\n        </div>\n    </section>',
    "            <div class=\"services-modern-grid\">\n{{SERVICE_CARDS}}\n            </div>\n        </div>\n    </section>",
    idx,
    count=1,
    flags=re.DOTALL,
)
idx = re.sub(
    r'    <section class="section handyman-details" id="handyman-details">.*?</section>',
    "{{HANDYMAN_SECTION}}",
    idx,
    count=1,
    flags=re.DOTALL,
)
idx = idx.replace('href="style.css"', 'href="{{ASSET_PREFIX}}style.css"')
idx = idx.replace('src="logo.webp"', 'src="{{ASSET_PREFIX}}logo.webp"')
idx = idx.replace("url('images/hero/", "url('{{ASSET_PREFIX}}images/hero/")
idx = idx.replace('src="script.js"', 'src="{{ASSET_PREFIX}}script.js"')

out = ROOT / "scripts" / "index.template.html"
out.write_text(idx, encoding="utf-8")
print(f"Wrote {out} ({len(idx)} chars)")
