
# -*- coding: utf-8 -*-
"""
Homepage (index.html) translations and URL helpers.

HOME_UI is the source of truth for hero copy and UI strings in all languages.
Regenerate HTML with: python scripts/generate-servico-pages.py
"""

from __future__ import annotations

from slug_registry import LANGS, LANG_HTML, home_url, render_home_hreflang

LANG_LABELS = {
    "pt": ("Português", "https://flagcdn.com/w20/pt.png"),
    "en": ("English", "https://flagcdn.com/w20/gb.png"),
    "es": ("Español", "https://flagcdn.com/w20/es.png"),
    "fr": ("Français", "https://flagcdn.com/w20/fr.png"),
}

# Alt text descritivo para as bandeiras do dropdown (localizado por idioma da página).
FLAG_ALT = {
    "pt": {"pt": "Bandeira de Portugal", "en": "Bandeira do Reino Unido", "es": "Bandeira de Espanha", "fr": "Bandeira de França"},
    "en": {"pt": "Flag of Portugal", "en": "Flag of the United Kingdom", "es": "Flag of Spain", "fr": "Flag of France"},
    "es": {"pt": "Bandera de Portugal", "en": "Bandera del Reino Unido", "es": "Bandera de España", "fr": "Bandera de Francia"},
    "fr": {"pt": "Drapeau du Portugal", "en": "Drapeau du Royaume-Uni", "es": "Drapeau de l'Espagne", "fr": "Drapeau de la France"},
}

def lang_switch_href(current: str, target: str) -> str:
    """Relative href from current language folder to target homepage."""
    if current == target:
        return "./" if current != "pt" else "/"
    if target == "pt":
        return "../" if current != "pt" else "/"
    if current == "pt":
        return f"/{target}/"
    return f"../{target}/"


def render_lang_switcher(
    current_lang: str,
    href_for_lang=None,
) -> str:
    """Language switcher. Optional href_for_lang(code) overrides homepage links."""
    info = LANG_LABELS[current_lang]
    options = []
    for code in LANGS:
        href = href_for_lang(code) if href_for_lang else lang_switch_href(current_lang, code)
        label, flag = LANG_LABELS[code]
        active = " active" if code == current_lang else ""
        flag_alt = FLAG_ALT[current_lang][code]
        options.append(
            f'                            <a href="{href}" class="lang-option lang-option--nav{active}" '
            f'hreflang="{LANG_HTML[code]}" lang="{LANG_HTML[code]}">'
            f'<img src="{flag}" alt="{flag_alt}"> {label}</a>'
        )
    current_flag_alt = FLAG_ALT[current_lang][current_lang]
    return f"""                    <div class="lang-switcher" id="lang-switcher">
                        <button type="button" class="lang-toggle" id="lang-toggle" aria-expanded="false">
                            <img src="{info[1]}" alt="{current_flag_alt}" class="lang-flag" id="lang-flag">
                            <span id="lang-label">{info[0]}</span>
                            <i class="fa-solid fa-chevron-down lang-chevron" aria-hidden="true"></i>
                        </button>
                        <div class="lang-dropdown" id="lang-dropdown">
{chr(10).join(options)}
                        </div>
                    </div>"""


# Keep HOME_META below — placeholder removed by replacing through end of old render_lang_switcher

HOME_META = {
    "pt": {
        "title": "Handyman e Reparações ao Domicílio | FAZDETUDO.PT",
        "description": (
            "Serviços de handyman, pequenas reparações, montagens e manutenção ao "
            "domicílio na Grande Lisboa e Margem Sul. Peça orçamento por WhatsApp."
        ),
        "og_title": "FAZDETUDO.PT | Handyman e Reparações ao Domicílio",
        "json_desc": (
            "Serviços de handyman, pequenas reparações, montagens e manutenção ao "
            "domicílio na Grande Lisboa, Margem Sul e Setúbal."
        ),
        "nav_aria": "Navegação principal",
        "logo_alt": "FAZDETUDO.PT - Serviços de handyman em Lisboa",
        "section_logo_alt": "Profissional faz tudo",
        "menu_aria": "Abrir menu",
        "review_prev": "Crítica anterior",
        "review_next": "Crítica seguinte",
        "wa_close": "Fechar chat",
        "wa_send": "Enviar mensagem",
        "wa_float": "Contactar via WhatsApp",
        "float_call": "Ligar agora",
        "address": "Grande Lisboa e Margem Sul, Portugal",
    },
    "en": {
        "title": "Handyman and Home Repair Services | FAZDETUDO.PT",
        "description": (
            "Handyman services, small repairs, assembly and home maintenance in "
            "Greater Lisbon and the South Bank. Request a quote on WhatsApp."
        ),
        "og_title": "FAZDETUDO.PT | Handyman and Home Repairs",
        "json_desc": (
            "Handyman services, small repairs, assembly and home maintenance across "
            "Greater Lisbon, the South Bank and Setúbal."
        ),
        "nav_aria": "Main navigation",
        "logo_alt": "FAZDETUDO.PT - Handyman services in Lisbon",
        "section_logo_alt": "Professional handyman",
        "menu_aria": "Open menu",
        "review_prev": "Previous review",
        "review_next": "Next review",
        "wa_close": "Close chat",
        "wa_send": "Send message",
        "wa_float": "Contact via WhatsApp",
        "float_call": "Call now",
        "address": "Greater Lisbon and South Bank, Portugal",
    },
    "es": {
        "title": "Manitas y Reparaciones a Domicilio | FAZDETUDO.PT",
        "description": (
            "Servicios de manitas, pequeñas reparaciones, montajes y mantenimiento a "
            "domicilio en la Gran Lisboa y Margen Sur. Pida presupuesto por WhatsApp."
        ),
        "og_title": "FAZDETUDO.PT | Manitas y Reparaciones a Domicilio",
        "json_desc": (
            "Servicios de manitas, pequeñas reparaciones, montajes y mantenimiento a "
            "domicilio en la Gran Lisboa, Margen Sur y Setúbal."
        ),
        "nav_aria": "Navegación principal",
        "logo_alt": "FAZDETUDO.PT - Servicios en Lisboa",
        "section_logo_alt": "Profesional manitas",
        "menu_aria": "Abrir menú",
        "review_prev": "Reseña anterior",
        "review_next": "Reseña siguiente",
        "wa_close": "Cerrar chat",
        "wa_send": "Enviar mensaje",
        "wa_float": "Contactar por WhatsApp",
        "float_call": "Llamar ahora",
        "address": "Gran Lisboa y Margen Sur, Portugal",
    },
    "fr": {
        "title": "Bricolage et Réparations à Domicile | FAZDETUDO.PT",
        "description": (
            "Services de bricolage, petites réparations, montage et entretien à "
            "domicile dans le Grand Lisbonne et la Rive Sud. Demandez un devis sur WhatsApp."
        ),
        "og_title": "FAZDETUDO.PT | Bricolage et Réparations à Domicile",
        "json_desc": (
            "Services de bricolage, petites réparations, montage et entretien à "
            "domicile dans le Grand Lisbonne, la Rive Sud et Setúbal."
        ),
        "nav_aria": "Navigation principale",
        "logo_alt": "FAZDETUDO.PT - Services à Lisbonne",
        "section_logo_alt": "Professionnel bricolage",
        "menu_aria": "Ouvrir le menu",
        "review_prev": "Avis précédent",
        "review_next": "Avis suivant",
        "wa_close": "Fermer le chat",
        "wa_send": "Envoyer le message",
        "wa_float": "Contacter via WhatsApp",
        "float_call": "Appeler maintenant",
        "address": "Grand Lisbonne et Rive Sud, Portugal",
    },
}

