#!/usr/bin/env python3
"""
Single entry point to regenerate the whole static site from templates + i18n.

Run from repo root:
    python scripts/generate-servico-pages.py

Outputs (overwrites):
  - index.html (PT) + en/es/fr/index.html
  - servico-*.html (PT) + en/es/fr/servico-*.html (18 services × 4 languages)

Source of truth:
  - scripts/home_page_i18n.py  → homepage copy (hero, UI strings)
  - scripts/service_page_i18n.py → service page copy
  - scripts/index.template.html, template-servico.html → layout (WhatsApp widget only)
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "template-servico.html").read_text(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent))

from service_page_i18n import (  # noqa: E402
    LANGS,
    LANG_HTML,
    SERVICE_COPY,
    UI,
    asset_prefix,
    build_body_html,
    index_href,
    localized_meta,
    page_url,
    render_hreflang_tags,
)

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}

LANG_DIRS = ("en", "es", "fr")


def json_ld(slug: str, lang: str) -> str:
    meta = localized_meta(slug, lang)
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": meta["service_name"],
        "description": meta["meta_description"],
        "provider": {
            "@type": "HomeAndConstructionBusiness",
            "name": "Faz de Tudo PT",
            "image": "https://www.fazdetudo.pt/logo.webp",
            "telephone": "+351932504112",
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Lisboa",
                "addressCountry": "PT",
            },
        },
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def get_body_html(slug: str, lang: str) -> str:
    if lang == "pt":
        try:
            from service_rich_content import SERVICE_BODIES
        except ImportError:
            SERVICE_BODIES = {}
        if slug in SERVICE_BODIES:
            return SERVICE_BODIES[slug].strip()
    return build_body_html(slug, lang).strip()


def render_page(slug: str, lang: str) -> str:
    meta = localized_meta(slug, lang)
    ui = UI[lang]
    prefix = asset_prefix(lang)
    canonical = page_url(slug, lang)

    return (
        TEMPLATE.replace("{{HTML_LANG}}", LANG_HTML[lang])
        .replace("{{PAGE_LANG}}", lang)
        .replace("{{PAGE_TITLE}}", meta["page_title"])
        .replace("{{META_DESCRIPTION}}", meta["meta_description"])
        .replace("{{CANONICAL_URL}}", canonical)
        .replace("{{HREFLANG_LINKS}}", render_hreflang_tags(slug))
        .replace("{{OG_TITLE}}", meta["og_title"])
        .replace("{{OG_LOCALE}}", OG_LOCALE[lang])
        .replace("{{ASSET_PREFIX}}", prefix)
        .replace("{{INDEX_HREF}}", index_href(lang))
        .replace("{{H1_TITLE}}", meta["h1"])
        .replace("{{LEAD_TEXT}}", ui["lead"])
        .replace("{{BODY_HTML}}", get_body_html(slug, lang))
        .replace("{{SERVICE_NAME}}", meta["service_name"])
        .replace("{{WA_TEXT}}", quote(meta["wa_message"], safe=""))
        .replace("{{BACK_LABEL}}", ui["back"])
        .replace("{{CTA_H3}}", ui["cta_h3"])
        .replace("{{CTA_P}}", ui["cta_p"].format(service=meta["service_name"]))
        .replace("{{CTA_WA}}", ui["cta_wa"])
        .replace("{{CTA_CALL}}", ui["cta_call"])
        .replace("{{FOOTER_TEXT}}", ui["footer"])
        .replace("{{FLOAT_WA}}", ui["float_wa"])
        .replace("{{FLOAT_TEL}}", ui["float_tel"])
        .replace("{{WA_GREETING}}", ui["wa_greeting"])
        .replace("{{WA_PLACEHOLDER}}", ui["wa_placeholder"])
        .replace("{{WA_CLOSE}}", ui["wa_close"])
        .replace("{{WA_ONLINE}}", ui["wa_online"])
        .replace("{{WA_FLOAT_LABEL}}", ui["wa_float_label"])
        .replace("{{WA_SEND}}", ui["wa_send"])
        .replace("{{JSON_LD}}", json_ld(slug, lang))
    )


def output_path(slug: str, lang: str) -> Path:
    if lang == "pt":
        return ROOT / slug
    return ROOT / lang / slug


def expected_service_paths() -> set[str]:
    paths = set()
    for slug in SERVICE_COPY:
        for lang in LANGS:
            paths.add(output_path(slug, lang).relative_to(ROOT).as_posix())
    return paths


def cleanup_stale_service_pages() -> list[str]:
    """Remove obsolete servico-*.html files no longer in SERVICE_COPY."""
    removed = []
    expected = expected_service_paths()
    for lang_dir in [ROOT, *[ROOT / code for code in LANG_DIRS]]:
        if not lang_dir.is_dir():
            continue
        for path in lang_dir.glob("servico-*.html"):
            rel = path.relative_to(ROOT).as_posix()
            if rel not in expected:
                path.unlink()
                removed.append(rel)
    return removed


def _run_generate_homepages() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_homepages",
        Path(__file__).parent / "generate-homepages.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_fix_fa_aria_hidden() -> None:
    spec = importlib.util.spec_from_file_location(
        "fix_fa_aria_hidden",
        Path(__file__).parent / "fix-fa-aria-hidden.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def main() -> None:
    print("=== Regenerating fazdetudo.pt static HTML ===\n")

    removed = cleanup_stale_service_pages()
    if removed:
        print("Removed stale pages:")
        for rel in removed:
            print(f"  - {rel}")
        print()

    print("--- Homepages (PT + en/es/fr) ---")
    _run_generate_homepages()

    print("\n--- Service pages (18 × 4 languages) ---")
    written = []
    for slug in SERVICE_COPY:
        for lang in LANGS:
            path = output_path(slug, lang)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_page(slug, lang), encoding="utf-8")
            rel = path.relative_to(ROOT).as_posix()
            written.append(rel)
            print(f"wrote {rel}")

    print("\n--- Font Awesome aria-hidden pass ---")
    _run_fix_fa_aria_hidden()

    print(
        f"\nDone: {len(written)} service pages + 4 homepages "
        f"({len(SERVICE_COPY)} services × {len(LANGS)} languages)."
    )
    print("Copy source: scripts/home_page_i18n.py, scripts/service_page_i18n.py")
    print("Layout source: scripts/index.template.html, template-servico.html")


if __name__ == "__main__":
    main()
