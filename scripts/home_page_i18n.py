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

def lang_switch_href(current: str, target: str) -> str:
    """Relative href from current language folder to target homepage."""
    if current == target:
        return "./" if current != "pt" else "/"
    if target == "pt":
        return "../" if current != "pt" else "/"
    if current == "pt":
        return f"/{target}/"
    return f"../{target}/"


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
                        <button type="button" class="lang-toggle" id="lang-toggle" aria-expanded="false">
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
        "wa_close": "Fechar chat",
        "wa_send": "Enviar mensagem",
        "wa_float": "Contactar via WhatsApp",
        "float_call": "Ligar agora",
        "address": "Grande Lisboa e Margem Sul, Portugal",
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
        "wa_close": "Close chat",
        "wa_send": "Send message",
        "wa_float": "Contact via WhatsApp",
        "float_call": "Call now",
        "address": "Greater Lisbon and South Bank, Portugal",
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
        "wa_close": "Cerrar chat",
        "wa_send": "Enviar mensaje",
        "wa_float": "Contactar por WhatsApp",
        "float_call": "Llamar ahora",
        "address": "Gran Lisboa y Margen Sur, Portugal",
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
        "nav_about": "Sobre nós",
        "nav_contact": "Contacto",
        "footer_links": "Links",
        "hero_title": "O Seu Faz-Tudo de Confiança na Grande Lisboa e Margem Sul",
        "footer_tagline": "O Seu Faz-Tudo de Confiança na Grande Lisboa e Margem Sul",
        "hero_subtitle": "Precisa de reparar uma torneira, pendurar uma TV, pintar uma divisão ou resolver pequenos arranjos em casa? A Faz de Tudo PT trata da sua lista de tarefas com rapidez, limpeza e orçamento gratuito na Grande Lisboa e Margem Sul.",
        "hero_btn_quote": "Pedir orçamento por WhatsApp",
        "hero_btn_call": "Ligue agora",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Avaliado com 5.0 no Google",
        "services_title": "Os Nossos Serviços Profissionais",
        "services_subtitle": "Soluções fiáveis e especializadas para a manutenção, reparação e remodelação da sua casa ou empresa na Grande Lisboa e Margem Sul.",
        "advantages_title": "Porquê escolher-nos?",
        "testimonials_title": "Críticas",
        "recent_work_title": "Trabalhos recentes",
        "recent_work_subtitle": "Galeria de intervenções reais em preparação.",
        "recent_work_status": "EM ATUALIZAÇÃO",
        "recent_work_notice": "Estamos a preparar esta galeria com trabalhos reais. Em breve publicaremos antes/depois de intervenções concluídas.",
        "recent_work_cta": "Enviar fotos pelo WhatsApp",
        "view_google_reviews": "Ver críticas no Google",
        "reviews_google_label": "Avaliações no Google",
        "google_review_source": "Crítica de Google",
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
        "badge_acabamentos_premium": "Acabamentos Premium",
        "badge_muito_requisitado": "Muito Requisitado",
    },
    "en": {
        "nav_home": "Home",
        "nav_services": "Services",
        "nav_about": "About us",
        "nav_contact": "Contact",
        "footer_links": "Links",
        "hero_title": "Your Trusted Handyman in Greater Lisbon and South Bank",
        "footer_tagline": "Your Trusted Handyman in Greater Lisbon and South Bank",
        "hero_subtitle": "Need to fix a tap, mount a TV, paint a room or take care of small repairs at home? Faz de Tudo PT handles your task list quickly, cleanly and with a free quote across Greater Lisbon and the South Bank.",
        "hero_btn_quote": "Request quote on WhatsApp",
        "hero_btn_call": "Call now",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Rated 5.0 on Google",
        "services_title": "Our Professional Services",
        "services_subtitle": "Reliable, specialist solutions for maintenance, repairs and renovations at your home or business in Greater Lisbon and South Bank.",
        "advantages_title": "Why choose us?",
        "testimonials_title": "Reviews",
        "recent_work_title": "Recent work",
        "recent_work_subtitle": "Gallery of real projects in preparation.",
        "recent_work_status": "UPDATING SOON",
        "recent_work_notice": "We are preparing this gallery with real projects. Before/after photos of completed jobs will be published soon.",
        "recent_work_cta": "Send photos via WhatsApp",
        "view_google_reviews": "View reviews on Google",
        "reviews_google_label": "Reviews on Google",
        "google_review_source": "Google review",
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
        "badge_acabamentos_premium": "Premium Finishes",
        "badge_muito_requisitado": "Highly Requested",
    },
    "es": {
        "nav_home": "Inicio",
        "nav_services": "Servicios",
        "nav_about": "Sobre nosotros",
        "nav_contact": "Contacto",
        "footer_links": "Enlaces",
        "hero_title": "Su Manitas de Confianza en la Gran Lisboa y Margen Sur",
        "footer_tagline": "Su Manitas de Confianza en la Gran Lisboa y Margen Sur",
        "hero_subtitle": "¿Necesita reparar un grifo, colgar una TV, pintar una habitación o resolver pequeños arreglos en casa? Faz de Tudo PT se encarga de su lista de tareas con rapidez, limpieza y presupuesto gratuito en la Gran Lisboa y Margen Sur.",
        "hero_btn_quote": "Pedir presupuesto por WhatsApp",
        "hero_btn_call": "Llame ahora",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Valorado con 5.0 en Google",
        "services_title": "Nuestros Servicios Profesionales",
        "services_subtitle": "Soluciones fiables y especializadas para el mantenimiento, reparación y reforma de su hogar o empresa en la Gran Lisboa y Margen Sur.",
        "advantages_title": "¿Por qué elegirnos?",
        "testimonials_title": "Reseñas",
        "recent_work_title": "Trabajos recientes",
        "recent_work_subtitle": "Galería de trabajos reales en preparación.",
        "recent_work_status": "EN ACTUALIZACIÓN",
        "recent_work_notice": "Estamos preparando esta galería con trabajos reales. Pronto publicaremos antes/después de intervenciones concluidas.",
        "recent_work_cta": "Enviar fotos por WhatsApp",
        "view_google_reviews": "Ver reseñas en Google",
        "reviews_google_label": "Reseñas en Google",
        "google_review_source": "Reseña de Google",
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
        "badge_acabamentos_premium": "Acabados Premium",
        "badge_muito_requisitado": "Muy Solicitado",
    },
    "fr": {
        "nav_home": "Accueil",
        "nav_services": "Services",
        "nav_about": "À propos",
        "nav_contact": "Contact",
        "footer_links": "Liens",
        "hero_title": "Votre Bricoleur de Confiance dans le Grand Lisbonne et la Rive Sud",
        "footer_tagline": "Votre Bricoleur de Confiance dans le Grand Lisbonne et la Rive Sud",
        "hero_subtitle": "Besoin de réparer un robinet, fixer une TV, peindre une pièce ou régler de petits travaux à la maison ? Faz de Tudo PT s'occupe de votre liste de tâches rapidement, proprement et avec un devis gratuit dans le Grand Lisbonne et la Rive Sud.",
        "hero_btn_quote": "Demander un devis sur WhatsApp",
        "hero_btn_call": "Appelez maintenant",
        "hero_reviews": "⭐ ⭐ ⭐ ⭐ ⭐ Noté 5.0 sur Google",
        "services_title": "Nos Services Professionnels",
        "services_subtitle": "Solutions fiables et spécialisées pour l'entretien, la réparation et la rénovation de votre maison ou entreprise dans le Grand Lisbonne et la Rive Sud.",
        "advantages_title": "Pourquoi nous choisir ?",
        "testimonials_title": "Avis",
        "recent_work_title": "Travaux récents",
        "recent_work_subtitle": "Galerie d'interventions réelles en préparation.",
        "recent_work_status": "EN COURS DE MISE À JOUR",
        "recent_work_notice": "Nous préparons cette galerie avec des travaux réels. Bientôt, nous publierons des avant/après d'interventions terminées.",
        "recent_work_cta": "Envoyer des photos par WhatsApp",
        "view_google_reviews": "Voir les avis sur Google",
        "reviews_google_label": "Avis sur Google",
        "google_review_source": "Avis Google",
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
        "badge_acabamentos_premium": "Finitions Premium",
        "badge_muito_requisitado": "Très Demandé",
    },
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