# UI strings aligned with script.js T.*
HOME_UI = {
    "pt": {
        "nav_home": "Início",
        "nav_services": "Serviços",
        "nav_works": "Trabalhos",
        "nav_partners": "Parceiros",
        "nav_about": "Sobre nós",
        "nav_contact": "Contacto",
        "nav_articles": "Artigos",
        "footer_links": "Links",
        "footer_company": "Empresa",
        "header_quote": "Pedir orçamento",
        "hero_title_prefix": "Handyman e",
        "hero_title_accent": "Reparações",
        "hero_title_suffix": "ao Domicílio",
        "hero_language_label": "Atendimento em:",
        "services_kicker": "O QUE FAZEMOS",
        "recent_work_kicker": "TRABALHOS REALIZADOS",
        "partners_compact_title": "SERVIÇOS ESPECIALIZADOS",
        "cta_response_label": "Resposta rápida",
        "hero_eyebrow": "HANDYMAN · GRANDE LISBOA E MARGEM SUL",
        "hero_title": "Handyman e Reparações ao Domicílio",
        "hero_title_line1": "Handyman e reparações",
        "hero_title_line2": "para a sua casa.",
        "footer_tagline": "Handyman, reparações e manutenção ao domicílio.",
        "hero_subtitle": (
            "Pequenas reparações, montagens, manutenção e trabalhos em casa. "
            "Um contacto para resolver várias tarefas."
        ),
        "hero_btn_find": "Encontrar profissional",
        "hero_btn_help": "Preciso de ajuda",
        "hero_btn_quote": "Pedir orçamento por WhatsApp",
        "hero_btn_call": "Ligar agora",
        "hero_reviews_rating": "★★★★★ 5.0 no Google",
        "hero_reviews_suffix": "PT · EN · ES · RO",
        "trust_google": "5.0 Google",
        "trust_quote": "Orçamento gratuito",
        "trust_area": "Grande Lisboa e Margem Sul",
        "trust_langs": "PT · EN · ES · RO",
        "services_title": "Serviços de Handyman",
        "services_subtitle": (
            "Reparações, montagens, manutenção e pequenos trabalhos com "
            "atendimento direto na Grande Lisboa e Margem Sul."
        ),
        "services_see_all": "Ver todos os serviços",
        "services_see_less": "Ver menos serviços",
        "advantages_title": "Porquê escolher-nos?",
        "advantages_title_line1": "Um contacto.",
        "advantages_title_line2": "Várias soluções.",
        "advantages_text": (
            "Tratamos pequenas reparações, manutenção do dia a dia e trabalhos "
            "maiores — com o mesmo cuidado e um único ponto de contacto."
        ),
        "testimonials_title": "O que dizem os nossos clientes",
        "recent_work_title": "Veja alguns dos nossos trabalhos",
        "recent_work_subtitle": (
            "Veja alguns dos trabalhos de reparação, montagem, manutenção e "
            "remodelação realizados pela FAZDETUDO.PT."
        ),
        "recent_work_zone": "Zona",
        "recent_work_service": "Serviço",
        "recent_work_link": "Ver trabalho",
        "work_lightbox_close": "Fechar",
        "work_lightbox_dialog": "Visualização do trabalho",
        "work_lightbox_open_image": "Ver imagem em tamanho maior",
        "work_lightbox_open_video": "Ver vídeo em tamanho maior",
        "work_video_badge": "Vídeo",
        "work_lightbox_prev": "Imagem anterior",
        "work_lightbox_next": "Imagem seguinte",
        "view_google_reviews": "Ver avaliações no Google",
        "reviews_google_label": "Google",
        "google_review_source": "Crítica de Google",
        "faq_title": "Perguntas Frequentes",
        "partners_teaser_title": "Precisa de um serviço especializado?",
        "partners_teaser_text": (
            "Para alguns serviços trabalhamos com profissionais parceiros "
            "selecionados."
        ),
        "partners_teaser_cta": "Ver todos os parceiros",
        "partners_teaser_visit": "Visitar",
        "partners_teaser_contact": "Contactar",
        "partners_teaser_category_badge": "Parceiro nesta categoria",
        "contact_title": "Tem trabalhos para fazer em casa?",
        "contact_subtitle": (
            "Envie-nos fotografias e uma breve descrição do que precisa. "
            "Respondemos com orientação e orçamento."
        ),
        "contact_cta": "Pedir orçamento por WhatsApp",
        "contact_locations_aria": "Localizações",
        "address_primary_label": "Escritório principal",
        "address_secondary_label": "Segundo escritório / apoio operacional",
        "address_appointment_note": "Atendimento mediante marcação",
        "social_cta": "Siga-nos e veja os nossos trabalhos",
        "footer_rights": "FAZDETUDO.PT. Todos os direitos reservados.",
        "wa_greeting": "Como posso ajudar?",
        "wa_placeholder": "Escreva uma mensagem...",
        "wa_online": "Online",
        "learn_more": "Saber mais",
        "badge_premium": "Premium",
        "badge_specialty": "Especialidade",
        "badge_acabamentos_premium": "Acabamentos Premium",
        "badge_muito_requisitado": "Muito Requisitado",
        "badge_parceiro_recomendado": "Parceiro recomendado",
    },
    "en": {
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_works": "Our work",
        "nav_partners": "Partners",
        "nav_about": "About us",
        "nav_contact": "Contact",
        "nav_articles": "Articles",
        "footer_links": "Links",
        "footer_company": "Company",
        "header_quote": "Request a quote",
        "hero_title_prefix": "Handyman &",
        "hero_title_accent": "Home Repairs",
        "hero_title_suffix": "at Your Doorstep",
        "hero_language_label": "Service in:",
        "services_kicker": "WHAT WE DO",
        "recent_work_kicker": "RECENT WORK",
        "partners_compact_title": "SPECIALIST SERVICES",
        "cta_response_label": "Fast response",
        "hero_eyebrow": "HANDYMAN · GREATER LISBON & SOUTH BANK",
        "hero_title": "Handyman and Home Repair Services",
        "hero_title_line1": "Handyman and repairs",
        "hero_title_line2": "for your home.",
        "footer_tagline": "Handyman, repairs and home maintenance.",
        "hero_subtitle": (
            "Small repairs, assembly, maintenance and home jobs. "
            "One contact for multiple tasks."
        ),
        "hero_btn_find": "Find a professional",
        "hero_btn_help": "I need help",
        "hero_btn_quote": "Request a quote on WhatsApp",
        "hero_btn_call": "Call now",
        "hero_reviews_rating": "★★★★★ 5.0 on Google",
        "hero_reviews_suffix": "PT · EN · ES · RO",
        "trust_google": "5.0 Google",
        "trust_quote": "Free quote",
        "trust_area": "Greater Lisbon & South Bank",
        "trust_langs": "PT · EN · ES · RO",
        "services_title": "Handyman Services",
        "services_subtitle": (
            "Repairs, assembly, maintenance and small jobs with direct service "
            "across Greater Lisbon and the South Bank."
        ),
        "services_see_all": "View all services",
        "services_see_less": "Show fewer services",
        "advantages_title": "Why choose us?",
        "advantages_title_line1": "One contact.",
        "advantages_title_line2": "Multiple solutions.",
        "advantages_text": (
            "We handle small repairs, day-to-day maintenance and larger jobs — "
            "with the same care and a single point of contact."
        ),
        "testimonials_title": "What our clients say",
        "recent_work_title": "See some of our recent work",
        "recent_work_subtitle": (
            "See some of the repair, assembly, maintenance and renovation jobs "
            "carried out by FAZDETUDO.PT."
        ),
        "recent_work_zone": "Area",
        "recent_work_service": "Service",
        "recent_work_link": "View work",
        "work_lightbox_close": "Close",
        "work_lightbox_dialog": "Work preview",
        "work_lightbox_open_image": "View larger image",
        "work_lightbox_open_video": "View larger video",
        "work_video_badge": "Video",
        "work_lightbox_prev": "Previous image",
        "work_lightbox_next": "Next image",
        "view_google_reviews": "View reviews on Google",
        "reviews_google_label": "Google",
        "google_review_source": "Google review",
        "faq_title": "Frequently Asked Questions",
        "partners_teaser_title": "Need a specialist service?",
        "partners_teaser_text": (
            "For some services we work with selected partner professionals."
        ),
        "partners_teaser_cta": "View all partners",
        "partners_teaser_visit": "Visit",
        "partners_teaser_contact": "Contact",
        "partners_teaser_category_badge": "Partner in this category",
        "contact_title": "Have jobs to do at home?",
        "contact_subtitle": (
            "Send us photos and a short description of what you need. "
            "We'll reply with guidance and a quote."
        ),
        "contact_cta": "Request a quote on WhatsApp",
        "contact_locations_aria": "Locations",
        "address_primary_label": "Main office",
        "address_secondary_label": "Second office / operational support",
        "address_appointment_note": "By appointment only",
        "social_cta": "Follow us and see our work",
        "footer_rights": "FAZDETUDO.PT. All rights reserved.",
        "wa_greeting": "How can I help you?",
        "wa_placeholder": "Type a message...",
        "wa_online": "Online",
        "learn_more": "Learn more",
        "badge_premium": "Premium",
        "badge_specialty": "Specialty",
        "badge_acabamentos_premium": "Premium Finishes",
        "badge_muito_requisitado": "Highly Requested",
        "badge_parceiro_recomendado": "Recommended partner",
    },
    "es": {
        "nav_home": "Inicio",
        "nav_services": "Servicios",
        "nav_works": "Trabajos",
        "nav_partners": "Colaboradores",
        "nav_about": "Sobre nosotros",
        "nav_contact": "Contacto",
        "nav_articles": "Artículos",
        "footer_links": "Enlaces",
        "footer_company": "Empresa",
        "header_quote": "Pedir presupuesto",
        "hero_title_prefix": "Manitas y",
        "hero_title_accent": "Reparaciones",
        "hero_title_suffix": "a Domicilio",
        "hero_language_label": "Atención en:",
        "services_kicker": "QUÉ HACEMOS",
        "recent_work_kicker": "TRABAJOS REALIZADOS",
        "partners_compact_title": "SERVICIOS ESPECIALIZADOS",
        "cta_response_label": "Respuesta rápida",
        "hero_eyebrow": "MANITAS · GRAN LISBOA Y MARGEN SUR",
        "hero_title": "Manitas y Reparaciones a Domicilio",
        "hero_title_line1": "Manitas y reparaciones",
        "hero_title_line2": "para su casa.",
        "footer_tagline": "Manitas, reparaciones y mantenimiento a domicilio.",
        "hero_subtitle": (
            "Pequeñas reparaciones, montajes, mantenimiento y trabajos en casa. "
            "Un único contacto para varias tareas."
        ),
        "hero_btn_find": "Encontrar profesional",
        "hero_btn_help": "Necesito ayuda",
        "hero_btn_quote": "Pedir presupuesto por WhatsApp",
        "hero_btn_call": "Llamar ahora",
        "hero_reviews_rating": "★★★★★ 5.0 en Google",
        "hero_reviews_suffix": "PT · EN · ES · RO",
        "trust_google": "5.0 Google",
        "trust_quote": "Presupuesto gratuito",
        "trust_area": "Gran Lisboa y Margen Sur",
        "trust_langs": "PT · EN · ES · RO",
        "services_title": "Servicios de Manitas",
        "services_subtitle": (
            "Reparaciones, montajes, mantenimiento y pequeños trabajos con "
            "atención directa en la Gran Lisboa y Margen Sur."
        ),
        "services_see_all": "Ver todos los servicios",
        "services_see_less": "Ver menos servicios",
        "advantages_title": "¿Por qué elegirnos?",
        "advantages_title_line1": "Un contacto.",
        "advantages_title_line2": "Varias soluciones.",
        "advantages_text": (
            "Nos ocupamos de pequeñas reparaciones, mantenimiento diario y "
            "trabajos mayores — con el mismo cuidado y un único punto de contacto."
        ),
        "testimonials_title": "Lo que dicen nuestros clientes",
        "recent_work_title": "Vea algunos de nuestros trabajos",
        "recent_work_subtitle": (
            "Vea algunos de los trabajos de reparación, montaje, mantenimiento y "
            "reforma realizados por FAZDETUDO.PT."
        ),
        "recent_work_zone": "Zona",
        "recent_work_service": "Servicio",
        "recent_work_link": "Ver trabajo",
        "work_lightbox_close": "Cerrar",
        "work_lightbox_dialog": "Vista del trabajo",
        "work_lightbox_open_image": "Ver imagen ampliada",
        "work_lightbox_open_video": "Ver vídeo ampliado",
        "work_video_badge": "Vídeo",
        "work_lightbox_prev": "Imagen anterior",
        "work_lightbox_next": "Imagen siguiente",
        "view_google_reviews": "Ver reseñas en Google",
        "reviews_google_label": "Google",
        "google_review_source": "Reseña de Google",
        "faq_title": "Preguntas Frecuentes",
        "partners_teaser_title": "¿Necesita un servicio especializado?",
        "partners_teaser_text": (
            "Para algunos servicios trabajamos con profesionales colaboradores "
            "seleccionados."
        ),
        "partners_teaser_cta": "Ver todos los colaboradores",
        "partners_teaser_visit": "Visitar",
        "partners_teaser_contact": "Contactar",
        "partners_teaser_category_badge": "Colaborador en esta categoría",
        "contact_title": "¿Tiene trabajos que hacer en casa?",
        "contact_subtitle": (
            "Envíenos fotografías y una breve descripción de lo que necesita. "
            "Respondemos con orientación y presupuesto."
        ),
        "contact_cta": "Pedir presupuesto por WhatsApp",
        "contact_locations_aria": "Ubicaciones",
        "address_primary_label": "Oficina principal",
        "address_secondary_label": "Segunda oficina / apoyo operativo",
        "address_appointment_note": "Atención con cita previa",
        "social_cta": "Síguenos y mira nuestros trabajos",
        "footer_rights": "FAZDETUDO.PT. Todos los derechos reservados.",
        "wa_greeting": "¿Cómo puedo ayudarle?",
        "wa_placeholder": "Escriba un mensaje...",
        "wa_online": "En línea",
        "learn_more": "Saber más",
        "badge_premium": "Premium",
        "badge_specialty": "Especialidad",
        "badge_acabamentos_premium": "Acabados Premium",
        "badge_muito_requisitado": "Muy Solicitado",
        "badge_parceiro_recomendado": "Colaborador recomendado",
    },
    "fr": {
        "nav_home": "Accueil",
        "nav_services": "Services",
        "nav_works": "Réalisations",
        "nav_partners": "Partenaires",
        "nav_about": "À propos",
        "nav_contact": "Contact",
        "nav_articles": "Articles",
        "footer_links": "Liens",
        "footer_company": "Entreprise",
        "header_quote": "Demander un devis",
        "hero_title_prefix": "Bricolage et",
        "hero_title_accent": "Réparations",
        "hero_title_suffix": "à Domicile",
        "hero_language_label": "Service en :",
        "services_kicker": "NOS SERVICES",
        "recent_work_kicker": "RÉALISATIONS",
        "partners_compact_title": "SERVICES SPÉCIALISÉS",
        "cta_response_label": "Réponse rapide",
        "hero_eyebrow": "BRICOLAGE · GRAND LISBONNE ET RIVE SUD",
        "hero_title": "Bricolage et Réparations à Domicile",
        "hero_title_line1": "Bricolage et réparations",
        "hero_title_line2": "pour votre maison.",
        "footer_tagline": "Bricolage, réparations et entretien à domicile.",
        "hero_subtitle": (
            "Petites réparations, montage, entretien et travaux à domicile. "
            "Un seul contact pour plusieurs tâches."
        ),
        "hero_btn_find": "Trouver un professionnel",
        "hero_btn_help": "J'ai besoin d'aide",
        "hero_btn_quote": "Demander un devis sur WhatsApp",
        "hero_btn_call": "Appeler maintenant",
        "hero_reviews_rating": "★★★★★ 5.0 sur Google",
        "hero_reviews_suffix": "PT · EN · ES · RO",
        "trust_google": "5.0 Google",
        "trust_quote": "Devis gratuit",
        "trust_area": "Grand Lisbonne et Rive Sud",
        "trust_langs": "PT · EN · ES · RO",
        "services_title": "Services de Bricolage",
        "services_subtitle": (
            "Réparations, montage, entretien et petits travaux avec un service "
            "direct dans le Grand Lisbonne et la Rive Sud."
        ),
        "services_see_all": "Voir tous les services",
        "services_see_less": "Voir moins de services",
        "advantages_title": "Pourquoi nous choisir ?",
        "advantages_title_line1": "Un contact.",
        "advantages_title_line2": "Plusieurs solutions.",
        "advantages_text": (
            "Nous prenons en charge petites réparations, entretien quotidien et "
            "travaux plus importants — avec le même soin et un seul interlocuteur."
        ),
        "testimonials_title": "Ce que disent nos clients",
        "recent_work_title": "Travaux réalisés",
        "recent_work_subtitle": (
            "Découvrez quelques travaux de réparation, montage, entretien et "
            "rénovation réalisés par FAZDETUDO.PT."
        ),
        "recent_work_zone": "Zone",
        "recent_work_service": "Service",
        "recent_work_link": "Voir le travail",
        "work_lightbox_close": "Fermer",
        "work_lightbox_dialog": "Aperçu du travail",
        "work_lightbox_open_image": "Voir l'image en grand",
        "work_lightbox_open_video": "Voir la vidéo en grand",
        "work_video_badge": "Vidéo",
        "work_lightbox_prev": "Image précédente",
        "work_lightbox_next": "Image suivante",
        "view_google_reviews": "Voir les avis sur Google",
        "reviews_google_label": "Google",
        "google_review_source": "Avis Google",
        "faq_title": "Questions Fréquentes",
        "partners_teaser_title": "Besoin d'un service spécialisé ?",
        "partners_teaser_text": (
            "Pour certains services, nous travaillons avec des professionnels "
            "partenaires sélectionnés."
        ),
        "partners_teaser_cta": "Voir tous les partenaires",
        "partners_teaser_visit": "Visiter",
        "partners_teaser_contact": "Contacter",
        "partners_teaser_category_badge": "Partenaire dans cette catégorie",
        "contact_title": "Des travaux à faire chez vous ?",
        "contact_subtitle": (
            "Envoyez-nous des photos et une brève description de votre besoin. "
            "Nous répondons avec des conseils et un devis."
        ),
        "contact_cta": "Demander un devis sur WhatsApp",
        "contact_locations_aria": "Implantations",
        "address_primary_label": "Bureau principal",
        "address_secondary_label": "Second bureau / appui opérationnel",
        "address_appointment_note": "Sur rendez-vous uniquement",
        "social_cta": "Suivez-nous et découvrez nos réalisations",
        "footer_rights": "FAZDETUDO.PT. Tous droits réservés.",
        "wa_greeting": "Comment puis-je vous aider ?",
        "wa_placeholder": "Écrivez un message...",
        "wa_online": "En ligne",
        "learn_more": "En savoir plus",
        "badge_premium": "Premium",
        "badge_specialty": "Spécialité",
        "badge_acabamentos_premium": "Finitions Premium",
        "badge_muito_requisitado": "Très Demandé",
        "badge_parceiro_recomendado": "Partenaire recommandé",
    },
}

