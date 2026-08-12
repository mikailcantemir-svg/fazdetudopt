#!/usr/bin/env python3
"""Generate multilingual /parceiros/ directory pages.

Outputs:
  - parceiros/index.html
  - en/parceiros/index.html
  - es/parceiros/index.html
  - fr/parceiros/index.html

Source of truth: scripts/recommended_partners.py
Integrated by scripts/generate-servico-pages.py.
"""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from home_page_i18n import HOME_META, HOME_UI, render_lang_switcher  # noqa: E402
from html_partials import (  # noqa: E402
    render_footer_service,
    render_head,
    render_header_home,
    render_wa_widget,
)
from partner_cards import build_partner_directory_card  # noqa: E402
from recommended_partners import (  # noqa: E402
    PAGE_FILTER_CATEGORY_IDS,
    PAGE_ZONE_FILTER_IDS,
    PARTNER_CATEGORIES,
    PARTNER_ZONES,
    PARTNERS_PAGE_META,
    PARTNERS_PAGE_UI,
    active_partners,
)
from site_config import (  # noqa: E402
    BASE_URL,
    HOME_WA_MESSAGE,
    LOGO_PATH,
    OG_IMAGE,
    wa_href_for_message,
    wa_href_home,
)
from slug_registry import (  # noqa: E402
    LANGS,
    LANG_HTML,
    index_href,
    institutional_asset_prefix,
    institutional_href,
    institutional_url,
    render_institutional_hreflang,
)
from template_engine import render_template  # noqa: E402

PAGE_ID = "parceiros"

OG_LOCALE = {
    "pt": "pt_PT",
    "en": "en_GB",
    "es": "es_ES",
    "fr": "fr_FR",
}


def _options_html(items: list[tuple[str, str]], all_label: str) -> str:
    lines = [
        f'                                <option value="">{html.escape(all_label)}</option>'
    ]
    for value, label in items:
        lines.append(
            f'                                <option value="{html.escape(value)}">'
            f"{html.escape(label)}</option>"
        )
    return "\n".join(lines)


def _recruit_benefits(ui: dict) -> str:
    blocks = []
    for icon, title, text in ui["recruit_benefits"]:
        blocks.append(
            f"""                    <div class="partners-recruit-benefit">
                        <div class="partners-recruit-benefit-icon" aria-hidden="true">
                            <i class="fa-solid fa-{html.escape(icon)}"></i>
                        </div>
                        <h3>{html.escape(title)}</h3>
                        <p>{html.escape(text)}</p>
                    </div>"""
        )
    return "\n".join(blocks)


