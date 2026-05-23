# -*- coding: utf-8 -*-
"""Homepage (index.html) translations and URL helpers."""

from __future__ import annotations

from service_page_i18n import BASE_URL, LANGS, LANG_HTML

LANG_LABELS = {
    "pt": ("Português", "https://flagcdn.com/w20/pt.png"),
    "en": ("English", "https://flagcdn.com/w20/gb.png"),
    "es": ("Español", "https://flagcdn.com/w20/es.png"),
    "fr": ("Français", "https://flagcdn.com/w20/fr.png"),
}

HOME_URLS = {
    "pt": f"{BASE_URL}/",
    "en": f"{BASE_URL}/en/",
    "es": f"{BASE_URL}/es/",
    "fr": f"{BASE_URL}/fr/",
}


def home_url(lang: str) -> str:
    return HOME_URLS[lang]


def lang_switch_href(current: str, target: str) -> str:
    """Relative href from current language folder to target homepage."""
    if current == target:
        return "./" if current != "pt" else "/"
    if target == "pt":
        return "../" if current != "pt" else "/"
    if current == "pt":
        return f"/{target}/"
    return f"../{target}/"


def render_home_hreflang() -> str:
    lines = [
        f'    <link rel="alternate" hreflang="pt-PT" href="{HOME_URLS["pt"]}" />',
        f'    <link rel="alternate" hreflang="pt" href="{HOME_URLS["pt"]}" />',
        f'    <link rel="alternate" hreflang="en" href="{HOME_URLS["en"]}" />',
        f'    <link rel="alternate" hreflang="es" href="{HOME_URLS["es"]}" />',
        f'    <link rel="alternate" hreflang="fr" href="{HOME_URLS["fr"]}" />',
        f'    <link rel="alternate" hreflang="x-default" href="{HOME_URLS["pt"]}" />',
    ]
    return "\n".join(lines)


def render_lang_switcher(current_lang: str) -> str:
    info = LANG_LABELS[current_lang]
    options = []
    for code in LANGS:
        href = lang_switch_href(current_lang, code)
        label, flag = LANG_LABELS[code]
        active = " active" if code == current_lang else ""
        options.append(
            f'                            <a href="{href}" class="lang-option lang-option--nav{active}" '
            f'hreflang="{LANG_HTML[code]}" lang="{LANG_HTML[code]}">'
            f'<img src="{flag}" alt=""> {label}</a>'
        )
    return f"""                    <div class="lang-switcher" id="lang-switcher">
                        <button class="lang-toggle" id="lang-toggle" aria-expanded="false">
                            <img src="{info[1]}" alt="" class="lang-flag" id="lang-flag">
                            <span id="lang-label">{info[0]}</span>
                            <i class="fa-solid fa-chevron-down lang-chevron" aria-hidden="true"></i>
                        </button>
                        <div class="lang-dropdown" id="lang-dropdown">
{chr(10).join(options)}
                        </div>
                    </div>"""


