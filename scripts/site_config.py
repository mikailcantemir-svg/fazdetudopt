# -*- coding: utf-8 -*-
"""Central site constants — single source for generators and documentation."""

from __future__ import annotations

from urllib.parse import quote

BASE_URL = "https://www.fazdetudo.pt"
PHONE_E164 = "+351932504112"
PHONE_DISPLAY = "932 504 112"
WHATSAPP_NUMBER = "351932504112"
EMAIL = "geral@fazdetudo.pt"
# Texto visível no HTML (anti-scraping); mailto usa EMAIL real
EMAIL_OBFUSCATED = "geral&#64;fazdetudo.pt"
DEFAULT_ADDRESS = "Grande Lisboa e Margem Sul, Portugal"

GOOGLE_REVIEWS_URL = (
    "https://www.google.com/maps/place/Faz+de+tudo+%7C+HANDYMAN/"
    "@38.760942,-9.2013644,17z/data=!4m6!3m5!1s0xd1ecd0033ab1b83:0x7c1b8284ba4b85da"
    "!8m2!3d38.7609378!4d-9.1987895!16s%2Fg%2F11nc7r6k6j"
)

FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61571666972567"
INSTAGRAM_URL = (
    "https://www.instagram.com/fazdetudo.pt"
    "?igsh=c3Y4OWMwYW85aDEy&utm_source=qr"
)

OG_IMAGE = f"{BASE_URL}/logo.webp"
LOGO_PATH = "logo.webp"

WA_MESSAGE: dict[str, str] = {
    "pt": "Olá! Gostaria de pedir um orçamento.",
    "en": "Hello! I would like to request a quote.",
    "es": "¡Hola! Me gustaría pedir un presupuesto.",
    "fr": "Bonjour ! Je souhaite demander un devis.",
}


def tel_href() -> str:
    return f"tel:{PHONE_E164}"


def mailto_href() -> str:
    return f"mailto:{EMAIL}"


def wa_href(lang: str = "pt") -> str:
    msg = WA_MESSAGE.get(lang, WA_MESSAGE["pt"])
    return wa_href_for_message(msg)


def wa_href_for_message(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def schema_telephone() -> str:
    return PHONE_E164
