
(() => {
    'use strict';

    let currentLang = 'pt';
    let reviewsSwiper = null;

    const CONFIG = {
        /* E.164 sem espaços — alinhado com scripts/site_config.py tel_href() */
        phone: '+351932504112',
        phone_display: '932 504 112',
        whatsapp: '351932504112',
        email: 'geral@fazdetudo.pt',
        email_obfuscated: 'geral&#64;fazdetudo.pt',
        address: 'Grande Lisboa e Margem Sul, Portugal',
        googleReviews: {
            url: 'https://share.google/We1LViOoXucwIwBQl',
            rating: 5,
            count: 9,
            reviews: [
                {
                    name: 'Mamadu',
                    avatar: null,
                    rating: 5,
                    text: 'Recomendo! Muito bom.',
                    isNew: true
                },
                {
                    name: 'Leandro',
                    avatar: null,
                    rating: 5,
                    text: '',
                    isNew: true
                },
                {
                    name: 'Djadja',
                    avatar: null,
                    rating: 5,
                    text: 'Ajudou a montar os móveis, preços acessíveis.',
                    isNew: true
                },
                {
                    name: 'Carla',
                    avatar: null,
                    rating: 5,
                    text: 'Recomendo! Muito bom profissional.',
                    isNew: true
                },
                {
                    name: 'Rita',
                    avatar: null,
                    rating: 5,
                    text: 'Ótimo trabalho recomendável.',
                    isNew: true
                },
                {
                    name: 'Valenty',
                    avatar: null,
                    rating: 5,
                    text: 'Ótima empresa! 👌🏻💯',
                    isNew: true
                },
                {
                    name: 'Sambis',
                    avatar: null,
                    rating: 5,
                    text: 'Excelente profissional e um trabalho top. RECOMENDO!',
                    isNew: true
                },
                {
                    name: 'Ana',
                    avatar: null,
                    rating: 5,
                    text: '',
                    isNew: true
                },
                {
                    name: 'Isabel',
                    avatar: null,
                    rating: 5,
                    text: 'Excelente servicio me realizaron servicio de pintura y montado de muebles recomendado 💯',
                    isNew: true
                }
            ]
        }
    };

    const ADVANTAGE_ICONS = ['file-invoice', 'location-dot', 'users', 'broom', 'screwdriver-wrench', 'comments'];

    const SERVICE_LANDING_SLUGS = [
        'servico-remodelacoes.html',
        'servico-recuperar-casa.html',
        'servico-pinturas.html',
        'servico-limpezas.html',
        'servico-canalizacoes.html',
        'servico-electricidade.html',
        'servico-carpintaria.html',
        'servico-reparacoes-gerais.html',
        'servico-manutencao.html',
        'servico-pintura-fachadas-alpinismo.html',
        'servico-jardinagem.html',
        'servico-mudancas.html',
        'servico-informatica.html',
        'servico-serralharia.html',
        'servico-climatizacao.html',
        'servico-estores-persianas.html',
        'servico-decoracao-interiores.html',
        'servico-piscinas.html'
    ];

    function detectPageLang() {
        const fromAttr = document.documentElement.getAttribute('data-page-lang');
        if (fromAttr && LANGS[fromAttr]) return fromAttr;
        const path = window.location.pathname.replace(/\\/g, '/');
        const match = path.match(/^\/(en|es|fr)(\/|$)/);
        if (match) return match[1];
        return 'pt';
    }

    /** Relative prefix for service landing links (empty when already inside /en/, /es/, /fr/). */
    function getServiceBasePath() {
        const path = window.location.pathname.replace(/\\/g, '/');
        if (/^\/(en|es|fr)(\/|$)/.test(path)) return '';
        const lang = detectPageLang();
        return lang === 'pt' ? '' : `${lang}/`;
    }

    function homeServicesHashUrl() {
        const path = window.location.pathname.replace(/\\/g, '/');
        const langMatch = path.match(/^\/(en|es|fr)(\/|$)/);
        if (langMatch) return `/${langMatch[1]}/#services`;
        return '/#services';
    }

    function serviceLandingUrl(serviceIndex) {
        const slug = SERVICE_LANDING_SLUGS[serviceIndex];
        const base = getServiceBasePath();
        if (!slug) return homeServicesHashUrl();
        return `${base}${slug}`;
    }

    const LANGS = {
        pt: { label: 'Português', flag: 'https://flagcdn.com/w20/pt.png' },
        en: { label: 'English', flag: 'https://flagcdn.com/w20/gb.png' },
        es: { label: 'Español', flag: 'https://flagcdn.com/w20/es.png' },
        fr: { label: 'Français', flag: 'https://flagcdn.com/w20/fr.png' }
    };

    const ICON_MAP = {
        'paint-roller': 'fa-solid fa-paint-roller',
        'building': 'fa-solid fa-building',
        'faucet-drip': 'fa-solid fa-faucet-drip',
        'bolt': 'fa-solid fa-bolt',
        'hammer': 'fa-solid fa-hammer',
        'screwdriver-wrench': 'fa-solid fa-screwdriver-wrench',
        'trowel-bricks': 'fa-solid fa-trowel-bricks',
        'broom': 'fa-solid fa-broom',
        'seedling': 'fa-solid fa-seedling',
        'truck-fast': 'fa-solid fa-truck-fast',
        'laptop-medical': 'fa-solid fa-laptop-medical',
        'key': 'fa-solid fa-key',
        'wind': 'fa-solid fa-wind',
        'window-maximize': 'fa-solid fa-window-maximize',
        'house-chimney': 'fa-solid fa-house-chimney',
        'house-circle-check': 'fa-solid fa-house-circle-check',
        'shield-halved': 'fa-solid fa-shield-halved',
        'couch': 'fa-solid fa-couch',
        'water-ladder': 'fa-solid fa-water-ladder',
        'award': 'fa-solid fa-award',
        'clock': 'fa-solid fa-clock',
        'euro-sign': 'fa-solid fa-euro-sign',
        'file-invoice': 'fa-solid fa-file-invoice',
        'location-dot': 'fa-solid fa-location-dot',
        'users': 'fa-solid fa-users',
        'comments': 'fa-solid fa-comments'
    };

    function getGoogleReviewsCount() {
        return CONFIG.googleReviews.reviews.length;
    }

    function getReviewsCountLabel(lang) {
        const n = getGoogleReviewsCount();
        const suffix = T[lang].reviews_count_suffix || T.pt.reviews_count_suffix;
        return `${n} ${suffix}`;
    }

    const T = {
        pt: {
            nav_home: 'Início', nav_services: 'Serviços', nav_works: 'Trabalhos', nav_partners: 'Parceiros', nav_about: 'Sobre nós', nav_contact: 'Contacto',
            nav_articles: 'Artigos',
            footer_links: 'Links',
            hero_title: 'Handyman e Reparações ao Domicílio',
            footer_tagline: 'Handyman, reparações e manutenção ao domicílio.',
            hero_subtitle: 'Pequenas reparações, montagens, manutenção e trabalhos em casa. Um único contacto para resolver várias tarefas.',
            hero_btn_find: 'Encontrar profissional',
            hero_btn_help: 'Preciso de ajuda',
            hero_btn_quote: 'Pedir orçamento por WhatsApp',
            hero_btn_call: 'Ligar agora',
            hero_eyebrow: 'HANDYMAN · GRANDE LISBOA E MARGEM SUL',
            hero_title_line1: 'Handyman e reparações',
            hero_title_line2: 'para a sua casa.',
            header_quote: 'Pedir orçamento',
            trust_google: '5.0 Google',
            trust_quote: 'Orçamento gratuito',
            trust_area: 'Grande Lisboa e Margem Sul',
            trust_langs: 'PT · EN · ES · RO',
            services_see_all: 'Ver todos os serviços',
            services_see_less: 'Ver menos serviços',
            advantages_title_line1: 'Um contacto.',
            advantages_title_line2: 'Várias soluções.',
            advantages_text: 'Tratamos pequenas reparações, manutenção do dia a dia e trabalhos maiores.',
            partners_teaser_title: 'Precisa de um serviço especializado?',
            partners_teaser_text: 'Para alguns serviços trabalhamos com profissionais parceiros selecionados.',
            partners_teaser_cta: 'Ver todos os parceiros',
            footer_company: 'Empresa',
            hero_reviews_rating: '★★★★★ 5.0 no Google',
            hero_reviews_suffix: 'Atendimento em Português · English · Español · Română',
            services_title: 'Serviços de Handyman',
            services_subtitle: 'Reparações, montagens, manutenção e pequenos trabalhos realizados com atendimento direto na Grande Lisboa e Margem Sul.',
            /* SYNC: Ordem = index.html → #services .services-modern-grid */
            services: [
                { name: 'Remodelações e Obras', description: 'Remodelação de cozinhas e casas de banho, construção de novas divisões, ampliações e obras estruturais. Do projeto à entrega da chave.' },
                { name: 'Recuperar Casa', description: 'Recuperação completa de casas devolutas, herdadas ou degradadas. Da estrutura aos acabamentos, devolvemos vida e habitabilidade ao seu imóvel.' },
                { name: 'Pinturas', description: 'Interior e exterior. Preparação de superfícies, primários e acabamentos de qualidade.' },
                { name: 'Limpezas', description: 'Limpezas domésticas, pós-obra, escritórios e condomínios.' },
                { name: 'Canalizações', description: 'Reparação de fugas, desentupimentos, reparação de autoclismos, instalação de torneiras, sanitas e sistemas de água.' },
                { name: 'Electricidade', description: 'Instalações eléctricas, tomadas, iluminação e quadros eléctricos.' },
                { name: 'Carpintaria', description: 'Montagem de móveis, reparação de portas, janelas e trabalhos em madeira.' },
                { name: 'Reparações Gerais', description: 'Pequenas e grandes reparações para manter a sua casa em perfeitas condições.' },
                { name: 'Manutenção', description: 'Serviços de manutenção preventiva, reparações gerais e lavagem de alta pressão de telhados, pátios e fachadas.' },
                { name: 'Pintura de Fachadas (Alpinismo)', description: 'Pintura e reabilitação de fachadas e prédios com recurso a alpinismo industrial. Mais rápido, económico e sem necessidade de andaimes.' },
                { name: 'Jardinagem', description: 'Manutenção de jardins, poda de árvores e sistemas de rega.' },
                { name: 'Mudanças', description: 'Mudanças residenciais e comerciais. Transporte, embalagem e montagem.' },
                { name: 'Informática', description: 'Reparação de computadores, redes Wi-Fi e smart home.' },
                { name: 'Serralharia', description: 'Substituição e reparação de fechaduras, abertura de portas urgente, portões, grades e alumínios.' },
                { name: 'Climatização', description: 'Instalação, manutenção e reparação de ar condicionado e aquecimento.' },
                { name: 'Estores e Persianas', description: 'Reparação e instalação de estores, persianas, mosquiteiras e toldos.' },
                { name: 'Decoração de Interiores', description: 'Cortinas, papel de parede, iluminação decorativa, molduras e home staging.' },
                { name: 'Piscinas', description: 'Construção, manutenção, reparação, limpeza e tratamento de piscinas.' }
            ],
            advantages_title: 'Porquê escolher-nos?',
            advantages: [
                { name: 'Orçamento grátis', description: 'Orçamento sem compromisso para planear o seu projeto com tranquilidade.' },
                { name: 'Atendimento na Grande Lisboa e Margem Sul', description: 'Deslocamo-nos à sua casa ou empresa em Lisboa, Cascais, Almada, Setúbal e arredores.' },
                { name: 'Equipa polivalente', description: 'Um único contacto para reparações, manutenção e obras especializadas.' },
                { name: 'Trabalho limpo e organizado', description: 'Protegemos o espaço e deixamos tudo arrumado no final.' },
                { name: 'Soluções para pequenas reparações e obras maiores', description: 'Do detalhe ao projeto completo, com a mesma dedicação.' },
                { name: 'Contacto rápido por WhatsApp', description: 'Resposta ágil para marcar visitas e pedidos de orçamento.' }
            ],
            testimonials_title: 'O que dizem os nossos clientes',
            recent_work_title: 'Veja alguns dos nossos trabalhos',
            recent_work_subtitle: 'Veja alguns dos trabalhos de reparação, montagem, manutenção e remodelação realizados pela FAZDETUDO.PT.',
            recent_work_zone: 'Zona',
            recent_work_service: 'Serviço',
            recent_work_link: 'Ver trabalho',
            work_lightbox_close: 'Fechar',
            work_lightbox_dialog: 'Visualização do trabalho',
            work_lightbox_open_image: 'Ver imagem em tamanho maior',
            work_lightbox_open_video: 'Ver vídeo em tamanho maior',
            work_lightbox_prev: 'Imagem anterior',
            work_lightbox_next: 'Imagem seguinte',
            reviews_google_label: 'Google',
            google_review_source: 'Crítica de Google',
            google_new: 'NOVA',
            reviews_count_suffix: 'críticas',
            view_google_reviews: 'Ver avaliações no Google',
            faq_title: 'Perguntas Frequentes',
            faqs: [
                { question: 'Fazem pequenas reparações?', answer: 'Sim. Pendurar prateleiras, ajustar portas, retocar pinturas e resolver a lista de arranjos do dia a dia fazem parte do nosso trabalho quotidiano.' },
                { question: 'Posso pedir orçamento por WhatsApp?', answer: 'Sim. Envie fotos e uma breve descrição pelo WhatsApp e respondemos com orientação e orçamento gratuito.' },
                { question: 'Que zonas atendem?', answer: 'Grande Lisboa e Margem Sul, incluindo Lisboa, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro e Setúbal.' },
                { question: 'Fazem urgências?', answer: 'Sempre que possível atendemos urgências. Contacte-nos para confirmar disponibilidade no mesmo dia ou no dia seguinte.' },
                { question: 'Trabalham para casas e empresas?', answer: 'Sim. Atendemos particulares, condomínios, escritórios e comércios.' },
                { question: 'O orçamento é gratuito?', answer: 'Sim. O orçamento é gratuito e sem compromisso.' }
            ],
            contact_title: 'Tem trabalhos para fazer em casa?',
            contact_subtitle: 'Envie-nos fotografias e uma breve descrição do que precisa. Respondemos com orientação e orçamento.',
            contact_cta: 'Pedir orçamento por WhatsApp',
            social_cta: 'Siga-nos e veja os nossos trabalhos',
            footer_rights: 'FAZDETUDO.PT. Todos os direitos reservados.',
            wa_message: 'Olá! Gostaria de pedir um orçamento para um serviço de handyman/reparação.',
            wa_greeting: 'Como posso ajudar?',
            wa_placeholder: 'Escreva uma mensagem...'
        },
        en: {
            nav_home: 'Home', nav_services: 'Services', nav_works: 'Our work', nav_partners: 'Partners', nav_about: 'About us', nav_contact: 'Contact',
            nav_articles: 'Articles',
            footer_links: 'Links',
            hero_title: 'Handyman and Home Repair Services',
            footer_tagline: 'Handyman, repairs and home maintenance.',
            hero_subtitle: 'Small repairs, assembly, maintenance and home jobs across Greater Lisbon and the South Bank. One contact for multiple tasks.',
            hero_btn_find: 'Find a professional',
            hero_btn_help: 'I need help',
            hero_btn_quote: 'Request a quote on WhatsApp',
            hero_btn_call: 'Call now',
            hero_eyebrow: 'HANDYMAN · GREATER LISBON & SOUTH BANK',
            hero_title_line1: 'Handyman and repairs',
            hero_title_line2: 'for your home.',
            header_quote: 'Request a quote',
            trust_google: '5.0 Google',
            trust_quote: 'Free quote',
            trust_area: 'Greater Lisbon & South Bank',
            trust_langs: 'PT · EN · ES · RO',
            services_see_all: 'View all services',
            services_see_less: 'Show fewer services',
            advantages_title_line1: 'One contact.',
            advantages_title_line2: 'Multiple solutions.',
            advantages_text: 'We handle small repairs, day-to-day maintenance and larger jobs.',
            partners_teaser_title: 'Need a specialist service?',
            partners_teaser_text: 'For some services we work with selected partner professionals.',
            partners_teaser_cta: 'View all partners',
            footer_company: 'Company',
            hero_reviews_rating: '★★★★★ 5.0 on Google',
            hero_reviews_suffix: 'Service in Portuguese · English · Español · Română',
            services_title: 'Handyman Services',
            services_subtitle: 'Repairs, assembly, maintenance and small jobs with direct service across Greater Lisbon and the South Bank.',
            services: [
                { name: 'Renovations & Construction', description: 'Kitchen and bathroom renovations, building new rooms, extensions and structural works. From design to handover.' },
                { name: 'Home Restoration', description: 'Complete restoration of vacant, inherited or run-down houses. From structure to finishes, we bring your property back to life.' },
                { name: 'Painting', description: 'Interior and exterior. Surface preparation, primers and quality finishes.' },
                { name: 'Cleaning', description: 'Home, post-construction, office and condominium cleaning.' },
                { name: 'Plumbing', description: 'Leak repair, tap, toilet and water system installation.' },
                { name: 'Electrical', description: 'Electrical installations, sockets, lighting and electrical panels.' },
                { name: 'Carpentry', description: 'Furniture assembly, door and window repair, woodwork.' },
                { name: 'General Repairs', description: 'Small and large repairs to keep your home in perfect condition.' },
                { name: 'Maintenance', description: 'Preventive maintenance services for properties and condominiums.' },
                { name: 'Facade Painting (Rope Access)', description: 'Painting and refurbishment of facades and buildings using industrial rope access. Faster, more economical and no scaffolding required.' },
                { name: 'Gardening', description: 'Garden maintenance, tree pruning and irrigation systems.' },
                { name: 'Moving', description: 'Residential and commercial moving. Transport, packing and assembly.' },
                { name: 'IT Services', description: 'Computer repair, Wi-Fi networks and smart home.' },
                { name: 'Locksmithing', description: 'Locks, gates, grilles, aluminium and emergency door opening.' },
                { name: 'Air Conditioning', description: 'Installation, maintenance and repair of air conditioning and heating.' },
                { name: 'Blinds & Shutters', description: 'Repair and installation of blinds, shutters, mosquito nets and awnings.' },
                { name: 'Interior Design', description: 'Curtains, wallpaper, decorative lighting, frames and home staging.' },
                { name: 'Pools', description: 'Pool construction, maintenance, repair, cleaning and water treatment.' }
            ],
            advantages_title: 'Why choose us?',
            advantages: [
                { name: 'Free quote', description: 'No-obligation quote so you can plan your project with confidence.' },
                { name: 'Coverage in Greater Lisbon and South Bank', description: 'We come to your home or business in Lisbon, Cascais, Almada, Setúbal and surrounding areas.' },
                { name: 'Versatile team', description: 'One point of contact for repairs, maintenance and specialist works.' },
                { name: 'Clean, organised work', description: 'We protect your space and leave everything tidy when we finish.' },
                { name: 'Small repairs and larger projects', description: 'From quick fixes to full projects, with the same care throughout.' },
                { name: 'Fast contact via WhatsApp', description: 'Quick replies to schedule visits and request quotes.' }
            ],
            testimonials_title: 'What our clients say',
            recent_work_title: 'See some of our recent work',
            recent_work_subtitle: 'See some of the repair, assembly, maintenance and renovation jobs carried out by FAZDETUDO.PT.',
            recent_work_zone: 'Area',
            recent_work_service: 'Service',
            recent_work_link: 'View work',
            work_lightbox_close: 'Close',
            work_lightbox_dialog: 'Work preview',
            work_lightbox_open_image: 'View larger image',
            work_lightbox_open_video: 'View larger video',
            work_lightbox_prev: 'Previous image',
            work_lightbox_next: 'Next image',
            reviews_google_label: 'Google',
            google_review_source: 'Google review',
            google_new: 'NEW',
            reviews_count_suffix: 'reviews',
            view_google_reviews: 'View reviews on Google',
            faq_title: 'Frequently Asked Questions',
            faqs: [
                { question: 'Do you handle small repairs?', answer: 'Yes. Hanging shelves, adjusting doors, touch-up painting and everyday fix-it jobs are part of our daily work.' },
                { question: 'Can I request a quote via WhatsApp?', answer: 'Yes. Send photos and a short description on WhatsApp and we will reply with guidance and a free quote.' },
                { question: 'Which areas do you cover?', answer: 'Greater Lisbon and the South Bank, including Lisbon, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro and Setúbal.' },
                { question: 'Do you handle emergencies?', answer: 'Whenever possible we attend urgent jobs. Contact us to confirm same-day or next-day availability.' },
                { question: 'Do you work for homes and businesses?', answer: 'Yes. We serve private clients, condominiums, offices and retail premises.' },
                { question: 'Is the quote free?', answer: 'Yes. Quotes are free and without obligation.' }
            ],
            contact_title: 'Have jobs to do at home?',
            contact_subtitle: 'Send us photos and a short description of what you need. We will reply with guidance and a quote.',
            contact_cta: 'Request a quote on WhatsApp',
            social_cta: 'Follow us and see our work',
            footer_rights: 'FAZDETUDO.PT. All rights reserved.',
            wa_message: 'Hello! I would like to request a quote for a handyman or home repair service.',
            wa_greeting: 'How can I help you?',
            wa_placeholder: 'Type a message...'
        },
        es: {
            nav_home: 'Inicio', nav_services: 'Servicios', nav_works: 'Trabajos', nav_partners: 'Colaboradores', nav_about: 'Sobre nosotros', nav_contact: 'Contacto',
            nav_articles: 'Artículos',
            footer_links: 'Enlaces',
            hero_title: 'Manitas y Reparaciones a Domicilio',
            footer_tagline: 'Manitas, reparaciones y mantenimiento a domicilio.',
            hero_subtitle: 'Pequeñas reparaciones, montaje, mantenimiento y trabajos en casa en la Gran Lisboa y Margen Sur. Un contacto para resolver varias tareas.',
            hero_btn_find: 'Encontrar profesional',
            hero_btn_help: 'Necesito ayuda',
            hero_btn_quote: 'Pedir presupuesto por WhatsApp',
            hero_btn_call: 'Llamar ahora',
            hero_eyebrow: 'MANITAS · GRAN LISBOA Y MARGEN SUR',
            hero_title_line1: 'Manitas y reparaciones',
            hero_title_line2: 'para su casa.',
            header_quote: 'Pedir presupuesto',
            trust_google: '5.0 Google',
            trust_quote: 'Presupuesto gratuito',
            trust_area: 'Gran Lisboa y Margen Sur',
            trust_langs: 'PT · EN · ES · RO',
            services_see_all: 'Ver todos los servicios',
            services_see_less: 'Ver menos servicios',
            advantages_title_line1: 'Un contacto.',
            advantages_title_line2: 'Varias soluciones.',
            advantages_text: 'Nos ocupamos de pequeñas reparaciones, mantenimiento diario y trabajos mayores.',
            partners_teaser_title: '¿Necesita un servicio especializado?',
            partners_teaser_text: 'Para algunos servicios trabajamos con profesionales colaboradores seleccionados.',
            partners_teaser_cta: 'Ver todos los colaboradores',
            footer_company: 'Empresa',
            hero_reviews_rating: '★★★★★ 5.0 en Google',
            hero_reviews_suffix: 'Atención en Português · English · Español · Română',
            services_title: 'Servicios de Manitas',
            services_subtitle: 'Reparaciones, montajes, mantenimiento y pequeños trabajos con atención directa en la Gran Lisboa y Margen Sur.',
            services: [
                { name: 'Reformas y Obras', description: 'Reforma de cocinas y baños, construcción de nuevas estancias, ampliaciones y obras estructurales. Del proyecto a la entrega.' },
                { name: 'Recuperar Casa', description: 'Recuperación completa de casas vacías, heredadas o deterioradas. De la estructura a los acabados, devolvemos vida y habitabilidad a su inmueble.' },
                { name: 'Pinturas', description: 'Interior y exterior. Preparación de superficies, imprimaciones y acabados de calidad.' },
                { name: 'Limpieza', description: 'Limpiezas domésticas, post-obra, oficinas y comunidades.' },
                { name: 'Fontanería', description: 'Reparación de fugas, instalación de grifos, sanitarios y sistemas de agua.' },
                { name: 'Electricidad', description: 'Instalaciones eléctricas, enchufes, iluminación y cuadros eléctricos.' },
                { name: 'Carpintería', description: 'Montaje de muebles, reparación de puertas, ventanas y trabajos en madera.' },
                { name: 'Reparaciones generales', description: 'Pequeñas y grandes reparaciones para mantener su casa en perfectas condiciones.' },
                { name: 'Mantenimiento', description: 'Servicios de mantenimiento preventivo para propiedades y comunidades.' },
                { name: 'Pintura de Fachadas (Alpinismo)', description: 'Pintura y rehabilitación de fachadas y edificios con alpinismo industrial. Más rápido, económico y sin necesidad de andamios.' },
                { name: 'Jardinería', description: 'Mantenimiento de jardines, poda de árboles y sistemas de riego.' },
                { name: 'Mudanzas', description: 'Mudanzas residenciales y comerciales. Transporte, embalaje y montaje.' },
                { name: 'Informática', description: 'Reparación de ordenadores, redes Wi-Fi y smart home.' },
                { name: 'Cerrajería', description: 'Cerraduras, portones, rejas, aluminio y apertura urgente de puertas.' },
                { name: 'Climatización', description: 'Instalación, mantenimiento y reparación de aire acondicionado y calefacción.' },
                { name: 'Persianas y estores', description: 'Reparación e instalación de estores, persianas, mosquiteras y toldos.' },
                { name: 'Decoración de interiores', description: 'Cortinas, papel pintado, iluminación decorativa, molduras y home staging.' },
                { name: 'Piscinas', description: 'Construcción, mantenimiento, reparación, limpieza y tratamiento de piscinas.' }
            ],
            advantages_title: '¿Por qué elegirnos?',
            advantages: [
                { name: 'Presupuesto gratis', description: 'Presupuesto sin compromiso para planificar su proyecto con tranquilidad.' },
                { name: 'Servicio en la Gran Lisboa y Margen Sur', description: 'Nos desplazamos a su hogar o empresa en Lisboa, Cascais, Almada, Setúbal y alrededores.' },
                { name: 'Equipo polivalente', description: 'Un solo contacto para reparaciones, mantenimiento y obras especializadas.' },
                { name: 'Trabajo limpio y organizado', description: 'Protegemos el espacio y lo dejamos todo recogido al terminar.' },
                { name: 'Pequeñas reparaciones y obras mayores', description: 'Del detalle al proyecto completo, con la misma dedicación.' },
                { name: 'Contacto rápido por WhatsApp', description: 'Respuesta ágil para visitas y solicitudes de presupuesto.' }
            ],
            testimonials_title: 'Lo que dicen nuestros clientes',
            recent_work_title: 'Vea algunos de nuestros trabajos',
            recent_work_subtitle: 'Vea algunos de los trabajos de reparación, montaje, mantenimiento y reforma realizados por FAZDETUDO.PT.',
            recent_work_zone: 'Zona',
            recent_work_service: 'Servicio',
            recent_work_link: 'Ver trabajo',
            work_lightbox_close: 'Cerrar',
            work_lightbox_dialog: 'Vista del trabajo',
            work_lightbox_open_image: 'Ver imagen ampliada',
            work_lightbox_open_video: 'Ver vídeo ampliado',
            work_lightbox_prev: 'Imagen anterior',
            work_lightbox_next: 'Imagen siguiente',
            reviews_google_label: 'Google',
            google_review_source: 'Reseña de Google',
            google_new: 'NUEVA',
            reviews_count_suffix: 'reseñas',
            view_google_reviews: 'Ver reseñas en Google',
            faq_title: 'Preguntas Frecuentes',
            faqs: [
                { question: '¿Hacen pequeñas reparaciones?', answer: 'Sí. Colgar estanterías, ajustar puertas, retocar pinturas y resolver arreglos del día a día forman parte de nuestro trabajo habitual.' },
                { question: '¿Puedo pedir presupuesto por WhatsApp?', answer: 'Sí. Envíe fotos y una breve descripción por WhatsApp y le respondemos con orientación y presupuesto gratuito.' },
                { question: '¿Qué zonas atienden?', answer: 'Gran Lisboa y Margen Sur, incluyendo Lisboa, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro y Setúbal.' },
                { question: '¿Atienden urgencias?', answer: 'Siempre que es posible atendemos urgencias. Contáctenos para confirmar disponibilidad el mismo día o al siguiente.' },
                { question: '¿Trabajan para hogares y empresas?', answer: 'Sí. Atendemos particulares, comunidades de vecinos, oficinas y comercios.' },
                { question: '¿El presupuesto es gratuito?', answer: 'Sí. El presupuesto es gratuito y sin compromiso.' }
            ],
            contact_title: '¿Tiene trabajos que hacer en casa?',
            contact_subtitle: 'Envíenos fotografías y una breve descripción de lo que necesita. Respondemos con orientación y presupuesto.',
            contact_cta: 'Pedir presupuesto por WhatsApp',
            social_cta: 'Síguenos y mira nuestros trabajos',
            footer_rights: 'FAZDETUDO.PT. Todos los derechos reservados.',
            wa_message: '¡Hola! Me gustaría solicitar un presupuesto para un servicio de handyman o reparación.',
            wa_greeting: '¿Cómo puedo ayudarle?',
            wa_placeholder: 'Escriba un mensaje...'
        },
        fr: {
            nav_home: 'Accueil', nav_services: 'Services', nav_works: 'Réalisations', nav_partners: 'Partenaires', nav_about: 'À propos', nav_contact: 'Contact',
            nav_articles: 'Articles',
            footer_links: 'Liens',
            hero_title: 'Bricolage et Réparations à Domicile',
            footer_tagline: 'Bricolage, réparations et entretien à domicile.',
            hero_subtitle: 'Petites réparations, montage, entretien et travaux à domicile dans le Grand Lisbonne et la Rive Sud. Un contact pour plusieurs tâches.',
            hero_btn_find: 'Trouver un professionnel',
            hero_btn_help: 'J\'ai besoin d\'aide',
            hero_btn_quote: 'Demander un devis sur WhatsApp',
            hero_btn_call: 'Appeler maintenant',
            hero_eyebrow: 'BRICOLAGE · GRAND LISBONNE ET RIVE SUD',
            hero_title_line1: 'Bricolage et réparations',
            hero_title_line2: 'pour votre maison.',
            header_quote: 'Demander un devis',
            trust_google: '5.0 Google',
            trust_quote: 'Devis gratuit',
            trust_area: 'Grand Lisbonne et Rive Sud',
            trust_langs: 'PT · EN · ES · RO',
            services_see_all: 'Voir tous les services',
            services_see_less: 'Voir moins de services',
            advantages_title_line1: 'Un contact.',
            advantages_title_line2: 'Plusieurs solutions.',
            advantages_text: 'Nous prenons en charge petites réparations, entretien quotidien et travaux plus importants.',
            partners_teaser_title: 'Besoin d\'un service spécialisé ?',
            partners_teaser_text: 'Pour certains services, nous travaillons avec des professionnels partenaires sélectionnés.',
            partners_teaser_cta: 'Voir tous les partenaires',
            footer_company: 'Entreprise',
            hero_reviews_rating: '★★★★★ 5.0 sur Google',
            hero_reviews_suffix: 'Service en Portugais · English · Español · Română',
            services_title: 'Services de Bricolage',
            services_subtitle: 'Réparations, montage, entretien et petits travaux avec un service direct dans le Grand Lisbonne et la Rive Sud.',
            services: [
                { name: 'Rénovations et Travaux', description: 'Rénovation de cuisines et salles de bains, construction de nouvelles pièces, extensions et gros œuvre. Du projet à la livraison.' },
                { name: 'Rénover une Maison', description: 'Récupération complète de maisons vacantes, héritées ou dégradées. De la structure aux finitions, nous redonnons vie à votre bien.' },
                { name: 'Peinture', description: 'Intérieur et extérieur. Préparation des surfaces, apprêts et finitions de qualité.' },
                { name: 'Nettoyage', description: 'Nettoyage domestique, après-travaux, bureaux et copropriétés.' },
                { name: 'Plomberie', description: 'Réparation de fuites, installation de robinets, toilettes et systèmes d\'eau.' },
                { name: 'Électricité', description: 'Installations électriques, prises, éclairage et tableaux électriques.' },
                { name: 'Menuiserie', description: 'Montage de meubles, réparation de portes, fenêtres et travaux en bois.' },
                { name: 'Réparations générales', description: 'Petites et grandes réparations pour maintenir votre maison en parfait état.' },
                { name: 'Entretien', description: 'Services d\'entretien préventif pour propriétés et copropriétés.' },
                { name: 'Peinture de Façades (Alpinisme)', description: 'Peinture et réhabilitation de façades et immeubles par alpinisme industriel. Plus rapide, économique et sans échafaudage.' },
                { name: 'Jardinage', description: 'Entretien de jardins, taille d\'arbres et systèmes d\'irrigation.' },
                { name: 'Déménagements', description: 'Déménagements résidentiels et commerciaux. Transport, emballage et montage.' },
                { name: 'Informatique', description: 'Réparation d\'ordinateurs, réseaux Wi-Fi et maison intelligente.' },
                { name: 'Serrurerie', description: 'Serrures, portails, grilles, aluminium et ouverture de portes urgente.' },
                { name: 'Climatisation', description: 'Installation, entretien et réparation de climatisation et chauffage.' },
                { name: 'Stores et volets', description: 'Réparation et installation de stores, volets, moustiquaires et auvents.' },
                { name: 'Décoration d\'intérieur', description: 'Rideaux, papier peint, éclairage décoratif, moulures et home staging.' },
                { name: 'Piscines', description: 'Construction, entretien, réparation, nettoyage et traitement de l\'eau.' }
            ],
            advantages_title: 'Pourquoi nous choisir ?',
            advantages: [
                { name: 'Devis gratuit', description: 'Devis sans engagement pour planifier votre projet en toute sérénité.' },
                { name: 'Intervention Grand Lisbonne et Rive Sud', description: 'Nous nous déplaçons chez vous à Lisbonne, Cascais, Almada, Setúbal et environs.' },
                { name: 'Équipe polyvalente', description: 'Un seul interlocuteur pour réparations, entretien et travaux spécialisés.' },
                { name: 'Travail propre et soigné', description: 'Nous protégeons les lieux et laissons tout rangé à la fin.' },
                { name: 'Petites réparations et grands travaux', description: 'Du détail au projet complet, avec le même sérieux.' },
                { name: 'Contact rapide par WhatsApp', description: 'Réponse rapide pour planifier des visites et demander un devis.' }
            ],
            testimonials_title: 'Ce que disent nos clients',
            recent_work_title: 'Découvrez quelques-unes de nos réalisations',
            recent_work_subtitle: 'Découvrez quelques travaux de réparation, montage, entretien et rénovation réalisés par FAZDETUDO.PT.',
            recent_work_zone: 'Zone',
            recent_work_service: 'Service',
            recent_work_link: 'Voir le travail',
            work_lightbox_close: 'Fermer',
            work_lightbox_dialog: 'Aperçu du travail',
            work_lightbox_open_image: "Voir l'image en grand",
            work_lightbox_open_video: 'Voir la vidéo en grand',
            work_lightbox_prev: 'Image précédente',
            work_lightbox_next: 'Image suivante',
            reviews_google_label: 'Google',
            google_review_source: 'Avis Google',
            google_new: 'NOUVEAU',
            reviews_count_suffix: 'avis',
            view_google_reviews: 'Voir les avis sur Google',
            faq_title: 'Questions Fréquentes',
            faqs: [
                { question: 'Faites-vous les petites réparations ?', answer: 'Oui. Fixer des étagères, ajuster des portes, retouches de peinture et petits travaux du quotidien font partie de notre activité.' },
                { question: 'Puis-je demander un devis par WhatsApp ?', answer: 'Oui. Envoyez des photos et une courte description sur WhatsApp ; nous répondons avec des conseils et un devis gratuit.' },
                { question: 'Quelles zones couvrez-vous ?', answer: 'Grand Lisbonne et Rive Sud, dont Lisbonne, Cascais, Oeiras, Sintra, Almada, Seixal, Barreiro et Setúbal.' },
                { question: 'Intervenez-vous en urgence ?', answer: 'Dans la mesure du possible nous traitons les urgences. Contactez-nous pour confirmer une disponibilité rapide.' },
                { question: 'Travaillez-vous pour particuliers et entreprises ?', answer: 'Oui. Nous intervenons pour les particuliers, copropriétés, bureaux et commerces.' },
                { question: 'Le devis est-il gratuit ?', answer: 'Oui. Le devis est gratuit et sans engagement.' }
            ],
            contact_title: 'Des travaux à faire chez vous ?',
            contact_subtitle: 'Envoyez-nous des photos et une brève description de votre besoin. Nous répondons avec des conseils et un devis.',
            contact_cta: 'Demander un devis sur WhatsApp',
            social_cta: 'Suivez-nous et découvrez nos réalisations',
            footer_rights: 'FAZDETUDO.PT. Tous droits réservés.',
            wa_message: 'Bonjour ! Je souhaite demander un devis pour un service de handyman ou de réparation à domicile.',
            wa_greeting: 'Comment puis-je vous aider ?',
            wa_placeholder: 'Écrivez un message...'
        }
    };

    function t(key) { return T[currentLang][key] || T.pt[key] || ''; }

    function getWaMessage() {
        const fromPage = document.documentElement.getAttribute('data-wa-message');
        if (fromPage && fromPage.trim()) return fromPage.trim();
        return t('wa_message');
    }

    function renderAdvantages() {
        const grid = document.getElementById('advantages-grid');
        if (grid && !grid.children.length) {
            grid.innerHTML = T[currentLang].advantages.map((a, i) => `
                <div class="advantage-card fade-in">
                    <div class="advantage-icon">
                        <i class="${ICON_MAP[ADVANTAGE_ICONS[i]] || 'fa-solid fa-star'}"></i>
                    </div>
                    <h3>${a.name}</h3>
                    <p>${a.description}</p>
                </div>
            `).join('');
        }
    }

    function renderStars(rating) {
        return Array.from({ length: 5 }, (_, i) =>
            `<i class="fa-solid fa-star${i < rating ? '' : ' google-star-empty'}" aria-hidden="true"></i>`
        ).join('');
    }

    function renderReviewAvatar(review) {
        if (review.avatar) {
            return `<img src="${review.avatar}" alt="${review.name}" class="google-review-avatar" width="40" height="40" loading="lazy" referrerpolicy="no-referrer">`;
        }
        const initial = review.name.trim().charAt(0).toUpperCase();
        return `<div class="google-review-avatar google-review-avatar--initial" aria-hidden="true">${initial}</div>`;
    }

    function initReviewsSwiper() {
        if (typeof Swiper === 'undefined') return;

        if (reviewsSwiper) {
            reviewsSwiper.destroy(true, true);
            reviewsSwiper = null;
        }

        const el = document.getElementById('reviews-swiper');
        if (!el) return;

        reviewsSwiper = new Swiper(el, {
            slidesPerView: 1,
            spaceBetween: 30,
            loop: true,
            navigation: {
                nextEl: '.reviews-swiper-next',
                prevEl: '.reviews-swiper-prev'
            },
            pagination: {
                el: '.reviews-swiper-pagination',
                clickable: true
            }
        });
    }

    function renderTestimonials() {
        const wrapper = document.getElementById('testimonials-swiper-wrapper');
        const summary = document.getElementById('testimonials-summary');
        const link = document.getElementById('google-reviews-link');
        const lang = T[currentLang];
        const { googleReviews } = CONFIG;

        if (summary && !summary.children.length) {
            summary.innerHTML = `
                <div class="reviews-aggregate fade-in">
                    <span class="reviews-score">${googleReviews.rating.toFixed(1)}</span>
                    <div class="reviews-stars" aria-label="${googleReviews.rating} / 5">${renderStars(googleReviews.rating)}</div>
                    <span class="reviews-count">${lang.reviews_google_label || getReviewsCountLabel(currentLang)}</span>
                    <span class="reviews-google" aria-hidden="true"><i class="fab fa-google" aria-hidden="true"></i></span>
                </div>
            `;
        }

        if (wrapper && !wrapper.children.length) {
            wrapper.innerHTML = googleReviews.reviews.map(review => {
                const textBlock = review.text
                    ? `<p class="google-review-text">${review.text}</p>`
                    : '';
                const newBadge = review.isNew
                    ? `<span class="google-review-new">${lang.google_new}</span>`
                    : '';

                return `
                    <div class="swiper-slide">
                        <article class="google-review-card">
                            <div class="google-review-top">
                                ${renderReviewAvatar(review)}
                                <div class="google-review-meta">
                                    <strong class="google-review-name">${review.name}</strong>
                                    <span class="google-review-source">
                                        <i class="fab fa-google" aria-hidden="true"></i>
                                        ${lang.google_review_source}
                                    </span>
                                </div>
                            </div>
                            <div class="google-review-rating-row">
                                <span class="google-review-stars" aria-label="${review.rating} / 5">${renderStars(review.rating)}</span>
                                ${newBadge}
                            </div>
                            ${textBlock}
                        </article>
                    </div>
                `;
            }).join('');
        }

        if (link) {
            link.href = googleReviews.url;
            link.textContent = lang.view_google_reviews;
        }

        if (wrapper && wrapper.children.length) {
            requestAnimationFrame(() => initReviewsSwiper());
        }
    }

    function renderFAQ() {
        const list = document.getElementById('faq-list');
        if (list && !list.children.length) {
            list.innerHTML = T[currentLang].faqs.map((f, i) => `
                <div class="faq-item fade-in">
                    <button type="button" class="faq-question" aria-expanded="false" aria-controls="faq-answer-${i}">
                        ${f.question}
                        <i class="fa-solid fa-chevron-down" aria-hidden="true"></i>
                    </button>
                    <div class="faq-answer" id="faq-answer-${i}">
                        <div class="faq-answer-inner">${f.answer}</div>
                    </div>
                </div>
            `).join('');
        }
    }

    function setupFAQListeners() {
        const list = document.getElementById('faq-list');
        if (!list) return;
        list.addEventListener('click', e => {
            const btn = e.target.closest('.faq-question');
            if (!btn) return;
            const item = btn.closest('.faq-item');
            const isActive = item.classList.contains('active');
            list.querySelectorAll('.faq-item.active').forEach(el => el.classList.remove('active'));
            if (!isActive) item.classList.add('active');
        });
    }

    function applyTexts() {
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const val = t(el.dataset.i18n);
            if (val) el.textContent = val;
        });

        const phoneText = document.getElementById('footer-phone-text');
        if (phoneText) phoneText.textContent = CONFIG.phone_display;
        const emailText = document.getElementById('footer-email-text');
        if (emailText) emailText.innerHTML = CONFIG.email_obfuscated;
        const addressText = document.getElementById('footer-address-text');
        if (addressText) addressText.textContent = CONFIG.address;
    }

    function renderFooterServices() {
        const list = document.getElementById('footer-services-list');
        if (list && !list.children.length) {
            const services = T[currentLang].services || T.pt.services;
            list.innerHTML = services.map((s, i) =>
                `<li><a href="${serviceLandingUrl(i)}">${s.name}</a></li>`
            ).join('');
        }
    }

    function setupLinks() {
        const waNum = CONFIG.whatsapp;
        const waMsg = encodeURIComponent(getWaMessage());
        const telHref = `tel:${CONFIG.phone}`;

        ['header-phone', 'btn-call', 'cta-phone', 'footer-phone'].forEach(id => {
            const el = document.getElementById(id);
            if (!el || el.tagName !== 'A') return;
            const current = el.getAttribute('href') || '';
            if (current.startsWith('tel:') && current.replace(/\s/g, '') === telHref) return;
            el.href = telHref;
        });

        ['btn-quote', 'cta-quote'].forEach(id => {
            const el = document.getElementById(id);
            if (!el || el.tagName !== 'A') return;
            el.href = `https://wa.me/${waNum}?text=${waMsg}`;
        });

        const emailEl = document.getElementById('footer-email');
        if (emailEl && emailEl.tagName === 'A') {
            const mailto = `mailto:${CONFIG.email}`;
            if (emailEl.getAttribute('href') !== mailto) emailEl.href = mailto;
        }

        const greeting = document.getElementById('wa-greeting');
        if (greeting) greeting.textContent = t('wa_greeting');
        const input = document.getElementById('wa-chat-input');
        if (input) input.placeholder = t('wa_placeholder');
    }

    function setupWhatsAppChat() {
        const widget = document.getElementById('wa-widget');
        const chat = document.getElementById('wa-chat');
        const btn = document.getElementById('whatsapp-float');
        const closeBtn = document.getElementById('wa-chat-close');
        const input = document.getElementById('wa-chat-input');
        const sendBtn = document.getElementById('wa-chat-send');
        const timeEl = document.getElementById('wa-chat-time');
        if (!widget || !btn) return;

        function updateTime() {
            if (timeEl) {
                const now = new Date();
                timeEl.textContent = now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0');
            }
        }

        function toggleChat() {
            const isOpen = widget.classList.toggle('open');
            if (isOpen) {
                updateTime();
                setTimeout(() => input && input.focus(), 300);
            }
        }

        function sendMessage() {
            const msg = (input && input.value.trim()) || getWaMessage();
            const url = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank', 'noopener');
            if (input) input.value = '';
            widget.classList.remove('open');
        }

        btn.addEventListener('click', (e) => { e.stopPropagation(); toggleChat(); });
        if (closeBtn) closeBtn.addEventListener('click', (e) => { e.stopPropagation(); toggleChat(); });
        if (sendBtn) sendBtn.addEventListener('click', sendMessage);
        if (input) input.addEventListener('keydown', (e) => { if (e.key === 'Enter') sendMessage(); });

        document.addEventListener('click', (e) => {
            if (widget.classList.contains('open') && !widget.contains(e.target)) {
                widget.classList.remove('open');
            }
        });
    }

    function renderFAQSchema() {
        const faqs = T[currentLang].faqs;
        if (!faqs) return;
        let script = document.getElementById('faq-schema');
        /* Skip when FAQ JSON-LD already rendered in static HTML */
        if (script && script.textContent.trim()) return;
        if (!script) {
            script = document.createElement('script');
            script.id = 'faq-schema';
            script.type = 'application/ld+json';
            document.head.appendChild(script);
        }
        script.textContent = JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': faqs.map(f => ({
                '@type': 'Question',
                'name': f.question,
                'acceptedAnswer': {
                    '@type': 'Answer',
                    'text': f.answer
                }
            }))
        });
    }

    function applyLanguage(lang) {
        currentLang = lang;
        document.documentElement.lang = lang;
        applyTexts();
        renderFooterServices();
        renderAdvantages();
        renderTestimonials();
        renderFAQ();
        renderFAQSchema();
        setupLinks();
        requestAnimationFrame(() => setupScrollAnimations());
    }

    function setupLangSwitcher() {
        const switcher = document.getElementById('lang-switcher');
        const toggle = document.getElementById('lang-toggle');
        const dropdown = document.getElementById('lang-dropdown');
        const flag = document.getElementById('lang-flag');
        const label = document.getElementById('lang-label');
        if (!switcher || !toggle || !dropdown) return;

        function setLangOpen(open) {
            dropdown.classList.toggle('open', open);
            toggle.classList.toggle('open', open);
            toggle.setAttribute('aria-expanded', String(open));
        }

        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            setLangOpen(!dropdown.classList.contains('open'));
        });

        dropdown.addEventListener('click', (e) => {
            e.stopPropagation();
            if (e.target.closest('a.lang-option--nav')) {
                setLangOpen(false);
            }
        });

        document.addEventListener('click', (e) => {
            if (switcher.contains(e.target)) return;
            setLangOpen(false);
        });
    }

    function setupHeader() {
        const header = document.getElementById('header');
        const toggle = document.getElementById('menu-toggle');
        const nav = document.getElementById('nav');
        if (!header || !toggle || !nav) return;

        window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 20));

        function setNavOpen(open) {
            toggle.classList.toggle('active', open);
            nav.classList.toggle('active', open);
        }

        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            setNavOpen(!nav.classList.contains('active'));
        });

        nav.addEventListener('click', (e) => {
            e.stopPropagation();
            if (e.target.closest('.nav-link')) setNavOpen(false);
        });

        document.addEventListener('click', (e) => {
            if (toggle.contains(e.target) || nav.contains(e.target)) return;
            setNavOpen(false);
        });
    }

    function setupScrollAnimations() {
        const observer = new IntersectionObserver(
            entries => entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); observer.unobserve(e.target); } }),
            { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
        );
        document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    }

    function setupWorkLightbox() {
        const root = document.getElementById('work-lightbox');
        if (!root) return;

        const content = document.getElementById('work-lightbox-content');
        const titleEl = document.getElementById('work-lightbox-title');
        const closeBtn = document.getElementById('work-lightbox-close');
        const prevBtn = document.getElementById('work-lightbox-prev');
        const nextBtn = document.getElementById('work-lightbox-next');
        const counterEl = document.getElementById('work-lightbox-counter');
        const backdrop = root.querySelector('.work-lightbox-backdrop');
        const dialog = root.querySelector('.work-lightbox-dialog');
        if (!content || !titleEl || !closeBtn || !prevBtn || !nextBtn || !counterEl || !backdrop) return;

        const galleries = new Map();
        document.querySelectorAll('.work-lightbox-trigger').forEach(btn => {
            const galleryId = btn.dataset.gallery;
            if (!galleryId) return;
            if (!galleries.has(galleryId)) galleries.set(galleryId, []);
            galleries.get(galleryId).push(btn);
        });
        galleries.forEach(items => {
            items.sort((a, b) => Number(a.dataset.index) - Number(b.dataset.index));
        });

        let currentItems = [];
        let currentIndex = 0;
        let touchStartX = 0;

        function itemFromTrigger(trigger) {
            return {
                type: trigger.dataset.type,
                full: trigger.dataset.full,
                title: trigger.dataset.title || '',
                poster: trigger.dataset.poster || '',
            };
        }

        function appendMedia(item) {
            if (item.type === 'video') {
                const video = document.createElement('video');
                video.src = item.full;
                video.controls = true;
                video.muted = true;
                video.autoplay = true;
                video.playsInline = true;
                video.setAttribute('playsinline', '');
                if (item.poster) video.poster = item.poster;
                content.appendChild(video);
                video.play().catch(() => {});
                return;
            }
            const img = document.createElement('img');
            img.src = item.full;
            img.alt = item.title;
            img.decoding = 'async';
            content.appendChild(img);
        }

        function updateNavUi() {
            const multi = currentItems.length > 1;
            prevBtn.hidden = !multi;
            nextBtn.hidden = !multi;
            counterEl.hidden = !multi;
            if (multi) {
                counterEl.textContent = `${currentIndex + 1} / ${currentItems.length}`;
            } else {
                counterEl.textContent = '';
            }
        }

        function renderLightboxItem(index) {
            const trigger = currentItems[index];
            if (!trigger) return;
            const item = itemFromTrigger(trigger);
            if (!item.full) return;

            currentIndex = index;
            content.innerHTML = '';
            appendMedia(item);
            titleEl.textContent = item.title;
            updateNavUi();
        }

        function closeLightbox() {
            root.classList.remove('is-open');
            root.setAttribute('aria-hidden', 'true');
            document.body.classList.remove('lightbox-open');
            content.innerHTML = '';
            titleEl.textContent = '';
            currentItems = [];
            currentIndex = 0;
            prevBtn.hidden = true;
            nextBtn.hidden = true;
            counterEl.hidden = true;
            counterEl.textContent = '';
        }

        function openLightbox(trigger) {
            const galleryId = trigger.dataset.gallery;
            currentItems = galleryId ? (galleries.get(galleryId) || [trigger]) : [trigger];
            currentIndex = Number(trigger.dataset.index) || 0;
            if (currentIndex < 0 || currentIndex >= currentItems.length) currentIndex = 0;

            renderLightboxItem(currentIndex);
            root.classList.add('is-open');
            root.setAttribute('aria-hidden', 'false');
            document.body.classList.add('lightbox-open');
            closeBtn.focus();
        }

        function goNext() {
            if (currentItems.length <= 1) return;
            renderLightboxItem((currentIndex + 1) % currentItems.length);
        }

        function goPrev() {
            if (currentItems.length <= 1) return;
            renderLightboxItem((currentIndex - 1 + currentItems.length) % currentItems.length);
        }

        document.querySelectorAll('.work-lightbox-trigger').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                openLightbox(btn);
            });
        });

        closeBtn.addEventListener('click', closeLightbox);
        backdrop.addEventListener('click', closeLightbox);
        prevBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            goPrev();
        });
        nextBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            goNext();
        });

        document.addEventListener('keydown', (e) => {
            if (!root.classList.contains('is-open')) return;
            if (e.key === 'Escape') {
                closeLightbox();
                return;
            }
            if (e.key === 'ArrowRight') {
                e.preventDefault();
                goNext();
            } else if (e.key === 'ArrowLeft') {
                e.preventDefault();
                goPrev();
            }
        });

        const swipeTarget = dialog || content;
        swipeTarget.addEventListener('touchstart', (e) => {
            if (!root.classList.contains('is-open') || currentItems.length <= 1) return;
            touchStartX = e.changedTouches[0].clientX;
        }, { passive: true });

        swipeTarget.addEventListener('touchend', (e) => {
            if (!root.classList.contains('is-open') || currentItems.length <= 1) return;
            const touchEndX = e.changedTouches[0].clientX;
            const delta = touchEndX - touchStartX;
            if (delta > 50) goPrev();
            else if (delta < -50) goNext();
        }, { passive: true });
    }

    function setupWorkCarousels() {
        document.querySelectorAll('[data-work-carousel]').forEach(carousel => {
            const slides = [...carousel.querySelectorAll('.work-carousel-slide')];
            if (slides.length <= 1) return;

            const prevBtn = carousel.querySelector('.work-carousel-prev');
            const nextBtn = carousel.querySelector('.work-carousel-next');
            const dots = [...carousel.querySelectorAll('.work-carousel-dot')];
            let index = slides.findIndex(s => s.classList.contains('active'));
            if (index < 0) index = 0;

            function goTo(nextIndex) {
                index = (nextIndex + slides.length) % slides.length;
                slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === index);
                    dot.setAttribute('aria-selected', i === index ? 'true' : 'false');
                });
            }

            prevBtn?.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                goTo(index - 1);
            });
            nextBtn?.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                goTo(index + 1);
            });
            dots.forEach((dot, i) => {
                dot.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    goTo(i);
                });
            });

            let touchStartX = 0;
            carousel.addEventListener('touchstart', (e) => {
                if (e.target.closest('.work-carousel-btn, .work-carousel-dot')) return;
                touchStartX = e.changedTouches[0].clientX;
            }, { passive: true });

            carousel.addEventListener('touchend', (e) => {
                if (e.target.closest('.work-carousel-btn, .work-carousel-dot')) return;
                const touchEndX = e.changedTouches[0].clientX;
                const delta = touchEndX - touchStartX;
                if (delta > 45) goTo(index - 1);
                else if (delta < -45) goTo(index + 1);
            }, { passive: true });
        });
    }

    function setupPartnerDirectory() {
        const select = document.getElementById('partner-category-select');
        const grid = document.getElementById('partner-directory-grid');
        const results = document.getElementById('partner-directory-results');
        const empty = document.getElementById('partner-directory-empty');
        if (!select || !grid || !results) return;

        const cards = [...grid.querySelectorAll('[data-partner-category]')];

        function applyFilter(opts) {
            const scrollOnMobile = opts && opts.scrollOnMobile;
            const value = select.value || '';

            if (!value) {
                cards.forEach((card) => { card.hidden = true; });
                if (empty) empty.hidden = true;
                results.hidden = true;
                return;
            }

            let visible = 0;
            cards.forEach((card) => {
                const match = card.getAttribute('data-partner-category') === value;
                card.hidden = !match;
                if (match) visible += 1;
            });

            results.hidden = false;
            if (empty) empty.hidden = visible > 0;

            if (scrollOnMobile && window.matchMedia('(max-width: 768px)').matches) {
                results.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        }

        select.addEventListener('change', () => applyFilter({ scrollOnMobile: true }));
        applyFilter();
    }

    function setupPartnersPageDirectory() {
        const serviceSelect = document.getElementById('partners-service-select');
        const zoneSelect = document.getElementById('partners-zone-select');
        const list = document.getElementById('partners-results-list');
        const empty = document.getElementById('partners-empty');
        if (!serviceSelect || !zoneSelect || !list) return;

        const cards = [...list.querySelectorAll('[data-partner-category]')];

        function matchesZone(card, zone) {
            if (!zone) return true;
            const zones = (card.getAttribute('data-partner-zones') || '')
                .trim()
                .split(/\s+/)
                .filter(Boolean);
            if (!zones.length) return false;
            return zones.includes(zone);
        }

        function applyFilters() {
            const service = serviceSelect.value || '';
            const zone = zoneSelect.value || '';
            let visible = 0;

            cards.forEach((card) => {
                const serviceOk = !service || card.getAttribute('data-partner-category') === service;
                const zoneOk = matchesZone(card, zone);
                const match = serviceOk && zoneOk;
                card.hidden = !match;
                if (match) visible += 1;
            });

            if (empty) empty.hidden = visible > 0;
        }

        serviceSelect.addEventListener('change', applyFilters);
        zoneSelect.addEventListener('change', applyFilters);
        applyFilters();
    }


    function setupServicesMore() {
        const toggle = document.getElementById('services-more-toggle');
        const more = document.getElementById('services-more');
        if (!toggle || !more) return;
        const label = toggle.querySelector('[data-i18n="services_see_all"]') || toggle.querySelector('span');
        const lang = detectPageLang();
        const openText = (T[lang] && T[lang].services_see_all) || (label && label.textContent) || 'Ver todos os serviços';
        const lessText = (T[lang] && T[lang].services_see_less) || 'Ver menos serviços';
        toggle.addEventListener('click', () => {
            const opening = more.hasAttribute('hidden');
            if (opening) {
                more.removeAttribute('hidden');
                toggle.setAttribute('aria-expanded', 'true');
                if (label) label.textContent = lessText;
            } else {
                more.setAttribute('hidden', '');
                toggle.setAttribute('aria-expanded', 'false');
                if (label) label.textContent = openText;
            }
        });
    }


    function setupWorkRail() {
        const rail = document.getElementById('recent-work-grid');
        if (!rail) return;
        const buttons = document.querySelectorAll('[data-work-rail-dir]');
        buttons.forEach((button) => {
            button.addEventListener('click', () => {
                const dir = Number(button.getAttribute('data-work-rail-dir')) || 1;
                const card = rail.querySelector('.recent-work-card');
                const amount = card ? card.getBoundingClientRect().width + 18 : rail.clientWidth * 0.72;
                rail.scrollBy({ left: amount * dir, behavior: 'smooth' });
            });
        });
    }
    function init() {
        applyLanguage(detectPageLang());
        setupFAQListeners();
        setupHeader();
        setupLangSwitcher();
        setupWhatsAppChat();
        setupWorkCarousels();
        setupWorkLightbox();
        setupWorkRail();
        setupPartnerDirectory();
        setupPartnersPageDirectory();
        setupServicesMore();
        const yearEl = document.getElementById('year');
        if (yearEl) yearEl.textContent = new Date().getFullYear();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
