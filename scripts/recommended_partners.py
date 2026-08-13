"""
Centralized partners directory (homepage + /parceiros/).

Flags (independent — paid featured ≠ recommended):
  active       → shown in directory when True
  recommended  → validated/trusted ("Parceiro recomendado")
  featured     → paid commercial highlight ("Em destaque")

Badge rules:
  - If recommended: show recommended badge (gender-aware via feminine=True).
  - Else: show "Parceiro FAZDETUDO.PT".
  - If featured: also show "Em destaque".

Optional fields:
  location    → i18n display string for the card
  zones       → list of zone ids (a partner may cover several)
  categories  → optional list of category ids for multi-category filters
                (falls back to [category] when omitted)

Add a partner:
  1. Ensure category in PARTNER_CATEGORIES (+ FILTER_CATEGORY_IDS / PAGE_FILTER_CATEGORY_IDS).
  2. Append to RECOMMENDED_PARTNERS with active/recommended/featured.
  3. python scripts/generate-servico-pages.py
"""

from __future__ import annotations

from site_config import BASE_URL

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
    "instalacao-tv": {
        "pt": "Instalação de TV na Parede",
        "en": "TV Wall Mounting",
        "es": "Instalación de TV en Pared",
        "fr": "Installation de TV au Mur",
    },
    "obras-gerais": {
        "pt": "Obras Gerais",
        "en": "General Construction Works",
        "es": "Obras Generales",
        "fr": "Travaux Généraux",
    },
    "recuperacao-casa": {
        "pt": "Recuperação de Casas",
        "en": "Home Restoration",
        "es": "Rehabilitación de Viviendas",
        "fr": "Rénovation de Maisons",
    },
    "remodelacoes-gerais": {
        "pt": "Remodelações Gerais",
        "en": "General Renovations",
        "es": "Reformas Generales",
        "fr": "Rénovations Générales",
    },
}

# Homepage partner finder — ordered subset; runtime filters to categories with partners.
FILTER_CATEGORY_IDS = (
    "avac",
    "limpezas",
    "instalacao-tv",
    "obras-gerais",
    "recuperacao-casa",
    "remodelacoes-gerais",
)

# Full partners page — all service filters prepared for growth
PAGE_FILTER_CATEGORY_IDS = (
    "avac",
    "limpezas",
    "instalacao-tv",
    "pinturas",
    "canalizacoes",
    "electricidade",
    "carpintaria",
    "jardinagem",
    "piscinas",
    "obras-gerais",
    "recuperacao-casa",
    "remodelacoes-gerais",
)

PARTNER_ZONES: dict[str, dict[str, str]] = {
    "grande-lisboa": {
        "pt": "Grande Lisboa",
        "en": "Greater Lisbon",
        "es": "Gran Lisboa",
        "fr": "Grand Lisbonne",
    },
    "lisboa": {
        "pt": "Lisboa",
        "en": "Lisbon",
        "es": "Lisboa",
        "fr": "Lisbonne",
    },
    "cascais-oeiras": {
        "pt": "Cascais / Oeiras",
        "en": "Cascais / Oeiras",
        "es": "Cascais / Oeiras",
        "fr": "Cascais / Oeiras",
    },
    "sintra": {
        "pt": "Sintra",
        "en": "Sintra",
        "es": "Sintra",
        "fr": "Sintra",
    },
    "margem-sul": {
        "pt": "Margem Sul",
        "en": "South Bank",
        "es": "Margen Sur",
        "fr": "Rive Sud",
    },
    "azeitao": {
        "pt": "Azeitão",
        "en": "Azeitão",
        "es": "Azeitão",
        "fr": "Azeitão",
    },
    "setubal": {
        "pt": "Setúbal",
        "en": "Setúbal",
        "es": "Setúbal",
        "fr": "Setúbal",
    },
}

PAGE_ZONE_FILTER_IDS = (
    "grande-lisboa",
    "lisboa",
    "cascais-oeiras",
    "sintra",
    "margem-sul",
    "azeitao",
    "setubal",
)

