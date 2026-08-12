# -*- coding: utf-8 -*-
"""Translations and hreflang helpers for static servico-*.html pages."""

from __future__ import annotations

from site_config import BASE_URL
from slug_registry import (
    LANGS,
    LANG_HTML,
    HREFLANG_CODES,
    SERVICE_SLUGS,
    asset_prefix,
    index_href,
    page_url,
    render_hreflang_tags,
)

def _zone_li(strong: str, detail: str) -> str:
    return (
        f'                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> '
        f'<strong>{strong}</strong> ({detail})</li>'
    )


ZONES_LI_BY_LANG = {
    "pt": "\n".join([
        _zone_li("Lisboa", "Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações"),
        _zone_li("Loures e Odivelas", "Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas"),
        _zone_li("Sintra e Amadora", "Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira"),
        _zone_li("Cascais e Oeiras", "Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana"),
        _zone_li("Vila Franca de Xira", "Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo"),
        _zone_li("Margem Sul", "Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete"),
        _zone_li("Setúbal e Sesimbra", "Azeitão, Palmela, Quinta do Anjo"),
    ]),
    "en": "\n".join([
        _zone_li("Lisbon", "Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações"),
        _zone_li("Loures and Odivelas", "Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas"),
        _zone_li("Sintra and Amadora", "Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira"),
        _zone_li("Cascais and Oeiras", "Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana"),
        _zone_li("Vila Franca de Xira", "Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo"),
        _zone_li("South Bank (Margem Sul)", "Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete"),
        _zone_li("Setúbal and Sesimbra", "Azeitão, Palmela, Quinta do Anjo"),
    ]),
    "es": "\n".join([
        _zone_li("Lisboa", "Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações"),
        _zone_li("Loures y Odivelas", "Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas"),
        _zone_li("Sintra y Amadora", "Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira"),
        _zone_li("Cascais y Oeiras", "Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana"),
        _zone_li("Vila Franca de Xira", "Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo"),
        _zone_li("Margen Sur", "Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete"),
        _zone_li("Setúbal y Sesimbra", "Azeitão, Palmela, Quinta do Anjo"),
    ]),
    "fr": "\n".join([
        _zone_li("Lisbonne", "Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações"),
        _zone_li("Loures et Odivelas", "Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas"),
        _zone_li("Sintra et Amadora", "Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira"),
        _zone_li("Cascais et Oeiras", "Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana"),
        _zone_li("Vila Franca de Xira", "Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo"),
        _zone_li("Rive Sud (Margem Sul)", "Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete"),
        _zone_li("Setúbal et Sesimbra", "Azeitão, Palmela, Quinta do Anjo"),
    ]),
}

# Compat: corpos PT ricos e código legado
ZONES_LI = ZONES_LI_BY_LANG["pt"]

UI = {
    "pt": {
        "lead": "Serviço profissional e atendimento rápido na Grande Lisboa e Margem Sul.",
        "h2_what": "O que fazemos nesta área:",
        "h2_zones": "Zonas de Atendimento",
        "zones_p": "Prestamos serviços nas seguintes zonas:",
        "skip_link": "Saltar para o conteúdo",
        "back": "Voltar ao Início",
        "cta_h3": "Precisa de assistência ou quer um orçamento gratuito?",
        "cta_p": "Clique abaixo para falar diretamente com o nosso técnico especialista em {service}.",
        "cta_wa": "Orçamento por WhatsApp",
        "cta_call": "Ligar: 932 504 112",
        "footer": "© 2026 FAZDETUDO.PT. Todos os direitos reservados. Especialistas em Reparações ao Domicílio.",
        "wa_greeting": "Como posso ajudar?",
        "wa_placeholder": "Escreva uma mensagem...",
        "wa_close": "Fechar chat",
        "wa_online": "Online",
        "wa_float_label": "Contactar via WhatsApp",
        "wa_send": "Enviar mensagem",
        "page_title_tpl": "{h1} | FAZDETUDO.PT",
        "meta_tpl": "{name} em Lisboa, Cascais e Setúbal. {desc} Orçamento grátis com a FAZDETUDO.PT.",
        "og_tpl": "{name} | FAZDETUDO.PT",
    },
    "en": {
        "lead": "Professional service and responsive support across Greater Lisbon and the South Bank.",
        "h2_what": "What we do in this area:",
        "h2_zones": "Service Areas",
        "zones_p": "We provide services across:",
        "skip_link": "Skip to content",
        "back": "Back to Home",
        "cta_h3": "Need help or a free quote?",
        "cta_p": "Click below to speak directly with our {service} specialist.",
        "cta_wa": "Quote via WhatsApp",
        "cta_call": "Call: 932 504 112",
        "footer": "© 2026 FAZDETUDO.PT. All rights reserved. Home repair specialists.",
        "wa_greeting": "How can I help you?",
        "wa_placeholder": "Type a message...",
        "wa_close": "Close chat",
        "wa_online": "Online",
        "wa_float_label": "Contact via WhatsApp",
        "wa_send": "Send message",
        "page_title_tpl": "{h1} | FAZDETUDO.PT",
        "meta_tpl": "{name} in Lisbon, Cascais and Setúbal. {desc} Free quote from FAZDETUDO.PT.",
        "og_tpl": "{name} | FAZDETUDO.PT",
    },
    "es": {
        "lead": "Servicio profesional y atención rápida en la Gran Lisboa y Margen Sur.",
        "h2_what": "Qué hacemos en esta área:",
        "h2_zones": "Zonas de Servicio",
        "zones_p": "Prestamos servicio en las siguientes zonas:",
        "skip_link": "Saltar al contenido",
        "back": "Volver al Inicio",
        "cta_h3": "¿Necesita ayuda o un presupuesto gratis?",
        "cta_p": "Haga clic abajo para hablar directamente con nuestro especialista en {service}.",
        "cta_wa": "Presupuesto por WhatsApp",
        "cta_call": "Llamar: 932 504 112",
        "footer": "© 2026 FAZDETUDO.PT. Todos los derechos reservados. Especialistas en reparaciones a domicilio.",
        "wa_greeting": "¿Cómo puedo ayudarle?",
        "wa_placeholder": "Escriba un mensaje...",
        "wa_close": "Cerrar chat",
        "wa_online": "En línea",
        "wa_float_label": "Contactar por WhatsApp",
        "wa_send": "Enviar mensaje",
        "page_title_tpl": "{h1} | FAZDETUDO.PT",
        "meta_tpl": "{name} en Lisboa, Cascais y Setúbal. {desc} Presupuesto gratis con FAZDETUDO.PT.",
        "og_tpl": "{name} | FAZDETUDO.PT",
    },
    "fr": {
        "lead": "Service professionnel et réponse rapide dans le Grand Lisbonne et la Rive Sud.",
        "h2_what": "Ce que nous faisons dans ce domaine :",
        "h2_zones": "Zones d'intervention",
        "zones_p": "Nous intervenons dans les zones suivantes :",
        "skip_link": "Aller au contenu",
        "back": "Retour à l'accueil",
        "cta_h3": "Besoin d'aide ou d'un devis gratuit ?",
        "cta_p": "Cliquez ci-dessous pour parler directement à notre spécialiste {service}.",
        "cta_wa": "Devis par WhatsApp",
        "cta_call": "Appeler : 932 504 112",
        "footer": "© 2026 FAZDETUDO.PT. Tous droits réservés. Spécialistes en réparations à domicile.",
        "wa_greeting": "Comment puis-je vous aider ?",
        "wa_placeholder": "Écrivez un message...",
        "wa_close": "Fermer le chat",
        "wa_online": "En ligne",
        "wa_float_label": "Contacter via WhatsApp",
        "wa_send": "Envoyer le message",
        "page_title_tpl": "{h1} | FAZDETUDO.PT",
        "meta_tpl": "{name} à Lisbonne, Cascais et Setúbal. {desc} Devis gratuit avec FAZDETUDO.PT.",
        "og_tpl": "{name} | FAZDETUDO.PT",
    },
}