HOME_META = {
    "pt": {
        "title": "Faz de Tudo | Serviços de Handyman e Reparações ao Domicílio",
        "description": "Precisa de especialistas? Do AVAC e piscinas, às remodelações completas e pequenas reparações. O Faz de Tudo tem a equipa certa para qualquer obra ou manutenção na sua casa ou empresa na Grande Lisboa, Cascais, Estoril e Setúbal. Rapidez e garantia!",
        "og_title": "Faz de Tudo | Serviços de Handyman e Reparações",
        "json_desc": "Serviços profissionais de handyman, remodelações, AVAC, pintura em alpinismo e manutenção de piscinas na Grande Lisboa e Setúbal.",
        "nav_aria": "Navegação principal",
        "logo_alt": "Faz de Tudo PT - Serviços de faz tudo em Lisboa",
        "section_logo_alt": "Profissional faz tudo",
        "menu_aria": "Abrir menu",
        "review_prev": "Crítica anterior",
        "review_next": "Crítica seguinte",
        "view_google": "Ver críticas no Google",
        "wa_close": "Fechar chat",
        "wa_send": "Enviar mensagem",
        "wa_float": "Contactar via WhatsApp",
        "float_call": "Ligar agora",
        "address": "Lisboa, Portugal",
    },
    "en": {
        "title": "Faz de Tudo | Handyman and Home Repair Services",
        "description": "Need specialists? From HVAC and pools to full renovations and small repairs. Faz de Tudo has the right team for any job at your home or business in Greater Lisbon, Cascais, Estoril and Setúbal.",
        "og_title": "Faz de Tudo | Handyman and Home Repair Services",
        "json_desc": "Professional handyman, renovations, HVAC, rope-access facade painting and pool maintenance across Greater Lisbon and Setúbal.",
        "nav_aria": "Main navigation",
        "logo_alt": "Faz de Tudo PT - Handyman services in Lisbon",
        "section_logo_alt": "Professional handyman",
        "menu_aria": "Open menu",
        "review_prev": "Previous review",
        "review_next": "Next review",
        "view_google": "View reviews on Google",
        "wa_close": "Close chat",
        "wa_send": "Send message",
        "wa_float": "Contact via WhatsApp",
        "float_call": "Call now",
        "address": "Lisbon, Portugal",
    },
    "es": {
        "title": "Faz de Tudo | Servicios de Manitas y Reparaciones a Domicilio",
        "description": "¿Necesita especialistas? Del AVAC y piscinas a reformas completas y pequeñas reparaciones. Faz de Tudo tiene el equipo adecuado en la Gran Lisboa, Cascais, Estoril y Setúbal.",
        "og_title": "Faz de Tudo | Servicios de Manitas y Reparaciones",
        "json_desc": "Servicios profesionales de manitas, reformas, climatización, pintura en alpinismo y mantenimiento de piscinas en la Gran Lisboa y Setúbal.",
        "nav_aria": "Navegación principal",
        "logo_alt": "Faz de Tudo PT - Servicios en Lisboa",
        "section_logo_alt": "Profesional manitas",
        "menu_aria": "Abrir menú",
        "review_prev": "Reseña anterior",
        "review_next": "Reseña siguiente",
        "view_google": "Ver reseñas en Google",
        "wa_close": "Cerrar chat",
        "wa_send": "Enviar mensaje",
        "wa_float": "Contactar por WhatsApp",
        "float_call": "Llamar ahora",
        "address": "Lisboa, Portugal",
    },
    "fr": {
        "title": "Faz de Tudo | Services de Bricolage et Réparations à Domicile",
        "description": "Besoin de spécialistes ? De la climatisation et piscines aux rénovations complètes et petites réparations. Faz de Tudo intervient dans le Grand Lisbonne, Cascais, Estoril et Setúbal.",
        "og_title": "Faz de Tudo | Bricolage et Réparations à Domicile",
        "json_desc": "Services professionnels de bricolage, rénovations, CVC, peinture en cordes et entretien de piscines dans le Grand Lisbonne et Setúbal.",
        "nav_aria": "Navigation principale",
        "logo_alt": "Faz de Tudo PT - Services à Lisbonne",
        "section_logo_alt": "Professionnel bricolage",
        "menu_aria": "Ouvrir le menu",
        "review_prev": "Avis précédent",
        "review_next": "Avis suivant",
        "view_google": "Voir les avis sur Google",
        "wa_close": "Fermer le chat",
        "wa_send": "Envoyer le message",
        "wa_float": "Contacter via WhatsApp",
        "float_call": "Appeler maintenant",
        "address": "Lisbonne, Portugal",
    },
}