# Homepage shows these first; remaining SERVICE_CARDS stay available via "see all".
HOME_FEATURED_SERVICE_SLUGS = [
    "servico-reparacoes-gerais.html",
    "servico-carpintaria.html",
    "servico-pinturas.html",
    "servico-canalizacoes.html",
    "servico-electricidade.html",
    "servico-climatizacao.html",
    "servico-limpezas.html",
    "servico-manutencao.html",
]

WHY_US_POINTS = {
    "pt": [
        "Orçamento sem compromisso",
        "Grande Lisboa e Margem Sul",
        "Trabalho limpo e organizado",
        "Pequenas reparações e trabalhos maiores",
        "Contacto rápido por WhatsApp",
    ],
    "en": [
        "No-obligation quote",
        "Greater Lisbon and South Bank",
        "Clean, organised work",
        "Small repairs and larger jobs",
        "Fast contact via WhatsApp",
    ],
    "es": [
        "Presupuesto sin compromiso",
        "Gran Lisboa y Margen Sur",
        "Trabajo limpio y organizado",
        "Pequeñas reparaciones y trabajos mayores",
        "Contacto rápido por WhatsApp",
    ],
    "fr": [
        "Devis sans engagement",
        "Grand Lisbonne et Rive Sud",
        "Travail propre et soigné",
        "Petites réparations et travaux plus importants",
        "Contact rapide via WhatsApp",
    ],
}

GOOGLE_RATING = 5.0