# SYNC: slug order = script.js SERVICE_LANDING_SLUGS / index.html services grid
SERVICE_COPY: dict[str, dict[str, dict]] = {
    "servico-remodelacoes.html": {
        "pt": {
            "name": "Remodelações e Obras",
            "h1": "Remodelações, Obras e Construção em Lisboa e Margem Sul",
            "page_title": "Remodelações, Obras e Construção em Lisboa | FAZDETUDO.PT",
            "desc": "Remodelações e obras através de parceiro especializado.",
            "wa": "Olá! Gostaria de pedir um orçamento para remodelações.",
            "intro": "Serviço disponibilizado através de parceiro <strong>FAZDETUDO.PT</strong> especializado em obras e remodelações na Grande Lisboa e Margem Sul.",
            "features": [
                "Remodelação completa de cozinhas e casas de banho.",
                "Substituição de pavimentos e revestimentos.",
                "Obras com cronograma e preço fechado quando possível.",
                "Coordenação de canalização, electricidade e pintura.",
            ],
        },
        "en": {
            "name": "Renovations & Construction",
            "h1": "Renovations, Building Work and Construction in Lisbon",
            "page_title": "Renovations and Construction in Lisbon | FAZDETUDO.PT",
            "desc": "Renovations and building work through a specialist partner.",
            "wa": "Hello! I would like a quote for renovations.",
            "intro": "Service provided through a <strong>FAZDETUDO.PT</strong> partner specialised in construction and renovations across Greater Lisbon and the South Bank.",
            "features": [
                "Complete kitchen and bathroom renovations.",
                "Flooring and wall finish replacement.",
                "Projects with agreed timeline and fixed price when possible.",
                "Plumbing, electrical and painting coordinated on site.",
            ],
        },
        "es": {
            "name": "Reformas y Obras",
            "h1": "Reformas, Obras y Construcción en Lisboa y Margen Sur",
            "page_title": "Reformas, Obras y Construcción en Lisboa | FAZDETUDO.PT",
            "desc": "Reformas y obras a través de colaborador especializado.",
            "wa": "¡Hola! Me gustaría un presupuesto para reformas.",
            "intro": "Servicio disponible a través de un colaborador <strong>FAZDETUDO.PT</strong> especializado en obras y reformas en la Gran Lisboa y Margen Sur.",
            "features": [
                "Reforma integral de cocinas y baños.",
                "Sustitución de suelos y revestimientos.",
                "Obras con calendario y precio cerrado cuando es posible.",
                "Fontanería, electricidad y pintura coordinadas.",
            ],
        },
        "fr": {
            "name": "Rénovations et Travaux",
            "h1": "Rénovations, Travaux et Construction à Lisbonne",
            "page_title": "Rénovations et Travaux à Lisbonne | FAZDETUDO.PT",
            "desc": "Rénovations et travaux via un partenaire spécialisé.",
            "wa": "Bonjour ! Je souhaite un devis pour des rénovations.",
            "intro": "Service proposé via un partenaire <strong>FAZDETUDO.PT</strong> spécialisé en travaux et rénovations dans le Grand Lisbonne et la Rive Sud.",
            "features": [
                "Rénovation complète de cuisines et salles de bains.",
                "Remplacement de sols et revêtements.",
                "Chantiers avec planning et prix fixe lorsque possible.",
                "Plomberie, électricité et peinture coordonnées.",
            ],
        },
    },
    "servico-recuperar-casa.html": {
        "pt": {
            "name": "Recuperar Casa",
            "h1": "Recuperação de Casas Antigas, Devolutas e Degradadas",
            "page_title": "Recuperação de Casas Antigas e Degradadas | FAZDETUDO.PT",
            "desc": "Recuperação integral de imóveis degradados.",
            "wa": "Olá! Gostaria de pedir um orçamento para recuperação de casa.",
            "intro": "Serviço disponibilizado através de parceiro <strong>FAZDETUDO.PT</strong> especializado na recuperação de <strong>casas devolutas, herdadas ou degradadas</strong> na Grande Lisboa e Margem Sul.",
            "features": [
                "Avaliação completa do imóvel e patologias.",
                "Tratamento de humidades e infiltrações.",
                "Renovação de instalações e coberturas.",
                "Entrega pronta a habitar com um único interlocutor.",
            ],
        },
        "en": {
            "name": "Home Restoration",
            "h1": "Restoration of Old, Vacant and Run-Down Homes",
            "desc": "Full restoration of old and run-down properties, ready to live in or rent.",
            "wa": "Hello! I would like a quote for home restoration.",
            "intro": "Service provided through a <strong>FAZDETUDO.PT</strong> partner specialised in restoring <strong>vacant, inherited or run-down homes</strong> across Greater Lisbon and the South Bank.",
            "features": [
                "Full property assessment and defect report.",
                "Damp treatment and leak repair.",
                "Upgraded utilities, roofs and finishes.",
                "Turnkey delivery with one project manager.",
            ],
        },
        "es": {
            "name": "Recuperar Casa",
            "h1": "Recuperación de Casas Antiguas, Vacías y Deterioradas",
            "page_title": "Recuperación de Casas Antiguas y Degradadas | FAZDETUDO.PT",
            "desc": "Recuperación integral de casas deterioradas, listas para habitar o alquilar.",
            "wa": "¡Hola! Me gustaría un presupuesto para recuperar una casa.",
            "intro": "Servicio disponible a través de un colaborador <strong>FAZDETUDO.PT</strong> especializado en recuperar <strong>casas vacías, heredadas o deterioradas</strong> en la Gran Lisboa y Margen Sur.",
            "features": [
                "Evaluación completa del inmueble.",
                "Tratamiento de humedades e infiltraciones.",
                "Renovación de instalaciones y cubiertas.",
                "Entrega lista para habitar con un solo interlocutor.",
            ],
        },
        "fr": {
            "name": "Rénover une Maison",
            "h1": "Réhabilitation de Maisons Anciennes et Dégradées",
            "page_title": "Réhabilitation de Maisons Anciennes | FAZDETUDO.PT",
            "desc": "Récupération complète de biens dégradés.",
            "wa": "Bonjour ! Je souhaite un devis pour rénover une maison.",
            "intro": "Service proposé via un partenaire <strong>FAZDETUDO.PT</strong> spécialisé dans la restauration de <strong>maisons vacantes, héritées ou dégradées</strong> dans le Grand Lisbonne et la Rive Sud.",
            "features": [
                "Diagnostic complet du bien.",
                "Traitement des humidités et infiltrations.",
                "Rénovation des installations et toitures.",
                "Livraison clé en main avec un seul interlocuteur.",
            ],
        },
    },
    "servico-pinturas.html": {
        "pt": {
            "name": "Pinturas",
            "h1": "Pinturas Interiores e Exteriores Profissionais",
            "page_title": "Pinturas Interiores e Exteriores | FAZDETUDO.PT",
            "desc": "Pintura interior e exterior com acabamentos profissionais.",
            "wa": "Olá! Gostaria de pedir um orçamento para pinturas.",
            "intro": "Referência em <strong>pintura residencial e comercial na Grande Lisboa e Margem Sul</strong> com orçamento gratuito.",
            "features": [
                "Preparação profissional de superfícies e primários.",
                "Pintura de interiores: paredes, tetos e portas.",
                "Pintura de exteriores resistentes ao sol e à chuva.",
                "Proteção de mobiliário e entrega limpa do espaço.",
            ],
        },
        "en": {
            "name": "Painting",
            "h1": "Professional Interior and Exterior Painting",
            "desc": "Interior and exterior painting with quality finishes.",
            "wa": "Hello! I would like a quote for painting.",
            "intro": "Trusted <strong>residential and commercial painting across Greater Lisbon and the South Bank</strong> with free quotes.",
            "features": [
                "Professional surface preparation and primers.",
                "Interior painting: walls, ceilings and doors.",
                "Durable exterior coatings for sun and rain.",
                "Furniture protection and clean handover.",
            ],
        },
        "es": {
            "name": "Pinturas",
            "h1": "Pinturas Interiores y Exteriores Profesionales",
            "page_title": "Pinturas Interiores y Exteriores | FAZDETUDO.PT",
            "desc": "Pintura interior y exterior con acabados de calidad.",
            "wa": "¡Hola! Me gustaría un presupuesto para pinturas.",
            "intro": "Referencia en <strong>pintura residencial y comercial en la Gran Lisboa y Margen Sur</strong> con presupuesto gratis.",
            "features": [
                "Preparación profesional de superficies e imprimaciones.",
                "Pintura de interiores: paredes, techos y puertas.",
                "Pintura exterior resistente al sol y la lluvia.",
                "Protección del mobiliario y entrega limpia.",
            ],
        },
        "fr": {
            "name": "Peinture",
            "h1": "Peinture Intérieure et Extérieure Professionnelle",
            "page_title": "Peinture Intérieure et Extérieure | FAZDETUDO.PT",
            "desc": "Peinture intérieure et extérieure, enduits et finitions de qualité soignées.",
            "wa": "Bonjour ! Je souhaite un devis pour de la peinture.",
            "intro": "Référence en <strong>peinture résidentielle et commerciale dans le Grand Lisbonne</strong> avec devis gratuit.",
            "features": [
                "Préparation des surfaces et apprêts professionnels.",
                "Peinture intérieure : murs, plafonds et portes.",
                "Revêtements extérieurs résistants au soleil et à la pluie.",
                "Protection du mobilier et remise des lieux propres.",
            ],
        },
    },
    "servico-canalizacoes.html": {
        "pt": {
            "name": "Canalizações",
            "h1": "Canalizador e Serviços de Canalização Urgente",
            "desc": "Fugas, desentupimentos e reparações urgentes.",
            "wa": "Olá! Gostaria de pedir um orçamento para canalizações.",
            "intro": "<strong>Canalizador de confiança na Grande Lisboa e Margem Sul</strong> com diagnóstico rigoroso e reparação duradoura.",
            "features": [
                "Reparação de fugas visíveis e ocultas.",
                "Desentupimentos em sanitas, ralos e cozinhas.",
                "Substituição de torneiras, sifões e autoclismos.",
                "Atendimento urgente para casa e comércio.",
            ],
        },
        "en": {
            "name": "Plumbing",
            "h1": "Plumber and Emergency Plumbing Services",
            "desc": "Leak detection, drain unblocking, pipe repairs and urgent plumbing call-outs at home.",
            "wa": "Hello! I would like a quote for plumbing.",
            "intro": "Trusted <strong>plumber across Greater Lisbon and the South Bank</strong> with clear diagnosis and lasting repairs.",
            "features": [
                "Visible and hidden leak repair.",
                "Unblocking toilets, sinks and drains.",
                "Tap, trap and cistern replacement.",
                "Urgent call-outs for homes and businesses.",
            ],
        },
        "es": {
            "name": "Fontanería",
            "h1": "Fontanero y Fontanería Urgente",
            "desc": "Fugas, desatascos y reparaciones urgentes.",
            "wa": "¡Hola! Me gustaría un presupuesto para fontanería.",
            "intro": "<strong>Fontanero de confianza en la Gran Lisboa y Margen Sur</strong> con diagnóstico claro.",
            "features": [
                "Reparación de fugas visibles y ocultas.",
                "Desatascos en inodoros, fregaderos y desagües.",
                "Sustitución de grifos, sifones e inodoros.",
                "Urgencias para hogar y comercio.",
            ],
        },
        "fr": {
            "name": "Plomberie",
            "h1": "Plombier et Dépannage Plomberie Urgent",
            "desc": "Détection de fuites, débouchage, réparations et dépannage en urgence.",
            "wa": "Bonjour ! Je souhaite un devis pour de la plomberie.",
            "intro": "<strong>Plombier de confiance dans le Grand Lisbonne</strong> avec diagnostic clair et réparation durable.",
            "features": [
                "Réparation de fuites visibles et cachées.",
                "Débouchage WC, éviers et canalisations.",
                "Remplacement de robinets, siphons et chasses.",
                "Urgences pour particuliers et commerces.",
            ],
        },
    },
    "servico-electricidade.html": {
        "pt": {
            "name": "Electricidade",
            "h1": "Serviços de Electricidade para Casa e Negócio",
            "desc": "Avarias, tomadas, iluminação e quadros eléctricos.",
            "wa": "Olá! Gostaria de pedir um orçamento para electricidade.",
            "intro": "Especialistas em <strong>electricidade em Lisboa, Margem Sul e Cascais</strong> com orçamento claro.",
            "features": [
                "Reparação de avarias e disjuntores a disparar.",
                "Instalação de tomadas, interruptores e candeeiros.",
                "Modernização de quadros eléctricos.",
                "Circuitos dedicados para forno e ar condicionado.",
            ],
        },
        "en": {
            "name": "Electrical",
            "h1": "Electrical Services for Home and Business",
            "desc": "Faults, sockets, lighting, fuse boards and rewiring for homes and businesses.",
            "wa": "Hello! I would like a quote for electrical work.",
            "intro": "Specialists in <strong>electrical services across Greater Lisbon, South Bank and Cascais</strong>.",
            "features": [
                "Fault finding and tripping breakers.",
                "Sockets, switches and light fittings.",
                "Fuse board upgrades and safety improvements.",
                "Dedicated circuits for ovens and AC units.",
            ],
        },
        "es": {
            "name": "Electricidad",
            "h1": "Servicios de Electricidad para Hogar y Negocio",
            "desc": "Averías, enchufes, iluminación y cuadros.",
            "wa": "¡Hola! Me gustaría un presupuesto para electricidad.",
            "intro": "Especialistas en <strong>electricidad en la Gran Lisboa, Margen Sur y Cascais</strong>.",
            "features": [
                "Reparación de averías y magnetotérmicos.",
                "Instalación de enchufes, interruptores y luces.",
                "Modernización de cuadros eléctricos.",
                "Circuitos dedicados para horno y aire acondicionado.",
            ],
        },
        "fr": {
            "name": "Électricité",
            "h1": "Services d'Électricité pour Maison et Entreprise",
            "page_title": "Services d'Électricité Maison et Entreprise | FAZDETUDO.PT",
            "desc": "Pannes, prises, éclairage, tableaux et mise aux normes par un électricien.",
            "wa": "Bonjour ! Je souhaite un devis pour l'électricité.",
            "intro": "Spécialistes <strong>électricité Grand Lisbonne, Rive Sud et Cascais</strong>.",
            "features": [
                "Dépannage et disjoncteurs qui sautent.",
                "Prises, interrupteurs et luminaires.",
                "Mise aux normes des tableaux électriques.",
                "Circuits dédiés four et climatisation.",
            ],
        },
    },
    "servico-carpintaria.html": {
        "pt": {
            "name": "Carpintaria",
            "h1": "Carpintaria e Montagem de Móveis ao Domicílio",
            "desc": "Montagem de móveis, portas e trabalhos em madeira.",
            "wa": "Olá! Gostaria de pedir um orçamento para carpintaria.",
            "intro": "<strong>Carpintaria em Lisboa e Margem Sul</strong> com precisão e acabamento profissional.",
            "features": [
                "Montagem de móveis IKEA e por medida.",
                "Afinação de portas que raspam ou não fecham.",
                "Rodapés, guarnições e prateleiras fixas.",
                "Reparação de dobradiças e corrediças.",
            ],
        },
        "en": {
            "name": "Carpentry",
            "h1": "Carpentry and Furniture Assembly at Home",
            "desc": "Flat-pack furniture assembly, fitted wardrobes, doors and custom woodwork at home.",
            "wa": "Hello! I would like a quote for carpentry.",
            "intro": "<strong>Carpentry across Greater Lisbon and the South Bank</strong> with precise, professional finishes.",
            "features": [
                "IKEA and custom furniture assembly.",
                "Adjusting sticking or misaligned doors.",
                "Skirting, trim and fitted shelving.",
                "Hinge, slide and handle repairs.",
            ],
        },
        "es": {
            "name": "Carpintería",
            "h1": "Carpintería y Montaje de Muebles a Domicilio",
            "desc": "Montaje de muebles, armarios a medida, puertas y trabajos de madera a domicilio.",
            "wa": "¡Hola! Me gustaría un presupuesto para carpintería.",
            "intro": "<strong>Carpintería en la Gran Lisboa y Margen Sur</strong> con acabado profesional.",
            "features": [
                "Montaje de muebles IKEA y a medida.",
                "Ajuste de puertas que rozan o no cierran.",
                "Rodapiés, molduras y estanterías.",
                "Reparación de bisagras y correderas.",
            ],
        },
        "fr": {
            "name": "Menuiserie",
            "h1": "Menuiserie et Montage de Meubles à Domicile",
            "desc": "Montage de meubles, placards sur mesure, portes et travaux de menuiserie à domicile.",
            "wa": "Bonjour ! Je souhaite un devis pour menuiserie.",
            "intro": "<strong>Menuiserie Grand Lisbonne et Rive Sud</strong> avec finitions soignées.",
            "features": [
                "Montage meubles IKEA et sur mesure.",
                "Réglage de portes qui frottent.",
                "Plinthes, moulures et étagères.",
                "Réparation charnières et coulisses.",
            ],
        },
    },
    "servico-reparacoes-gerais.html": {
        "pt": {
            "name": "Reparações Gerais",
            "h1": "Reparações Gerais e Faz-Tudo ao Domicílio",
            "desc": "Faz de tudo para várias tarefas numa visita.",
            "wa": "Olá! Gostaria de pedir um orçamento para reparações gerais.",
            "intro": "O seu <strong>faz de tudo de confiança na Grande Lisboa e Margem Sul</strong> — uma visita, vários arranjos.",
            "features": [
                "Fixação de TVs, estantes e espelhos.",
                "Montagem de móveis e cortinados.",
                "Silicone, furos e pequenas reparações.",
                "Tarefas rápidas de manutenção geral.",
            ],
        },
        "en": {
            "name": "General Repairs",
            "h1": "General Repairs and Handyman at Home",
            "desc": "Handyman for multiple small jobs and repairs in a single home visit.",
            "wa": "Hello! I would like a quote for general repairs.",
            "intro": "Your trusted <strong>handyman across Greater Lisbon and the South Bank</strong> — one visit, many fixes.",
            "features": [
                "TV, shelf and mirror mounting.",
                "Furniture and curtain rail assembly.",
                "Silicone, holes and minor wall repairs.",
                "Quick general maintenance tasks.",
            ],
        },
        "es": {
            "name": "Reparaciones generales",
            "h1": "Reparaciones Generales y Manitas a Domicilio",
            "desc": "Manitas para varias tareas en una visita.",
            "wa": "¡Hola! Me gustaría un presupuesto para reparaciones generales.",
            "intro": "Su <strong>manitas de confianza en la Gran Lisboa y Margen Sur</strong> — una visita, varios arreglos.",
            "features": [
                "Fijación de TV, estanterías y espejos.",
                "Montaje de muebles y cortinajes.",
                "Silicona, agujeros y pequeñas reparaciones.",
                "Tareas rápidas de mantenimiento.",
            ],
        },
        "fr": {
            "name": "Réparations générales",
            "h1": "Réparations Générales et Bricolage à Domicile",
            "desc": "Homme à tout faire, plusieurs tâches.",
            "wa": "Bonjour ! Je souhaite un devis pour réparations générales.",
            "intro": "Votre <strong>homme à tout faire Grand Lisbonne et Rive Sud</strong> — une visite, plusieurs réparations.",
            "features": [
                "Fixation TV, étagères et miroirs.",
                "Montage meubles et tringles à rideaux.",
                "Silicone, trous et petites réparations.",
                "Entretien général rapide.",
            ],
        },
    },
    "servico-manutencao.html": {
        "pt": {
            "name": "Manutenção",
            "h1": "Manutenção Preventiva e Reparações para Condomínios",
            "page_title": "Manutenção Preventiva para Condomínios | FAZDETUDO.PT",
            "desc": "Manutenção preventiva e lavagem alta pressão.",
            "wa": "Olá! Gostaria de pedir um orçamento para manutenção.",
            "intro": "<strong>Manutenção preventiva na Grande Lisboa e Margem Sul</strong> para evitar obras caras.",
            "features": [
                "Inspeção de telhados, calhas e ralos.",
                "Lavagem de alta pressão em pátios e terraços.",
                "Reparações pontuais em condomínios.",
                "Planos mensais ou trimestrais acordados.",
            ],
        },
        "en": {
            "name": "Maintenance",
            "h1": "Preventive Maintenance for Buildings and Homes",
            "page_title": "Preventive Maintenance for Buildings | FAZDETUDO.PT",
            "desc": "Preventive maintenance, small repairs and pressure washing for buildings and homes.",
            "wa": "Hello! I would like a quote for maintenance.",
            "intro": "<strong>Preventive maintenance across Greater Lisbon and the South Bank</strong> to avoid costly repairs.",
            "features": [
                "Roof, gutter and drain inspection.",
                "Pressure washing patios and terraces.",
                "Minor repairs for condominiums.",
                "Monthly or quarterly service plans.",
            ],
        },
        "es": {
            "name": "Mantenimiento",
            "h1": "Mantenimiento Preventivo para Comunidades y Hogares",
            "page_title": "Mantenimiento Preventivo para Comunidades | FAZDETUDO.PT",
            "desc": "Mantenimiento preventivo y alta presión.",
            "wa": "¡Hola! Me gustaría un presupuesto para mantenimiento.",
            "intro": "<strong>Mantenimiento preventivo en la Gran Lisboa y Margen Sur</strong> para evitar obras caras.",
            "features": [
                "Inspección de tejados, canalones y desagües.",
                "Lavado a alta presión en patios y terrazas.",
                "Reparaciones puntuales en comunidades.",
                "Planes mensuales o trimestrales.",
            ],
        },
        "fr": {
            "name": "Entretien",
            "h1": "Entretien Préventif pour Immeubles et Maisons",
            "desc": "Entretien préventif et nettoyage haute pression.",
            "wa": "Bonjour ! Je souhaite un devis pour entretien.",
            "intro": "<strong>Entretien préventif Grand Lisbonne et Rive Sud</strong> pour éviter les gros travaux.",
            "features": [
                "Inspection toitures, gouttières et drains.",
                "Nettoyage haute pression terrasses et patios.",
                "Petites réparations en copropriété.",
                "Contrats mensuels ou trimestriels.",
            ],
        },
    },
    "servico-limpezas.html": {
        "pt": {
            "name": "Limpezas",
            "h1": "Limpezas Domésticas e Pós-Obra Profissionais",
            "desc": "Limpeza doméstica, pós-obra e comercial através de parceira FAZDETUDO.PT.",
            "wa": "Olá! Gostaria de pedir um orçamento para limpezas.",
            "intro": "Serviço realizado por parceira <strong>FAZDETUDO.PT</strong>. <strong>Limpezas profissionais</strong> para casa, escritório e pós-obra na Margem Sul e Azeitão.",
            "features": [
                "Limpeza profunda de apartamentos e moradias.",
                "Limpeza pós-obra com remoção de pó.",
                "Escritórios, lojas e espaços comerciais.",
                "Planos semanal, quinzenal ou pontual.",
            ],
        },
        "en": {
            "name": "Cleaning",
            "h1": "Domestic and Post-Construction Cleaning",
            "desc": "Home, post-construction and commercial cleaning through a FAZDETUDO.PT partner.",
            "wa": "Hello! I would like a quote for cleaning.",
            "intro": "Service provided by a <strong>FAZDETUDO.PT</strong> partner. <strong>Professional cleaning</strong> for homes, offices and post-build on the South Bank and in Azeitão.",
            "features": [
                "Deep cleaning for flats and houses.",
                "Post-construction dust and debris removal.",
                "Offices, shops and commercial spaces.",
                "Weekly, bi-weekly or one-off plans.",
            ],
        },
        "es": {
            "name": "Limpieza",
            "h1": "Limpiezas Domésticas y Post-Obra Profesionales",
            "page_title": "Limpiezas Domésticas y Post-Obra | FAZDETUDO.PT",
            "desc": "Limpieza doméstica, post-obra y comercial a través de colaboradora FAZDETUDO.PT.",
            "wa": "¡Hola! Me gustaría un presupuesto para limpieza.",
            "intro": "Servicio realizado por colaboradora <strong>FAZDETUDO.PT</strong>. <strong>Limpieza profesional</strong> para hogar, oficina y post-obra en Margen Sur y Azeitão.",
            "features": [
                "Limpieza profunda de pisos y casas.",
                "Limpieza post-obra y eliminación de polvo.",
                "Oficinas, tiendas y locales comerciales.",
                "Planes semanal, quincenal o puntual.",
            ],
        },
        "fr": {
            "name": "Nettoyage",
            "h1": "Nettoyage Domestique et Après-Travaux",
            "desc": "Nettoyage maison, après-travaux et bureaux via une partenaire FAZDETUDO.PT.",
            "wa": "Bonjour ! Je souhaite un devis pour nettoyage.",
            "intro": "Service réalisé par une partenaire <strong>FAZDETUDO.PT</strong>. <strong>Nettoyage professionnel</strong> pour maison, bureau et fin de chantier sur la Rive Sud et à Azeitão.",
            "features": [
                "Nettoyage en profondeur appartements et maisons.",
                "Nettoyage après travaux et poussières.",
                "Bureaux, commerces et locaux.",
                "Formules hebdo, bimensuelles ou ponctuelles.",
            ],
        },
    },
    "servico-jardinagem.html": {
        "pt": {
            "name": "Jardinagem",
            "h1": "Jardinagem e Manutenção de Jardins",
            "desc": "Relva, poda, sistemas de rega e limpeza e manutenção de jardins.",
            "wa": "Olá! Gostaria de pedir um orçamento para jardinagem.",
            "intro": "<strong>Jardinagem na Grande Lisboa e Margem Sul</strong> para moradias e condomínios.",
            "features": [
                "Corte de relva e tratamento de sebes.",
                "Poda de árvores e arbustos.",
                "Limpeza de terrenos e jardins.",
                "Instalação e reparação de rega automática.",
            ],
        },
        "en": {
            "name": "Gardening",
            "h1": "Gardening and Garden Maintenance",
            "desc": "Lawn care, hedge and tree pruning, irrigation systems and regular garden maintenance.",
            "wa": "Hello! I would like a quote for gardening.",
            "intro": "<strong>Gardening across Greater Lisbon and the South Bank</strong> for homes and condominiums.",
            "features": [
                "Lawn mowing and hedge trimming.",
                "Tree and shrub pruning.",
                "Garden and plot clearance.",
                "Irrigation system install and repair.",
            ],
        },
        "es": {
            "name": "Jardinería",
            "h1": "Jardinería y Mantenimiento de Jardines",
            "desc": "Césped, poda, sistemas de riego y limpieza y mantenimiento de jardines.",
            "wa": "¡Hola! Me gustaría un presupuesto para jardinería.",
            "intro": "<strong>Jardinería en la Gran Lisboa y Margen Sur</strong> para hogares y comunidades.",
            "features": [
                "Corte de césped y setos.",
                "Poda de árboles y arbustos.",
                "Limpieza de terrenos y jardines.",
                "Instalación y reparación de riego automático.",
            ],
        },
        "fr": {
            "name": "Jardinage",
            "h1": "Jardinage et Entretien de Jardins",
            "desc": "Entretien de pelouse, taille de haies et arbres, arrosage et nettoyage de jardins.",
            "wa": "Bonjour ! Je souhaite un devis pour jardinage.",
            "intro": "<strong>Jardinage Grand Lisbonne et Rive Sud</strong> pour maisons et copropriétés.",
            "features": [
                "Tonte et taille de haies.",
                "Élagage arbres et arbustes.",
                "Nettoyage de terrains et jardins.",
                "Installation et réparation arrosage.",
            ],
        },
    },
    "servico-informatica.html": {
        "pt": {
            "name": "Informática",
            "h1": "Assistência Informática e Redes Wi-Fi",
            "desc": "Reparação de PCs, redes Wi-Fi, impressoras, backups e smart home.",
            "wa": "Olá! Gostaria de pedir um orçamento para informática.",
            "intro": "<strong>Assistência informática ao domicílio</strong> na Grande Lisboa e Margem Sul.",
            "features": [
                "Remoção de vírus e otimização de PCs.",
                "Configuração de Wi-Fi e redes.",
                "Impressoras e partilha em rede.",
                "Backup e smart home básica.",
            ],
        },
        "en": {
            "name": "IT Services",
            "h1": "IT Support and Wi-Fi Networks",
            "desc": "PC repair, Wi-Fi setup, networks, printers, backups and basic smart home installation.",
            "wa": "Hello! I would like a quote for IT support.",
            "intro": "<strong>On-site IT support</strong> across Greater Lisbon and the South Bank.",
            "features": [
                "Virus removal and PC optimisation.",
                "Wi-Fi setup and network tuning.",
                "Printers and shared office devices.",
                "Backup and basic smart home setup.",
            ],
        },
        "es": {
            "name": "Informática",
            "h1": "Asistencia Informática y Redes Wi-Fi",
            "desc": "Reparación de PCs, redes Wi-Fi, impresoras, copias de seguridad y smart home.",
            "wa": "¡Hola! Me gustaría un presupuesto para informática.",
            "intro": "<strong>Asistencia informática a domicilio</strong> en la Gran Lisboa y Margen Sur.",
            "features": [
                "Eliminación de virus y optimización.",
                "Configuración de Wi-Fi y redes.",
                "Impresoras y recursos en red.",
                "Copias de seguridad y smart home básica.",
            ],
        },
        "fr": {
            "name": "Informatique",
            "h1": "Assistance Informatique et Réseaux Wi-Fi",
            "desc": "PC, Wi-Fi, imprimantes et maison connectée.",
            "wa": "Bonjour ! Je souhaite un devis pour informatique.",
            "intro": "<strong>Assistance informatique à domicile</strong> Grand Lisbonne et Rive Sud.",
            "features": [
                "Suppression virus et optimisation PC.",
                "Configuration Wi-Fi et réseaux.",
                "Imprimantes et partage réseau.",
                "Sauvegarde et domotique de base.",
            ],
        },
    },
    "servico-serralharia.html": {
        "pt": {
            "name": "Serralharia",
            "h1": "Serralharia e Abertura de Portas Urgente",
            "desc": "Abertura urgente de portas, troca de fechaduras e cilindros, portões e segurança.",
            "wa": "Olá! Gostaria de pedir um orçamento para serralharia.",
            "intro": "<strong>Serralharia na Grande Lisboa e Margem Sul</strong> com resposta rápida.",
            "features": [
                "Abertura de portas trancadas.",
                "Substituição de cilindros e fechaduras.",
                "Reparação de portões de garagem.",
                "Reforço de segurança em portas de entrada.",
            ],
        },
        "en": {
            "name": "Locksmithing",
            "h1": "Locksmithing and Emergency Door Opening",
            "desc": "Emergency door opening, lock and cylinder replacement, gates and security upgrades.",
            "wa": "Hello! I would like a quote for locksmithing.",
            "intro": "<strong>Locksmith services across Greater Lisbon and the South Bank</strong> with fast response.",
            "features": [
                "Emergency door opening.",
                "Cylinder and lock replacement.",
                "Garage gate repair.",
                "Entry door security upgrades.",
            ],
        },
        "es": {
            "name": "Cerrajería",
            "h1": "Cerrajería y Apertura Urgente de Puertas",
            "desc": "Apertura urgente, cambio de cerraduras y bombines, portones y seguridad.",
            "wa": "¡Hola! Me gustaría un presupuesto para cerrajería.",
            "intro": "<strong>Cerrajería en la Gran Lisboa y Margen Sur</strong> con respuesta rápida.",
            "features": [
                "Apertura de puertas cerradas.",
                "Sustitución de bombines y cerraduras.",
                "Reparación de portones de garaje.",
                "Refuerzo de seguridad en puertas.",
            ],
        },
        "fr": {
            "name": "Serrurerie",
            "h1": "Serrurerie et Ouverture de Porte d'Urgence",
            "desc": "Ouverture en urgence, remplacement de serrures et cylindres, portails et sécurité.",
            "wa": "Bonjour ! Je souhaite un devis pour serrurerie.",
            "intro": "<strong>Serrurerie Grand Lisbonne et Rive Sud</strong> avec intervention rapide.",
            "features": [
                "Ouverture de porte en urgence.",
                "Remplacement de cylindres et serrures.",
                "Réparation portails de garage.",
                "Renforcement sécurité porte d'entrée.",
            ],
        },
    },
    "servico-climatizacao.html": {
        "pt": {
            "name": "Climatização",
            "h1": "Instalação e Reparação de Ar Condicionado (AVAC)",
            "page_title": "Ar Condicionado e Climatização (AVAC) | FAZDETUDO.PT",
            "desc": "Instalação, manutenção e reparação AVAC através da AirFix.pt.",
            "wa": "Olá! Gostaria de pedir um orçamento para climatização.",
            "intro": "Serviço especializado realizado através da <strong>AirFix.pt</strong>, parceiro <strong>FAZDETUDO.PT</strong> — instalação, limpeza e manutenção de ar condicionado na Grande Lisboa e Margem Sul.",
            "features": [
                "Instalação de splits e multisplit.",
                "Carga de gás e limpeza de filtros.",
                "Reparação de avarias e fugas.",
                "Manutenção preventiva anual.",
            ],
        },
        "en": {
            "name": "Air Conditioning",
            "h1": "Air Conditioning Installation and Repair (HVAC)",
            "page_title": "Air Conditioning and HVAC Repair | FAZDETUDO.PT",
            "desc": "AC installation, cleaning and HVAC maintenance via AirFix.pt.",
            "wa": "Hello! I would like a quote for air conditioning.",
            "intro": "Specialist service provided through <strong>AirFix.pt</strong>, a <strong>FAZDETUDO.PT</strong> partner — air conditioning installation, cleaning and maintenance across Greater Lisbon and the South Bank.",
            "features": [
                "Split and multi-split installation.",
                "Gas recharge and filter cleaning.",
                "Breakdown and leak repair.",
                "Annual preventive maintenance.",
            ],
        },
        "es": {
            "name": "Climatización",
            "h1": "Instalación y Reparación de Aire Acondicionado",
            "page_title": "Aire Acondicionado y Climatización | FAZDETUDO.PT",
            "desc": "Instalación, mantenimiento y reparación.",
            "wa": "¡Hola! Me gustaría un presupuesto para climatización.",
            "intro": "Servicio especializado realizado a través de <strong>AirFix.pt</strong>, colaborador <strong>FAZDETUDO.PT</strong> — instalación, limpieza y mantenimiento de aire acondicionado en la Gran Lisboa y Margen Sur.",
            "features": [
                "Instalación de splits y multisplit.",
                "Carga de gas y limpieza de filtros.",
                "Reparación de averías y fugas.",
                "Mantenimiento preventivo anual.",
            ],
        },
        "fr": {
            "name": "Climatisation",
            "h1": "Installation et Réparation Climatisation (CVC)",
            "page_title": "Climatisation et Réparation (CVC) | FAZDETUDO.PT",
            "desc": "Installation, nettoyage et entretien CVC via AirFix.pt.",
            "wa": "Bonjour ! Je souhaite un devis pour climatisation.",
            "intro": "Service spécialisé réalisé via <strong>AirFix.pt</strong>, partenaire <strong>FAZDETUDO.PT</strong> — installation, nettoyage et entretien de climatisation dans le Grand Lisbonne et la Rive Sud.",
            "features": [
                "Installation splits et multisplits.",
                "Recharge gaz et nettoyage filtres.",
                "Dépannage pannes et fuites.",
                "Entretien préventif annuel.",
            ],
        },
    },
    "servico-estores-persianas.html": {
        "pt": {
            "name": "Estores e Persianas",
            "h1": "Reparação e Instalação de Estores e Persianas",
            "desc": "Estores, persianas, mosquiteiras e toldos.",
            "wa": "Olá! Gostaria de pedir um orçamento para estores e persianas.",
            "intro": "<strong>Estores e persianas na Grande Lisboa e Margem Sul</strong> com peças adequadas.",
            "features": [
                "Substituição de fitas e lâminas.",
                "Reparação de motores eléctricos.",
                "Instalação de estores novos.",
                "Mosquiteiras e toldos.",
            ],
        },
        "en": {
            "name": "Blinds & Shutters",
            "h1": "Blinds and Shutters Repair and Installation",
            "desc": "Blinds, shutters, mosquito nets and awnings.",
            "wa": "Hello! I would like a quote for blinds and shutters.",
            "intro": "<strong>Blinds and shutters across Greater Lisbon and the South Bank</strong> with quality parts.",
            "features": [
                "Tape and slat replacement.",
                "Electric motor repair.",
                "New shutter installation.",
                "Mosquito nets and awnings.",
            ],
        },
        "es": {
            "name": "Persianas y estores",
            "h1": "Reparación e Instalación de Persianas y Estores",
            "page_title": "Reparación de Persianas y Estores | FAZDETUDO.PT",
            "desc": "Estores, persianas, mosquiteras y toldos.",
            "wa": "¡Hola! Me gustaría un presupuesto para persianas.",
            "intro": "<strong>Persianas y estores en la Gran Lisboa y Margen Sur</strong>.",
            "features": [
                "Sustitución de cintas y lamas.",
                "Reparación de motores eléctricos.",
                "Instalación de estores nuevos.",
                "Mosquiteras y toldos.",
            ],
        },
        "fr": {
            "name": "Stores et volets",
            "h1": "Réparation et Pose de Stores et Volets",
            "desc": "Stores, volets, moustiquaires et auvents.",
            "wa": "Bonjour ! Je souhaite un devis pour stores et volets.",
            "intro": "<strong>Stores et volets Grand Lisbonne et Rive Sud</strong>.",
            "features": [
                "Remplacement sangles et lames.",
                "Réparation moteurs électriques.",
                "Pose de stores neufs.",
                "Moustiquaires et auvents.",
            ],
        },
    },
    "servico-decoracao-interiores.html": {
        "pt": {
            "name": "Decoração de Interiores",
            "h1": "Decoração de Interiores e Home Staging",
            "desc": "Cortinas, papel de parede e home staging.",
            "wa": "Olá! Gostaria de pedir um orçamento para decoração de interiores.",
            "intro": "<strong>Decoração de interiores na Grande Lisboa e Margem Sul</strong> para habitar ou vender.",
            "features": [
                "Cortinados e varões decorativos.",
                "Papel de parede e painéis.",
                "Iluminação decorativa.",
                "Home staging para venda ou arrendamento.",
            ],
        },
        "en": {
            "name": "Interior Design",
            "h1": "Interior Design and Home Staging",
            "desc": "Curtains, wallpaper, decorative lighting and home staging for sale or rent.",
            "wa": "Hello! I would like a quote for interior design.",
            "intro": "<strong>Interior design across Greater Lisbon and the South Bank</strong> to live in or sell.",
            "features": [
                "Curtains and decorative poles.",
                "Wallpaper and feature panels.",
                "Decorative lighting design.",
                "Home staging for sale or rent.",
            ],
        },
        "es": {
            "name": "Decoración de interiores",
            "h1": "Decoración de Interiores y Home Staging",
            "desc": "Cortinas, papel pintado y home staging.",
            "wa": "¡Hola! Me gustaría un presupuesto para decoración.",
            "intro": "<strong>Decoración de interiores en la Gran Lisboa y Margen Sur</strong>.",
            "features": [
                "Cortinas y barras decorativas.",
                "Papel pintado y paneles.",
                "Iluminación decorativa.",
                "Home staging para venta o alquiler.",
            ],
        },
        "fr": {
            "name": "Décoration d'intérieur",
            "h1": "Décoration Intérieure et Home Staging",
            "desc": "Rideaux, papier peint et home staging.",
            "wa": "Bonjour ! Je souhaite un devis pour décoration intérieure.",
            "intro": "<strong>Décoration intérieure Grand Lisbonne et Rive Sud</strong>.",
            "features": [
                "Rideaux et tringles décoratives.",
                "Papier peint et panneaux.",
                "Éclairage décoratif.",
                "Home staging vente ou location.",
            ],
        },
    },
    "servico-piscinas.html": {
        "pt": {
            "name": "Piscinas",
            "service_type": "Construção, Manutenção e Reparação de Piscinas",
            "h1": "Construção, Manutenção e Reparação de Piscinas",
            "page_title": "Construção e Manutenção de Piscinas em Lisboa | FAZDETUDO.PT",
            "meta_description": (
                "Construção, manutenção e reparação de piscinas na Grande Lisboa e Margem Sul. "
                "Piscinas novas, remodelações, limpeza, filtração e tratamento de água."
            ),
            "desc": "Construção, manutenção e reparação de piscinas novas e existentes.",
            "wa": "Olá! Gostaria de pedir um orçamento para construção ou manutenção de piscinas.",
            "intro": (
                "A FAZDETUDO.PT oferece <strong>construção, manutenção e reparação de piscinas "
                "na Grande Lisboa e Margem Sul</strong> — desde piscinas novas a remodelações, "
                "com atendimento em Lisboa, Cascais, Almada, Setúbal e arredores."
            ),
            "features": [
                "Construção de piscinas novas para moradias e condomínios.",
                "Remodelação de piscinas existentes.",
                "Reparação de fugas e substituição de revestimentos.",
                "Instalação e manutenção de sistemas de filtração.",
                "Limpeza, tratamento de água e manutenção regular.",
            ],
        },
        "en": {
            "name": "Pools",
            "service_type": "Pool Construction, Maintenance and Repair",
            "h1": "Pool Construction, Maintenance and Repair",
            "page_title": "Pool Construction and Maintenance in Lisbon | FAZDETUDO.PT",
            "meta_description": (
                "Pool construction, maintenance and repair across Greater Lisbon and the South Bank. "
                "New pools, renovations, cleaning, filtration and water treatment."
            ),
            "desc": "New pool builds, renovations, cleaning and water treatment.",
            "wa": "Hello! I would like a quote for pool construction or maintenance.",
            "intro": (
                "<strong>Pool construction, maintenance and repair across Greater Lisbon and the South Bank</strong> "
                "— new builds, renovations and ongoing care in Lisbon, Cascais, Almada and Setúbal."
            ),
            "features": [
                "Construction of new residential and commercial pools.",
                "Renovation of existing pools.",
                "Leak repair and lining replacement.",
                "Filtration systems installation and servicing.",
                "Cleaning, water treatment and regular maintenance.",
            ],
        },
        "es": {
            "name": "Piscinas",
            "service_type": "Construcción, Mantenimiento y Reparación de Piscinas",
            "h1": "Construcción, Mantenimiento y Reparación de Piscinas",
            "page_title": "Construcción y Mantenimiento de Piscinas | FAZDETUDO.PT",
            "meta_description": (
                "Construcción, mantenimiento y reparación de piscinas en la Gran Lisboa y Margen Sur. "
                "Piscinas nuevas, reformas, limpieza, filtración y tratamiento del agua."
            ),
            "desc": "Construcción, mantenimiento y reparación de piscinas nuevas y existentes.",
            "wa": "¡Hola! Me gustaría un presupuesto para construcción o mantenimiento de piscinas.",
            "intro": (
                "<strong>Construcción, mantenimiento y reparación de piscinas en la Gran Lisboa y Margen Sur</strong> "
                "— desde piscinas nuevas hasta reformas, con servicio en Lisboa, Cascais, Almada y Setúbal."
            ),
            "features": [
                "Construcción de piscinas nuevas para viviendas y comunidades.",
                "Reforma de piscinas existentes.",
                "Reparación de fugas y sustitución de revestimientos.",
                "Instalación y mantenimiento de sistemas de filtración.",
                "Limpieza, tratamiento del agua y mantenimiento regular.",
            ],
        },
        "fr": {
            "name": "Piscines",
            "service_type": "Construction, Entretien et Réparation de Piscines",
            "h1": "Construction, Entretien et Réparation de Piscines",
            "page_title": "Construction et Entretien de Piscines | FAZDETUDO.PT",
            "meta_description": (
                "Construction, entretien et réparation de piscines au Grand Lisbonne et Rive Sud. "
                "Piscines neuves, rénovations, nettoyage, filtration et traitement de l'eau."
            ),
            "desc": "Construction, entretien et réparation de piscines neuves et existantes.",
            "wa": "Bonjour ! Je souhaite un devis pour construction ou entretien de piscine.",
            "intro": (
                "<strong>Construction, entretien et réparation de piscines au Grand Lisbonne et Rive Sud</strong> "
                "— piscines neuves, rénovations et suivi régulier à Lisbonne, Cascais, Almada et Setúbal."
            ),
            "features": [
                "Construction de piscines neuves pour maisons et copropriétés.",
                "Rénovation de piscines existantes.",
                "Réparation de fuites et remplacement de revêtements.",
                "Installation et entretien de systèmes de filtration.",
                "Nettoyage, traitement de l'eau et entretien régulier.",
            ],
        },
    },
}

