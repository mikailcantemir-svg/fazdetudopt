"""
Centralized partners directory (homepage).

Flags (independent — paid featured ≠ recommended):
  active       → shown in directory when True
  recommended  → validated/trusted ("Parceiro recomendado")
  featured     → paid commercial highlight ("Em destaque")

Badge rules:
  - If recommended: show recommended badge (gender-aware via feminine=True).
  - Else: show "Parceiro FAZDETUDO.PT".
  - If featured: also show "Em destaque".

Add a partner:
  1. Ensure category in PARTNER_CATEGORIES (+ FILTER_CATEGORY_IDS if new).
  2. Append to RECOMMENDED_PARTNERS with active/recommended/featured.
  3. python scripts/generate-servico-pages.py
"""

from __future__ import annotations

PARTNER_CATEGORIES: dict[str, dict[str, str]] = {
    "avac": {
        "pt": "Ar Condicionado / AVAC",
        "en": "Air Conditioning / HVAC",
        "es": "Aire acondicionado / AVAC",
        "fr": "Climatisation / CVC",
    },
    "limpezas": {
        "pt": "Limpezas",
        "en": "Cleaning",
        "es": "Limpiezas",
        "fr": "Ménage",
    },
    "pinturas": {
        "pt": "Pinturas",
        "en": "Painting",
        "es": "Pintura",
        "fr": "Peinture",
    },
    "canalizacoes": {
        "pt": "Canalizações",
        "en": "Plumbing",
        "es": "Fontanería",
        "fr": "Plomberie",
    },
    "electricidade": {
        "pt": "Electricidade",
        "en": "Electrical",
        "es": "Electricidad",
        "fr": "Électricité",
    },
    "carpintaria": {
        "pt": "Carpintaria",
        "en": "Carpentry",
        "es": "Carpintería",
        "fr": "Menuiserie",
    },
    "jardinagem": {
        "pt": "Jardinagem",
        "en": "Gardening",
        "es": "Jardinería",
        "fr": "Jardinage",
    },
    "piscinas": {
        "pt": "Piscinas",
        "en": "Pools",
        "es": "Piscinas",
        "fr": "Piscines",
    },
}

FILTER_CATEGORY_IDS = ("avac", "limpezas")

PARTNER_STATUS_LABELS = {
    "partner": {
        "pt": "Parceiro FAZDETUDO.PT",
        "en": "FAZDETUDO.PT partner",
        "es": "Colaborador FAZDETUDO.PT",
        "fr": "Partenaire FAZDETUDO.PT",
    },
    "recommended": {
        "pt": "Parceiro recomendado",
        "en": "Recommended partner",
        "es": "Colaborador recomendado",
        "fr": "Partenaire recommandé",
    },
    "recommended_f": {
        "pt": "Parceira recomendada",
        "en": "Recommended partner",
        "es": "Colaboradora recomendada",
        "fr": "Partenaire recommandée",
    },
    "featured": {
        "pt": "Em destaque",
        "en": "Featured",
        "es": "Destacado",
        "fr": "En vedette",
    },
}

PARTNER_DIRECTORY_UI = {
    "pt": {
        "title": "Que profissional procura?",
        "subtitle": "Escolha o serviço e encontre profissionais disponíveis para contacto direto.",
        "select_label": "Selecione um serviço",
        "select_placeholder": "Selecione um serviço",
        "select_aria": "Selecionar um serviço para ver profissionais",
        "empty": "Ainda não há parceiros nesta categoria. Em breve teremos novidades.",
        "results_aria": "Profissionais disponíveis",
    },
    "en": {
        "title": "Which professional do you need?",
        "subtitle": "Choose a service and find professionals available for direct contact.",
        "select_label": "Select a service",
        "select_placeholder": "Select a service",
        "select_aria": "Select a service to see professionals",
        "empty": "No partners in this category yet. More coming soon.",
        "results_aria": "Available professionals",
    },
    "es": {
        "title": "¿Qué profesional busca?",
        "subtitle": "Elija el servicio y encuentre profesionales disponibles para contacto directo.",
        "select_label": "Seleccione un servicio",
        "select_placeholder": "Seleccione un servicio",
        "select_aria": "Seleccionar un servicio para ver profesionales",
        "empty": "Aún no hay colaboradores en esta categoría. Pronto habrá novedades.",
        "results_aria": "Profesionales disponibles",
    },
    "fr": {
        "title": "Quel professionnel recherchez-vous ?",
        "subtitle": "Choisissez le service et trouvez des professionnels disponibles pour un contact direct.",
        "select_label": "Sélectionnez un service",
        "select_placeholder": "Sélectionnez un service",
        "select_aria": "Sélectionner un service pour voir les professionnels",
        "empty": "Pas encore de partenaires dans cette catégorie. Bientôt de nouvelles options.",
        "results_aria": "Professionnels disponibles",
    },
}

