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
PRIMARY_OFFICE_STREET_LINE1 = "R. José Saramago"
PRIMARY_OFFICE_STREET_LINE2 = "1675-180 Pontinha"
SECOND_OFFICE_STREET_LINE1 = "R. Ana de Castro Osório"
SECOND_OFFICE_STREET_LINE2 = "2925-060 São Lourenço"
BRAND_NAME = "FAZDETUDO.PT"

# Google Analytics 4 Measurement ID (e.g. "G-XXXXXXXX").
# Empty = analytics loader stays dormant (no gtag / no network calls).
# Even when set, loading still requires explicit consent via FazdetudoAnalytics.grantConsent().
GA4_MEASUREMENT_ID = ""

GOOGLE_REVIEWS_URL = "https://share.google/We1LViOoXucwIwBQl"

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

# Homepage CTAs + chat widget (direct handyman quote). Service pages keep WA_MESSAGE;
# /parceiros/ empty-state and recruit keep their own messages.
HOME_WA_MESSAGE: dict[str, str] = {
    "pt": "Olá! Gostaria de pedir um orçamento para um serviço de faz de tudo/reparação.",
    "en": "Hello! I would like to request a quote for a handyman or home repair service.",
    "es": "¡Hola! Me gustaría solicitar un presupuesto para un servicio de handyman o reparación.",
    "fr": "Bonjour ! Je souhaite demander un devis pour un service de handyman ou de réparation à domicile.",
}

# Homepage SOS / urgent repair strip (photos + location + timing).
# Honest urgency — never promise 24h / guaranteed same-day response.
QUICK_REPAIR_WA_MESSAGE: dict[str, str] = {
    "pt": (
        "Olá! Preciso de uma reparação urgente.\n"
        "\n"
        "Vou enviar algumas fotografias.\n"
        "\n"
        "Localização:\n"
        "Problema:\n"
        "Quando preciso que fique resolvido:\n"
        "\n"
        "Obrigado."
    ),
    "en": (
        "Hello! I need an urgent repair.\n"
        "\n"
        "I will send a few photos.\n"
        "\n"
        "Location:\n"
        "Problem:\n"
        "When I need it done:\n"
        "\n"
        "Thank you."
    ),
    "es": (
        "¡Hola! Necesito una reparación urgente.\n"
        "\n"
        "Voy a enviar algunas fotografías.\n"
        "\n"
        "Ubicación:\n"
        "Problema:\n"
        "Cuándo necesito que quede resuelto:\n"
        "\n"
        "Gracias."
    ),
    "fr": (
        "Bonjour ! J’ai besoin d’une réparation urgente.\n"
        "\n"
        "Je vais envoyer quelques photos.\n"
        "\n"
        "Lieu :\n"
        "Problème :\n"
        "Quand j’ai besoin que ce soit terminé :\n"
        "\n"
        "Merci."
    ),
}


def tel_href() -> str:
    return f"tel:{PHONE_E164}"


def mailto_href() -> str:
    return f"mailto:{EMAIL}"


def wa_href(lang: str = "pt") -> str:
    msg = WA_MESSAGE.get(lang, WA_MESSAGE["pt"])
    return wa_href_for_message(msg)


def wa_href_home(lang: str = "pt") -> str:
    msg = HOME_WA_MESSAGE.get(lang, HOME_WA_MESSAGE["pt"])
    return wa_href_for_message(msg)


def wa_href_quick_repair(lang: str = "pt") -> str:
    msg = QUICK_REPAIR_WA_MESSAGE.get(lang, QUICK_REPAIR_WA_MESSAGE["pt"])
    return wa_href_for_message(msg)


def wa_href_for_message(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def schema_telephone() -> str:
    return PHONE_E164
