# -*- coding: utf-8 -*-
"""Shared HTML builders for partner directory cards."""

from __future__ import annotations

import html

from recommended_partners import (
    PARTNER_CATEGORIES,
    PARTNER_STATUS_LABELS,
    partner_badge_keys,
    partner_category_ids,
    partner_zone_ids,
)
from slug_registry import service_page_href


def build_partner_directory_card(
    partner: dict,
    lang: str,
    prefix: str,
    *,
    hidden: bool = True,
    extra_class: str = "",
) -> str:
    """Render one partner card (homepage directory or /parceiros/ listing)."""
    copy = partner["copy"][lang]
    category_id = partner["category"]
    category_ids = partner_category_ids(partner) or (
        [category_id] if category_id in PARTNER_CATEGORIES else []
    )
    category_label = PARTNER_CATEGORIES[category_id][lang]
    name = html.escape(partner["name"])
    cat_esc = html.escape(category_label)
    card_classes = [
        "partner-dir-card",
        f'partner-dir-card--{html.escape(partner["type"])}',
    ]
    if extra_class:
        card_classes.append(extra_class)
    card_class = " ".join(card_classes)

    status_flags = []
    if partner.get("recommended"):
        status_flags.append("recommended")
    if partner.get("featured"):
        status_flags.append("featured")
    status_attr = " ".join(status_flags) if status_flags else "partner"

    zones = partner_zone_ids(partner)
    zones_attr = html.escape(" ".join(zones), quote=True)
    categories_attr = html.escape(" ".join(category_ids), quote=True)

    badges_html = []
    for key in partner_badge_keys(partner):
        label = PARTNER_STATUS_LABELS[key][lang]
        mod = key.replace("_f", "")
        badges_html.append(
            f'<span class="partner-dir-badge partner-dir-badge--{html.escape(mod)}">'
            f"{html.escape(label)}</span>"
        )
    badges_block = "\n                            ".join(badges_html)

    hidden_attr = " hidden" if hidden else ""
    service_href = html.escape(
        service_page_href(partner["service_slug"], lang), quote=True
    )
    data_attrs = (
        f'data-partner-category="{html.escape(category_id)}" '
        f'data-partner-categories="{categories_attr}" '
        f'data-partner-zones="{zones_attr}" '
        f'data-partner-id="{html.escape(partner["id"])}" '
        f'data-partner-status="{html.escape(status_attr)}"'
    )

    location_html = ""
    if partner.get("location"):
        loc = partner["location"].get(lang) or partner["location"].get("pt")
        if loc:
            location_html = (
                f'\n                        <p class="partner-dir-location">'
                f'<i class="fa-solid fa-location-dot" aria-hidden="true"></i> '
                f"{html.escape(loc)}</p>"
            )

    if partner["type"] == "external":
        website = html.escape(partner["website"], quote=True)
        logo = partner.get("logo")
        if logo:
            logo_src = html.escape(f"{prefix}{logo}", quote=True)
            media_html = (
                f'<div class="partner-dir-media">'
                f'<img src="{logo_src}" alt="{name}" width="72" height="72" '
                f'loading="lazy" decoding="async"></div>'
            )
        else:
            media_html = (
                '<div class="partner-dir-media partner-dir-media--icon" aria-hidden="true">'
                '<i class="fa-solid fa-tv"></i></div>'
            )
        return f"""                <article class="{card_class}" {data_attrs}{hidden_attr}>
                    {media_html}
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-blurb">{html.escape(copy["blurb"])}</p>{location_html}
                        <div class="partner-dir-actions">
                            <a class="partner-dir-btn partner-dir-btn--primary" href="{website}" target="_blank" rel="noopener" aria-label="{html.escape(copy["visit_aria"])}">{html.escape(copy["primary_cta"])}</a>
                            <a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">{html.escape(copy["secondary_cta"])}</a>
                        </div>
                    </div>
                </article>"""

    photo = partner.get("photo")
    if photo:
        photo_src = html.escape(f"{prefix}{photo}", quote=True)
        media_html = (
            f'<div class="partner-dir-media partner-dir-media--photo">'
            f'<img src="{photo_src}" alt="{name}" width="96" height="96" '
            f'loading="lazy" decoding="async"></div>'
        )
    else:
        media_html = (
            '<div class="partner-dir-media partner-dir-media--icon '
            'partner-dir-media--fallback" aria-hidden="true">'
            '<i class="fa-solid fa-helmet-safety"></i></div>'
        )

    tel_href_val = html.escape(partner["tel_href"], quote=True)
    wa_href = partner.get("whatsapp_href")
    wa_btn = ""
    if wa_href:
        wa_href_val = html.escape(wa_href, quote=True)
        wa_label = html.escape(copy.get("whatsapp", "WhatsApp"))
        wa_aria = html.escape(copy.get("wa_aria", wa_label))
        wa_btn = f"""
                            <a class="partner-dir-btn partner-dir-btn--whatsapp" href="{wa_href_val}" target="_blank" rel="noopener noreferrer" aria-label="{wa_aria}">
                                <i class="fa-brands fa-whatsapp" aria-hidden="true"></i>
                                <span>{wa_label}</span>
                            </a>"""
    return f"""                <article class="{card_class}" {data_attrs}{hidden_attr}>
                    {media_html}
                    <div class="partner-dir-body">
                        <div class="partner-dir-meta">
                            {badges_block}
                            <span class="partner-dir-category">{cat_esc}</span>
                        </div>
                        <h3 class="partner-dir-name">{name}</h3>
                        <p class="partner-dir-role">{html.escape(copy["role"])}</p>{location_html}
                        <p class="partner-dir-phone">{html.escape(partner["phone_display"])}</p>
                        <div class="partner-dir-actions">
                            <a class="partner-dir-btn partner-dir-btn--call" href="{tel_href_val}" aria-label="{html.escape(copy["call_aria"])}">
                                <i class="fa-solid fa-phone" aria-hidden="true"></i>
                                <span>{html.escape(copy["call"])}</span>
                            </a>{wa_btn}
                            <a class="partner-dir-btn partner-dir-btn--secondary" href="{service_href}">{html.escape(copy["secondary_cta"])}</a>
                        </div>
                    </div>
                </article>"""