HOW_IT_WORKS = {
    "pt": {
        "title": "Encontrar um profissional é simples",
        "steps": [
            (
                "1",
                "list",
                "Escolha o serviço",
                "Diga-nos que tipo de profissional procura.",
            ),
            (
                "2",
                "users",
                "Veja os profissionais disponíveis",
                "Consulte parceiros, especialidades e formas de contacto.",
            ),
            (
                "3",
                "comments",
                "Contacte diretamente",
                "Ligue, envie WhatsApp ou visite o site do profissional.",
            ),
        ],
    },
    "en": {
        "title": "Finding a professional is simple",
        "steps": [
            (
                "1",
                "list",
                "Choose the service",
                "Tell us what kind of professional you need.",
            ),
            (
                "2",
                "users",
                "See available professionals",
                "Browse partners, specialties and contact options.",
            ),
            (
                "3",
                "comments",
                "Contact them directly",
                "Call, message on WhatsApp or visit the professional's website.",
            ),
        ],
    },
    "es": {
        "title": "Encontrar un profesional es sencillo",
        "steps": [
            (
                "1",
                "list",
                "Elija el servicio",
                "Díganos qué tipo de profesional busca.",
            ),
            (
                "2",
                "users",
                "Vea los profesionales disponibles",
                "Consulte colaboradores, especialidades y formas de contacto.",
            ),
            (
                "3",
                "comments",
                "Contacte directamente",
                "Llame, envíe WhatsApp o visite el sitio del profesional.",
            ),
        ],
    },
    "fr": {
        "title": "Trouver un professionnel, c'est simple",
        "steps": [
            (
                "1",
                "list",
                "Choisissez le service",
                "Indiquez le type de professionnel dont vous avez besoin.",
            ),
            (
                "2",
                "users",
                "Voyez les professionnels disponibles",
                "Consultez partenaires, spécialités et moyens de contact.",
            ),
            (
                "3",
                "comments",
                "Contactez directement",
                "Appelez, écrivez sur WhatsApp ou visitez le site du professionnel.",
            ),
        ],
    },
}


def partner_badge_keys(partner: dict) -> list[str]:
    """Return status badge keys for a partner (order = display order)."""
    keys: list[str] = []
    if partner.get("recommended"):
        keys.append("recommended_f" if partner.get("feminine") else "recommended")
    else:
        keys.append("partner")
    if partner.get("featured"):
        keys.append("featured")
    return keys


def active_partners() -> list[dict]:
    return [p for p in RECOMMENDED_PARTNERS if p.get("active", True)]


# type: "external" | "direct_contact"
RECOMMENDED_PARTNERS: list[dict] = [
    {
        "id": "airfix",
        "active": True,
        "category": "avac",
        "type": "external",
        "name": "AirFix.pt",
        "recommended": True,
        "featured": False,
        "logo": "assets/partners/airfix-icon.png",
        "website": "https://airfix.pt/",
        "service_slug": "servico-climatizacao.html",
        "copy": {
            "pt": {
                "blurb": (
                    "Instalação, manutenção, limpeza e assistência técnica de ar condicionado."
                ),
                "primary_cta": "Visitar AirFix.pt",
                "secondary_cta": "Ver serviços de AVAC",
                "visit_aria": "Visitar AirFix.pt",
            },
            "en": {
                "blurb": (
                    "Air conditioning installation, maintenance, cleaning and technical support."
                ),
                "primary_cta": "Visit AirFix.pt",
                "secondary_cta": "View HVAC services",
                "visit_aria": "Visit AirFix.pt",
            },
            "es": {
                "blurb": (
                    "Instalación, mantenimiento, limpieza y asistencia técnica de aire acondicionado."
                ),
                "primary_cta": "Visitar AirFix.pt",
                "secondary_cta": "Ver servicios de AVAC",
                "visit_aria": "Visitar AirFix.pt",
            },
            "fr": {
                "blurb": (
                    "Installation, entretien, nettoyage et assistance technique en climatisation."
                ),
                "primary_cta": "Visiter AirFix.pt",
                "secondary_cta": "Voir les services CVC",
                "visit_aria": "Visiter AirFix.pt",
            },
        },
    },
    {
        "id": "caterina",
        "active": True,
        "category": "limpezas",
        "type": "direct_contact",
        "name": "Caterina",
        "recommended": True,
        "featured": False,
        "feminine": True,
        "photo": "assets/partners/caterina.jpg",
        "phone_display": "963 212 185",
        "tel_href": "tel:+351963212185",
        "whatsapp_href": "https://wa.me/351963212185",
        "service_slug": "servico-limpezas.html",
        "copy": {
            "pt": {
                "role": "Empregada de limpeza · contacto direto",
                "call": "Ligar",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Ver serviço",
                "call_aria": "Ligar diretamente para Caterina, parceira de limpezas",
                "wa_aria": "Contactar Caterina por WhatsApp",
            },
            "en": {
                "role": "Cleaning professional · direct contact",
                "call": "Call",
                "whatsapp": "WhatsApp",
                "secondary_cta": "View service",
                "call_aria": "Call Caterina directly, recommended cleaning partner",
                "wa_aria": "Contact Caterina on WhatsApp",
            },
            "es": {
                "role": "Profesional de limpieza · contacto directo",
                "call": "Llamar",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Ver servicio",
                "call_aria": "Llamar directamente a Caterina, colaboradora de limpieza",
                "wa_aria": "Contactar a Caterina por WhatsApp",
            },
            "fr": {
                "role": "Professionnelle du ménage · contact direct",
                "call": "Appeler",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Voir le service",
                "call_aria": "Appeler directement Caterina, partenaire ménage recommandée",
                "wa_aria": "Contacter Caterina sur WhatsApp",
            },
        },
    },
]
