# -*- coding: utf-8 -*-
"""Central site constants — single source for generators and documentation."""

from __future__ import annotations

from urllib.parse import quote

BASE_URL = "https://www.fazdetudo.pt"
PHONE_E164 = "+351932504112"
PHONE_DISPLAY = "932 504 112"
WHATSAPP_NUMBER = "351932504112"
EMAIL = "geral@fazdetudo.pt"
DEFAULT_ADDRESS = "Grande Lisboa e Margem Sul, Portugal"

GOOGLE_REVIEWS_URL = (
    "https://www.google.com/search?q=Faz+de+tudo+HANDYMAN+Lisboa"
)

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
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(msg)}"
