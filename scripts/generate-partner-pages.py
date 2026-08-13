#!/usr/bin/env python3
"""Generate individual partner profile pages (PT-first).

Output example:
  parceiros/maria-limpezas/index.html

Source of truth for contacts: scripts/recommended_partners.py
SEO/content for each profile lives in partner["profile"].
Does NOT touch homepage HOME_META / H1 / schema.
"""

from __future__ import annotations

import html
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
)
from recommended_partners import (  # noqa: E402
    PARTNER_CATEGORIES,
    PARTNER_PROFILE_UI,
    PARTNER_STATUS_LABELS,
    partner_badge_keys,
    partner_profile_content,
    partner_profile_path,
    partner_profile_seo,
    partner_profile_url,
    partners_with_profiles,
)
from site_config import BASE_URL, OG_IMAGE  # noqa: E402
from template_engine import render_template  # noqa: E402

LANG = "pt"
HTML_LANG = "pt-PT"
OG_LOCALE = "pt_PT"
# Depth: /parceiros/<slug>/ → two levels up to site root
ASSET_PREFIX = "../../"


def _media_html(partner: dict) -> str:
    name = html.escape(partner["name"])
    logo = partner.get("logo")
    photo = partner.get("photo")
    if logo:
        src = html.escape(f"{ASSET_PREFIX}{logo}", quote=True)
        wide = " partner-profile-media--wide" if partner.get("logo_wide") else ""
        return (
            f'<div class="partner-profile-media{wide}">'
            f'<img src="{src}" alt="{name}" width="120" height="120" '
            f'loading="eager" decoding="async"></div>'
        )
    if photo:
        src = html.escape(f"{ASSET_PREFIX}{photo}", quote=True)
        return (
            f'<div class="partner-profile-media partner-profile-media--photo">'
            f'<img src="{src}" alt="{name}" width="120" height="120" '
            f'loading="eager" decoding="async"></div>'
        )
    icon = html.escape(partner.get("icon") or "user")
    return (
        '<div class="partner-profile-media partner-profile-media--icon" aria-hidden="true">'
        f'<i class="fa-solid fa-{icon}"></i></div>'
    )


def _actions_html(partner: dict, ui: dict) -> str:
    parts: list[str] = []
    copy = partner["copy"][LANG]
    ctx = "partner_profile"
    pid = html.escape(partner["id"], quote=True)
    pcat = html.escape(partner["category"], quote=True)
    base_track = (
        f'data-track="partner_contact" data-partner-id="{pid}" '
        f'data-partner-category="{pcat}" data-source-context="{ctx}"'
    )
    if partner.get("tel_href"):
        parts.append(
            f'<a class="btn btn-primary btn-lg partner-profile-btn partner-profile-btn--call" '
            f'href="{html.escape(partner["tel_href"], quote=True)}" '
            f'aria-label="{html.escape(copy.get("call_aria", ui["call"]), quote=True)}" '
            f'{base_track} data-contact-method="phone">'
            f'<i class="fa-solid fa-phone" aria-hidden="true"></i> '
            f'{html.escape(ui["call"])}</a>'
        )
    if partner.get("whatsapp_href"):
        parts.append(
            f'<a class="btn btn-outline btn-lg partner-profile-btn partner-profile-btn--whatsapp" '
            f'href="{html.escape(partner["whatsapp_href"], quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" '
            f'aria-label="{html.escape(copy.get("wa_aria", ui["whatsapp"]), quote=True)}" '
            f'{base_track} data-contact-method="whatsapp">'
            f'<i class="fa-brands fa-whatsapp" aria-hidden="true"></i> '
            f'{html.escape(ui["whatsapp"])}</a>'
        )
    if partner.get("type") == "external" and partner.get("website"):
        cta = partner["copy"][LANG].get("primary_cta", "Visitar site")
        if not cta.rstrip().endswith("→"):
            cta = f"{cta} →"
        parts.append(
            f'<a class="btn btn-primary btn-lg" '
            f'href="{html.escape(partner["website"], quote=True)}" '
            f'target="_blank" rel="noopener noreferrer" '
            f'{base_track} data-contact-method="website">'
            f"{html.escape(cta)}</a>"
        )
    return "\n                        ".join(parts)


def _sections_html(content: dict) -> str:
    blocks: list[str] = []
    for section in content.get("sections") or []:
        blocks.append(f"                <h2>{html.escape(section['h2'])}</h2>")
        blocks.append(f"                {section['html']}")
    return "\n".join(blocks)


def _breadcrumb_html(partner: dict, ui: dict, canonical: str) -> str:
    name = html.escape(partner["name"])
    return (
        f'<a href="{BASE_URL}/">{html.escape(ui["breadcrumb_home"])}</a>'
        '<span aria-hidden="true"> › </span>'
        f'<a href="{BASE_URL}/parceiros/">{html.escape(ui["breadcrumb_partners"])}</a>'
        '<span aria-hidden="true"> › </span>'
        f'<span aria-current="page">{name}</span>'
    )


def _entity_ld(partner: dict, canonical: str) -> dict:
    """Person for direct_contact; Organization for external brands."""
    category_id = partner.get("category")
    category_label = (
        PARTNER_CATEGORIES[category_id][LANG]
        if category_id in PARTNER_CATEGORIES
        else None
    )
    area = (partner.get("location") or {}).get(LANG) or None

    if partner.get("type") == "external":
        entity: dict = {
            "@type": "Organization",
            "name": partner["name"],
            "url": canonical,
        }
        website = partner.get("website")
        if website:
            entity["sameAs"] = website
        if category_label:
            entity["description"] = category_label
        if area:
            entity["areaServed"] = area
        return entity

    entity = {
        "@type": "Person",
        "name": partner["name"],
        "url": canonical,
    }
    if partner.get("tel_href"):
        entity["telephone"] = partner["tel_href"].replace("tel:", "")
    if category_label:
        entity["jobTitle"] = category_label
    if area:
        entity["areaServed"] = area
    return entity