ADVANTAGES = [
    {
        "icon": "file-invoice",
        "pt": ("Orçamento grátis", "Orçamento sem compromisso para planear o seu projeto com tranquilidade."),
        "en": ("Free quote", "No-obligation quote so you can plan your project with confidence."),
        "es": ("Presupuesto gratis", "Presupuesto sin compromiso para planificar su proyecto con tranquilidad."),
        "fr": ("Devis gratuit", "Devis sans engagement pour planifier votre projet en toute sérénité."),
    },
    {
        "icon": "location-dot",
        "pt": (
            "Atendimento na Grande Lisboa e Margem Sul",
            "Deslocamo-nos à sua casa ou empresa em Lisboa, Cascais, Almada, Setúbal e arredores.",
        ),
        "en": (
            "Coverage in Greater Lisbon and South Bank",
            "We come to your home or business in Lisbon, Cascais, Almada, Setúbal and surrounding areas.",
        ),
        "es": (
            "Servicio en la Gran Lisboa y Margen Sur",
            "Nos desplazamos a su hogar o empresa en Lisboa, Cascais, Almada, Setúbal y alrededores.",
        ),
        "fr": (
            "Intervention Grand Lisbonne et Rive Sud",
            "Nous nous déplaçons chez vous à Lisbonne, Cascais, Almada, Setúbal et environs.",
        ),
    },
    {
        "icon": "users",
        "pt": ("Equipa polivalente", "Um único contacto para reparações, manutenção e obras especializadas."),
        "en": ("Versatile team", "One point of contact for repairs, maintenance and specialist works."),
        "es": ("Equipo polivalente", "Un solo contacto para reparaciones, mantenimiento y obras especializadas."),
        "fr": ("Équipe polyvalente", "Un seul interlocuteur pour réparations, entretien et travaux spécialisés."),
    },
    {
        "icon": "broom",
        "pt": ("Trabalho limpo e organizado", "Protegemos o espaço e deixamos tudo arrumado no final."),
        "en": ("Clean, organised work", "We protect your space and leave everything tidy when we finish."),
        "es": ("Trabajo limpio y organizado", "Protegemos el espacio y lo dejamos todo recogido al terminar."),
        "fr": ("Travail propre et soigné", "Nous protégeons les lieux et laissons tout rangé à la fin."),
    },
    {
        "icon": "screwdriver-wrench",
        "pt": (
            "Soluções para pequenas reparações e obras maiores",
            "Do detalhe ao projeto completo, com a mesma dedicação.",
        ),
        "en": (
            "Small repairs and larger projects",
            "From quick fixes to full projects, with the same care throughout.",
        ),
        "es": (
            "Pequeñas reparaciones y obras mayores",
            "Del detalle al proyecto completo, con la misma dedicación.",
        ),
        "fr": (
            "Petites réparations et grands travaux",
            "Du détail au projet complet, avec le même sérieux.",
        ),
    },
    {
        "icon": "comments",
        "pt": ("Contacto rápido por WhatsApp", "Resposta ágil para marcar visitas e pedidos de orçamento."),
        "en": ("Fast contact via WhatsApp", "Quick replies to schedule visits and request quotes."),
        "es": ("Contacto rápido por WhatsApp", "Respuesta ágil para visitas y solicitudes de presupuesto."),
        "fr": ("Contact rapide par WhatsApp", "Réponse rapide pour planifier des visites et demander un devis."),
    },
]

FAQ_ITEMS = [
    {
        "pt": (
            "Fazem pequenas reparações?",
            "Sim. Pendurar prateleiras, ajustar portas, retocar pinturas e resolver a lista de arranjos do dia a dia fazem parte do nosso trabalho quotidiano.",
        ),
        "en": (
            "Do you handle small repairs?",
            "Yes. Hanging shelves, adjusting doors, touch-up painting and everyday fix-it jobs are part of our daily work.",
        ),
        "es": (
            "¿Hacen pequeñas reparaciones?",
            "Sí. Colgar estanterías, ajustar puertas, retocar pinturas y resolver arreglos del día a día forman parte de nuestro trabajo habitual.",
        ),
        "fr": (
            "Faites-vous les petites réparations ?",
            "Oui. Fixer des étagères, ajuster des portes, retouches de peinture et petits travaux du quotidien font partie de notre activité.",
        ),
    },
    {
        "pt": (
            "Posso pedir orçamento por WhatsApp?",
            "Sim. Envie fotos e uma breve descrição pelo WhatsApp e respondemos com orientação e orçamento gratuito.",
        ),
        "en": (
            "Can I request a quote via WhatsApp?",
            "Yes. Send photos and a short description on WhatsApp and we will reply with guidance and a free quote.",
        ),
        "es": (
            "¿Puedo pedir presupuesto por WhatsApp?",
            "Sí. Envíe fotos y una breve descripción por WhatsApp y le respondemos con orientación y presupuesto gratuito.",
        ),
        "fr": (
            "Puis-je demander un devis par WhatsApp ?",
            "Oui. Envoyez des photos et une courte description sur WhatsApp ; nous répondons avec des conseils et un devis gratuit.",
        ),
    },
    {
        "pt": (
            "Que zonas atendem?",
            "Grande Lisboa e Margem Sul, incluindo Lisboa, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro e Setúbal.",
        ),
        "en": (
            "Which areas do you cover?",
            "Greater Lisbon and the South Bank, including Lisbon, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro and Setúbal.",
        ),
        "es": (
            "¿Qué zonas atienden?",
            "Gran Lisboa y Margen Sur, incluyendo Lisboa, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro y Setúbal.",
        ),
        "fr": (
            "Quelles zones couvrez-vous ?",
            "Grand Lisbonne et Rive Sud, dont Lisbonne, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro et Setúbal.",
        ),
    },
    {
        "pt": (
            "Fazem urgências?",
            "Sempre que possível atendemos urgências. Contacte-nos para confirmar disponibilidade no mesmo dia ou no dia seguinte.",
        ),
        "en": (
            "Do you handle emergencies?",
            "Whenever possible we attend urgent jobs. Contact us to confirm same-day or next-day availability.",
        ),
        "es": (
            "¿Atienden urgencias?",
            "Siempre que es posible atendemos urgencias. Contáctenos para confirmar disponibilidad el mismo día o al siguiente.",
        ),
        "fr": (
            "Intervenez-vous en urgence ?",
            "Dans la mesure du possible nous traitons les urgences. Contactez-nous pour confirmer une disponibilité rapide.",
        ),
    },
    {
        "pt": (
            "Trabalham para casas e empresas?",
            "Sim. Atendemos particulares, condomínios, escritórios e comércios.",
        ),
        "en": (
            "Do you work for homes and businesses?",
            "Yes. We serve private clients, condominiums, offices and retail premises.",
        ),
        "es": (
            "¿Trabajan para hogares y empresas?",
            "Sí. Atendemos particulares, comunidades de vecinos, oficinas y comercios.",
        ),
        "fr": (
            "Travaillez-vous pour particuliers et entreprises ?",
            "Oui. Nous intervenons pour les particuliers, copropriétés, bureaux et commerces.",
        ),
    },
    {
        "pt": (
            "O orçamento é gratuito?",
            "Sim. O orçamento é gratuito e sem compromisso.",
        ),
        "en": (
            "Is the quote free?",
            "Yes. Quotes are free and without obligation.",
        ),
        "es": (
            "¿El presupuesto es gratuito?",
            "Sí. El presupuesto es gratuito y sin compromiso.",
        ),
        "fr": (
            "Le devis est-il gratuit ?",
            "Oui. Le devis est gratuit et sans engagement.",
        ),
    },
]

# Críticas reais do Google (ficha Maps). Por idioma: (primeiro_nome, texto).
# Não inventar comentários; texto vazio se a review no Google não tiver texto.
# Rating 5 estrelas aplicado no gerador (build_testimonials_cards).
TESTIMONIAL_CARDS = [
    {
        "pt": ("Mamadu", "Recomendo! Muito bom."),
        "en": ("Mamadu", "Highly recommended! Very good."),
        "es": ("Mamadu", "¡Recomiendo! Muy bueno."),
        "fr": ("Mamadu", "Je recommande ! Très bien."),
    },
    {
        "pt": ("Leandro", ""),
        "en": ("Leandro", ""),
        "es": ("Leandro", ""),
        "fr": ("Leandro", ""),
    },
    {
        "pt": ("Djadja", "Ajudou a montar os móveis, preços acessíveis."),
        "en": ("Djadja", "Helped assemble the furniture, affordable prices."),
        "es": ("Djadja", "Ayudó a montar los muebles, precios accesibles."),
        "fr": ("Djadja", "A aidé à monter les meubles, prix abordables."),
    },
    {
        "pt": ("Carla", "Recomendo! Muito bom profissional."),
        "en": ("Carla", "Highly recommended! Very good professional."),
        "es": ("Carla", "¡Recomiendo! Muy buen profesional."),
        "fr": ("Carla", "Je recommande ! Très bon professionnel."),
    },
    {
        "pt": ("Rita", "Ótimo trabalho recomendável."),
        "en": ("Rita", "Great work, highly recommendable."),
        "es": ("Rita", "Excelente trabajo, recomendable."),
        "fr": ("Rita", "Excellent travail, recommandable."),
    },
    {
        "pt": ("Valenty", "Ótima empresa! 👌🏻💯"),
        "en": ("Valenty", "Great company! 👌🏻💯"),
        "es": ("Valenty", "¡Excelente empresa! 👌🏻💯"),
        "fr": ("Valenty", "Excellente entreprise ! 👌🏻💯"),
    },
    {
        "pt": ("Sambis", "Excelente profissional e um trabalho top. RECOMENDO!"),
        "en": ("Sambis", "Excellent professional and top-quality work. I RECOMMEND!"),
        "es": ("Sambis", "Excelente profesional y un trabajo top. ¡RECOMIENDO!"),
        "fr": ("Sambis", "Excellent professionnel et un travail au top. JE RECOMMANDE !"),
    },
    {
        "pt": ("Ana", ""),
        "en": ("Ana", ""),
        "es": ("Ana", ""),
        "fr": ("Ana", ""),
    },
    {
        "pt": (
            "Isabel",
            "Excelente servicio me realizaron servicio de pintura y montado de muebles recomendado 💯",
        ),
        "en": (
            "Isabel",
            "Excellent service — they carried out painting and furniture assembly for me. Highly recommended 💯",
        ),
        "es": (
            "Isabel",
            "Excelente servicio, me realizaron servicio de pintura y montaje de muebles. Recomendado 💯",
        ),
        "fr": (
            "Isabel",
            "Excellent service — ils ont réalisé la peinture et le montage de meubles pour moi. Recommandé 💯",
        ),
    },
]