# UI strings aligned with script.js T.*
HOME_UI = {
    "pt": {
        "nav_home": "Início",
        "nav_services": "Serviços",
        "nav_about": "Sobre nós",
        "nav_contact": "Contacto",
        "footer_links": "Links",
        "hero_title": "O Seu Faz-Tudo de Confiança na Grande Lisboa e Margem Sul",
        "hero_subtitle": "Precisa de pendurar um varão, retocar uma pintura, reparar uma torneira ou resolver aquela lista de pequenos arranjos que nunca mais acabam? Dispomos também de serviços especializados, mas somos, acima de tudo, o parceiro ideal para cuidar do seu espaço com rapidez, eficácia e limpeza. Esqueça as complicações: um único contacto resolve tudo.",
        "hero_btn_quote": "Pedir orçamento grátis",
        "hero_btn_call": "Ligue agora",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Avaliado com 5.0 no Google",
        "services_title": "Os Nossos Serviços Profissionais",
        "services_subtitle": "Soluções fiáveis e especializadas para a manutenção, reparação e remodelação da sua casa ou empresa na Grande Lisboa.",
        "advantages_title": "Porquê escolher-nos?",
        "testimonials_title": "Críticas",
        "faq_title": "Perguntas Frequentes",
        "contact_title": "Contacte-nos",
        "contact_subtitle": "Estamos prontos para ajudar. Peça o seu orçamento grátis.",
        "social_cta": "Siga-nos e veja os nossos trabalhos",
        "footer_rights": "Faz de Tudo PT. Todos os direitos reservados.",
        "wa_greeting": "Como posso ajudar?",
        "wa_placeholder": "Escreva uma mensagem...",
        "wa_online": "Online",
        "learn_more": "Saber mais",
        "badge_premium": "Premium",
        "badge_specialty": "Especialidade",
    },
    "en": {
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_about": "About us",
        "nav_contact": "Contact",
        "footer_links": "Links",
        "hero_title": "Your trusted handyman in Portugal",
        "hero_subtitle": "Painting, plumbing, electrical, carpentry and much more. Professional service with quality guarantee.",
        "hero_btn_quote": "Get a free quote",
        "hero_btn_call": "Call now",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Rated 5.0 on Google",
        "services_title": "Our Professional Services",
        "services_subtitle": "Reliable, specialist solutions for maintenance, repairs and renovations at your home or business in Greater Lisbon.",
        "advantages_title": "Why choose us?",
        "testimonials_title": "Reviews",
        "faq_title": "Frequently Asked Questions",
        "contact_title": "Contact us",
        "contact_subtitle": "We are ready to help. Request your free quote.",
        "social_cta": "Follow us and see our work",
        "footer_rights": "Faz de Tudo PT. All rights reserved.",
        "wa_greeting": "How can I help you?",
        "wa_placeholder": "Type a message...",
        "wa_online": "Online",
        "learn_more": "Learn more",
        "badge_premium": "Premium",
        "badge_specialty": "Specialty",
    },
    "es": {
        "nav_home": "Inicio",
        "nav_services": "Servicios",
        "nav_about": "Sobre nosotros",
        "nav_contact": "Contacto",
        "footer_links": "Enlaces",
        "hero_title": "Su profesional de confianza en Portugal",
        "hero_subtitle": "Pinturas, fontanería, electricidad, carpintería y mucho más. Servicio profesional con garantía de calidad.",
        "hero_btn_quote": "Pedir presupuesto gratis",
        "hero_btn_call": "Llame ahora",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Valorado con 5.0 en Google",
        "services_title": "Nuestros Servicios Profesionales",
        "services_subtitle": "Soluciones fiables y especializadas para el mantenimiento, reparación y reforma de su hogar o empresa en la Gran Lisboa.",
        "advantages_title": "¿Por qué elegirnos?",
        "testimonials_title": "Reseñas",
        "faq_title": "Preguntas Frecuentes",
        "contact_title": "Contáctenos",
        "contact_subtitle": "Estamos listos para ayudar. Solicite su presupuesto gratis.",
        "social_cta": "Síguenos y mira nuestros trabajos",
        "footer_rights": "Faz de Tudo PT. Todos los derechos reservados.",
        "wa_greeting": "¿Cómo puedo ayudarle?",
        "wa_placeholder": "Escriba un mensaje...",
        "wa_online": "En línea",
        "learn_more": "Saber más",
        "badge_premium": "Premium",
        "badge_specialty": "Especialidad",
    },
    "fr": {
        "nav_home": "Accueil",
        "nav_services": "Services",
        "nav_about": "À propos",
        "nav_contact": "Contact",
        "footer_links": "Liens",
        "hero_title": "Votre homme à tout faire de confiance au Portugal",
        "hero_subtitle": "Peinture, plomberie, électricité, menuiserie et bien plus. Service professionnel avec garantie de qualité.",
        "hero_btn_quote": "Devis gratuit",
        "hero_btn_call": "Appelez maintenant",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Noté 5.0 sur Google",
        "services_title": "Nos Services Professionnels",
        "services_subtitle": "Solutions fiables et spécialisées pour l'entretien, la réparation et la rénovation de votre maison ou entreprise dans le Grand Lisbonne.",
        "advantages_title": "Pourquoi nous choisir ?",
        "testimonials_title": "Avis",
        "faq_title": "Questions Fréquentes",
        "contact_title": "Contactez-nous",
        "contact_subtitle": "Nous sommes prêts à vous aider. Demandez votre devis gratuit.",
        "social_cta": "Suivez-nous et découvrez nos réalisations",
        "footer_rights": "Faz de Tudo PT. Tous droits réservés.",
        "wa_greeting": "Comment puis-je vous aider ?",
        "wa_placeholder": "Écrivez un message...",
        "wa_online": "En ligne",
        "learn_more": "En savoir plus",
        "badge_premium": "Premium",
        "badge_specialty": "Spécialité",
    },
}