PARTNER_STATUS_LABELS = {
    "partner": {
        "pt": "Parceiro FAZDETUDO.PT",
        "en": "FAZDETUDO.PT partner",
        "es": "Colaborador FAZDETUDO.PT",
        "fr": "Partenaire FAZDETUDO.PT",
    },
    "partner_f": {
        "pt": "Parceira FAZDETUDO.PT",
        "en": "FAZDETUDO.PT partner",
        "es": "Colaboradora FAZDETUDO.PT",
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
        "kicker": "SERVIÇOS ESPECIALIZADOS",
        "title": "Procura um serviço especializado?",
        "subtitle": (
            "Escolha o serviço de que precisa e veja imediatamente os profissionais disponíveis."
        ),
        "handyman_note": "Para pequenas reparações e handyman, fale diretamente connosco.",
        "handyman_cta": "Pedir orçamento por WhatsApp →",
        "handyman_aria": "Pedir orçamento handyman por WhatsApp à FAZDETUDO.PT",
        "select_label": "Que serviço procura?",
        "select_placeholder": "Que serviço procura?",
        "select_aria": "Selecionar um serviço para ver parceiros disponíveis",
        "services_available": "Serviços disponíveis",
        "back_services": "Ver todos os serviços",
        "count_one": "1 profissional disponível",
        "count_many": "{n} profissionais disponíveis",
        "results_aria": "Resultados de parceiros",
        "empty": "Ainda não há parceiros nesta categoria. Em breve teremos novidades.",
        "cta_all": "Ver todos os parceiros →",
    },
    "en": {
        "kicker": "SPECIALIST SERVICES",
        "title": "Looking for a specialist service?",
        "subtitle": (
            "Choose the service you need and see available professionals immediately."
        ),
        "handyman_note": "For small repairs and handyman jobs, contact us directly.",
        "handyman_cta": "Request a quote on WhatsApp →",
        "handyman_aria": "Request a handyman quote on WhatsApp from FAZDETUDO.PT",
        "select_label": "What service do you need?",
        "select_placeholder": "What service do you need?",
        "select_aria": "Select a service to see available partners",
        "services_available": "Available services",
        "back_services": "View all services",
        "count_one": "1 professional available",
        "count_many": "{n} professionals available",
        "results_aria": "Partner results",
        "empty": "No partners in this category yet. More coming soon.",
        "cta_all": "View all partners →",
    },
    "es": {
        "kicker": "SERVICIOS ESPECIALIZADOS",
        "title": "¿Busca un servicio especializado?",
        "subtitle": (
            "Elija el servicio que necesita y vea de inmediato los profesionales disponibles."
        ),
        "handyman_note": "Para pequeñas reparaciones y handyman, hable directamente con nosotros.",
        "handyman_cta": "Pedir presupuesto por WhatsApp →",
        "handyman_aria": "Pedir presupuesto handyman por WhatsApp a FAZDETUDO.PT",
        "select_label": "¿Qué servicio busca?",
        "select_placeholder": "¿Qué servicio busca?",
        "select_aria": "Seleccionar un servicio para ver colaboradores disponibles",
        "services_available": "Servicios disponibles",
        "back_services": "Ver todos los servicios",
        "count_one": "1 profesional disponible",
        "count_many": "{n} profesionales disponibles",
        "results_aria": "Resultados de colaboradores",
        "empty": "Aún no hay colaboradores en esta categoría. Pronto habrá novedades.",
        "cta_all": "Ver todos los colaboradores →",
    },
    "fr": {
        "kicker": "SERVICES SPÉCIALISÉS",
        "title": "Vous recherchez un service spécialisé ?",
        "subtitle": (
            "Choisissez le service dont vous avez besoin et consultez immédiatement "
            "les professionnels disponibles."
        ),
        "handyman_note": "Pour les petites réparations et le handyman, contactez-nous directement.",
        "handyman_cta": "Demander un devis sur WhatsApp →",
        "handyman_aria": "Demander un devis handyman sur WhatsApp à FAZDETUDO.PT",
        "select_label": "Quel service recherchez-vous ?",
        "select_placeholder": "Quel service recherchez-vous ?",
        "select_aria": "Sélectionner un service pour voir les partenaires disponibles",
        "services_available": "Services disponibles",
        "back_services": "Voir tous les services",
        "count_one": "1 professionnel disponible",
        "count_many": "{n} professionnels disponibles",
        "results_aria": "Résultats des partenaires",
        "empty": "Pas encore de partenaires dans cette catégorie. Bientôt de nouvelles options.",
        "cta_all": "Voir tous les partenaires →",
    },
}

# Font Awesome icons for homepage category tiles (no marketplace imagery).
PARTNER_CATEGORY_ICONS: dict[str, str] = {
    "avac": "snowflake",
    "limpezas": "broom",
    "instalacao-tv": "tv",
    "obras-gerais": "helmet-safety",
    "recuperacao-casa": "house",
    "remodelacoes-gerais": "paint-roller",
    "pinturas": "paint-roller",
    "canalizacoes": "faucet",
    "electricidade": "bolt",
    "carpintaria": "hammer",
    "jardinagem": "leaf",
    "piscinas": "water",
}

PARTNERS_PAGE_META = {
    "pt": {
        "title": "Profissionais e Parceiros em Lisboa | FAZDETUDO.PT",
        "description": (
            "Encontre profissionais para AVAC, limpezas, canalização, eletricidade, "
            "pinturas e outros serviços na Grande Lisboa, Margem Sul e Setúbal."
        ),
        "og_title": "Profissionais e Parceiros | FAZDETUDO.PT",
    },
    "en": {
        "title": "Professionals and Partners in Lisbon | FAZDETUDO.PT",
        "description": (
            "Find professionals for HVAC, cleaning, plumbing, electrical, painting "
            "and more across Greater Lisbon, the South Bank and Setúbal."
        ),
        "og_title": "Professionals and Partners | FAZDETUDO.PT",
    },
    "es": {
        "title": "Profesionales y colaboradores en Lisboa | FAZDETUDO.PT",
        "description": (
            "Encuentre profesionales de AVAC, limpieza, fontanería, electricidad, "
            "pintura y más en Gran Lisboa, Margen Sur y Setúbal."
        ),
        "og_title": "Profesionales y colaboradores | FAZDETUDO.PT",
    },
    "fr": {
        "title": "Professionnels et partenaires à Lisbonne | FAZDETUDO.PT",
        "description": (
            "Trouvez des professionnels pour CVC, ménage, plomberie, électricité, "
            "peinture et plus dans le Grand Lisbonne, la Rive Sud et Setúbal."
        ),
        "og_title": "Professionnels et partenaires | FAZDETUDO.PT",
    },
}

