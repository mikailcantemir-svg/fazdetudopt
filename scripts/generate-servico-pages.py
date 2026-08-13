#!/usr/bin/env python3
"""
Single entry point to regenerate the whole static site from templates + i18n.

Run from repo root:
    python scripts/generate-servico-pages.py

Outputs (overwrites):
  - index.html (PT) + en/es/fr/index.html
  - servico-*.html (PT) + en/es/fr/servico-*.html (16 services × 4 languages)
  - sitemap.xml, dist/, fazdetudopt-codigo-gemini.txt (auto)

Source of truth:
  - scripts/home_page_i18n.py  → homepage copy
  - scripts/service_page_i18n.py → service page copy
  - scripts/slug_registry.py → URLs + hreflang
  - scripts/site_config.py → contactos globais
  - scripts/templates/ → layouts + partials
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))

from html_partials import (  # noqa: E402
    render_footer_service,
    render_head,
    render_header_service,
    render_wa_widget,
)
from service_page_i18n import LANGS, LANG_HTML, SERVICE_COPY, UI, build_body_html, localized_meta  # noqa: E402
from slug_registry import (  # noqa: E402
    SERVICE_SLUGS,
    asset_prefix,
    index_href,
    page_url,
    render_hreflang_tags_for_service,
    service_id_from_slug,
)
from recommended_partners import (  # noqa: E402
    partners_for_service,
    partner_schema_entity,
)
from partner_cards import build_partner_sidebar_card  # noqa: E402
from site_config import (  # noqa: E402
    BASE_URL,
    OG_IMAGE,
    PRIMARY_OFFICE_STREET_LINE1,
    PRIMARY_OFFICE_STREET_LINE2,
    schema_telephone,
    tel_href,
    wa_href_for_message,
)
from template_engine import render_template  # noqa: E402

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}

LANG_DIRS = ("en", "es", "fr")

_ZONE_H2_MARKERS = (
    "<h2>Zonas de Atendimento</h2>",
    "<h2>Zonas de Atendimento na Grande Lisboa e Setúbal:</h2>",
    "<h2>Service Areas</h2>",
    "<h2>Zonas de Servicio</h2>",
    "<h2>Zones d'intervention</h2>",
)


def _default_provider() -> dict:
    return {
        "@type": "HomeAndConstructionBusiness",
        "name": "FAZDETUDO.PT",
        "url": BASE_URL,
        "image": OG_IMAGE,
        "telephone": schema_telephone(),
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": PRIMARY_OFFICE_STREET_LINE1,
            "addressLocality": "Pontinha",
            "postalCode": PRIMARY_OFFICE_STREET_LINE2.split()[0],
            "addressCountry": "PT",
        },
    }


def json_ld(slug: str, lang: str) -> str:
    meta = localized_meta(slug, lang)
    partners = partners_for_service(slug)
    brand = None
    if partners:
        entities = [partner_schema_entity(p) for p in partners]
        provider = entities[0] if len(entities) == 1 else entities
        brand = {"@type": "Brand", "name": "FAZDETUDO.PT", "url": BASE_URL}
    else:
        provider = _default_provider()
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": meta["service_name"],
        "description": meta["meta_description"],
        "provider": provider,
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
        ],
    }
    if brand:
        data["brand"] = brand
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


def split_body_at_zones(body: str, lang: str) -> tuple[str, str]:
    """Split service body so partners can sit before zones on mobile."""
    markers = list(_ZONE_H2_MARKERS)
    ui_marker = f'<h2>{UI[lang]["h2_zones"]}</h2>'
    if ui_marker not in markers:
        markers.insert(0, ui_marker)

    for marker in markers:
        idx = body.find(marker)
        if idx != -1:
            return body[:idx].rstrip(), body[idx:].lstrip()
    return body, ""


def build_sidebar_partners_html(slug: str, lang: str, prefix: str) -> str:
    partners = partners_for_service(slug)
    if not partners:
        return ""
    cards = "\n".join(
        build_partner_sidebar_card(partner, lang, prefix) for partner in partners
    )
    return f"""                <div class="service-sidebar-partners" id="service-partners">
{cards}
                </div>"""


def render_page(slug: str, lang: str) -> str:
    service_id = service_id_from_slug(slug)
    meta = localized_meta(slug, lang)
    ui = UI[lang]
    prefix = asset_prefix(lang)
    canonical = page_url(slug, lang)
    partners = partners_for_service(slug)
    body = get_body_html(slug, lang)

    cta_p = ui["cta_p"].format(service=meta["service_name"])
    cta_h3 = ui["cta_h3"]
    cta_call = ui["cta_call"]
    cta_wa = ui["cta_wa"]
    call_href = tel_href()
    wa_link = wa_href_for_message(meta["wa_message"])
    hide_float_wa = False
    layout_mod = ""
    cta_box_mod = ""
    sidebar_partners = ""
    body_before = body
    body_after = ""

    if partners:
        hide_float_wa = True
        layout_mod = "service-layout--partners"
        cta_box_mod = "service-cta-box--partners"
        cta_h3 = ui["partners_sidebar_h3"]
        cta_p = ui["partners_sidebar_p"]
        sidebar_partners = build_sidebar_partners_html(slug, lang, prefix)
        body_before, body_after = split_body_at_zones(body, lang)
        cta_actions_block = ""
    else:
        cta_actions_block = (
            '                <div class="service-cta-box-actions">\n'
            f'                    <a href="{wa_link}" class="btn btn-primary btn-lg" '
            f'target="_blank" rel="noopener noreferrer">\n'
            f'                        <i class="fa-brands fa-whatsapp" aria-hidden="true"></i> {cta_wa}\n'
            f"                    </a>\n"
            f'                    <a href="{call_href}" class="btn btn-outline btn-lg service-cta-call">\n'
            f'                        <i class="fa-solid fa-phone" aria-hidden="true"></i> {cta_call}\n'
            f"                    </a>\n"
            "                </div>"
        )

    body_after_block = ""
    if body_after.strip():
        body_after_block = (
            '                <div class="service-main-col service-main-col--bottom">\n'
            '                    <div class="service-rich-text">\n'
            f"{body_after}\n"
            "                    </div>\n"
            "                </div>"
        )

    head = render_head(
        page_title=meta["page_title"],
        meta_description=meta["meta_description"],
        canonical_url=canonical,
        hreflang_block=render_hreflang_tags_for_service(service_id),
        og_title=meta["og_title"],
        og_description=meta["meta_description"],
        og_locale=OG_LOCALE[lang],
        json_ld=json_ld(slug, lang),
        asset_prefix=prefix,
        include_swiper_css=False,
    )

    wa_widget = ""
    if not hide_float_wa:
        wa_widget = render_wa_widget(
            asset_prefix=prefix,
            wa_online=ui["wa_online"],
            wa_greeting=ui["wa_greeting"],
            wa_placeholder=ui["wa_placeholder"],
            wa_close=ui["wa_close"],
            wa_send=ui["wa_send"],
            wa_float_label=ui["wa_float_label"],
        )

    html = render_template(
        "service.html",
        {
            "HTML_LANG": LANG_HTML[lang],
            "PAGE_LANG": lang,
            "HEAD": head,
            "SKIP_LINK": ui["skip_link"],
            "HEADER_SERVICE": render_header_service(
                asset_prefix=prefix,
                index_href=index_href(lang),
                back_label=ui["back"],
            ),
            "FOOTER": render_footer_service(footer_text=ui["footer"]),
            "WA_WIDGET": wa_widget,
            "ASSET_PREFIX": prefix,
            "H1_TITLE": meta["h1"],
            "LEAD_TEXT": ui["lead"],
            "LAYOUT_MOD": layout_mod,
            "CTA_BOX_MOD": cta_box_mod,
            "BODY_BEFORE": body_before,
            "BODY_AFTER_BLOCK": body_after_block,
            "SIDEBAR_PARTNERS": sidebar_partners,
            "CTA_H3": cta_h3,
            "CTA_P": cta_p,
            "CTA_ACTIONS_BLOCK": cta_actions_block,
        },
    )
    return html


def output_path(slug: str, lang: str) -> Path:
    if lang == "pt":
        return ROOT / slug
    return ROOT / lang / slug


def expected_service_paths() -> set[str]:
    paths = set()
    for slug in SERVICE_SLUGS:
        for lang in LANGS:
            paths.add(output_path(slug, lang).relative_to(ROOT).as_posix())
    return paths


def cleanup_stale_service_pages() -> list[str]:
    removed = []
    expected = expected_service_paths()
    # Keep soft-redirect stubs for retired services (rewritten by generate-lisboa-redirects)
    spec = importlib.util.spec_from_file_location(
        "generate_lisboa_redirects",
        SCRIPTS / "generate-lisboa-redirects.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    keep = set()
    for old in getattr(mod, "RETIRED_SERVICE_REDIRECTS", {}):
        keep.add(old)
        for lang in LANG_DIRS:
            keep.add(f"{lang}/{old}")

    for lang_dir in [ROOT, *[ROOT / code for code in LANG_DIRS]]:
        if not lang_dir.is_dir():
            continue
        for path in lang_dir.glob("servico-*.html"):
            rel = path.relative_to(ROOT).as_posix()
            if rel in expected or rel in keep:
                continue
            path.unlink()
            removed.append(rel)
    return removed


def _run_generate_homepages() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_homepages",
        SCRIPTS / "generate-homepages.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_fix_fa_aria_hidden() -> None:
    spec = importlib.util.spec_from_file_location(
        "fix_fa_aria_hidden",
        SCRIPTS / "fix-fa-aria-hidden.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_lisboa_redirects() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_lisboa_redirects",
        SCRIPTS / "generate-lisboa-redirects.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_articles() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_articles",
        SCRIPTS / "generate-articles.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_parceiros() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_parceiros",
        SCRIPTS / "generate-parceiros.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_generate_sitemap() -> None:
    spec = importlib.util.spec_from_file_location(
        "generate_sitemap",
        SCRIPTS / "generate-sitemap.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_build_dist() -> None:
    spec = importlib.util.spec_from_file_location(
        "build_dist",
        SCRIPTS / "build-dist.py",
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()


def _run_bundle_for_gemini() -> None:
    spec = importlib.util.spec_from_file_location(
        "bundle_for_gemini",
        SCRIPTS / "bundle-for-gemini.py",
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

    print("\n--- Service pages (16 × 4 languages) ---")
    written = []
    for slug in SERVICE_SLUGS:
        for lang in LANGS:
            path = output_path(slug, lang)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render_page(slug, lang), encoding="utf-8")
            rel = path.relative_to(ROOT).as_posix()
            written.append(rel)
            print(f"wrote {rel}")

    print("\n--- Articles (Guias e Dicas) ---")
    _run_generate_articles()

    print("\n--- Partners directory (/parceiros/) ---")
    _run_generate_parceiros()

    print("\n--- Font Awesome aria-hidden pass ---")
    _run_fix_fa_aria_hidden()

    print("\n--- Legacy SEO redirects (17× *-lisboa.html + .htaccess) ---")
    _run_generate_lisboa_redirects()

    print("\n--- Sitemap ---")
    _run_generate_sitemap()

    print("\n--- dist/ (GitHub Pages artifact) ---")
    _run_build_dist()

    print("\n--- Gemini code bundle (fazdetudopt-codigo-gemini.txt) ---")
    _run_bundle_for_gemini()

    print(
        f"\nDone: {len(written)} service pages + 4 homepages "
        f"({len(SERVICE_SLUGS)} services × {len(LANGS)} languages)."
    )
    print("Templates: scripts/templates/ | Registry: scripts/slug_registry.py")
    print("Deploy: dist/ (favicons + static assets; see .github/workflows/pages.yml)")


if __name__ == "__main__":
    main()