def _json_ld(lang: str, canonical: str) -> str:
    meta = PARTNERS_PAGE_META[lang]
    data = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": meta["og_title"],
        "description": meta["description"],
        "url": canonical,
        "isPartOf": {"@type": "WebSite", "name": "FAZDETUDO.PT", "url": BASE_URL + "/"},
        "about": {
            "@type": "ItemList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": p["name"],
                }
                for i, p in enumerate(active_partners())
            ],
        },
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_partners_page(lang: str) -> str:
    ui = PARTNERS_PAGE_UI[lang]
    meta = PARTNERS_PAGE_META[lang]
    home_ui = HOME_UI[lang]
    home_meta = HOME_META[lang]
    prefix = institutional_asset_prefix(lang)
    canonical = institutional_url(PAGE_ID, lang)
    home = index_href(lang)

    service_options = _options_html(
        [(cid, PARTNER_CATEGORIES[cid][lang]) for cid in PAGE_FILTER_CATEGORY_IDS],
        ui["service_all"],
    )
    zone_options = _options_html(
        [(zid, PARTNER_ZONES[zid][lang]) for zid in PAGE_ZONE_FILTER_IDS],
        ui["zone_all"],
    )
    cards = "\n".join(
        build_partner_directory_card(
            p,
            lang,
            prefix,
            hidden=False,
            extra_class="partners-listing-card",
        )
        for p in active_partners()
    )

    empty_wa = wa_href_for_message(ui["empty_wa"])
    recruit_wa = wa_href_for_message(ui["recruit_wa"])

    head = render_head(
        page_title=meta["title"],
        meta_description=meta["description"],
        canonical_url=canonical,
        hreflang_block=render_institutional_hreflang(PAGE_ID),
        og_title=meta["og_title"],
        og_description=meta["description"],
        og_locale=OG_LOCALE[lang],
        og_image=OG_IMAGE,
        json_ld=_json_ld(lang, canonical),
        asset_prefix=prefix,
        include_swiper_css=False,
    )
    header = render_header_home(
        asset_prefix=prefix,
        logo_href=home,
        lang_switcher=render_lang_switcher(
            lang,
            href_for_lang=lambda code: institutional_href(PAGE_ID, code),
        ),
        nav_home_href=home,
        nav_services_href=f"{home}#services",
        nav_works_href=f"{home}#recent-work",
        nav_partners_href=institutional_href(PAGE_ID, lang),
        nav_about_href=f"{home}#advantages",
        nav_contact_href=f"{home}#contact",
        nav_home_label=home_ui["nav_home"],
        nav_services_label=home_ui["nav_services"],
        nav_works_label=home_ui["nav_works"],
        nav_partners_label=home_ui["nav_partners"],
        nav_about_label=home_ui["nav_about"],
        nav_contact_label=home_ui["nav_contact"],
        header_quote_label=home_ui.get("header_quote", "Pedir orçamento"),
        wa_href=wa_href_home(lang),
        lang=lang,
        nav_aria=home_meta["nav_aria"],
        logo_alt=home_meta["logo_alt"],
        menu_aria=home_meta["menu_aria"],
    )
    footer = render_footer_service(footer_text=ui["footer"])
    wa_widget = render_wa_widget(
        asset_prefix=prefix,
        wa_online=ui["wa_online"],
        wa_greeting=ui["wa_greeting"],
        wa_placeholder=ui["wa_placeholder"],
        wa_close=ui["wa_close"],
        wa_send=ui["wa_send"],
        wa_float_label=ui["wa_float"],
    )

    home_wa_message = HOME_WA_MESSAGE.get(lang, HOME_WA_MESSAGE["pt"])
    wa_message_attr = html.escape(home_wa_message, quote=True)

    return render_template(
        "parceiros.html",
        {
            "HTML_LANG": LANG_HTML[lang],
            "PAGE_LANG": lang,
            "HEAD": head,
            "HEADER_HOME": header,
            "FOOTER": footer,
            "WA_WIDGET": wa_widget,
            "ASSET_PREFIX": prefix,
            "LOGO_PATH": LOGO_PATH,
            "WA_MESSAGE_ATTR": wa_message_attr,
            "SKIP_LINK": html.escape(ui["skip_link"]),
            "HERO_TITLE": html.escape(ui["hero_title"]),
            "HERO_SUBTITLE": html.escape(ui["hero_subtitle"]),
            "HERO_AREA": html.escape(ui["hero_area"]),
            "SEARCH_TITLE": html.escape(ui["search_title"]),
            "SERVICE_LABEL": html.escape(ui["service_label"]),
            "SERVICE_ARIA": html.escape(ui["service_aria"]),
            "SERVICE_OPTIONS": service_options,
            "ZONE_LABEL": html.escape(ui["zone_label"]),
            "ZONE_ARIA": html.escape(ui["zone_aria"]),
            "ZONE_OPTIONS": zone_options,
            "RESULTS_ARIA": html.escape(ui["results_aria"]),
            "PARTNER_CARDS": cards,
            "EMPTY_TITLE": html.escape(ui["empty_title"]),
            "EMPTY_TEXT": html.escape(ui["empty_text"]),
            "EMPTY_CTA": html.escape(ui["empty_cta"]),
            "EMPTY_WA_HREF": html.escape(empty_wa, quote=True),
            "RECRUIT_TITLE": html.escape(ui["recruit_title"]),
            "RECRUIT_TEXT": html.escape(ui["recruit_text"]),
            "RECRUIT_BENEFITS": _recruit_benefits(ui),
            "RECRUIT_CTA": html.escape(ui["recruit_cta"]),
            "RECRUIT_ARIA": html.escape(ui["recruit_aria"]),
            "RECRUIT_WA_HREF": html.escape(recruit_wa, quote=True),
        },
    )


def output_path(lang: str) -> Path:
    if lang == "pt":
        return ROOT / "parceiros" / "index.html"
    return ROOT / lang / "parceiros" / "index.html"


def main() -> None:
    written = []
    for lang in LANGS:
        path = output_path(lang)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_partners_page(lang), encoding="utf-8")
        written.append(path.relative_to(ROOT).as_posix())
        print(f"wrote {written[-1]}")
    print(f"\nTotal: {len(written)} partners pages")


if __name__ == "__main__":
    main()