# SYNC: order = index.html services grid = script.js SERVICE_LANDING_SLUGS
SERVICE_CARDS = [
    {
        "slug": "servico-remodelacoes.html",
        "icon": "house-chimney",
        "featured": True,
        "badge": "premium",
        "pt": ("Remodelações e Obras", "Remodelação de cozinhas e casas de banho, construção de novas divisões, ampliações e obras estruturais. Do projeto à entrega da chave."),
        "en": ("Renovations & Construction", "Kitchen and bathroom renovations, new rooms, extensions and structural works. From design to handover."),
        "es": ("Reformas y Obras", "Reforma de cocinas y baños, nuevas estancias, ampliaciones y obras estructurales. Del proyecto a la entrega."),
        "fr": ("Rénovations et Travaux", "Rénovation cuisines et salles de bains, nouvelles pièces, extensions et gros œuvre. Du projet à la livraison."),
    },
    {
        "slug": "servico-recuperar-casa.html",
        "icon": "house-circle-check",
        "featured": True,
        "badge": "specialty",
        "pt": ("Recuperar Casa", "Recuperação completa de casas devolutas, herdadas ou degradadas. Da estrutura aos acabamentos, devolvemos vida e habitabilidade ao seu imóvel."),
        "en": ("Home Restoration", "Complete restoration of vacant, inherited or run-down homes. From structure to finishes, we bring your property back to life."),
        "es": ("Recuperar Casa", "Recuperación completa de casas vacías, heredadas o deterioradas. De la estructura a los acabados, devolvemos habitabilidad."),
        "fr": ("Rénover une Maison", "Récupération complète de maisons vacantes, héritées ou dégradées. De la structure aux finitions."),
    },
    {
        "slug": "servico-pinturas.html",
        "icon": "paint-roller",
        "featured": False,
        "badge": None,
        "pt": ("Pinturas Gerais", "Pintura interior e exterior com proteção de mobiliário, tratamento de humidades e acabamentos perfeitos."),
        "en": ("General Painting", "Interior and exterior painting with furniture protection, damp treatment and flawless finishes."),
        "es": ("Pinturas Generales", "Pintura interior y exterior con protección del mobiliario, humedades y acabados perfectos."),
        "fr": ("Peinture Générale", "Peinture intérieure et extérieure avec protection du mobilier et finitions impeccables."),
    },
    {
        "slug": "servico-pintura-fachadas-alpinismo.html",
        "icon": "building",
        "featured": True,
        "badge": "specialty",
        "pt": ("Pintura em Alpinismo", "Reabilitação de fachadas em altura com trabalho em cordas. Sem andaimes, mais rápido e económico."),
        "en": ("Rope-Access Facade Painting", "High-rise facade refurbishment with industrial rope access. No scaffolding, faster and more economical."),
        "es": ("Pintura en Alpinismo", "Rehabilitación de fachadas en altura con cuerdas. Sin andamios, más rápido y económico."),
        "fr": ("Peinture en Cordes", "Réhabilitation de façades en hauteur par cordes. Sans échafaudage, plus rapide et économique."),
    },
    {
        "slug": "servico-canalizacoes.html",
        "icon": "faucet-drip",
        "featured": False,
        "badge": None,
        "pt": ("Canalizações", "Reparação de fugas, desentupimentos urgentes, substituição de torneiras, autoclismos e tubagens."),
        "en": ("Plumbing", "Leak repair, urgent unblocking, tap, toilet and pipe replacement."),
        "es": ("Fontanería", "Reparación de fugas, desatascos urgentes, grifos, inodoros y tuberías."),
        "fr": ("Plomberie", "Réparation de fuites, débouchage urgent, robinets, WC et canalisations."),
    },
    {
        "slug": "servico-electricidade.html",
        "icon": "bolt",
        "featured": False,
        "badge": None,
        "pt": ("Electricidade", "Avarias elétricas, quadros, disjuntores, instalação de tomadas e modernização para iluminação LED."),
        "en": ("Electrical", "Electrical faults, fuse boards, breakers, sockets and LED lighting upgrades."),
        "es": ("Electricidad", "Averías eléctricas, cuadros, magnetotérmicos, enchufes e iluminación LED."),
        "fr": ("Électricité", "Pannes électriques, tableaux, disjoncteurs, prises et éclairage LED."),
    },
    {
        "slug": "servico-carpintaria.html",
        "icon": "hammer",
        "featured": False,
        "badge": None,
        "pt": ("Carpintaria", "Montagem de móveis (IKEA e medida), afinação de portas, rodapés e pequenas estruturas em madeira."),
        "en": ("Carpentry", "Furniture assembly (IKEA and custom), door adjustment, skirting and woodwork."),
        "es": ("Carpintería", "Montaje de muebles (IKEA y a medida), ajuste de puertas, rodapiés y madera."),
        "fr": ("Menuiserie", "Montage de meubles (IKEA et sur mesure), réglage de portes et boiseries."),
    },
    {
        "slug": "servico-reparacoes-gerais.html",
        "icon": "screwdriver-wrench",
        "featured": False,
        "badge": None,
        "pt": ("Reparações Gerais", "O seu faz-tudo para fixar prateleiras, TVs, cortinados, selar juntas e resolver a lista de pequenos arranjos."),
        "en": ("General Repairs", "Your handyman for shelves, TVs, curtain rails, silicone sealing and small fix-it jobs."),
        "es": ("Reparaciones Generales", "Su manitas para estanterías, TV, cortinajes, silicona y pequeños arreglos."),
        "fr": ("Réparations Générales", "Votre bricoleur pour étagères, TV, tringles, silicone et petites réparations."),
    },
    {
        "slug": "servico-manutencao.html",
        "icon": "trowel-bricks",
        "featured": False,
        "badge": None,
        "pt": ("Manutenção", "Planos preventivos para condomínios, inspeção de telhados, calhas e lavagem de pátios a alta pressão."),
        "en": ("Maintenance", "Preventive plans for condominiums, roof and gutter inspection, pressure washing."),
        "es": ("Mantenimiento", "Planes preventivos para comunidades, tejados, canalones y lavado a presión."),
        "fr": ("Entretien", "Plans préventifs pour copropriétés, toitures, gouttières et nettoyage haute pression."),
    },
    {
        "slug": "servico-limpezas.html",
        "icon": "broom",
        "featured": False,
        "badge": None,
        "pt": ("Limpezas", "Limpeza profunda doméstica, pós-obra, escritórios e condomínios com equipas experientes e rigorosas."),
        "en": ("Cleaning", "Deep domestic, post-construction, office and condominium cleaning by experienced teams."),
        "es": ("Limpieza", "Limpieza profunda doméstica, post-obra, oficinas y comunidades con equipos expertos."),
        "fr": ("Nettoyage", "Nettoyage profond domestique, après-travaux, bureaux et copropriétés."),
    },
    {
        "slug": "servico-jardinagem.html",
        "icon": "seedling",
        "featured": False,
        "badge": None,
        "pt": ("Jardinagem", "Manutenção de jardins, corte de relva, poda de árvores, limpeza de terrenos e reparação de sistemas de rega."),
        "en": ("Gardening", "Garden maintenance, lawn mowing, tree pruning, plot clearance and irrigation repair."),
        "es": ("Jardinería", "Mantenimiento de jardines, césped, poda, limpieza de terrenos y riego."),
        "fr": ("Jardinage", "Entretien de jardins, tonte, taille, nettoyage de terrains et arrosage."),
    },
    {
        "slug": "servico-mudancas.html",
        "icon": "truck-fast",
        "featured": False,
        "badge": None,
        "pt": ("Mudanças", "Mudanças residenciais e comerciais com transporte seguro, embalagem cuidada e desmontagem de móveis."),
        "en": ("Moving", "Residential and commercial moves with safe transport, careful packing and furniture disassembly."),
        "es": ("Mudanzas", "Mudanzas residenciales y comerciales con transporte seguro, embalaje y montaje."),
        "fr": ("Déménagements", "Déménagements résidentiels et commerciaux avec transport sécurisé et emballage."),
    },
    {
        "slug": "servico-informatica.html",
        "icon": "laptop-medical",
        "featured": False,
        "badge": None,
        "pt": ("Informática", "Reparação de computadores, configuração de redes Wi-Fi estáveis, impressoras e soluções de smart home."),
        "en": ("IT Services", "Computer repair, stable Wi-Fi setup, printers and smart home solutions."),
        "es": ("Informática", "Reparación de ordenadores, Wi-Fi, impresoras y smart home."),
        "fr": ("Informatique", "Réparation PC, Wi-Fi, imprimantes et maison connectée."),
    },
    {
        "slug": "servico-serralharia.html",
        "icon": "key",
        "featured": False,
        "badge": None,
        "pt": ("Serralharia", "Abertura de portas urgente, substituição de fechaduras e cilindros, e reparação de portões e grades."),
        "en": ("Locksmithing", "Emergency door opening, lock and cylinder replacement, gates and grilles."),
        "es": ("Cerrajería", "Apertura urgente de puertas, cerraduras, portones y rejas."),
        "fr": ("Serrurerie", "Ouverture de porte d'urgence, serrures, portails et grilles."),
    },
    {
        "slug": "servico-climatizacao.html",
        "icon": "wind",
        "featured": False,
        "badge": None,
        "pt": ("Climatização (AVAC)", "Instalação de ar condicionado (splits), cargas de gás, limpeza de filtros e manutenção preventiva AVAC."),
        "en": ("Air Conditioning (HVAC)", "AC installation (splits), gas recharge, filter cleaning and preventive HVAC maintenance."),
        "es": ("Climatización (AVAC)", "Instalación de aire acondicionado, carga de gas, filtros y mantenimiento AVAC."),
        "fr": ("Climatisation (CVC)", "Installation climatisation, recharge gaz, filtres et entretien CVC."),
    },
    {
        "slug": "servico-estores-persianas.html",
        "icon": "window-maximize",
        "featured": False,
        "badge": None,
        "pt": ("Estores e Persianas", "Reparação de estores manuais e eléctricos, fitas partidas, motores encravados e montagem de mosquiteiras."),
        "en": ("Blinds & Shutters", "Manual and electric blind repair, broken tapes, stuck motors and mosquito nets."),
        "es": ("Persianas y Estores", "Reparación de estores manuales y eléctricos, cintas, motores y mosquiteras."),
        "fr": ("Stores et Volets", "Réparation de stores manuels et électriques, sangles, moteurs et moustiquaires."),
    },
    {
        "slug": "servico-decoracao-interiores.html",
        "icon": "couch",
        "featured": False,
        "badge": None,
        "pt": ("Decoração de Interiores", "Aplicação de cortinados, papel de parede, iluminação e home staging para valorizar ou vender o seu imóvel."),
        "en": ("Interior Design", "Curtains, wallpaper, lighting and home staging to enhance or sell your property."),
        "es": ("Decoración de Interiores", "Cortinas, papel pintado, iluminación y home staging para vender su inmueble."),
        "fr": ("Décoration Intérieure", "Rideaux, papier peint, éclairage et home staging pour valoriser votre bien."),
    },
    {
        "slug": "servico-piscinas.html",
        "icon": "water-ladder",
        "featured": False,
        "badge": None,
        "pt": ("Piscinas", "Manutenção e limpeza de piscinas, equilíbrio químico da água, revisão de filtros, bombas e deteção de fugas."),
        "en": ("Swimming Pools", "Pool maintenance and cleaning, water chemistry, filters, pumps and leak detection."),
        "es": ("Piscinas", "Mantenimiento y limpieza de piscinas, química del agua, filtros, bombas y fugas."),
        "fr": ("Piscines", "Entretien et nettoyage de piscines, chimie de l'eau, filtres, pompes et fuites."),
    },
]

