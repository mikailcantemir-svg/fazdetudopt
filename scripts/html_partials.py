# -*- coding: utf-8 -*-
"""Compose page fragments from scripts/templates/partials/."""

from __future__ import annotations

from template_engine import render_partial
from analytics_bootstrap import analytics_bootstrap_html
from site_config import (
    EMAIL_OBFUSCATED,
    FACEBOOK_URL,
    INSTAGRAM_URL,
    LOGO_PATH,
    OG_IMAGE,
    PHONE_DISPLAY,
    PRIMARY_OFFICE_STREET_LINE1,
    PRIMARY_OFFICE_STREET_LINE2,
    SECOND_OFFICE_STREET_LINE1,
    SECOND_OFFICE_STREET_LINE2,
    tel_href,
    wa_href_home,
)

SWIPER_STYLESHEET = (
    '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css">\n'
)


def render_head(
    *,
    page_title: str,
    meta_description: str,
    canonical_url: str,
    hreflang_block: str,
    og_title: str,
    og_description: str,
    og_locale: str,
    og_image: str = OG_IMAGE,
    json_ld: str,
    asset_prefix: str,
    include_swiper_css: bool = False,
    faq_json_ld: str = "",
) -> str:
    extra_styles = SWIPER_STYLESHEET if include_swiper_css else ""
    faq_block = ""
    if faq_json_ld.strip():
        faq_block = (
            '\n    <script type="application/ld+json" id="faq-schema">\n'
            f"    {faq_json_ld}\n"
            "    </script>"
        )
    return render_partial(
        "head.html",
        {
            "PAGE_TITLE": page_title,
            "META_DESCRIPTION": meta_description,
            "CANONICAL_URL": canonical_url,
            "HREFLANG_BLOCK": hreflang_block,
            "OG_TITLE": og_title,
            "OG_DESCRIPTION": og_description,
            "OG_LOCALE": og_locale,
            "OG_IMAGE": og_image,
            "JSON_LD": json_ld,
            "FAQ_JSON_LD": faq_block,
            "ASSET_PREFIX": asset_prefix,
            "LOGO_PATH": LOGO_PATH,
            "EXTRA_STYLESHEETS": extra_styles,
            "ANALYTICS_BOOTSTRAP": analytics_bootstrap_html(),
        },
    )


def render_header_home(
    *,
    asset_prefix: str,
    logo_href: str,
    lang_switcher: str,
    nav_home_href: str = "#hero",
    nav_services_href: str = "#services",
    nav_works_href: str = "#recent-work",
    nav_partners_href: str = "#parceiros-recomendados",
    nav_about_href: str = "#advantages",
    nav_contact_href: str = "#contact",
    nav_home_label: str = "Início",
    nav_services_label: str = "Serviços",
    nav_works_label: str = "Trabalhos",
    nav_partners_label: str = "Parceiros",
    nav_about_label: str = "Sobre nós",
    nav_contact_label: str = "Contacto",
    header_quote_label: str = "Pedir orçamento",
    wa_href: str | None = None,
    lang: str = "pt",
    nav_aria: str = "Navegação principal",
    logo_alt: str = "FAZDETUDO.PT - Handyman e faz-tudo em Lisboa",
    menu_aria: str = "Abrir menu",
) -> str:
    return render_partial(
        "header-home.html",
        {
            "ASSET_PREFIX": asset_prefix,
            "LOGO_PATH": LOGO_PATH,
            "LOGO_HREF": logo_href,
            "LOGO_ALT": logo_alt,
            "LANG_SWITCHER": lang_switcher,
            "TEL_HREF": tel_href(),
            "PHONE_DISPLAY": PHONE_DISPLAY,
            "WA_HREF": wa_href if wa_href is not None else wa_href_home(lang),
            "HEADER_QUOTE_LABEL": header_quote_label,
            "NAV_HOME_HREF": nav_home_href,
            "NAV_SERVICES_HREF": nav_services_href,
            "NAV_WORKS_HREF": nav_works_href,
            "NAV_PARTNERS_HREF": nav_partners_href,
            "NAV_ABOUT_HREF": nav_about_href,
            "NAV_CONTACT_HREF": nav_contact_href,
            "NAV_HOME_LABEL": nav_home_label,
            "NAV_SERVICES_LABEL": nav_services_label,
            "NAV_WORKS_LABEL": nav_works_label,
            "NAV_PARTNERS_LABEL": nav_partners_label,
            "NAV_ABOUT_LABEL": nav_about_label,
            "NAV_CONTACT_LABEL": nav_contact_label,
            "NAV_ARIA": nav_aria,
            "MENU_ARIA": menu_aria,
        },
    )


def render_header_service(
    *,
    asset_prefix: str,
    index_href: str,
    back_label: str,
    logo_href: str | None = None,
) -> str:
    return render_partial(
        "header-service.html",
        {
            "ASSET_PREFIX": asset_prefix,
            "LOGO_PATH": LOGO_PATH,
            "LOGO_HREF": logo_href or index_href,
            "INDEX_HREF": index_href,
            "BACK_LABEL": back_label,
            "TEL_HREF": tel_href(),
            "PHONE_DISPLAY": PHONE_DISPLAY,
        },
    )


def render_footer_home(
    *,
    asset_prefix: str,
    email_href: str,
    footer_services: str,
) -> str:
    return render_partial(
        "footer.html",
        {
            "ASSET_PREFIX": asset_prefix,
            "LOGO_PATH": LOGO_PATH,
            "TEL_HREF": tel_href(),
            "EMAIL_HREF": email_href,
            "PHONE_DISPLAY": PHONE_DISPLAY,
            "EMAIL_OBFUSCATED": EMAIL_OBFUSCATED,
            "FACEBOOK_URL": FACEBOOK_URL,
            "INSTAGRAM_URL": INSTAGRAM_URL,
            "FOOTER_SERVICES": footer_services,
            "PRIMARY_OFFICE_STREET_LINE1": PRIMARY_OFFICE_STREET_LINE1,
            "PRIMARY_OFFICE_STREET_LINE2": PRIMARY_OFFICE_STREET_LINE2,
            "SECOND_OFFICE_STREET_LINE1": SECOND_OFFICE_STREET_LINE1,
            "SECOND_OFFICE_STREET_LINE2": SECOND_OFFICE_STREET_LINE2,
        },
    )


def render_footer_service(*, footer_text: str) -> str:
    return render_partial("footer-service.html", {"FOOTER_TEXT": footer_text})


def render_wa_widget(
    *,
    asset_prefix: str,
    wa_online: str,
    wa_greeting: str,
    wa_placeholder: str,
    wa_close: str,
    wa_send: str,
    wa_float_label: str,
) -> str:
    return render_partial(
        "wa-widget.html",
        {
            "ASSET_PREFIX": asset_prefix,
            "LOGO_PATH": LOGO_PATH,
            "WA_ONLINE": wa_online,
            "WA_GREETING": wa_greeting,
            "WA_PLACEHOLDER": wa_placeholder,
            "WA_CLOSE": wa_close,
            "WA_SEND": wa_send,
            "WA_FLOAT_LABEL": wa_float_label,
        },
    )