# Before/after cards — replace image paths when dedicated photos are available.
RECENT_WORK_ITEMS = [
    {
        "before": "images/hero/ferramentas.webp",
        "after": "images/hero/obra.webp",
        "pt": (
            "Reparações gerais",
            "Arranjos em casa",
            "Substituição de fechos, ajuste de portas e pequenas reparações com acabamento cuidado.",
        ),
        "en": (
            "General repairs",
            "Home fixes",
            "Lock replacement, door adjustment and small repairs with a neat finish.",
        ),
        "es": (
            "Reparaciones generales",
            "Arreglos en casa",
            "Sustitución de cerraduras, ajuste de puertas y pequeñas reparaciones con buen acabado.",
        ),
        "fr": (
            "Réparations générales",
            "Petits travaux",
            "Remplacement de serrures, réglage de portes et petites réparations soignées.",
        ),
        "wa": {
            "pt": "Olá! Vi o trabalho de reparações gerais e gostaria de um orçamento.",
            "en": "Hello! I saw the general repairs project and would like a quote.",
            "es": "¡Hola! Vi el trabajo de reparaciones generales y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu le projet de réparations générales et je souhaite un devis.",
        },
    },
    {
        "before": "images/hero/hero-3.webp",
        "after": "images/hero/hero-4.webp",
        "pt": (
            "Pintura",
            "Sala renovada",
            "Preparação de paredes, retoque de imperfeições e pintura com acabamento uniforme.",
        ),
        "en": (
            "Painting",
            "Refreshed living room",
            "Wall preparation, defect touch-up and painting with an even, clean finish.",
        ),
        "es": (
            "Pintura",
            "Salón renovado",
            "Preparación de paredes, retoque de imperfecciones y pintura con acabado uniforme.",
        ),
        "fr": (
            "Peinture",
            "Salon rafraîchi",
            "Préparation des murs, retouches et peinture avec une finition uniforme.",
        ),
        "wa": {
            "pt": "Olá! Vi o trabalho de pintura e gostaria de um orçamento.",
            "en": "Hello! I saw the painting project and would like a quote.",
            "es": "¡Hola! Vi el trabajo de pintura y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu le projet de peinture et je souhaite un devis.",
        },
    },
    {
        "before": "images/hero/obra.webp",
        "after": "images/hero/hero-3.webp",
        "pt": (
            "Remodelação",
            "Cozinha funcional",
            "Atualização de zonas de trabalho e acabamentos para um espaço mais prático.",
        ),
        "en": (
            "Renovation",
            "Functional kitchen",
            "Worktop zones and finishes updated for a more practical space.",
        ),
        "es": (
            "Reforma",
            "Cocina funcional",
            "Actualización de zonas de trabajo y acabados para un espacio más práctico.",
        ),
        "fr": (
            "Rénovation",
            "Cuisine fonctionnelle",
            "Mise à jour des plans de travail et finitions pour un espace plus pratique.",
        ),
        "wa": {
            "pt": "Olá! Vi a remodelação de cozinha e gostaria de um orçamento.",
            "en": "Hello! I saw the kitchen renovation and would like a quote.",
            "es": "¡Hola! Vi la reforma de cocina y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu la rénovation de cuisine et je souhaite un devis.",
        },
    },
    {
        "before": "images/hero/hero-4.webp",
        "after": "images/hero/ferramentas.webp",
        "pt": (
            "Montagem",
            "Móveis montados",
            "Montagem de móveis e fixação segura de prateleiras e acessórios.",
        ),
        "en": (
            "Assembly",
            "Furniture fitted",
            "Furniture assembly and secure mounting of shelves and fittings.",
        ),
        "es": (
            "Montaje",
            "Muebles montados",
            "Montaje de muebles y fijación segura de estanterías y accesorios.",
        ),
        "fr": (
            "Montage",
            "Meubles montés",
            "Montage de meubles et fixation sécurisée d'étagères et accessoires.",
        ),
        "wa": {
            "pt": "Olá! Vi o trabalho de montagem e gostaria de um orçamento.",
            "en": "Hello! I saw the assembly project and would like a quote.",
            "es": "¡Hola! Vi el trabajo de montaje y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu le projet de montage et je souhaite un devis.",
        },
    },
    {
        "before": "images/hero/hero-3.webp",
        "after": "images/hero/obra.webp",
        "pt": (
            "Canalizações",
            "Casa de banho",
            "Reparação de fugas e substituição de torneira com teste de estanquidade.",
        ),
        "en": (
            "Plumbing",
            "Bathroom",
            "Leak repair and tap replacement with a watertight check.",
        ),
        "es": (
            "Fontanería",
            "Baño",
            "Reparación de fugas y sustitución de grifo con prueba de estanqueidad.",
        ),
        "fr": (
            "Plomberie",
            "Salle de bain",
            "Réparation de fuite et remplacement de robinet avec test d'étanchéité.",
        ),
        "wa": {
            "pt": "Olá! Vi o trabalho de canalizações e gostaria de um orçamento.",
            "en": "Hello! I saw the plumbing project and would like a quote.",
            "es": "¡Hola! Vi el trabajo de fontanería y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu le projet de plomberie et je souhaite un devis.",
        },
    },
    {
        "before": "images/hero/ferramentas.webp",
        "after": "images/hero/hero-4.webp",
        "pt": (
            "Limpeza pós-obra",
            "Espaço entregue",
            "Limpeza profunda após intervenção para entregar o espaço pronto a usar.",
        ),
        "en": (
            "Post-work cleaning",
            "Ready to use",
            "Deep clean after the job so the space is ready to use.",
        ),
        "es": (
            "Limpieza post-obra",
            "Espacio listo",
            "Limpieza profunda tras la intervención para dejar el espacio listo.",
        ),
        "fr": (
            "Nettoyage après travaux",
            "Espace prêt",
            "Nettoyage en profondeur après intervention pour un espace prêt à l'emploi.",
        ),
        "wa": {
            "pt": "Olá! Vi o trabalho de limpeza pós-obra e gostaria de um orçamento.",
            "en": "Hello! I saw the post-work cleaning and would like a quote.",
            "es": "¡Hola! Vi la limpieza post-obra y me gustaría un presupuesto.",
            "fr": "Bonjour ! J'ai vu le nettoyage après travaux et je souhaite un devis.",
        },
    },
]

RECENT_WORK_WA = {
    "pt": "Olá! Quero enviar fotos de um trabalho para a galeria de trabalhos recentes.",
    "en": "Hello! I would like to send photos of a job for the recent work gallery.",
    "es": "¡Hola! Quiero enviar fotos de un trabajo para la galería de trabajos recientes.",
    "fr": "Bonjour ! Je souhaite envoyer des photos d'un travail pour la galerie de travaux récents.",
}

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