HANDYMAN = {
    "pt": {
        "badge": "Serviço do Dia a Dia",
        "title": "O que faz um Handyman Profissional?",
        "subtitle": "Não gaste o seu fim de semana com ferramentas. Nós resolvemos a sua lista de pequenos arranjos pendentes com rapidez e eficácia.",
        "cta": "Ver Todos os Detalhes de Reparações",
        "boxes": [
            ("Pequenas Instalações", "wand-magic-sparkles", [
                "Fixação de suportes de TV na parede",
                "Instalação de varões e calhas de cortinados",
                "Pendurar quadros, espelhos pesados e painéis",
                "Montagem de prateleiras, cubos e nichos",
                "Fixação de acessórios de casa de banho e cozinha",
            ]),
            ("Portas, Janelas e Ferragens", "door-closed", [
                "Afinação de portas que arrastam ou caixilharias",
                "Substituição de fechaduras, canhões e trincos",
                "Troca de puxadores de portas e armários",
                "Instalação de molas de retorno e batentes",
                "Lubrificação e ajuste de calhas de correr",
            ]),
            ("Bricolage e Ajustes Rápidos", "plug", [
                "Substituição de lâmpadas antigas por focos LED",
                "Troca de espelhos de tomadas e interruptores avariados",
                "Aplicação de silicone de vedação em banheiras e bancas",
                "Tapar furos antigos em Pladur ou alvenaria",
                "Montagem e fixação de móveis modulares",
            ]),
            ("Manutenção Preventiva", "house-laptop", [
                "Lavagem de alta pressão em pátios, terraços e muros",
                "Limpeza de caleiras e desentupimento de ralos externos",
                "Pequenos restauros em portões ou vedações de madeira",
                "Isolamento de pequenas fissuras externas com mástique",
                "Montagem de estendais de roupa (parede ou teto)",
            ]),
        ],
    },
    "en": {
        "badge": "Everyday Service",
        "title": "What Does a Professional Handyman Do?",
        "subtitle": "Don't spend your weekend with tools. We clear your pending small jobs quickly and efficiently.",
        "cta": "View All General Repair Details",
        "boxes": [
            ("Small Installations", "wand-magic-sparkles", [
                "TV wall mount installation",
                "Curtain poles and track fitting",
                "Hanging pictures, heavy mirrors and panels",
                "Shelf, cube and niche mounting",
                "Bathroom and kitchen accessory fitting",
            ]),
            ("Doors, Windows & Hardware", "door-closed", [
                "Adjusting sticking doors and frames",
                "Lock, cylinder and latch replacement",
                "Door and cabinet handle replacement",
                "Door closer and stop installation",
                "Lubrication and sliding track adjustment",
            ]),
            ("Quick Fixes & DIY", "plug", [
                "Replacing old bulbs with LED fittings",
                "Faulty socket and switch faceplate replacement",
                "Silicone sealing for baths and worktops",
                "Filling old holes in plasterboard or masonry",
                "Modular furniture assembly and fixing",
            ]),
            ("Preventive Maintenance", "house-laptop", [
                "Pressure washing patios, terraces and walls",
                "Gutter cleaning and external drain clearing",
                "Minor gate or wooden fence repairs",
                "Sealing small external cracks with mastic",
                "Clothes line installation (wall or ceiling)",
            ]),
        ],
    },
    "es": {
        "badge": "Servicio del Día a Día",
        "title": "¿Qué hace un Manitas Profesional?",
        "subtitle": "No pierda el fin de semana con herramientas. Resolvemos su lista de pequeños arreglos con rapidez.",
        "cta": "Ver Todos los Detalles de Reparaciones",
        "boxes": [
            ("Pequeñas Instalaciones", "wand-magic-sparkles", [
                "Fijación de soportes de TV en la pared",
                "Instalación de varillas y rieles de cortinas",
                "Colgar cuadros, espejos pesados y paneles",
                "Montaje de estanterías y nichos",
                "Fijación de accesorios de baño y cocina",
            ]),
            ("Puertas, Ventanas y Herrajes", "door-closed", [
                "Ajuste de puertas que rozan o carpintería",
                "Sustitución de cerraduras y cerrojos",
                "Cambio de tiradores de puertas y armarios",
                "Instalación de muelles y topes",
                "Lubricación de carriles correderos",
            ]),
            ("Bricolaje y Ajustes Rápidos", "plug", [
                "Sustitución de bombillas antiguas por LED",
                "Cambio de tapas de enchufes e interruptores",
                "Aplicación de silicona en bañeras y encimeras",
                "Tapar agujeros en pladur o mampostería",
                "Montaje de muebles modulares",
            ]),
            ("Mantenimiento Preventivo", "house-laptop", [
                "Lavado a alta presión en patios y terrazas",
                "Limpieza de canalones y desagües exteriores",
                "Pequeñas reparaciones en portones o vallas",
                "Sellado de fisuras externas con masilla",
                "Montaje de tendederos",
            ]),
        ],
    },
    "fr": {
        "badge": "Service du Quotidien",
        "title": "Que fait un Homme à Tout Faire Professionnel ?",
        "subtitle": "Ne passez pas votre week-end avec des outils. Nous traitons votre liste de petits travaux rapidement.",
        "cta": "Voir Tous les Détails des Réparations",
        "boxes": [
            ("Petites Installations", "wand-magic-sparkles", [
                "Fixation de supports TV muraux",
                "Pose de tringles et rails à rideaux",
                "Accrochage de tableaux, miroirs lourds et panneaux",
                "Montage d'étagères et niches",
                "Fixation d'accessoires salle de bain et cuisine",
            ]),
            ("Portes, Fenêtres et Quincaillerie", "door-closed", [
                "Réglage de portes qui frottent",
                "Remplacement de serrures et cylindres",
                "Changement de poignées de portes et placards",
                "Pose de ferme-portes et butées",
                "Lubrification des rails coulissants",
            ]),
            ("Bricolage et Ajustements Rapides", "plug", [
                "Remplacement d'ampoules par LED",
                "Changement de plaques prises et interrupteurs",
                "Joint silicone pour baignoires et plans de travail",
                "Rebouchage de trous dans placo ou maçonnerie",
                "Montage de meubles modulaires",
            ]),
            ("Entretien Préventif", "house-laptop", [
                "Nettoyage haute pression terrasses et murs",
                "Nettoyage de gouttières et drains extérieurs",
                "Petites réparations de portails ou clôtures bois",
                "Scellement de petites fissures extérieures",
                "Pose de séchoirs à linge",
            ]),
        ],
    },
}
