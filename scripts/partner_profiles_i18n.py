# -*- coding: utf-8 -*-
"""Multilingual SEO + body copy for partner profile pages.

Merged onto each partner["profile"] by recommended_partners.apply_profile_i18n().
Build fails if a published profile is missing any of LANGS.
"""

from __future__ import annotations

from slug_registry import LANGS

# Complete profile payloads keyed by partner id.
PROFILE_BY_ID: dict[str, dict] = {
    "airfix": {
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
            "en": {
                "title": "AirFix.pt | Air Conditioning & HVAC",
                "meta_description": (
                    "Meet AirFix.pt, a FAZDETUDO.PT partner specialised in air "
                    "conditioning installation, maintenance, cleaning and technical support."
                ),
                "h1": "AirFix.pt — Air Conditioning & HVAC",
                "og_title": "AirFix.pt | Air Conditioning & HVAC",
            },
            "es": {
                "title": "AirFix.pt | Aire Acondicionado y Climatización",
                "meta_description": (
                    "Conozca AirFix.pt, colaborador FAZDETUDO.PT especializado en "
                    "instalación, mantenimiento, limpieza y asistencia técnica de "
                    "aire acondicionado y climatización."
                ),
                "h1": "AirFix.pt — Aire Acondicionado y Climatización",
                "og_title": "AirFix.pt | Aire Acondicionado y Climatización",
            },
            "fr": {
                "title": "AirFix.pt | Climatisation et CVC",
                "meta_description": (
                    "Découvrez AirFix.pt, partenaire FAZDETUDO.PT spécialisé dans "
                    "l'installation, l'entretien, le nettoyage et l'assistance technique "
                    "en climatisation et CVC."
                ),
                "h1": "AirFix.pt — Climatisation et CVC",
                "og_title": "AirFix.pt | Climatisation et CVC",
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
                            "<p>Instalação, manutenção, limpeza e assistência técnica "
                            "de ar condicionado.</p>"
                        ),
                    },
                ],
            },
            "en": {
                "intro": (
                    "AirFix.pt is part of the FAZDETUDO.PT partner network for specialist "
                    "air conditioning and HVAC services. View the available services and "
                    "visit AirFix.pt directly for information or a quote."
                ),
                "contact_note": (
                    "For information or a quote, visit the official AirFix.pt website."
                ),
                "sections": [
                    {
                        "h2": "Air Conditioning & HVAC Services",
                        "html": (
                            "<p>Air conditioning installation, maintenance, cleaning "
                            "and technical support.</p>"
                        ),
                    },
                ],
            },
            "es": {
                "intro": (
                    "AirFix.pt forma parte de la red de colaboradores FAZDETUDO.PT para "
                    "servicios especializados de aire acondicionado y climatización. "
                    "Consulte los servicios disponibles y visite directamente AirFix.pt "
                    "para solicitar información o presupuesto."
                ),
                "contact_note": (
                    "Para información o presupuesto, visite directamente el sitio "
                    "oficial de AirFix.pt."
                ),
                "sections": [
                    {
                        "h2": "Servicios de Aire Acondicionado y Climatización",
                        "html": (
                            "<p>Instalación, mantenimiento, limpieza y asistencia "
                            "técnica de aire acondicionado.</p>"
                        ),
                    },
                ],
            },
            "fr": {
                "intro": (
                    "AirFix.pt fait partie du réseau de partenaires FAZDETUDO.PT pour "
                    "les services spécialisés de climatisation et CVC. Consultez les "
                    "services disponibles et visitez directement AirFix.pt pour demander "
                    "des informations ou un devis."
                ),
                "contact_note": (
                    "Pour des informations ou un devis, visitez directement le site "
                    "officiel d'AirFix.pt."
                ),
                "sections": [
                    {
                        "h2": "Services de Climatisation et CVC",
                        "html": (
                            "<p>Installation, entretien, nettoyage et assistance "
                            "technique en climatisation.</p>"
                        ),
                    },
                ],
            },
        },
    },
    "caterina": {
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
            "en": {
                "title": "Caterina | Cleaning Professional in the South Bank",
                "meta_description": (
                    "Meet Caterina, a cleaning professional in the South Bank and "
                    "Azeitão. Contact her directly by phone or WhatsApp to check availability."
                ),
                "h1": "Caterina — Cleaning Services in the South Bank",
                "og_title": "Caterina | Cleaning Services in the South Bank",
            },
            "es": {
                "title": "Caterina | Profesional de Limpieza en Margen Sur",
                "meta_description": (
                    "Conozca a Caterina, profesional de limpieza en Margen Sur y "
                    "Azeitão. Contáctela directamente por teléfono o WhatsApp para "
                    "verificar disponibilidad."
                ),
                "h1": "Caterina — Servicios de Limpieza en Margen Sur",
                "og_title": "Caterina | Servicios de Limpieza en Margen Sur",
            },
            "fr": {
                "title": "Caterina | Professionnelle du Ménage sur la Rive Sud",
                "meta_description": (
                    "Découvrez Caterina, professionnelle du ménage sur la Rive Sud "
                    "et à Azeitão. Contactez-la directement par téléphone ou WhatsApp "
                    "pour vérifier ses disponibilités."
                ),
                "h1": "Caterina — Services de Ménage sur la Rive Sud",
                "og_title": "Caterina | Services de Ménage sur la Rive Sud",
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
            "en": {
                "intro": (
                    "Caterina is part of the FAZDETUDO.PT partner network for cleaning "
                    "services in the South Bank and Azeitão. You can contact her directly "
                    "by phone or WhatsApp to explain the service you need and confirm "
                    "availability."
                ),
                "sections": [
                    {
                        "h2": "Cleaning services",
                        "html": (
                            "<p>She may take requests related to domestic cleaning, "
                            "regular cleaning, one-off cleaning or other cleaning needs "
                            "— always subject to direct confirmation with the professional.</p>"
                        ),
                    },
                    {
                        "h2": "Service area",
                        "html": (
                            "<p>South Bank · Azeitão.</p>"
                            "<p>The exact travel area should be confirmed directly "
                            "with the professional.</p>"
                        ),
                    },
                ],
            },
            "es": {
                "intro": (
                    "Caterina forma parte de la red de colaboradores FAZDETUDO.PT para "
                    "servicios de limpieza en Margen Sur y Azeitão. Puede contactarla "
                    "directamente por teléfono o WhatsApp para explicar el servicio que "
                    "necesita y confirmar disponibilidad."
                ),
                "sections": [
                    {
                        "h2": "Servicios de limpieza",
                        "html": (
                            "<p>Puede recibir solicitudes relacionadas con limpieza "
                            "doméstica, limpieza regular, limpieza puntual u otras "
                            "necesidades de limpieza — siempre sujeto a confirmación "
                            "directa con la profesional.</p>"
                        ),
                    },
                    {
                        "h2": "Zona de servicio",
                        "html": (
                            "<p>Margen Sur · Azeitão.</p>"
                            "<p>La zona exacta de desplazamiento debe confirmarse "
                            "directamente con la profesional.</p>"
                        ),
                    },
                ],
            },
            "fr": {
                "intro": (
                    "Caterina fait partie du réseau de partenaires FAZDETUDO.PT pour "
                    "les services de ménage sur la Rive Sud et à Azeitão. Vous pouvez "
                    "la contacter directement par téléphone ou WhatsApp pour expliquer "
                    "le service souhaité et confirmer ses disponibilités."
                ),
                "sections": [
                    {
                        "h2": "Services de ménage",
                        "html": (
                            "<p>Elle peut recevoir des demandes liées au ménage "
                            "domestique, au ménage régulier, au ménage ponctuel ou à "
                            "d'autres besoins de nettoyage — toujours sous réserve de "
                            "confirmation directe avec la professionnelle.</p>"
                        ),
                    },
                    {
                        "h2": "Zone d'intervention",
                        "html": (
                            "<p>Rive Sud · Azeitão.</p>"
                            "<p>La zone exacte de déplacement doit être confirmée "
                            "directement avec la professionnelle.</p>"
                        ),
                    },
                ],
            },
        },
    },
    "maria-limpezas": {
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
            "en": {
                "title": "Maria | Cleaning Professional in Greater Lisbon",
                "meta_description": (
                    "Meet Maria, a cleaning professional in Greater Lisbon. "
                    "Domestic cleaning services with direct contact by phone or WhatsApp."
                ),
                "h1": "Maria — Cleaning Services in Greater Lisbon",
                "og_title": "Maria | Cleaning Professional in Greater Lisbon",
            },
            "es": {
                "title": "Maria | Profesional de Limpieza en Gran Lisboa",
                "meta_description": (
                    "Conozca a Maria, profesional de limpieza en Gran Lisboa. "
                    "Servicios de limpieza doméstica y contacto directo por teléfono "
                    "o WhatsApp."
                ),
                "h1": "Maria — Servicios de Limpieza en Gran Lisboa",
                "og_title": "Maria | Profesional de Limpieza en Gran Lisboa",
            },
            "fr": {
                "title": "Maria | Professionnelle du Ménage dans le Grand Lisbonne",
                "meta_description": (
                    "Découvrez Maria, professionnelle du ménage dans le Grand Lisbonne. "
                    "Services de ménage domestique et contact direct par téléphone "
                    "ou WhatsApp."
                ),
                "h1": "Maria — Services de Ménage dans le Grand Lisbonne",
                "og_title": "Maria | Professionnelle du Ménage dans le Grand Lisbonne",
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
            "en": {
                "intro": (
                    "Maria is part of the FAZDETUDO.PT partner network for cleaning "
                    "services in Greater Lisbon. You can contact her directly by phone "
                    "or WhatsApp to explain the type of property, the service required "
                    "and availability."
                ),
                "sections": [
                    {
                        "h2": "Cleaning services in Greater Lisbon",
                        "html": (
                            "<p>Through this profile you can contact Maria for domestic "
                            "cleaning requests — for example regular, deep or one-off "
                            "cleaning — always subject to direct confirmation.</p>"
                            "<p>Contact Maria directly to confirm availability and the "
                            "type of cleaning required. Do not assume every type of "
                            "service without agreeing first.</p>"
                        ),
                    },
                    {
                        "h2": "How to request the service",
                        "html": (
                            "<ol>"
                            "<li>state the location;</li>"
                            "<li>state the type and size of the property;</li>"
                            "<li>explain the type of cleaning;</li>"
                            "<li>send photos on WhatsApp if useful;</li>"
                            "<li>confirm availability directly with Maria.</li>"
                            "</ol>"
                        ),
                    },
                    {
                        "h2": "Service area",
                        "html": (
                            "<p>Greater Lisbon.</p>"
                            "<p>The exact travel area should be confirmed directly "
                            "with the professional.</p>"
                        ),
                    },
                ],
            },
            "es": {
                "intro": (
                    "Maria forma parte de la red de colaboradores FAZDETUDO.PT para "
                    "servicios de limpieza en Gran Lisboa. Puede contactarla "
                    "directamente por teléfono o WhatsApp para explicar el tipo de "
                    "inmueble, el servicio solicitado y la disponibilidad."
                ),
                "sections": [
                    {
                        "h2": "Servicios de limpieza en Gran Lisboa",
                        "html": (
                            "<p>A través de este perfil puede contactar a Maria para "
                            "solicitudes de limpieza doméstica — por ejemplo limpieza "
                            "regular, profunda o puntual — siempre sujeto a "
                            "confirmación directa.</p>"
                            "<p>Contacte directamente a Maria para confirmar "
                            "disponibilidad y el tipo de limpieza deseado. No asuma "
                            "automáticamente todos los tipos de servicio sin acordarlo "
                            "antes.</p>"
                        ),
                    },
                    {
                        "h2": "Cómo pedir el servicio",
                        "html": (
                            "<ol>"
                            "<li>indicar la localidad;</li>"
                            "<li>indicar el tipo y el tamaño del inmueble;</li>"
                            "<li>explicar el tipo de limpieza;</li>"
                            "<li>enviar fotografías por WhatsApp, si es útil;</li>"
                            "<li>confirmar la disponibilidad directamente con Maria.</li>"
                            "</ol>"
                        ),
                    },
                    {
                        "h2": "Zona de servicio",
                        "html": (
                            "<p>Gran Lisboa.</p>"
                            "<p>La zona exacta de desplazamiento debe confirmarse "
                            "directamente con la profesional.</p>"
                        ),
                    },
                ],
            },
            "fr": {
                "intro": (
                    "Maria fait partie du réseau de partenaires FAZDETUDO.PT pour les "
                    "services de ménage dans le Grand Lisbonne. Vous pouvez la "
                    "contacter directement par téléphone ou WhatsApp pour expliquer "
                    "le type de logement, le service souhaité et les disponibilités."
                ),
                "sections": [
                    {
                        "h2": "Services de ménage dans le Grand Lisbonne",
                        "html": (
                            "<p>Via ce profil, vous pouvez contacter Maria pour des "
                            "demandes de ménage domestique — par exemple un ménage "
                            "régulier, en profondeur ou ponctuel — toujours sous "
                            "réserve de confirmation directe.</p>"
                            "<p>Contactez Maria directement pour confirmer les "
                            "disponibilités et le type de ménage souhaité. Ne supposez "
                            "pas automatiquement tous les types de service sans "
                            "convenir d'abord.</p>"
                        ),
                    },
                    {
                        "h2": "Comment demander le service",
                        "html": (
                            "<ol>"
                            "<li>indiquer la localité ;</li>"
                            "<li>indiquer le type et la taille du logement ;</li>"
                            "<li>expliquer le type de ménage ;</li>"
                            "<li>envoyer des photos sur WhatsApp, si c'est utile ;</li>"
                            "<li>confirmer les disponibilités directement avec Maria.</li>"
                            "</ol>"
                        ),
                    },
                    {
                        "h2": "Zone d'intervention",
                        "html": (
                            "<p>Grand Lisbonne.</p>"
                            "<p>La zone exacte de déplacement doit être confirmée "
                            "directement avec la professionnelle.</p>"
                        ),
                    },
                ],
            },
        },
    },
    "wallfixtv": {
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
            "en": {
                "title": "WallFixTV.pt | Professional TV Wall Mounting",
                "meta_description": (
                    "Meet WallFixTV.pt, a FAZDETUDO.PT partner specialised in "
                    "professional TV wall mounting and cable management."
                ),
                "h1": "WallFixTV.pt — Professional TV Wall Mounting",
                "og_title": "WallFixTV.pt | Professional TV Wall Mounting",
            },
            "es": {
                "title": "WallFixTV.pt | Instalación de TV en Pared",
                "meta_description": (
                    "Conozca WallFixTV.pt, colaborador FAZDETUDO.PT especializado en "
                    "instalación profesional de televisores en pared y organización "
                    "de cables."
                ),
                "h1": "WallFixTV.pt — Instalación de TV en Pared",
                "og_title": "WallFixTV.pt | Instalación de TV en Pared",
            },
            "fr": {
                "title": "WallFixTV.pt | Installation de TV au Mur",
                "meta_description": (
                    "Découvrez WallFixTV.pt, partenaire FAZDETUDO.PT spécialisé dans "
                    "l'installation professionnelle de téléviseurs au mur et "
                    "l'organisation des câbles."
                ),
                "h1": "WallFixTV.pt — Installation de TV au Mur",
                "og_title": "WallFixTV.pt | Installation de TV au Mur",
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
            "en": {
                "intro": (
                    "WallFixTV.pt is part of the FAZDETUDO.PT partner network for "
                    "specialist television wall mounting."
                ),
                "contact_note": (
                    "For information or a quote, visit the official WallFixTV.pt website."
                ),
                "sections": [
                    {
                        "h2": "Professional TV Wall Mounting",
                        "html": (
                            "<p>Professional TV wall mounting with accurate levelling, "
                            "suitable fixings, bracket installation and cable management.</p>"
                        ),
                    },
                    {
                        "h2": "Service area",
                        "html": "<p>Greater Lisbon · South Bank.</p>",
                    },
                ],
            },
            "es": {
                "intro": (
                    "WallFixTV.pt forma parte de la red de colaboradores FAZDETUDO.PT "
                    "para instalación especializada de televisores en pared."
                ),
                "contact_note": (
                    "Para información o presupuesto, visite directamente el sitio "
                    "oficial de WallFixTV.pt."
                ),
                "sections": [
                    {
                        "h2": "Instalación profesional de TV",
                        "html": (
                            "<p>Instalación profesional de televisores en pared, con "
                            "nivelación precisa, fijaciones adecuadas, montaje del "
                            "soporte y organización de cables.</p>"
                        ),
                    },
                    {
                        "h2": "Zona de servicio",
                        "html": "<p>Gran Lisboa · Margen Sur.</p>",
                    },
                ],
            },
            "fr": {
                "intro": (
                    "WallFixTV.pt fait partie du réseau de partenaires FAZDETUDO.PT "
                    "pour l'installation spécialisée de téléviseurs au mur."
                ),
                "contact_note": (
                    "Pour des informations ou un devis, visitez directement le site "
                    "officiel de WallFixTV.pt."
                ),
                "sections": [
                    {
                        "h2": "Installation professionnelle de TV",
                        "html": (
                            "<p>Installation professionnelle de téléviseurs au mur avec "
                            "nivellement précis, fixations adaptées, pose du support "
                            "et organisation des câbles.</p>"
                        ),
                    },
                    {
                        "h2": "Zone d'intervention",
                        "html": "<p>Grand Lisbonne · Rive Sud.</p>",
                    },
                ],
            },
        },
    },
    "valeriu": {
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
            "en": {
                "title": "Valeriu | Renovations and General Works in Lisbon",
                "meta_description": (
                    "Meet Valeriu, a FAZDETUDO.PT partner for renovations, home "
                    "restoration and general works in Lisbon, the South Bank and Azeitão."
                ),
                "h1": "Valeriu — Renovations and General Works",
                "og_title": "Valeriu | Renovations and General Works",
            },
            "es": {
                "title": "Valeriu | Reformas y Obras en Lisboa",
                "meta_description": (
                    "Conozca a Valeriu, colaborador FAZDETUDO.PT para reformas, "
                    "rehabilitación de viviendas y obras generales en Lisboa, Margen "
                    "Sur y Azeitão."
                ),
                "h1": "Valeriu — Reformas y Obras Generales",
                "og_title": "Valeriu | Reformas y Obras Generales",
            },
            "fr": {
                "title": "Valeriu | Rénovations et Travaux à Lisbonne",
                "meta_description": (
                    "Découvrez Valeriu, partenaire FAZDETUDO.PT pour les rénovations, "
                    "la rénovation de logements et les travaux généraux à Lisbonne, "
                    "sur la Rive Sud et à Azeitão."
                ),
                "h1": "Valeriu — Rénovations et Travaux Généraux",
                "og_title": "Valeriu | Rénovations et Travaux Généraux",
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
            "en": {
                "intro": (
                    "Valeriu is part of the FAZDETUDO.PT partner network for general "
                    "works, home restoration and renovations in Lisbon, the South Bank "
                    "and Azeitão."
                ),
                "contact_note": "Phone contact only.",
                "sections": [
                    {
                        "h2": "General Works and Renovations",
                        "html": (
                            "<p>Areas of work: general works, home restoration and "
                            "general renovations. Contact him directly to confirm "
                            "availability and the scope of the work required.</p>"
                        ),
                    },
                    {
                        "h2": "Service area",
                        "html": (
                            "<p>Lisbon · South Bank · Azeitão.</p>"
                            "<p>The exact travel area should be confirmed directly.</p>"
                        ),
                    },
                ],
            },
            "es": {
                "intro": (
                    "Valeriu forma parte de la red de colaboradores FAZDETUDO.PT para "
                    "obras generales, rehabilitación de viviendas y reformas en Lisboa, "
                    "Margen Sur y Azeitão."
                ),
                "contact_note": "Contacto solo por teléfono.",
                "sections": [
                    {
                        "h2": "Obras y reformas",
                        "html": (
                            "<p>Áreas de trabajo: obras generales, rehabilitación de "
                            "viviendas y reformas generales. Contacte directamente para "
                            "confirmar disponibilidad y el alcance del trabajo "
                            "solicitado.</p>"
                        ),
                    },
                    {
                        "h2": "Zona de servicio",
                        "html": (
                            "<p>Lisboa · Margen Sur · Azeitão.</p>"
                            "<p>La zona exacta de desplazamiento debe confirmarse "
                            "directamente.</p>"
                        ),
                    },
                ],
            },
            "fr": {
                "intro": (
                    "Valeriu fait partie du réseau de partenaires FAZDETUDO.PT pour "
                    "les travaux généraux, la rénovation de logements et les "
                    "rénovations à Lisbonne, sur la Rive Sud et à Azeitão."
                ),
                "contact_note": "Contact uniquement par téléphone.",
                "sections": [
                    {
                        "h2": "Travaux et rénovations",
                        "html": (
                            "<p>Domaines d'intervention : travaux généraux, rénovation "
                            "de logements et rénovations générales. Contactez-le "
                            "directement pour confirmer les disponibilités et le "
                            "périmètre des travaux souhaités.</p>"
                        ),
                    },
                    {
                        "h2": "Zone d'intervention",
                        "html": (
                            "<p>Lisbonne · Rive Sud · Azeitão.</p>"
                            "<p>La zone exacte de déplacement doit être confirmée "
                            "directement.</p>"
                        ),
                    },
                ],
            },
        },
    },
}


def validate_profile_i18n(partner_id: str, data: dict) -> None:
    for lang in LANGS:
        if lang not in data.get("seo", {}):
            raise ValueError(f"{partner_id}: missing profile seo[{lang}]")
        if lang not in data.get("content", {}):
            raise ValueError(f"{partner_id}: missing profile content[{lang}]")
        seo = data["seo"][lang]
        for key in ("title", "meta_description", "h1"):
            if not seo.get(key):
                raise ValueError(f"{partner_id}: missing seo[{lang}].{key}")
        content = data["content"][lang]
        if not content.get("intro"):
            raise ValueError(f"{partner_id}: missing content[{lang}].intro")


def apply_profile_i18n(partners: list[dict]) -> None:
    """Replace/merge profile seo+content for every partner with PROFILE_BY_ID entry."""
    for partner in partners:
        pid = partner.get("id")
        data = PROFILE_BY_ID.get(pid)
        if not data:
            continue
        validate_profile_i18n(pid, data)
        partner["profile"] = {
            "enabled": True,
            "slug": data["slug"],
            "seo": data["seo"],
            "content": data["content"],
        }