def _json_ld(partner: dict, canonical: str, ui: dict) -> str:
    breadcrumb = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": ui["breadcrumb_home"],
                "item": f"{BASE_URL}/",
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": ui["breadcrumb_partners"],
                "item": f"{BASE_URL}/parceiros/",
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": partner["name"],
                "item": canonical,
            },
        ],
    }

    data = {
        "@context": "https://schema.org",
        "@graph": [_entity_ld(partner, canonical), breadcrumb],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_partner_profile(partner: dict) -> str:
    ui = PARTNER_PROFILE_UI[LANG]
    seo = partner_profile_seo(partner, LANG)
    content = partner_profile_content(partner, LANG)
    if not seo or not content:
        raise ValueError(f"Partner {partner['id']} is missing profile seo/content")

    canonical = partner_profile_url(partner)
    assert canonical

    badge_key = partner_badge_keys(partner)[0]
    badge_label = PARTNER_STATUS_LABELS[badge_key][LANG]
    category_label = PARTNER_CATEGORIES[partner["category"]][LANG]
    location_label = (partner.get("location") or {}).get(LANG) or ""

    location_html = ""
    if location_label:
        location_html = (
            '<p class="partner-profile-location">'
            '<i class="fa-solid fa-location-dot" aria-hidden="true"></i> '
            f"{html.escape(location_label)}</p>"
        )

    phone_display = partner.get("phone_display") or ""
    phone_html = ""
    if phone_display:
        phone_html = (
            f'<p class="partner-profile-phone">{html.escape(phone_display)}</p>'
        )

    contact_items: list[str] = []
    if phone_display:
        contact_items.append(
            f'<li><strong>{html.escape(ui["phone_label"])}:</strong> '
            f"{html.escape(phone_display)}</li>"
        )
    if partner.get("whatsapp_href") and phone_display:
        contact_items.append(
            f'<li><strong>{html.escape(ui["whatsapp_label"])}:</strong> '
            f"{html.escape(phone_display)}</li>"
        )
    contact_parts: list[str] = []
    contact_note = content.get("contact_note")
    if contact_note:
        contact_parts.append(f"<p>{html.escape(contact_note)}</p>")
    if contact_items:
        contact_parts.append(
            '<ul class="partner-profile-contact-list">\n'
            + "\n".join(f"                    {item}" for item in contact_items)
            + "\n                </ul>"
        )
    contact_list_html = "\n                ".join(contact_parts)

    head = render_head(
        page_title=seo["title"],
        meta_description=seo["meta_description"],
        canonical_url=canonical,
        hreflang_block="",  # PT-only profiles: no fake alternates
        og_title=seo.get("og_title") or seo["title"],
        og_description=seo["meta_description"],
        og_locale=OG_LOCALE,
        og_image=OG_IMAGE,
        json_ld=_json_ld(partner, canonical, ui),
        asset_prefix=ASSET_PREFIX,
        include_swiper_css=False,
    )
    header = render_header_service(
        asset_prefix=ASSET_PREFIX,
        index_href=f"{BASE_URL}/parceiros/",
        back_label=ui["back_partners"],
        logo_href=f"{BASE_URL}/",
    )

    footer = render_footer_service(
        footer_text="FAZDETUDO.PT. Todos os direitos reservados."
    )

    return render_template(
        "partner-profile.html",
        {
            "HTML_LANG": HTML_LANG,
            "PAGE_LANG": LANG,
            "HEAD": head,
            "SKIP_LINK": "Saltar para o conteúdo",
            "HEADER_SERVICE": header,
            "FOOTER": footer,
            "ASSET_PREFIX": ASSET_PREFIX,
            "BREADCRUMB_HTML": _breadcrumb_html(partner, ui, canonical),
            "MEDIA_HTML": _media_html(partner),
            "BADGE_LABEL": html.escape(badge_label),
            "H1_TITLE": html.escape(seo["h1"]),
            "CATEGORY_LABEL": html.escape(category_label),
            "LOCATION_HTML": location_html,
            "PHONE_HTML": phone_html,
            "ACTIONS_HTML": _actions_html(partner, ui),
            "INTRO_HTML": html.escape(content["intro"]),
            "SECTIONS_HTML": _sections_html(content),
            "CONTACT_H2": html.escape(ui["contact_h2"].format(name=partner["name"])),
            "CONTACT_LIST_HTML": contact_list_html,
            "PARTNERS_HREF": f"{BASE_URL}/parceiros/",
            "BACK_PARTNERS": html.escape(ui["back_partners"]),
        },
    )


def main() -> None:
    written: list[str] = []
    for partner in partners_with_profiles():
        rel = partner_profile_path(partner)
        assert rel
        out_dir = ROOT / rel
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "index.html"
        html_out = render_partner_profile(partner)
        # Avoid trailing whitespace that fails git diff --check
        html_out = "\n".join(line.rstrip() for line in html_out.splitlines()) + "\n"
        out_path.write_text(html_out, encoding="utf-8")
        written.append(rel + "index.html")
        print(f"wrote {rel}index.html")
    print(f"Total: {len(written)} partner profile pages")


if __name__ == "__main__":
    main()