# Real project cards (images/trabalhos + videos/trabalhos). Regenerate after media changes.
RECENT_WORK = [
    {
        "gallery_id": "construcao-moradia-chave-na-mao",
        "image": "images/trabalhos/construcao-moradia-chave-na-mao-63.webp",
        "images": [
            "images/trabalhos/construcao-moradia-chave-na-mao-63.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-01.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-02.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-03.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-04.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-05.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-06.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-07.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-08.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-09.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-10.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-11.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-12.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-13.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-14.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-15.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-16.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-17.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-18.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-19.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-20.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-21.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-22.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-23.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-24.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-25.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-26.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-27.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-28.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-29.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-30.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-31.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-32.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-33.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-34.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-35.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-36.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-37.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-38.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-39.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-40.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-41.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-42.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-43.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-44.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-45.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-46.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-47.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-48.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-49.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-50.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-51.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-52.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-53.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-54.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-55.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-56.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-57.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-58.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-59.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-60.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-61.webp",
            "images/trabalhos/construcao-moradia-chave-na-mao-62.webp",
        ],
        "width": 1200,
        "height": 900,
        "slug": "servico-remodelacoes.html",
        "pt": {
            "title": "Construção de moradia chave na mão",
            "zone": "Azeitão, Margem Sul",
            "service_type": "Remodelações e Obras",
            "description": "Construção de casa do zero, desde a preparação inicial até aos acabamentos finais, com coordenação de obra e entrega chave na mão.",
            "alt": "Construção de moradia chave na mão em Azeitão, Margem Sul",
        },
        "en": {
            "title": "Turnkey house construction",
            "zone": "Azeitão, South Bank",
            "service_type": "Renovations & Construction",
            "description": "House built from the ground up, from initial preparation to final finishes, with project coordination and turnkey handover.",
            "alt": "Turnkey house construction in Azeitão, South Bank",
        },
        "es": {
            "title": "Construcción de vivienda llave en mano",
            "zone": "Azeitão, Margen Sur",
            "service_type": "Reformas y obras",
            "description": "Construcción de vivienda desde cero, desde la preparación inicial hasta los acabados finales, con coordinación de obra y entrega llave en mano.",
            "alt": "Construcción de vivienda llave en mano en Azeitão, Margen Sur",
        },
        "fr": {
            "title": "Construction de maison clé en main",
            "zone": "Azeitão, Rive Sud",
            "service_type": "Rénovations et travaux",
            "description": "Construction d'une maison depuis zéro, de la préparation initiale aux finitions, avec coordination de chantier et livraison clé en main.",
            "alt": "Construction de maison clé en main à Azeitão, Rive Sud",
        },
    },
    {
        "gallery_id": "levantamento-paredes-tijolo",
        "image": "images/trabalhos/levantamento-paredes-tijolo-02.webp",
        "images": [
            "images/trabalhos/levantamento-paredes-tijolo-02.webp",
            "images/trabalhos/levantamento-paredes-tijolo-01.webp",
            "images/trabalhos/levantamento-paredes-tijolo-03.webp",
            "images/trabalhos/levantamento-paredes-tijolo-04.webp",
            "images/trabalhos/levantamento-paredes-tijolo-05.webp",
            "images/trabalhos/levantamento-paredes-tijolo-06.webp",
            "images/trabalhos/levantamento-paredes-tijolo-07.webp",
            "images/trabalhos/levantamento-paredes-tijolo-08.webp",
            "images/trabalhos/levantamento-paredes-tijolo-09.webp",
            "images/trabalhos/levantamento-paredes-tijolo-10.webp",
            "images/trabalhos/levantamento-paredes-tijolo-11.webp",
            "images/trabalhos/levantamento-paredes-tijolo-12.webp",
        ],
        "width": 1200,
        "height": 675,
        "slug": "servico-remodelacoes.html",
        "pt": {
            "title": "Levantamento de paredes em tijolo",
            "zone": "Azeitão, Margem Sul",
            "service_type": "Remodelações e Obras",
            "description": "Execução de alvenaria com levantamento de paredes em tijolo, preparação da estrutura e organização da obra para continuação dos trabalhos de construção.",
            "alt": "Levantamento de paredes em tijolo na Grande Lisboa e Margem Sul",
        },
        "en": {
            "title": "Brick wall construction",
            "zone": "Azeitão, South Bank",
            "service_type": "Renovations & Construction",
            "description": "Brick masonry work with wall construction, structural preparation and site organisation for the next construction stages.",
            "alt": "Brick wall construction in Greater Lisbon and the South Bank",
        },
        "es": {
            "title": "Levantamiento de paredes de ladrillo",
            "zone": "Azeitão, Margen Sur",
            "service_type": "Reformas y obras",
            "description": "Trabajos de albañilería con levantamiento de paredes de ladrillo, preparación de la estructura y organización de la obra para las siguientes fases.",
            "alt": "Levantamiento de paredes de ladrillo en la Gran Lisboa y Margen Sur",
        },
        "fr": {
            "title": "Construction de murs en brique",
            "zone": "Azeitão, Rive Sud",
            "service_type": "Rénovations et travaux",
            "description": "Travaux de maçonnerie avec construction de murs en brique, préparation de la structure et organisation du chantier pour les étapes suivantes.",
            "alt": "Construction de murs en brique au Grand Lisbonne et Rive Sud",
        },
    },
    {
        "gallery_id": "impermeabilizacao-pavimento-casa-banho",
        "image": "images/trabalhos/impermeabilizacao-pavimento-casa-banho-04.webp",
        "images": [
            "images/trabalhos/impermeabilizacao-pavimento-casa-banho-04.webp",
            "images/trabalhos/impermeabilizacao-pavimento-casa-banho-01.webp",
            "images/trabalhos/impermeabilizacao-pavimento-casa-banho-02.webp",
            "images/trabalhos/impermeabilizacao-pavimento-casa-banho-03.webp",
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-reparacoes-gerais.html",
        "pt": {
            "title": "Impermeabilização de pavimento em casa de banho",
            "zone": "Grande Lisboa",
            "service_type": "Reparações gerais",
            "description": "Aplicação de membrana impermeabilizante no pavimento para prevenir infiltrações de água e proteger a base da casa de banho.",
            "alt": "Impermeabilização de pavimento em casa de banho na Grande Lisboa",
            "alts": [
                "Pavimento de casa de banho pronto após impermeabilização",
                "Base de duche e pavimento durante preparação para impermeabilização",
                "Piso de casa de banho em fase de intervenção e proteção",
                "Zona de duche finalizada com pavimento impermeabilizado",
            ],
        },
        "en": {
            "title": "Bathroom floor waterproofing",
            "zone": "Greater Lisbon",
            "service_type": "General repairs",
            "description": "Waterproof membrane applied to the floor to prevent water infiltration and protect the bathroom base.",
            "alt": "Bathroom floor waterproofing in Greater Lisbon",
            "alts": [
                "Bathroom floor ready after waterproofing work",
                "Shower base and floor during waterproofing preparation",
                "Bathroom floor under intervention and protection",
                "Finished shower area with waterproofed floor",
            ],
        },
        "es": {
            "title": "Impermeabilización del pavimento del baño",
            "zone": "Gran Lisboa",
            "service_type": "Reparaciones generales",
            "description": "Aplicación de membrana impermeabilizante en el pavimento para prevenir filtraciones y proteger la base del baño.",
            "alt": "Impermeabilización del pavimento del baño en la Gran Lisboa",
            "alts": [
                "Pavimento del baño listo tras la impermeabilización",
                "Base de ducha y suelo durante la preparación",
                "Suelo del baño en fase de intervención y protección",
                "Zona de ducha finalizada con pavimento impermeabilizado",
            ],
        },
        "fr": {
            "title": "Imperméabilisation du sol de salle de bain",
            "zone": "Grand Lisbonne",
            "service_type": "Réparations générales",
            "description": "Application d'une membrane d'étanchéité sur le sol pour prévenir les infiltrations et protéger la base de la salle de bain.",
            "alt": "Imperméabilisation du sol de salle de bain dans le Grand Lisbonne",
            "alts": [
                "Sol de salle de bain prêt après étanchéification",
                "Receveur de douche et sol en phase de préparation",
                "Sol de salle de bain en intervention et protection",
                "Zone de douche finalisée avec sol étanchéifié",
            ],
        },
    },
    {
        "image": "images/trabalhos/pintura-acabamentos-interiores-lisboa-01.webp",
        "images": [
            "images/trabalhos/pintura-acabamentos-interiores-lisboa-01.webp",
            "images/trabalhos/pintura-acabamentos-interiores-lisboa-02.webp",
            "images/trabalhos/pintura-acabamentos-interiores-lisboa-03.webp",
            "images/trabalhos/pintura-acabamentos-interiores-lisboa-04.webp",
            "images/trabalhos/pintura-acabamentos-interiores-lisboa-05.webp",
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-pinturas.html",
        "pt": {
            "title": "Pintura e acabamentos interiores",
            "zone": "Grande Lisboa",
            "service_type": "Pinturas",
            "description": "Pintura de paredes, tetos e pequenos retoques interiores com acabamento limpo e cuidado.",
            "alt": "Pintura interior profissional em espaço comercial na Grande Lisboa",
            "alts": [
                "Pintura interior em grande espaço comercial com pilares pretos e teto branco em Lisboa",
                "Obra de pintura interior com proteção de pavimento e equipamento profissional",
                "Parede de acento pintada a preto com logótipo branco e acabamento de teto",
                "Linha limpa entre parede escura e teto branco com proteção de equipamentos",
                "Pintura de paredes interiores com acabamento uniforme e coluna pintada",
            ],
        },
        "en": {
            "title": "Interior painting and finishes",
            "zone": "Greater Lisbon",
            "service_type": "Painting",
            "description": "Wall and ceiling painting plus small interior touch-ups with a clean, careful finish.",
            "alt": "Professional interior painting in a commercial space in Greater Lisbon",
            "alts": [
                "Interior painting in a large commercial space with black pillars and white ceiling in Lisbon",
                "Interior painting job with floor protection and professional equipment",
                "Black accent wall with white logo and ceiling finish",
                "Clean line between dark wall and white ceiling with protected fixtures",
                "Interior wall painting with uniform finish on a painted column",
            ],
        },
        "es": {
            "title": "Pintura y acabados interiores",
            "zone": "Gran Lisboa",
            "service_type": "Pinturas",
            "description": "Pintura de paredes, techos y pequeños retoques interiores con acabado limpio y cuidado.",
            "alt": "Pintura interior profesional en espacio comercial en la Gran Lisboa",
            "alts": [
                "Pintura interior en gran espacio comercial con pilares negros y techo blanco en Lisboa",
                "Obra de pintura interior con protección del suelo y equipo profesional",
                "Pared de acento pintada en negro con logotipo blanco y acabado de techo",
                "Línea limpia entre pared oscura y techo blanco con equipos protegidos",
                "Pintura de paredes interiores con acabado uniforme en columna",
            ],
        },
        "fr": {
            "title": "Peinture et finitions intérieures",
            "zone": "Grand Lisbonne",
            "service_type": "Peinture",
            "description": "Peinture de murs, plafonds et petites retouches intérieures avec une finition soignée.",
            "alt": "Peinture intérieure professionnelle dans un espace commercial au Grand Lisbonne",
            "alts": [
                "Peinture intérieure dans un grand espace commercial avec piliers noirs et plafond blanc à Lisbonne",
                "Travaux de peinture intérieure avec protection du sol et matériel professionnel",
                "Mur d'accent peint en noir avec logo blanc et finition de plafond",
                "Ligne nette entre mur foncé et plafond blanc avec équipements protégés",
                "Peinture de murs intérieurs avec finition uniforme sur un pilier",
            ],
        },
    },
    {
        "gallery_id": "restauro-madeira-exterior",
        "image": "images/trabalhos/restauro-madeira-exterior-lisboa-03.webp",
        "images": [
            "images/trabalhos/restauro-madeira-exterior-lisboa-03.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-01.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-02.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-04.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-05.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-06.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-07.webp",
            "images/trabalhos/restauro-madeira-exterior-lisboa-08.webp",
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-pinturas.html",
        "pt": {
            "title": "Restauro e pintura de madeira exterior",
            "zone": "Grande Lisboa e Margem Sul",
            "service_type": "Pintura e manutenção exterior",
            "description": "Tratamento, lixagem e aplicação de proteção em madeira exterior para recuperar o aspeto e aumentar a resistência ao sol e à humidade.",
            "alt": "Restauro e pintura de madeira exterior em mobiliário de jardim na Grande Lisboa",
            "alts": [
                "Detalhe de madeira exterior recuperada com acabamento uniforme",
                "Mobiliário de jardim em madeira antes do restauro e pintura exterior",
                "Estrutura de madeira exterior com tratamento e pintura de proteção aplicados",
                "Restauro de madeira exterior em zona de jardim na Grande Lisboa",
                "Mobiliário exterior em madeira com proteção contra sol e humidade",
                "Pérgola ou estrutura de jardim com madeira tratada e pintada",
                "Acabamento final em madeira exterior com aspeto renovado",
                "Detalhe de madeira exterior com proteção aplicada e acabamento uniforme",
            ],
        },
        "en": {
            "title": "Exterior wood restoration and painting",
            "zone": "Greater Lisbon and South Bank",
            "service_type": "Exterior painting and maintenance",
            "description": "Treatment, sanding and protective coating on exterior wood to restore appearance and improve resistance to sun and moisture.",
            "alt": "Exterior wood restoration and painting on garden furniture in Greater Lisbon",
            "alts": [
                "Detail of restored exterior wood with an even finish",
                "Garden wood furniture before exterior restoration and painting",
                "Exterior wood structure with protective treatment and paint applied",
                "Exterior wood restoration in a garden area in Greater Lisbon",
                "Exterior wood furniture protected against sun and moisture",
                "Pergola or garden structure with treated and painted wood",
                "Final finish on exterior wood with a refreshed look",
                "Detail of exterior wood with protective coating and even finish",
            ],
        },
        "es": {
            "title": "Restauración y pintura de madera exterior",
            "zone": "Gran Lisboa y Margen Sur",
            "service_type": "Pintura y mantenimiento exterior",
            "description": "Tratamiento, lijado y aplicación de protección en madera exterior para recuperar el aspecto y aumentar la resistencia al sol y la humedad.",
            "alt": "Restauración y pintura de madera exterior en mobiliario de jardín en la Gran Lisboa",
            "alts": [
                "Detalle de madera exterior recuperada con acabado uniforme",
                "Mobiliario de jardín en madera antes de la restauración y pintura exterior",
                "Estructura de madera exterior con tratamiento y pintura de protección",
                "Restauración de madera exterior en zona ajardinada en la Gran Lisboa",
                "Mobiliario exterior en madera protegido contra sol y humedad",
                "Pérgola o estructura de jardín con madera tratada y pintada",
                "Acabado final en madera exterior con aspecto renovado",
                "Detalle de madera exterior con protección aplicada y acabado uniforme",
            ],
        },
        "fr": {
            "title": "Restauration et peinture de bois extérieur",
            "zone": "Grand Lisbonne et Rive Sud",
            "service_type": "Peinture et entretien extérieur",
            "description": "Traitement, ponçage et application de protection sur bois extérieur pour retrouver l'aspect et renforcer la résistance au soleil et à l'humidité.",
            "alt": "Restauration et peinture de bois extérieur sur mobilier de jardin au Grand Lisbonne",
            "alts": [
                "Détail de bois extérieur restauré avec finition uniforme",
                "Mobilier de jardin en bois avant restauration et peinture extérieure",
                "Structure en bois extérieur avec traitement et peinture de protection",
                "Restauration de bois extérieur dans un jardin au Grand Lisbonne",
                "Mobilier extérieur en bois protégé contre le soleil et l'humidité",
                "Pergola ou structure de jardin avec bois traité et peint",
                "Finition finale sur bois extérieur avec aspect rafraîchi",
                "Détail de bois extérieur avec protection appliquée et finition uniforme",
            ],
        },
    },
    {
        "gallery_id": "montagem-moveis-sala",
        "image": "images/trabalhos/montagem-moveis-sala-lisboa-11.webp",
        "images": [
            "images/trabalhos/montagem-moveis-sala-lisboa-11.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-10.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-02.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-03.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-04.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-06.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-07.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-08.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-09.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-01.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-12.webp",
            "images/trabalhos/montagem-moveis-sala-lisboa-13.webp",
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-reparacoes-gerais.html",
        "pt": {
            "title": "Montagem de móveis de sala",
            "zone": "Grande Lisboa",
            "service_type": "Montagem de móveis",
            "description": "Montagem de mesa, aparador e móveis de sala, com afinação de portas, ferragens e acabamento limpo no espaço interior.",
            "alt": "Montagem de móveis de sala e jantar na Grande Lisboa",
            "alts": [
                "Aparador de sala montado com portas e prateleiras alinhadas",
                "Montagem de móveis de sala com mesa e cadeiras em apartamento",
                "Aparador ou armário de sala em processo de montagem",
                "Detalhe de ferragens e portas de móvel ajustadas na sala",
                "Mesa de jantar montada com acabamento alinhado no espaço",
                "Interior de sala com móveis novos montados e protegidos",
                "Ajuste de portas e gavetas em aparador de sala",
                "Mobiliário de sala com montagem profissional concluída",
                "Vista geral da sala com mesa e móveis montados",
                "Mesa de sala montada com estrutura estável e nivelada",
                "Detalhe de montagem de móvel com ferragens corretamente fixadas",
                "Sala com mobiliário montado e espaço interior organizado",
            ],
        },
        "en": {
            "title": "Living room furniture assembly",
            "zone": "Greater Lisbon",
            "service_type": "Furniture assembly",
            "description": "Assembly of dining table, sideboard and living room furniture, with door alignment, hardware adjustment and a tidy finish.",
            "alt": "Living and dining room furniture assembly in Greater Lisbon",
            "alts": [
                "Sideboard assembled with aligned doors and shelves",
                "Living room furniture assembly with table and chairs in an apartment",
                "Sideboard or living room cabinet during assembly",
                "Detail of adjusted hinges and doors on living room furniture",
                "Dining table assembled with aligned finish in the space",
                "Living room interior with newly assembled and protected furniture",
                "Door and drawer adjustment on a living room sideboard",
                "Living room furniture with professional assembly completed",
                "Wide view of the living room with table and furniture assembled",
                "Living room table assembled with stable, level structure",
                "Detail of furniture assembly with hardware correctly fitted",
                "Living room with assembled furniture and organised interior",
            ],
        },
        "es": {
            "title": "Montaje de muebles de salón",
            "zone": "Gran Lisboa",
            "service_type": "Montaje de muebles",
            "description": "Montaje de mesa, aparador y muebles de salón, con ajuste de puertas, herrajes y acabado limpio en el interior.",
            "alt": "Montaje de muebles de salón y comedor en la Gran Lisboa",
            "alts": [
                "Aparador de salón montado con puertas y estantes alineados",
                "Montaje de muebles de salón con mesa y sillas en apartamento",
                "Aparador o armario de salón en proceso de montaje",
                "Detalle de herrajes y puertas de mueble ajustadas en el salón",
                "Mesa de comedor montada con acabado alineado en el espacio",
                "Interior de salón con muebles nuevos montados y protegidos",
                "Ajuste de puertas y cajones en aparador de salón",
                "Mobiliario de salón con montaje profesional terminado",
                "Vista general del salón con mesa y muebles montados",
                "Mesa de salón montada con estructura estable y nivelada",
                "Detalle de montaje de mueble con herrajes correctamente fijados",
                "Salón con mobiliario montado y espacio interior organizado",
            ],
        },
        "fr": {
            "title": "Montage de meubles de salon",
            "zone": "Grand Lisbonne",
            "service_type": "Montage de meubles",
            "description": "Montage de table, buffet et meubles de salon, avec réglage des portes, quincaillerie et finition soignée dans l'espace intérieur.",
            "alt": "Montage de meubles de salon et salle à manger au Grand Lisbonne",
            "alts": [
                "Buffet de salon monté avec portes et étagères alignées",
                "Montage de meubles de salon avec table et chaises en appartement",
                "Buffet ou meuble de salon en cours de montage",
                "Détail de charnières et portes de meuble réglées dans le salon",
                "Table à manger montée avec finition alignée dans l'espace",
                "Intérieur de salon avec meubles neufs montés et protégés",
                "Réglage de portes et tiroirs sur un buffet de salon",
                "Mobilier de salon avec montage professionnel terminé",
                "Vue d'ensemble du salon avec table et meubles montés",
                "Table de salon montée avec structure stable et de niveau",
                "Détail de montage de meuble avec quincaillerie correctement fixée",
                "Salon avec mobilier monté et espace intérieur organisé",
            ],
        },
    },
    {
        "image": "images/trabalhos/relva-sistema-rega-lisboa-01.webp",
        "media": [
            {
                "type": "image",
                "src": "images/trabalhos/relva-sistema-rega-lisboa-01.webp",
            },
            {
                "type": "image",
                "src": "images/trabalhos/relva-sistema-rega-lisboa-02.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-preparacao-terreno.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-preparacao-terreno-poster.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-preparacao-terreno-02.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-preparacao-terreno-02-poster.webp",
            },
            {
                "type": "image",
                "src": "images/trabalhos/relva-sistema-rega-lisboa-04.webp",
            },
            {
                "type": "image",
                "src": "images/trabalhos/relva-sistema-rega-lisboa-05.webp",
            },
            {
                "type": "image",
                "src": "images/trabalhos/relva-sistema-rega-lisboa-06.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-01.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-01-poster.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-02.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-02-poster.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-03.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-03-poster.webp",
            },
            {
                "type": "video",
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-04.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-04-poster.webp",
            },
        ],
        "images": [
            "images/trabalhos/relva-sistema-rega-lisboa-01.webp",
            "images/trabalhos/relva-sistema-rega-lisboa-02.webp",
            "images/trabalhos/relva-sistema-rega-lisboa-03.webp",
            "images/trabalhos/relva-sistema-rega-lisboa-04.webp",
            "images/trabalhos/relva-sistema-rega-lisboa-05.webp",
            "images/trabalhos/relva-sistema-rega-lisboa-06.webp",
        ],
        "gallery_videos": [
            {
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-01.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-01-poster.webp",
            },
            {
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-02.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-02-poster.webp",
            },
            {
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-03.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-03-poster.webp",
            },
            {
                "video": "videos/trabalhos/relva-sistema-rega-lisboa-04.mp4",
                "poster": "images/trabalhos/relva-sistema-rega-lisboa-video-04-poster.webp",
            },
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-jardinagem.html",
        "pt": {
            "title": "Substituição de relva e sistema de rega",
            "zone": "Azeitão, Margem Sul",
            "service_type": "Jardinagem e manutenção exterior",
            "description": "Remoção de relva antiga, preparação do terreno, instalação de sistema de rega e colocação de relva nova.",
            "alt": "Relva nova e jardim renovado com sistema de rega na Grande Lisboa",
            "alts": [
                "Relva nova instalada em jardim de moradia na Grande Lisboa",
                "Colocação de relva nova com acabamento profissional no jardim",
                "Preparação do terreno e remoção de relva antiga no jardim",
                "Preparação do terreno e remoção de relva antiga no jardim",
                "Relvado renovado em quintal com árvores e zona exterior cuidada",
                "Relva nova com juntas visíveis após instalação profissional",
                "Relvado amplo e verde após substituição de relva no jardim",
            ],
        },
        "en": {
            "title": "Lawn replacement and irrigation system",
            "zone": "Azeitão, South Bank",
            "service_type": "Gardening and outdoor maintenance",
            "description": "Removal of old turf, ground preparation, irrigation system installation and new lawn laying.",
            "alt": "New lawn and renovated garden with irrigation in Greater Lisbon",
            "alts": [
                "New turf installed in a residential garden in Greater Lisbon",
                "Professional new lawn laying in the garden",
                "Ground preparation and removal of old turf",
                "Ground preparation and removal of old turf",
                "Renewed lawn in a backyard with trees and tidy outdoor space",
                "Fresh sod with visible seams after professional installation",
                "Large green lawn after turf replacement in the garden",
            ],
        },
        "es": {
            "title": "Sustitución de césped y sistema de riego",
            "zone": "Azeitão, Margen Sur",
            "service_type": "Jardinería y mantenimiento exterior",
            "description": "Retirada de césped antiguo, preparación del terreno, instalación de riego y colocación de césped nuevo.",
            "alt": "Césped nuevo y jardín renovado con riego en la Gran Lisboa",
            "alts": [
                "Césped nuevo instalado en jardín residencial en la Gran Lisboa",
                "Colocación de césped nuevo con acabado profesional",
                "Preparación del terreno y retirada de césped antiguo",
                "Preparación del terreno y retirada de césped antiguo",
                "Césped renovado en patio con árboles y zona exterior cuidada",
                "Césped nuevo tras instalación profesional",
                "Amplio césped verde tras sustitución en el jardín",
            ],
        },
        "fr": {
            "title": "Remplacement de gazon et système d'arrosage",
            "zone": "Azeitão, Rive Sud",
            "service_type": "Jardinage et entretien extérieur",
            "description": "Retrait de l'ancienne pelouse, préparation du sol, installation d'arrosage et pose de gazon neuf.",
            "alt": "Nouvelle pelouse et jardin rénové avec arrosage au Grand Lisbonne",
            "alts": [
                "Nouvelle pelouse installée dans un jardin résidentiel au Grand Lisbonne",
                "Pose de gazon neuf avec finition professionnelle",
                "Préparation du sol et retrait de l'ancienne pelouse",
                "Préparation du sol et retrait de l'ancienne pelouse",
                "Pelouse rénovée dans un jardin avec arbres",
                "Gazon neuf après installation professionnelle",
                "Grande pelouse verte après remplacement dans le jardin",
            ],
        },
    },
    {
        "image": "images/trabalhos/instalacao-tv-parede-lisboa-01.webp",
        "images": [
            "images/trabalhos/instalacao-tv-parede-lisboa-01.webp",
            "images/trabalhos/instalacao-tv-parede-lisboa-02.webp",
            "images/trabalhos/instalacao-tv-parede-lisboa-03.webp",
            "images/trabalhos/instalacao-tv-parede-lisboa-04.webp",
            "images/trabalhos/instalacao-tv-parede-lisboa-05.webp",
            "images/trabalhos/instalacao-tv-parede-lisboa-06.webp",
        ],
        "width": 1200,
        "height": 1600,
        "slug": "servico-reparacoes-gerais.html",
        "pt": {
            "title": "Instalação de TV na parede",
            "zone": "Grande Lisboa",
            "service_type": "Reparações gerais",
            "description": "Montagem de televisão na parede, passagem/organização de cabos e acabamento limpo no espaço interior.",
            "alt": "Televisão montada na parede com cabos organizados na Grande Lisboa",
            "alts": [
                "Televisão montada na parede na sala com móvel e cabos organizados",
                "TV na parede em escritório com passagem de cabos e secretária",
                "Montagem de televisão na parede com consola e soundbar",
                "Instalação de TV na parede com cabos e computador no escritório",
                "Televisão fixada na parede com ligação elétrica na parede",
                "TV montada na parede num apartamento com zona de estar",
            ],
        },
        "en": {
            "title": "Wall-mounted TV installation",
            "zone": "Greater Lisbon",
            "service_type": "General repairs",
            "description": "TV wall mounting, cable routing and tidy finishing in your living space.",
            "alt": "Wall-mounted TV with organised cables in Greater Lisbon",
            "alts": [
                "TV mounted on the wall in a living room with media unit and cables",
                "Wall-mounted TV in a home office with desk and cable routing",
                "TV wall mount above a wooden media console with soundbar",
                "TV installation with cables at a desk workspace",
                "TV on the wall with power connection routed to the outlet",
                "Wall-mounted TV in an open-plan apartment living area",
            ],
        },
        "es": {
            "title": "Instalación de TV en la pared",
            "zone": "Gran Lisboa",
            "service_type": "Reparaciones generales",
            "description": "Montaje de televisión en la pared, paso y organización de cables y acabado limpio en el interior.",
            "alt": "Televisión montada en la pared con cables organizados en la Gran Lisboa",
            "alts": [
                "TV montada en la pared en salón con mueble y cables",
                "TV en la pared en oficina con cables y escritorio",
                "Montaje de TV sobre mueble con barra de sonido",
                "Instalación de TV con cables en zona de trabajo",
                "TV fijada en la pared con conexión eléctrica",
                "TV montada en apartamento con zona de estar",
            ],
        },
        "fr": {
            "title": "Installation de TV murale",
            "zone": "Grand Lisbonne",
            "service_type": "Réparations générales",
            "description": "Fixation de téléviseur au mur, passage et rangement des câbles et finition soignée.",
            "alt": "Téléviseur fixé au mur avec câbles organisés au Grand Lisbonne",
            "alts": [
                "TV murale dans un salon avec meuble et câbles",
                "TV murale dans un bureau avec passage de câbles",
                "Montage TV au-dessus d'un meuble avec barre de son",
                "Installation TV avec câbles au bureau",
                "TV au mur avec raccordement électrique",
                "TV murale dans un appartement avec coin salon",
            ],
        },
    },
    {
        "image": "images/trabalhos/manutencao-interior-lisboa-01.webp",
        "video": "videos/trabalhos/manutencao-interior-lisboa-01.mp4",
        "width": 1200,
        "height": 1600,
        "slug": "servico-manutencao.html",
        "pt": {
            "title": "Manutenção e remodelação interior",
            "zone": "Grande Lisboa",
            "service_type": "Manutenção",
            "description": "Trabalhos de manutenção, reparação e melhoria de espaços interiores.",
            "alt": "Casa de banho remodelada com azulejos cinzentos na Grande Lisboa",
        },
        "en": {
            "title": "Interior maintenance and renovation",
            "zone": "Greater Lisbon",
            "service_type": "Maintenance",
            "description": "Maintenance, repair and improvement of interior spaces.",
            "alt": "Renovated bathroom with grey tiles in Greater Lisbon",
        },
        "es": {
            "title": "Mantenimiento y reforma interior",
            "zone": "Gran Lisboa",
            "service_type": "Mantenimiento",
            "description": "Trabajos de mantenimiento, reparación y mejora de espacios interiores.",
            "alt": "Baño reformado con azulejos grises en la Gran Lisboa",
        },
        "fr": {
            "title": "Entretien et rénovation intérieure",
            "zone": "Grand Lisbonne",
            "service_type": "Entretien",
            "description": "Travaux d'entretien, réparation et amélioration des espaces intérieurs.",
            "alt": "Salle de bain rénovée avec carrelage gris dans le Grand Lisbonne",
        },
    },
]

# SYNC: order = index.html services grid = script.js SERVICE_LANDING_SLUGS
SERVICE_CARDS = [
    {
        "slug": "servico-remodelacoes.html",
        "icon": "house-chimney",
        "featured": True,
        "badge": "specialty",
        "pt": ("Remodelações e Obras", "Remodelação de cozinhas e casas de banho, construção de novas divisões, ampliações e obras estruturais. Do projeto à entrega da chave."),
        "en": ("Renovations & Construction", "Kitchen and bathroom renovations, new rooms, extensions and structural works. From design to handover."),
        "es": ("Reformas y Obras", "Reforma de cocinas y baños, nuevas estancias, ampliaciones y obras estructurales. Del proyecto a la entrega."),
        "fr": ("Rénovations et Travaux", "Rénovation cuisines et salles de bains, nouvelles pièces, extensions et gros œuvre. Du projet à la livraison."),
    },
    {
        "slug": "servico-climatizacao.html",
        "icon": "wind",
        "featured": False,
        "badge": None,
        "pt": ("Climatização (AVAC)", "Instalação, manutenção, limpeza e reparação de ar condicionado para casas, apartamentos, lojas e empresas."),
        "en": ("Air Conditioning (HVAC)", "AC installation (splits), gas recharge, filter cleaning and preventive HVAC maintenance."),
        "es": ("Climatización (AVAC)", "Instalación de aire acondicionado, carga de gas, filtros y mantenimiento AVAC."),
        "fr": ("Climatisation (CVC)", "Installation climatisation, recharge gaz, filtres et entretien CVC."),
    },
    {
        "slug": "servico-pinturas.html",
        "icon": "paint-roller",
        "featured": True,
        "badge": "acabamentos_premium",
        "pt": ("Pinturas Gerais", "Pintura interior e exterior com proteção de mobiliário, tratamento de humidades e acabamentos premium."),
        "en": ("General Painting", "Interior and exterior painting with furniture protection, damp treatment and premium finishes."),
        "es": ("Pinturas Generales", "Pintura interior y exterior con protección del mobiliario, humedades y acabados premium."),
        "fr": ("Peinture Générale", "Peinture intérieure et extérieure avec protection du mobilier et finitions premium."),
    },
    {
        "slug": "servico-limpezas.html",
        "icon": "broom",
        "featured": False,
        "badge": None,
        "pt": ("Limpezas", "Limpezas domésticas, pós-obra, escritórios e condomínios."),
        "en": ("Cleaning", "Home, post-construction, office and condominium cleaning."),
        "es": ("Limpieza", "Limpiezas domésticas, post-obra, oficinas y comunidades."),
        "fr": ("Nettoyage", "Nettoyage domestique, après-travaux, bureaux et copropriétés."),
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
        "featured": True,
        "badge": "muito_requisitado",
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
        "slug": "servico-pintura-fachadas-alpinismo.html",
        "icon": "building",
        "featured": False,
        "badge": None,
        "pt": ("Pintura em Alpinismo", "Reabilitação de fachadas em altura com trabalho em cordas. Sem andaimes, mais rápido e económico."),
        "en": ("Rope-Access Facade Painting", "High-rise facade refurbishment with industrial rope access. No scaffolding, faster and more economical."),
        "es": ("Pintura en Alpinismo", "Rehabilitación de fachadas en altura con cuerdas. Sin andamios, más rápido y económico."),
        "fr": ("Peinture en Cordes", "Réhabilitation de façades en hauteur par cordes. Sans échafaudage, plus rapide et économique."),
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
        "slug": "servico-recuperar-casa.html",
        "icon": "house-circle-check",
        "featured": False,
        "badge": None,
        "pt": ("Recuperar Casa", "Recuperação completa de casas devolutas, herdadas ou degradadas. Da estrutura aos acabamentos, devolvemos vida e habitabilidade ao seu imóvel."),
        "en": ("Home Restoration", "Complete restoration of vacant, inherited or run-down homes. From structure to finishes, we bring your property back to life."),
        "es": ("Recuperar Casa", "Recuperación completa de casas vacías, heredadas o deterioradas. De la estructura a los acabados, devolvemos habitabilidad."),
        "fr": ("Rénover une Maison", "Récupération complète de maisons vacantes, héritées ou dégradées. De la structure aux finitions."),
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
        "pt": ("Piscinas", "Construção, manutenção, reparação, limpeza e tratamento de piscinas."),
        "en": ("Pools", "Pool construction, maintenance, repair, cleaning and water treatment."),
        "es": ("Piscinas", "Construcción, mantenimiento, reparación, limpieza y tratamiento de piscinas."),
        "fr": ("Piscines", "Construction, entretien, réparation, nettoyage et traitement de l'eau."),
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


PARTNER_RECRUIT = {
    "pt": {
        "badge": "NOVO · Procuramos parceiros",
        "title": "É profissional? Receba novos clientes através da FAZDETUDO.PT",
        "text": (
            "Tenha o seu perfil na categoria do seu serviço e permita que potenciais "
            "clientes entrem em contacto diretamente consigo."
        ),
        "benefits": [
            (
                "star",
                "Visibilidade na sua categoria",
                "O seu negócio aparece quando clientes procuram o seu serviço.",
            ),
            (
                "comments",
                "Contacto direto",
                "Telefone, WhatsApp ou website diretamente no seu perfil.",
            ),
            (
                "calendar-check",
                "Planos mensais",
                "Escolha entre presença normal ou maior destaque no site.",
            ),
        ],
        "cta": "Quero ser parceiro",
        "note": "Vagas limitadas por categoria e zona.",
        "wa_message": (
            "Olá! Sou profissional e gostaria de saber como posso aparecer na "
            "FAZDETUDO.PT e quais são os planos para parceiros."
        ),
        "cta_aria": "Contactar FAZDETUDO.PT no WhatsApp para ser parceiro",
    },
    "en": {
        "badge": "NEW · Looking for partners",
        "title": "Are you a professional? Get new clients through FAZDETUDO.PT",
        "text": (
            "Get your profile in your service category and let potential clients "
            "contact you directly."
        ),
        "benefits": [
            (
                "star",
                "Visibility in your category",
                "Your business appears when clients search for your service.",
            ),
            (
                "comments",
                "Direct contact",
                "Phone, WhatsApp or website right on your profile.",
            ),
            (
                "calendar-check",
                "Monthly plans",
                "Choose standard presence or greater visibility on the site.",
            ),
        ],
        "cta": "I want to become a partner",
        "note": "Limited spots per category and area.",
        "wa_message": (
            "Hello! I'm a professional and I'd like to know how I can appear on "
            "FAZDETUDO.PT and what the partner plans are."
        ),
        "cta_aria": "Contact FAZDETUDO.PT on WhatsApp to become a partner",
    },
    "es": {
        "badge": "NUEVO · Buscamos colaboradores",
        "title": "¿Es profesional? Reciba nuevos clientes a través de FAZDETUDO.PT",
        "text": (
            "Tenga su perfil en la categoría de su servicio y permita que potenciales "
            "clientes contacten directamente con usted."
        ),
        "benefits": [
            (
                "star",
                "Visibilidad en su categoría",
                "Su negocio aparece cuando los clientes buscan su servicio.",
            ),
            (
                "comments",
                "Contacto directo",
                "Teléfono, WhatsApp o web directamente en su perfil.",
            ),
            (
                "calendar-check",
                "Planes mensuales",
                "Elija entre presencia normal o mayor destaque en el sitio.",
            ),
        ],
        "cta": "Quiero ser colaborador",
        "note": "Plazas limitadas por categoría y zona.",
        "wa_message": (
            "¡Hola! Soy profesional y me gustaría saber cómo puedo aparecer en "
            "FAZDETUDO.PT y cuáles son los planes para colaboradores."
        ),
        "cta_aria": "Contactar FAZDETUDO.PT por WhatsApp para ser colaborador",
    },
    "fr": {
        "badge": "NOUVEAU · Nous cherchons des partenaires",
        "title": "Vous êtes professionnel ? Recevez de nouveaux clients via FAZDETUDO.PT",
        "text": (
            "Ayez votre profil dans la catégorie de votre service et permettez aux "
            "clients potentiels de vous contacter directement."
        ),
        "benefits": [
            (
                "star",
                "Visibilité dans votre catégorie",
                "Votre activité apparaît quand les clients cherchent votre service.",
            ),
            (
                "comments",
                "Contact direct",
                "Téléphone, WhatsApp ou site web directement sur votre profil.",
            ),
            (
                "calendar-check",
                "Formules mensuelles",
                "Choisissez une présence standard ou une meilleure mise en avant.",
            ),
        ],
        "cta": "Je veux devenir partenaire",
        "note": "Places limitées par catégorie et zone.",
        "wa_message": (
            "Bonjour ! Je suis professionnel et j'aimerais savoir comment apparaître "
            "sur FAZDETUDO.PT et quels sont les plans pour les partenaires."
        ),
        "cta_aria": "Contacter FAZDETUDO.PT sur WhatsApp pour devenir partenaire",
    },
}