# Garantir que todas as chaves de SERVICE_COPY estão no registry
assert set(SERVICE_COPY) == set(SERVICE_SLUGS), "SERVICE_COPY e slug_registry dessincronizados"


def localized_meta(slug: str, lang: str) -> dict:
    copy = SERVICE_COPY[slug][lang]
    ui = UI[lang]
    page_title = copy.get("page_title") or ui["page_title_tpl"].format(h1=copy["h1"])
    meta_description = copy.get("meta_description") or ui["meta_tpl"].format(
        name=copy["name"], desc=copy["desc"]
    )
    og_title = ui["og_tpl"].format(name=copy["name"])
    return {
        "service_name": copy.get("service_type", copy["name"]),
        "page_title": page_title,
        "meta_description": meta_description,
        "h1": copy["h1"],
        "wa_message": copy["wa"],
        "og_title": og_title,
    }


def build_body_html(slug: str, lang: str) -> str:
    copy = SERVICE_COPY[slug][lang]
    ui = UI[lang]
    items = "\n".join(
        f"                    <li>{feat}</li>" for feat in copy["features"]
    )
    zones = ZONES_LI_BY_LANG.get(lang, ZONES_LI_BY_LANG["pt"])
    return f"""
                <p>{copy["intro"]}</p>
                <h2>{ui["h2_what"]}</h2>
                <ul class="service-feature-list">
{items}
                </ul>
                <h2>{ui["h2_zones"]}</h2>
                <p>{ui["zones_p"]}</p>
                <ul class="service-zones-grid">{zones}
                </ul>"""