PARTNERS_PAGE_UI = {
    "pt": {
        "skip_link": "Saltar para o conteúdo",
        "hero_title": "Encontre o profissional certo para o seu serviço",
        "hero_subtitle": (
            "Consulte profissionais e empresas da rede FAZDETUDO.PT e contacte "
            "diretamente quem melhor responde ao que procura."
        ),
        "hero_area": "Grande Lisboa · Margem Sul · Setúbal",
        "search_title": "Procurar profissionais",
        "service_label": "Serviço",
        "service_all": "Todos os serviços",
        "service_aria": "Filtrar por serviço",
        "zone_label": "Zona",
        "zone_all": "Todas as zonas",
        "zone_aria": "Filtrar por zona",
        "results_aria": "Resultados da pesquisa de profissionais",
        "empty_title": "Ainda não temos um parceiro disponível para este serviço.",
        "empty_text": "Fale connosco e tentaremos ajudá-lo a encontrar uma solução.",
        "empty_cta": "Pedir ajuda",
        "empty_wa": (
            "Olá! Procuro um profissional através da FAZDETUDO.PT e ainda não "
            "encontrei na categoria/zona que selecionei. Podem ajudar-me?"
        ),
        "recruit_title": "É profissional? Apareça na FAZDETUDO.PT",
        "recruit_text": (
            "Divulgue os seus serviços perante clientes que já estão à procura "
            "de profissionais na sua área."
        ),
        "recruit_benefits": [
            (
                "id-card",
                "Perfil profissional",
                "Nome, serviço, zona e contactos.",
            ),
            (
                "comments",
                "Contacto direto",
                "Os clientes falam diretamente consigo.",
            ),
            (
                "arrow-trend-up",
                "Maior destaque",
                "Possibilidade de obter maior visibilidade através dos nossos planos para parceiros.",
            ),
        ],
        "recruit_cta": "Quero ser parceiro",
        "recruit_wa": (
            "Olá! Sou profissional e gostaria de saber como posso aparecer na "
            "FAZDETUDO.PT e quais são os planos para parceiros."
        ),
        "recruit_aria": "Contactar FAZDETUDO.PT no WhatsApp para ser parceiro",
        "nav_back": "Voltar ao início",
        "wa_online": "Online",
        "wa_greeting": "Olá! Como podemos ajudar?",
        "wa_placeholder": "Escreva a sua mensagem…",
        "wa_close": "Fechar chat",
        "wa_send": "Enviar",
        "wa_float": "WhatsApp",
        "footer": "FAZDETUDO.PT. Todos os direitos reservados.",
    },
    "en": {
        "skip_link": "Skip to content",
        "hero_title": "Find the right professional for your job",
        "hero_subtitle": (
            "Browse professionals and companies in the FAZDETUDO.PT network and "
            "contact directly whoever best matches what you need."
        ),
        "hero_area": "Greater Lisbon · South Bank · Setúbal",
        "search_title": "Search professionals",
        "service_label": "Service",
        "service_all": "All services",
        "service_aria": "Filter by service",
        "zone_label": "Area",
        "zone_all": "All areas",
        "zone_aria": "Filter by area",
        "results_aria": "Professional search results",
        "empty_title": "We don't have a partner available for this service yet.",
        "empty_text": "Talk to us and we'll try to help you find a solution.",
        "empty_cta": "Ask for help",
        "empty_wa": (
            "Hello! I'm looking for a professional through FAZDETUDO.PT and "
            "couldn't find one in the category/area I selected. Can you help?"
        ),
        "recruit_title": "Are you a professional? Appear on FAZDETUDO.PT",
        "recruit_text": (
            "Promote your services to clients who are already looking for "
            "professionals in your area."
        ),
        "recruit_benefits": [
            (
                "id-card",
                "Professional profile",
                "Name, service, area and contacts.",
            ),
            (
                "comments",
                "Direct contact",
                "Clients speak with you directly.",
            ),
            (
                "arrow-trend-up",
                "Greater visibility",
                "Option to get more visibility through our partner plans.",
            ),
        ],
        "recruit_cta": "I want to become a partner",
        "recruit_wa": (
            "Hello! I'm a professional and I'd like to know how I can appear on "
            "FAZDETUDO.PT and what the partner plans are."
        ),
        "recruit_aria": "Contact FAZDETUDO.PT on WhatsApp to become a partner",
        "nav_back": "Back to home",
        "wa_online": "Online",
        "wa_greeting": "Hello! How can we help?",
        "wa_placeholder": "Type your message…",
        "wa_close": "Close chat",
        "wa_send": "Send",
        "wa_float": "WhatsApp",
        "footer": "FAZDETUDO.PT. All rights reserved.",
    },
    "es": {
        "skip_link": "Saltar al contenido",
        "hero_title": "Encuentre al profesional adecuado para su servicio",
        "hero_subtitle": (
            "Consulte profesionales y empresas de la red FAZDETUDO.PT y contacte "
            "directamente con quien mejor responda a lo que busca."
        ),
        "hero_area": "Gran Lisboa · Margen Sur · Setúbal",
        "search_title": "Buscar profesionales",
        "service_label": "Servicio",
        "service_all": "Todos los servicios",
        "service_aria": "Filtrar por servicio",
        "zone_label": "Zona",
        "zone_all": "Todas las zonas",
        "zone_aria": "Filtrar por zona",
        "results_aria": "Resultados de la búsqueda de profesionales",
        "empty_title": "Aún no tenemos un colaborador disponible para este servicio.",
        "empty_text": "Hable con nosotros e intentaremos ayudarle a encontrar una solución.",
        "empty_cta": "Pedir ayuda",
        "empty_wa": (
            "¡Hola! Busco un profesional a través de FAZDETUDO.PT y aún no "
            "encontré en la categoría/zona que seleccioné. ¿Pueden ayudarme?"
        ),
        "recruit_title": "¿Es profesional? Aparezca en FAZDETUDO.PT",
        "recruit_text": (
            "Divulgue sus servicios ante clientes que ya buscan profesionales "
            "en su zona."
        ),
        "recruit_benefits": [
            (
                "id-card",
                "Perfil profesional",
                "Nombre, servicio, zona y contactos.",
            ),
            (
                "comments",
                "Contacto directo",
                "Los clientes hablan directamente con usted.",
            ),
            (
                "arrow-trend-up",
                "Mayor visibilidad",
                "Posibilidad de obtener más visibilidad con nuestros planes para colaboradores.",
            ),
        ],
        "recruit_cta": "Quiero ser colaborador",
        "recruit_wa": (
            "¡Hola! Soy profesional y me gustaría saber cómo puedo aparecer en "
            "FAZDETUDO.PT y cuáles son los planes para colaboradores."
        ),
        "recruit_aria": "Contactar FAZDETUDO.PT por WhatsApp para ser colaborador",
        "nav_back": "Volver al inicio",
        "wa_online": "En línea",
        "wa_greeting": "¡Hola! ¿Cómo podemos ayudar?",
        "wa_placeholder": "Escriba su mensaje…",
        "wa_close": "Cerrar chat",
        "wa_send": "Enviar",
        "wa_float": "WhatsApp",
        "footer": "FAZDETUDO.PT. Todos los derechos reservados.",
    },
    "fr": {
        "skip_link": "Aller au contenu",
        "hero_title": "Trouvez le bon professionnel pour votre besoin",
        "hero_subtitle": (
            "Consultez les professionnels et entreprises du réseau FAZDETUDO.PT "
            "et contactez directement celui qui répond le mieux à votre demande."
        ),
        "hero_area": "Grand Lisbonne · Rive Sud · Setúbal",
        "search_title": "Rechercher des professionnels",
        "service_label": "Service",
        "service_all": "Tous les services",
        "service_aria": "Filtrer par service",
        "zone_label": "Zone",
        "zone_all": "Toutes les zones",
        "zone_aria": "Filtrer par zone",
        "results_aria": "Résultats de recherche de professionnels",
        "empty_title": "Nous n'avons pas encore de partenaire disponible pour ce service.",
        "empty_text": "Contactez-nous et nous essaierons de vous aider à trouver une solution.",
        "empty_cta": "Demander de l'aide",
        "empty_wa": (
            "Bonjour ! Je cherche un professionnel via FAZDETUDO.PT et je n'en "
            "ai pas encore trouvé dans la catégorie/zone sélectionnée. Pouvez-vous m'aider ?"
        ),
        "recruit_title": "Vous êtes professionnel ? Apparaissez sur FAZDETUDO.PT",
        "recruit_text": (
            "Faites connaître vos services auprès de clients qui cherchent déjà "
            "des professionnels dans votre secteur."
        ),
        "recruit_benefits": [
            (
                "id-card",
                "Profil professionnel",
                "Nom, service, zone et contacts.",
            ),
            (
                "comments",
                "Contact direct",
                "Les clients vous parlent directement.",
            ),
            (
                "arrow-trend-up",
                "Plus de visibilité",
                "Possibilité d'obtenir plus de visibilité grâce à nos offres partenaires.",
            ),
        ],
        "recruit_cta": "Je veux devenir partenaire",
        "recruit_wa": (
            "Bonjour ! Je suis professionnel et j'aimerais savoir comment "
            "apparaître sur FAZDETUDO.PT et quelles sont les offres pour les partenaires."
        ),
        "recruit_aria": "Contacter FAZDETUDO.PT sur WhatsApp pour devenir partenaire",
        "nav_back": "Retour à l'accueil",
        "wa_online": "En ligne",
        "wa_greeting": "Bonjour ! Comment pouvons-nous vous aider ?",
        "wa_placeholder": "Écrivez votre message…",
        "wa_close": "Fermer le chat",
        "wa_send": "Envoyer",
        "wa_float": "WhatsApp",
        "footer": "FAZDETUDO.PT. Tous droits réservés.",
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
        keys.append("partner_f" if partner.get("feminine") else "partner")
    if partner.get("featured"):
        keys.append("featured")
    return keys


PARTNER_PROFILE_UI = {
    "pt": {
        "profile_cta": "Ver perfil →",
        "profile_aria": "Ver perfil de {name}",
        "breadcrumb_home": "Início",
        "breadcrumb_partners": "Parceiros",
        "back_partners": "Voltar aos parceiros",
        "contact_h2": "Contactar {name}",
        "phone_label": "Telefone",
        "whatsapp_label": "WhatsApp",
        "call": "Ligar",
        "whatsapp": "WhatsApp",
        "zone_note": (
            "A zona exacta de deslocação deve ser confirmada diretamente com a profissional."
        ),
    },
}


def partner_has_profile(partner: dict) -> bool:
    profile = partner.get("profile") or {}
    return bool(profile.get("enabled") and profile.get("slug"))


def partner_profile_slug(partner: dict) -> str | None:
    if not partner_has_profile(partner):
        return None
    return partner["profile"]["slug"]


def partner_profile_path(partner: dict) -> str | None:
    """Site-relative directory path, e.g. parceiros/maria-limpezas/."""
    slug = partner_profile_slug(partner)
    if not slug:
        return None
    return f"parceiros/{slug}/"


def partner_profile_href(partner: dict) -> str | None:
    """Root-absolute href for nav/cards, e.g. /parceiros/maria-limpezas/."""
    path = partner_profile_path(partner)
    return f"/{path}" if path else None


def partner_profile_url(partner: dict) -> str | None:
    path = partner_profile_path(partner)
    return f"{BASE_URL}/{path}" if path else None


def partners_with_profiles() -> list[dict]:
    return [p for p in active_partners() if partner_has_profile(p)]


def partner_profile_seo(partner: dict, lang: str = "pt") -> dict | None:
    if not partner_has_profile(partner):
        return None
    seo = (partner.get("profile") or {}).get("seo") or {}
    return seo.get(lang) or seo.get("pt")


def partner_profile_content(partner: dict, lang: str = "pt") -> dict | None:
    if not partner_has_profile(partner):
        return None
    content = (partner.get("profile") or {}).get("content") or {}
    return content.get(lang) or content.get("pt")


def active_partners() -> list[dict]:
    return [p for p in RECOMMENDED_PARTNERS if p.get("active", True)]


def get_partner(partner_id: str) -> dict | None:
    for partner in RECOMMENDED_PARTNERS:
        if partner.get("id") == partner_id:
            return partner
    return None


def partner_zone_ids(partner: dict) -> list[str]:
    zones = partner.get("zones") or []
    return [z for z in zones if z in PARTNER_ZONES]


def partner_category_ids(partner: dict) -> list[str]:
    """Return category ids used for filtering (multi-category aware)."""
    categories = partner.get("categories")
    if categories:
        return [c for c in categories if c in PARTNER_CATEGORIES]
    category = partner.get("category")
    return [category] if category in PARTNER_CATEGORIES else []


def homepage_filter_category_ids() -> tuple[str, ...]:
    """Category options for the homepage finder (only categories with active partners)."""
    used: set[str] = set()
    for partner in active_partners():
        used.update(partner_category_ids(partner))
    preferred = [cid for cid in FILTER_CATEGORY_IDS if cid in used]
    extras = [
        cid
        for cid in PAGE_FILTER_CATEGORY_IDS
        if cid in used and cid not in preferred
    ]
    return tuple(preferred + extras)


# Page slug → partner category ids (source of truth for service-page partner sections).
# Do NOT derive this from partner["service_slug"] — specialised categories stay explicit.
SERVICE_PARTNER_CATEGORIES: dict[str, list[str]] = {
    "servico-limpezas.html": ["limpezas"],
    "servico-climatizacao.html": ["avac"],
    "servico-remodelacoes.html": ["remodelacoes-gerais", "obras-gerais"],
    "servico-recuperar-casa.html": ["recuperacao-casa", "obras-gerais"],
}


def partners_for_service(slug: str) -> list[dict]:
    """Active partners matching any category mapped to this service page.

    Preserves RECOMMENDED_PARTNERS order and never returns duplicates.
    """
    category_ids = set(SERVICE_PARTNER_CATEGORIES.get(slug, []))
    if not category_ids:
        return []

    matched: list[dict] = []
    seen: set[str] = set()
    for partner in active_partners():
        partner_id = partner.get("id")
        if not partner_id or partner_id in seen:
            continue
        if category_ids.intersection(partner_category_ids(partner)):
            matched.append(partner)
            seen.add(partner_id)
    return matched


def partner_schema_entity(partner: dict) -> dict:
    """Build a Schema.org Person/Organization node from partner data only."""
    if partner.get("type") == "external":
        entity: dict = {
            "@type": "Organization",
            "name": partner["name"],
        }
        website = partner.get("website")
        if website:
            entity["url"] = website
        return entity

    entity = {
        "@type": "Person",
        "name": partner["name"],
    }
    tel_href = partner.get("tel_href") or ""
    if tel_href.startswith("tel:"):
        entity["telephone"] = tel_href[4:]
    return entity


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
        # No structured zone yet — do not invent coverage here.
        "zones": [],

        "profile": {
            "enabled": True,
            "slug": "airfix",
            "seo": {
                "pt": {
                    "title": "AirFix.pt | Ar Condicionado e AVAC",
                    "meta_description": (
                        "Conheça a AirFix.pt, parceiro FAZDETUDO.PT especializado em "
                        "instalação, manutenção, limpeza e assistência técnica de ar "
                        "condicionado e AVAC."
                    ),
                    "h1": "AirFix.pt — Ar Condicionado e AVAC",
                    "og_title": "AirFix.pt | Ar Condicionado e AVAC",
                },
            },
            "content": {
                "pt": {
                    "intro": (
                        "A AirFix.pt integra a rede de parceiros FAZDETUDO.PT para serviços "
                        "especializados de ar condicionado e AVAC. Consulte os serviços "
                        "disponíveis e visite diretamente a AirFix.pt para pedir informações "
                        "ou orçamento."
                    ),
                    "contact_note": (
                        "Para informações ou orçamento, visite diretamente o site oficial "
                        "da AirFix.pt."
                    ),
                    "sections": [
                        {
                            "h2": "Serviços de Ar Condicionado e AVAC",
                            "html": (
                                "<p>Serviços especializados de ar condicionado e AVAC, "
                                "incluindo instalação, manutenção, limpeza e assistência "
                                "técnica.</p>"
                            ),
                        },
                    ],
                },
            },
        },
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
        "location": {
            "pt": "Margem Sul · Azeitão",
            "en": "South Bank · Azeitão",
            "es": "Margen Sur · Azeitão",
            "fr": "Rive Sud · Azeitão",
        },
        "zones": ["margem-sul", "azeitao"],

        "profile": {
            "enabled": True,
            "slug": "caterina-limpezas",
            "seo": {
                "pt": {
                    "title": "Caterina | Empregada de Limpeza na Margem Sul",
                    "meta_description": (
                        "Conheça a Caterina, profissional de limpeza na Margem Sul e "
                        "Azeitão. Contacte diretamente por telefone ou WhatsApp para "
                        "verificar disponibilidade."
                    ),
                    "h1": "Caterina — Serviços de Limpeza na Margem Sul",
                    "og_title": "Caterina | Serviços de Limpeza na Margem Sul",
                },
            },
            "content": {
                "pt": {
                    "intro": (
                        "Caterina integra a rede de parceiros FAZDETUDO.PT para serviços "
                        "de limpeza na Margem Sul e Azeitão. Pode contactá-la diretamente "
                        "por telefone ou WhatsApp para explicar o serviço pretendido e "
                        "confirmar disponibilidade."
                    ),
                    "sections": [
                        {
                            "h2": "Serviços de limpeza",
                            "html": (
                                "<p>Pode receber pedidos relacionados com limpeza doméstica, "
                                "limpeza regular, limpeza pontual ou outras necessidades de "
                                "limpeza — sempre sujeito a confirmação direta com a "
                                "profissional.</p>"
                            ),
                        },
                        {
                            "h2": "Zona de atuação",
                            "html": (
                                "<p>Margem Sul · Azeitão.</p>"
                                "<p>A zona exacta de deslocação deve ser confirmada "
                                "diretamente com a profissional.</p>"
                            ),
                        },
                    ],
                },
            },
        },
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
    {
        "id": "maria-limpezas",
        "active": True,
        "category": "limpezas",
        "categories": ["limpezas"],
        "type": "direct_contact",
        "name": "Maria",
        "recommended": False,
        "featured": False,
        "feminine": True,
        # Keep homepage teaser light — Caterina remains the Limpezas card there.
        "home_showcase": False,
        "logo": "assets/partners/maria-limpezas.webp",
        "icon": "broom",
        "phone_display": "963 014 604",
        "tel_href": "tel:+351963014604",
        "whatsapp_href": "https://wa.me/351963014604",
        "service_slug": "servico-limpezas.html",
        "location": {
            "pt": "Grande Lisboa",
            "en": "Greater Lisbon",
            "es": "Gran Lisboa",
            "fr": "Grand Lisbonne",
        },
        "zones": [
            "grande-lisboa",
        ],
        "profile": {
            "enabled": True,
            "slug": "maria-limpezas",
            "seo": {
                "pt": {
                    "title": "Maria | Empregada de Limpeza na Grande Lisboa",
                    "meta_description": (
                        "Conheça a Maria, profissional de limpeza na Grande Lisboa. "
                        "Serviços de limpeza doméstica e contacto direto por telefone "
                        "ou WhatsApp."
                    ),
                    "h1": "Maria — Serviços de Limpeza na Grande Lisboa",
                    "og_title": "Maria | Empregada de Limpeza na Grande Lisboa",
                },
            },
            "content": {
                "pt": {
                    "intro": (
                        "Maria integra a rede de parceiros FAZDETUDO.PT para serviços de "
                        "limpeza na Grande Lisboa. Pode contactá-la diretamente por "
                        "telefone ou WhatsApp para explicar o tipo de imóvel, o serviço "
                        "pretendido e a disponibilidade."
                    ),
                    "sections": [
                        {
                            "h2": "Serviços de limpeza na Grande Lisboa",
                            "html": (
                                "<p>Através deste perfil pode contactar a Maria para "
                                "pedidos relacionados com limpeza doméstica — por "
                                "exemplo limpeza regular, profunda ou pontual — "
                                "sempre sujeito a confirmação direta.</p>"
                                "<p>Contacte diretamente a Maria para confirmar "
                                "disponibilidade e o tipo de limpeza pretendido. "
                                "Não assuma automaticamente todos os tipos de serviço "
                                "sem combinar antes.</p>"
                            ),
                        },
                        {
                            "h2": "Como pedir o serviço",
                            "html": (
                                "<ol>"
                                "<li>indicar a localidade;</li>"
                                "<li>indicar o tipo e a dimensão do imóvel;</li>"
                                "<li>explicar o tipo de limpeza;</li>"
                                "<li>enviar fotografias pelo WhatsApp, se for útil;</li>"
                                "<li>confirmar a disponibilidade diretamente com Maria.</li>"
                                "</ol>"
                            ),
                        },
                        {
                            "h2": "Zona de atuação",
                            "html": (
                                "<p>Grande Lisboa.</p>"
                                "<p>A zona exacta de deslocação deve ser confirmada "
                                "diretamente com a profissional.</p>"
                            ),
                        },
                    ],
                },
            },
        },
        "copy": {
            "pt": {
                "role": "Serviços de limpeza · contacto direto",
                "call": "Ligar",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Ver limpezas",
                "call_aria": (
                    "Ligar diretamente para Maria, parceira de serviços de limpeza"
                ),
                "wa_aria": "Contactar Maria por WhatsApp",
            },
            "en": {
                "role": "Cleaning services · direct contact",
                "call": "Call",
                "whatsapp": "WhatsApp",
                "secondary_cta": "View cleaning services",
                "call_aria": (
                    "Call Maria directly, cleaning services partner"
                ),
                "wa_aria": "Contact Maria on WhatsApp",
            },
            "es": {
                "role": "Servicios de limpieza · contacto directo",
                "call": "Llamar",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Ver servicios de limpieza",
                "call_aria": (
                    "Llamar directamente a Maria, colaboradora de servicios de limpieza"
                ),
                "wa_aria": "Contactar a Maria por WhatsApp",
            },
            "fr": {
                "role": "Services de nettoyage · contact direct",
                "call": "Appeler",
                "whatsapp": "WhatsApp",
                "secondary_cta": "Voir les services de nettoyage",
                "call_aria": (
                    "Appeler directement Maria, partenaire de services de nettoyage"
                ),
                "wa_aria": "Contacter Maria sur WhatsApp",
            },
        },
    },
    {
        "id": "wallfixtv",
        "active": True,
        "category": "instalacao-tv",
        "type": "external",
        "name": "WallFixTV.pt",
        "recommended": True,
        "featured": False,
        "logo": "assets/partners/wallfixtv-logo.png",
        "logo_wide": True,
        "website": "https://www.wallfixtv.pt/",
        "service_slug": "servico-reparacoes-gerais.html",
        "location": {
            "pt": "Grande Lisboa · Margem Sul",
            "en": "Greater Lisbon · South Bank",
            "es": "Gran Lisboa · Margen Sur",
            "fr": "Grand Lisbonne · Rive Sud",
        },
        "zones": [
            "grande-lisboa",
            "lisboa",
            "cascais-oeiras",
            "sintra",
            "margem-sul",
            "azeitao",
            "setubal",
        ],

        "profile": {
            "enabled": True,
            "slug": "wallfixtv",
            "seo": {
                "pt": {
                    "title": "WallFixTV.pt | Instalação de TV na Parede",
                    "meta_description": (
                        "Conheça a WallFixTV.pt, parceiro FAZDETUDO.PT especializado em "
                        "instalação profissional de televisões na parede e organização "
                        "de cabos."
                    ),
                    "h1": "WallFixTV.pt — Instalação de TV na Parede",
                    "og_title": "WallFixTV.pt | Instalação de TV na Parede",
                },
            },
            "content": {
                "pt": {
                    "intro": (
                        "A WallFixTV.pt integra a rede de parceiros FAZDETUDO.PT para "
                        "instalação especializada de televisões na parede."
                    ),
                    "contact_note": (
                        "Para informações ou orçamento, visite diretamente o site oficial "
                        "da WallFixTV.pt."
                    ),
                    "sections": [
                        {
                            "h2": "Instalação profissional de TV",
                            "html": (
                                "<p>Instalação profissional de televisões na parede, com "
                                "nivelamento, fixação adequada, montagem de suportes e "
                                "organização de cabos.</p>"
                            ),
                        },
                        {
                            "h2": "Zona de atuação",
                            "html": "<p>Grande Lisboa · Margem Sul.</p>",
                        },
                    ],
                },
            },
        },
        "copy": {
            "pt": {
                "blurb": (
                    "Instalação profissional de televisões na parede, com nivelamento, "
                    "fixação adequada, montagem de suportes e organização de cabos."
                ),
                "primary_cta": "Visitar WallFixTV.pt",
                "secondary_cta": "Ver serviços relacionados",
                "visit_aria": "Visitar WallFixTV.pt",
            },
            "en": {
                "blurb": (
                    "Professional TV wall mounting with accurate levelling, secure "
                    "fixings, bracket installation and cable management."
                ),
                "primary_cta": "Visit WallFixTV.pt",
                "secondary_cta": "View related services",
                "visit_aria": "Visit WallFixTV.pt",
            },
            "es": {
                "blurb": (
                    "Instalación profesional de televisores en pared, con nivelación, "
                    "fijación segura, montaje de soportes y organización de cables."
                ),
                "primary_cta": "Visitar WallFixTV.pt",
                "secondary_cta": "Ver servicios relacionados",
                "visit_aria": "Visitar WallFixTV.pt",
            },
            "fr": {
                "blurb": (
                    "Installation professionnelle de téléviseurs au mur avec nivellement "
                    "précis, fixations adaptées, pose du support et organisation des câbles."
                ),
                "primary_cta": "Visiter WallFixTV.pt",
                "secondary_cta": "Voir les services associés",
                "visit_aria": "Visiter WallFixTV.pt",
            },
        },
    },
    {
        "id": "valeriu",
        "active": True,
        "category": "remodelacoes-gerais",
        "categories": [
            "obras-gerais",
            "recuperacao-casa",
            "remodelacoes-gerais",
        ],
        "type": "direct_contact",
        "name": "Valeriu",
        "recommended": False,
        "featured": False,
        "phone_display": "964 400 960",
        "tel_href": "tel:+351964400960",
        "service_slug": "servico-remodelacoes.html",
        "location": {
            "pt": "Lisboa · Margem Sul · Azeitão",
            "en": "Lisbon · South Bank · Azeitão",
            "es": "Lisboa · Margen Sur · Azeitão",
            "fr": "Lisbonne · Rive Sud · Azeitão",
        },
        "zones": [
            "lisboa",
            "margem-sul",
            "azeitao",
        ],
        "profile": {
            "enabled": True,
            "slug": "valeriu",
            "seo": {
                "pt": {
                    "title": "Valeriu | Remodelações e Obras em Lisboa",
                    "meta_description": (
                        "Conheça Valeriu, parceiro FAZDETUDO.PT para remodelações, "
                        "recuperação de casas e obras gerais em Lisboa, Margem Sul e Azeitão."
                    ),
                    "h1": "Valeriu — Remodelações e Obras Gerais",
                    "og_title": "Valeriu | Remodelações e Obras Gerais",
                },
            },
            "content": {
                "pt": {
                    "intro": (
                        "Valeriu integra a rede de parceiros FAZDETUDO.PT para "
                        "trabalhos de obras gerais, recuperação de casas e remodelações "
                        "em Lisboa, Margem Sul e Azeitão."
                    ),
                    "contact_note": "Contacto apenas por telefone.",
                    "sections": [
                        {
                            "h2": "Obras e remodelações",
                            "html": (
                                "<p>Áreas de atuação: obras gerais, recuperação de casas e "
                                "remodelações gerais. Contacte diretamente para confirmar "
                                "disponibilidade e o âmbito do trabalho pretendido.</p>"
                            ),
                        },
                        {
                            "h2": "Zona de atuação",
                            "html": (
                                "<p>Lisboa · Margem Sul · Azeitão.</p>"
                                "<p>A zona exacta de deslocação deve ser confirmada "
                                "diretamente.</p>"
                            ),
                        },
                    ],
                },
            },
        },
        "copy": {
            "pt": {
                "role": (
                    "Obras gerais, recuperação de casas e remodelações · contacto direto"
                ),
                "call": "Ligar",
                "secondary_cta": "Ver remodelações",
                "call_aria": (
                    "Ligar diretamente para Valeriu, parceiro de obras "
                    "e remodelações"
                ),
            },
            "en": {
                "role": (
                    "General construction, home restoration and renovations · direct contact"
                ),
                "call": "Call",
                "secondary_cta": "View renovations",
                "call_aria": (
                    "Call Valeriu directly, construction and renovations partner"
                ),
            },
            "es": {
                "role": (
                    "Obras generales, rehabilitación de viviendas y reformas · contacto directo"
                ),
                "call": "Llamar",
                "secondary_cta": "Ver reformas",
                "call_aria": (
                    "Llamar directamente a Valeriu, colaborador de obras y reformas"
                ),
            },
            "fr": {
                "role": (
                    "Travaux généraux, rénovation de maisons et remodelage · contact direct"
                ),
                "call": "Appeler",
                "secondary_cta": "Voir les rénovations",
                "call_aria": (
                    "Appeler directement Valeriu, partenaire travaux et rénovations"
                ),
            },
        },
    },
]
