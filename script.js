(() => {
    'use strict';

    let currentLang = 'pt';
    let reviewsSwiper = null;

    const CONFIG = {
        phone: '+351 932504112',
        phone_display: '932 504 112',
        whatsapp: '351932504112',
        email: 'geral@fazdetudo.pt',
        address: 'Lisboa, Portugal',
        googleReviews: {
            url: 'https://www.google.com/search?sca_esv=9fc0643cb5b0db60&rlz=1C1GCEA_pt-PTPT1212PT1212&cs=1&output=search&q=Faz+de+tudo+-HANDYMAN&ludocid=8942884991647057370&lsig=AB86z5U1euJVZrgCPLuiW7ENF_mg&sa=X&ved=2ahUKEwi2xMTDgMmUAxV_fKQEHdpLNPsQj9IGegQIEhAJ&biw=1707&bih=932&dpr=1.5',
            rating: 5,
            count: 9,
            reviews: [
                {
                    name: 'Mamadu Sauane',
                    avatar: null,
                    rating: 5,
                    text: 'Recomendo! Muito bom.',
                    isNew: true
                },
                {
                    name: 'Leandro Conceição',
                    avatar: null,
                    rating: 5,
                    text: '',
                    isNew: true
                },
                {
                    name: 'Djadja Djassi',
                    avatar: null,
                    rating: 5,
                    text: 'Ajudou a montar os moveis, preço acessíveis.',
                    isNew: true
                },
                {
                    name: 'Carla Magalhaes',
                    avatar: null,
                    rating: 5,
                    text: 'Recomendo! Muito bom profissional.',
                    isNew: true
                },
                {
                    name: 'Rita Pereira',
                    avatar: null,
                    rating: 5,
                    text: 'Ótimo trabalho recomendável.',
                    isNew: true
                },
                {
                    name: 'Valenty Balde',
                    avatar: null,
                    rating: 5,
                    text: 'Ótimo empresa! ✌️ 💯',
                    isNew: true
                },
                {
                    name: 'Sambis Nbk',
                    avatar: null,
                    rating: 5,
                    text: 'Excelente profissional e um trabalho top . RECOMENDO !',
                    isNew: true
                },
                {
                    name: 'Ana Cwb',
                    avatar: 'https://lh3.googleusercontent.com/a-/ALV-UjXJ_dVcU7rVWeSDeWt94gQzcy7HeV01eC1D1UY2iBbJmJVOPzYW=s64-c-rp-mo-br100',
                    rating: 5,
                    text: '',
                    isNew: true
                },
                {
                    name: 'Isabel Gutierrez',
                    avatar: null,
                    rating: 5,
                    text: 'Excelente servicio me realizaron servicio de pintura y montado de muebles recomendado 💯',
                    isNew: true
                }
            ]
        }
    };

    const SERVICE_ICONS = [
        'paint-roller', 'building', 'faucet-drip', 'bolt', 'hammer', 'screwdriver-wrench',
        'gear', 'broom', 'leaf', 'truck', 'laptop', 'lock', 'temperature-half',
        'house-chimney', 'blinds', 'couch', 'water-ladder'
    ];

    const ADVANTAGE_ICONS = ['award', 'shield-halved', 'clock', 'euro-sign'];

    const SERVICE_CATEGORIES = [
        { id: 'obras', icon: 'house-chimney', titleKey: 'cat_obras', descKey: 'cat_obras_desc', serviceIndices: [0, 1, 13, 4] },
        { id: 'instalacoes', icon: 'screwdriver-wrench', titleKey: 'cat_instalacoes', descKey: 'cat_instalacoes_desc', serviceIndices: [2, 3, 12, 10] },
        { id: 'manutencao', icon: 'gear', titleKey: 'cat_manutencao', descKey: 'cat_manutencao_desc', serviceIndices: [5, 6, 11, 14] },
        { id: 'casa', icon: 'leaf', titleKey: 'cat_casa', descKey: 'cat_casa_desc', serviceIndices: [7, 8, 9, 15, 16] }
    ];

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
        'gear': 'fa-solid fa-gear',
        'broom': 'fa-solid fa-broom',
        'leaf': 'fa-solid fa-leaf',
        'truck': 'fa-solid fa-truck',
        'laptop': 'fa-solid fa-laptop',
        'lock': 'fa-solid fa-lock',
        'temperature-half': 'fa-solid fa-temperature-half',
        'house-chimney': 'fa-solid fa-house-chimney',
        'blinds': 'fa-solid fa-bars',
        'shield-halved': 'fa-solid fa-shield-halved',
        'couch': 'fa-solid fa-couch',
        'water-ladder': 'fa-solid fa-water-ladder',
        'award': 'fa-solid fa-award',
        'clock': 'fa-solid fa-clock',
        'euro-sign': 'fa-solid fa-euro-sign'
    };

    const T = {
        pt: {
            nav_home: 'Início', nav_services: 'Serviços', nav_about: 'Sobre nós', nav_contact: 'Contacto',
            footer_links: 'Links',
            hero_title: 'O seu faz tudo de confiança em Portugal',
            hero_subtitle: 'Pinturas, canalizações, electricidade, carpintaria e muito mais. Serviço profissional com garantia de qualidade.',
            hero_btn_quote: 'Pedir orçamento grátis',
            hero_btn_call: 'Ligue agora',
            services_title: 'Os nossos serviços',
            services_subtitle: 'Soluções completas para a sua casa ou escritório',
            cat_obras: 'Obras & Remodelações',
            cat_obras_desc: 'Pinturas, fachadas, remodelações e carpintaria para renovar o seu espaço.',
            cat_instalacoes: 'Instalações Técnicas',
            cat_instalacoes_desc: 'Canalização, electricidade, climatização e soluções informáticas.',
            cat_manutencao: 'Manutenção & Reparações',
            cat_manutencao_desc: 'Reparações, manutenção, serralharia e estores no dia a dia.',
            cat_casa: 'Casa & Exterior',
            cat_casa_desc: 'Limpeza, jardim, mudanças, decoração e manutenção de piscinas.',
            cat_view_services: 'Ver serviços',
            services: [
                { name: 'Pinturas', description: 'Interior e exterior. Preparação de superfícies, primários e acabamentos de qualidade.' },
                { name: 'Pintura de Fachadas (Alpinismo)', description: 'Pintura e reabilitação de fachadas e prédios com recurso a alpinismo industrial. Mais rápido, económico e sem necessidade de andaimes.' },
                { name: 'Canalizações', description: 'Reparação de fugas, instalação de torneiras, sanitas e sistemas de água.' },
                { name: 'Electricidade', description: 'Instalações eléctricas, tomadas, iluminação e quadros eléctricos.' },
                { name: 'Carpintaria', description: 'Montagem de móveis, reparação de portas, janelas e trabalhos em madeira.' },
                { name: 'Reparações Gerais', description: 'Pequenas e grandes reparações para manter a sua casa em perfeitas condições.' },
                { name: 'Manutenção', description: 'Serviços de manutenção preventiva para propriedades e condomínios.' },
                { name: 'Limpezas', description: 'Limpeza doméstica, pós-obra, de escritórios e espaços comerciais.' },
                { name: 'Jardinagem', description: 'Manutenção de jardins, poda de árvores e sistemas de rega.' },
                { name: 'Mudanças', description: 'Mudanças residenciais e comerciais. Transporte, embalagem e montagem.' },
                { name: 'Informática', description: 'Reparação de computadores, redes Wi-Fi e smart home.' },
                { name: 'Serralharia', description: 'Fechaduras, portões, grades, alumínios e abertura de portas urgente.' },
                { name: 'Climatização', description: 'Instalação, manutenção e reparação de ar condicionado e aquecimento.' },
                { name: 'Remodelações', description: 'Remodelação de cozinhas, casas de banho, pavimentos e obras gerais.' },
                { name: 'Estores e Persianas', description: 'Reparação e instalação de estores, persianas, mosquiteiras e toldos.' },
                { name: 'Decoração de Interiores', description: 'Cortinas, papel de parede, iluminação decorativa, molduras e home staging.' },
                { name: 'Piscinas', description: 'Limpeza, manutenção e reparação de piscinas. Tratamento de água, filtros, bombas e revestimentos.' }
            ],
            advantages_title: 'Porquê escolher-nos?',
            advantages: [
                { name: 'Experiência comprovada', description: 'Mais de 5 anos de experiência com profissionalismo e dedicação.' },
                { name: 'Qualidade garantida', description: 'Garantia em todos os trabalhos realizados. Satisfação assegurada.' },
                { name: 'Resposta rápida', description: 'Orçamentos em 24h. Disponibilidade para urgências.' },
                { name: 'Preços justos', description: 'Orçamentos transparentes sem surpresas. Melhor relação qualidade-preço.' }
            ],
            testimonials_title: 'Críticas',
            google_review_source: 'Crítica de Google',
            google_new: 'NOVA',
            reviews_count: '9 críticas',
            view_google_reviews: 'Ver críticas no Google',
            faq_title: 'Perguntas Frequentes',
            faqs: [
                { question: 'Que serviços de faz tudo oferecem?', answer: 'Oferecemos uma vasta gama de serviços incluindo pinturas, canalizações, electricidade, carpintaria, reparações gerais, manutenção, limpezas, jardinagem, mudanças, informática, serralharia, climatização, remodelações, estores e persianas, decoração de interiores e piscinas.' },
                { question: 'Quanto tempo demora para receber um orçamento?', answer: 'Normalmente respondemos com um orçamento dentro de 24 horas após o primeiro contacto. Para situações urgentes, fazemos o possível para responder no próprio dia.' },
                { question: 'Os vossos profissionais são certificados?', answer: 'Sim, todos os nossos profissionais são qualificados e possuem as certificações necessárias para realizar os trabalhos com segurança e qualidade.' },
                { question: 'Trabalham aos fins de semana?', answer: 'Sim, trabalhamos aos sábados mediante marcação prévia. Para situações de emergência, temos disponibilidade aos domingos e feriados.' },
                { question: 'Oferecem garantia nos trabalhos realizados?', answer: 'Sim, oferecemos garantia em todos os trabalhos realizados. O período de garantia varia conforme o tipo de serviço prestado.' },
                { question: 'Qual é a área de cobertura?', answer: 'Cobrimos toda a zona da Grande Lisboa e arredores, incluindo Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas e outras localidades.' }
            ],
            contact_title: 'Contacte-nos',
            contact_subtitle: 'Estamos prontos para ajudar. Peça o seu orçamento grátis.',
            social_cta: 'Siga-nos e veja os nossos trabalhos',
            footer_rights: 'Faz de Tudo PT. Todos os direitos reservados.',
            wa_message: 'Olá! Gostaria de pedir um orçamento.',
            wa_greeting: 'Como posso ajudar?',
            wa_placeholder: 'Escreva uma mensagem...'
        },
        en: {
            nav_home: 'Home', nav_services: 'Services', nav_about: 'About us', nav_contact: 'Contact',
            footer_links: 'Links',
            hero_title: 'Your trusted handyman in Portugal',
            hero_subtitle: 'Painting, plumbing, electrical, carpentry and much more. Professional service with quality guarantee.',
            hero_btn_quote: 'Get a free quote',
            hero_btn_call: 'Call now',
            services_title: 'Our services',
            services_subtitle: 'Complete solutions for your home or office',
            cat_obras: 'Works & Renovations',
            cat_obras_desc: 'Painting, facades, renovations and carpentry to transform your space.',
            cat_instalacoes: 'Technical Installations',
            cat_instalacoes_desc: 'Plumbing, electrical, HVAC and IT solutions.',
            cat_manutencao: 'Maintenance & Repairs',
            cat_manutencao_desc: 'Repairs, maintenance, locksmithing and blinds for everyday needs.',
            cat_casa: 'Home & Outdoor',
            cat_casa_desc: 'Cleaning, gardening, moving, décor and pool maintenance.',
            cat_view_services: 'View services',
            services: [
                { name: 'Painting', description: 'Interior and exterior. Surface preparation, primers and quality finishes.' },
                { name: 'Facade Painting (Rope Access)', description: 'Painting and refurbishment of facades and buildings using industrial rope access. Faster, more economical and no scaffolding required.' },
                { name: 'Plumbing', description: 'Leak repair, tap, toilet and water system installation.' },
                { name: 'Electrical', description: 'Electrical installations, sockets, lighting and electrical panels.' },
                { name: 'Carpentry', description: 'Furniture assembly, door and window repair, woodwork.' },
                { name: 'General Repairs', description: 'Small and large repairs to keep your home in perfect condition.' },
                { name: 'Maintenance', description: 'Preventive maintenance services for properties and condominiums.' },
                { name: 'Cleaning', description: 'Domestic, post-construction, office and commercial space cleaning.' },
                { name: 'Gardening', description: 'Garden maintenance, tree pruning and irrigation systems.' },
                { name: 'Moving', description: 'Residential and commercial moving. Transport, packing and assembly.' },
                { name: 'IT Services', description: 'Computer repair, Wi-Fi networks and smart home.' },
                { name: 'Locksmithing', description: 'Locks, gates, grilles, aluminium and emergency door opening.' },
                { name: 'Air Conditioning', description: 'Installation, maintenance and repair of air conditioning and heating.' },
                { name: 'Renovations', description: 'Kitchen, bathroom, flooring renovations and general works.' },
                { name: 'Blinds & Shutters', description: 'Repair and installation of blinds, shutters, mosquito nets and awnings.' },
                { name: 'Interior Design', description: 'Curtains, wallpaper, decorative lighting, frames and home staging.' },
                { name: 'Swimming Pools', description: 'Cleaning, maintenance and repair of pools. Water treatment, filters, pumps and linings.' }
            ],
            advantages_title: 'Why choose us?',
            advantages: [
                { name: 'Proven experience', description: 'Over 5 years of experience with professionalism and dedication.' },
                { name: 'Guaranteed quality', description: 'Warranty on all work performed. Satisfaction assured.' },
                { name: 'Fast response', description: 'Quotes within 24h. Available for emergencies.' },
                { name: 'Fair prices', description: 'Transparent quotes with no surprises. Best value for money.' }
            ],
            testimonials_title: 'Reviews',
            google_review_source: 'Google review',
            google_new: 'NEW',
            reviews_count: '9 reviews',
            view_google_reviews: 'View reviews on Google',
            faq_title: 'Frequently Asked Questions',
            faqs: [
                { question: 'What handyman services do you offer?', answer: 'We offer a wide range of services including painting, plumbing, electrical, carpentry, general repairs, maintenance, cleaning, gardening, moving, IT, locksmithing, air conditioning, renovations, blinds and shutters, interior design and swimming pools.' },
                { question: 'How long does it take to receive a quote?', answer: 'We usually respond with a quote within 24 hours of first contact. For urgent situations, we do our best to respond the same day.' },
                { question: 'Are your professionals certified?', answer: 'Yes, all our professionals are qualified and hold the necessary certifications to carry out work safely and with quality.' },
                { question: 'Do you work on weekends?', answer: 'Yes, we work on Saturdays by appointment. For emergencies, we are available on Sundays and public holidays.' },
                { question: 'Do you offer warranty on completed work?', answer: 'Yes, we offer a warranty on all work completed. The warranty period varies depending on the type of service provided.' },
                { question: 'What is your coverage area?', answer: 'We cover the entire Greater Lisbon area and surroundings, including Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas and other locations.' }
            ],
            contact_title: 'Contact us',
            contact_subtitle: 'We are ready to help. Request your free quote.',
            social_cta: 'Follow us and see our work',
            footer_rights: 'Faz de Tudo PT. All rights reserved.',
            wa_message: 'Hello! I would like to request a quote.',
            wa_greeting: 'How can I help you?',
            wa_placeholder: 'Type a message...'
        },
        es: {
            nav_home: 'Inicio', nav_services: 'Servicios', nav_about: 'Sobre nosotros', nav_contact: 'Contacto',
            footer_links: 'Enlaces',
            hero_title: 'Su profesional de confianza en Portugal',
            hero_subtitle: 'Pinturas, fontanería, electricidad, carpintería y mucho más. Servicio profesional con garantía de calidad.',
            hero_btn_quote: 'Pedir presupuesto gratis',
            hero_btn_call: 'Llame ahora',
            services_title: 'Nuestros servicios',
            services_subtitle: 'Soluciones completas para su hogar u oficina',
            cat_obras: 'Obras y Reformas',
            cat_obras_desc: 'Pinturas, fachadas, reformas y carpintería para renovar su espacio.',
            cat_instalacoes: 'Instalaciones Técnicas',
            cat_instalacoes_desc: 'Fontanería, electricidad, climatización e informática.',
            cat_manutencao: 'Mantenimiento y Reparaciones',
            cat_manutencao_desc: 'Reparaciones, mantenimiento, cerrajería y persianas.',
            cat_casa: 'Hogar y Exterior',
            cat_casa_desc: 'Limpieza, jardinería, mudanzas, decoración y piscinas.',
            cat_view_services: 'Ver servicios',
            services: [
                { name: 'Pinturas', description: 'Interior y exterior. Preparación de superficies, imprimaciones y acabados de calidad.' },
                { name: 'Pintura de Fachadas (Alpinismo)', description: 'Pintura y rehabilitación de fachadas y edificios con alpinismo industrial. Más rápido, económico y sin necesidad de andamios.' },
                { name: 'Fontanería', description: 'Reparación de fugas, instalación de grifos, sanitarios y sistemas de agua.' },
                { name: 'Electricidad', description: 'Instalaciones eléctricas, enchufes, iluminación y cuadros eléctricos.' },
                { name: 'Carpintería', description: 'Montaje de muebles, reparación de puertas, ventanas y trabajos en madera.' },
                { name: 'Reparaciones generales', description: 'Pequeñas y grandes reparaciones para mantener su casa en perfectas condiciones.' },
                { name: 'Mantenimiento', description: 'Servicios de mantenimiento preventivo para propiedades y comunidades.' },
                { name: 'Limpieza', description: 'Limpieza doméstica, post-obra, de oficinas y espacios comerciales.' },
                { name: 'Jardinería', description: 'Mantenimiento de jardines, poda de árboles y sistemas de riego.' },
                { name: 'Mudanzas', description: 'Mudanzas residenciales y comerciales. Transporte, embalaje y montaje.' },
                { name: 'Informática', description: 'Reparación de ordenadores, redes Wi-Fi y smart home.' },
                { name: 'Cerrajería', description: 'Cerraduras, portones, rejas, aluminio y apertura urgente de puertas.' },
                { name: 'Climatización', description: 'Instalación, mantenimiento y reparación de aire acondicionado y calefacción.' },
                { name: 'Reformas', description: 'Reformas de cocinas, baños, suelos y obras generales.' },
                { name: 'Persianas y estores', description: 'Reparación e instalación de estores, persianas, mosquiteras y toldos.' },
                { name: 'Decoración de interiores', description: 'Cortinas, papel pintado, iluminación decorativa, molduras y home staging.' },
                { name: 'Piscinas', description: 'Limpieza, mantenimiento y reparación de piscinas. Tratamiento de agua, filtros, bombas y revestimientos.' }
            ],
            advantages_title: '¿Por qué elegirnos?',
            advantages: [
                { name: 'Experiencia comprobada', description: 'Más de 5 años de experiencia con profesionalismo y dedicación.' },
                { name: 'Calidad garantizada', description: 'Garantía en todos los trabajos realizados. Satisfacción asegurada.' },
                { name: 'Respuesta rápida', description: 'Presupuestos en 24h. Disponibilidad para urgencias.' },
                { name: 'Precios justos', description: 'Presupuestos transparentes sin sorpresas. Mejor relación calidad-precio.' }
            ],
            testimonials_title: 'Reseñas',
            google_review_source: 'Reseña de Google',
            google_new: 'NUEVA',
            reviews_count: '9 reseñas',
            view_google_reviews: 'Ver reseñas en Google',
            faq_title: 'Preguntas Frecuentes',
            faqs: [
                { question: '¿Qué servicios ofrecen?', answer: 'Ofrecemos una amplia gama de servicios que incluyen pinturas, fontanería, electricidad, carpintería, reparaciones generales, mantenimiento, limpieza, jardinería, mudanzas, informática, cerrajería, climatización, reformas, persianas y estores, decoración de interiores y piscinas.' },
                { question: '¿Cuánto tiempo tarda en recibir un presupuesto?', answer: 'Normalmente respondemos con un presupuesto dentro de las 24 horas. Para situaciones urgentes, hacemos lo posible por responder el mismo día.' },
                { question: '¿Sus profesionales están certificados?', answer: 'Sí, todos nuestros profesionales están cualificados y poseen las certificaciones necesarias para realizar los trabajos con seguridad y calidad.' },
                { question: '¿Trabajan los fines de semana?', answer: 'Sí, trabajamos los sábados con cita previa. Para emergencias, tenemos disponibilidad los domingos y festivos.' },
                { question: '¿Ofrecen garantía en los trabajos realizados?', answer: 'Sí, ofrecemos garantía en todos los trabajos realizados. El período de garantía varía según el tipo de servicio.' },
                { question: '¿Cuál es el área de cobertura?', answer: 'Cubrimos toda la zona de la Gran Lisboa y alrededores, incluyendo Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas y otras localidades.' }
            ],
            contact_title: 'Contáctenos',
            contact_subtitle: 'Estamos listos para ayudar. Solicite su presupuesto gratis.',
            social_cta: 'Síguenos y mira nuestros trabajos',
            footer_rights: 'Faz de Tudo PT. Todos los derechos reservados.',
            wa_message: '¡Hola! Me gustaría pedir un presupuesto.',
            wa_greeting: '¿Cómo puedo ayudarle?',
            wa_placeholder: 'Escriba un mensaje...'
        },
        fr: {
            nav_home: 'Accueil', nav_services: 'Services', nav_about: 'À propos', nav_contact: 'Contact',
            footer_links: 'Liens',
            hero_title: 'Votre homme à tout faire de confiance au Portugal',
            hero_subtitle: 'Peinture, plomberie, électricité, menuiserie et bien plus. Service professionnel avec garantie de qualité.',
            hero_btn_quote: 'Devis gratuit',
            hero_btn_call: 'Appelez maintenant',
            services_title: 'Nos services',
            services_subtitle: 'Solutions complètes pour votre maison ou bureau',
            cat_obras: 'Travaux & Rénovations',
            cat_obras_desc: 'Peinture, façades, rénovations et menuiserie pour transformer votre espace.',
            cat_instalacoes: 'Installations Techniques',
            cat_instalacoes_desc: 'Plomberie, électricité, climatisation et informatique.',
            cat_manutencao: 'Entretien & Réparations',
            cat_manutencao_desc: 'Réparations, entretien, serrurerie et stores.',
            cat_casa: 'Maison & Extérieur',
            cat_casa_desc: 'Nettoyage, jardin, déménagement, déco et piscines.',
            cat_view_services: 'Voir les services',
            services: [
                { name: 'Peinture', description: 'Intérieur et extérieur. Préparation des surfaces, apprêts et finitions de qualité.' },
                { name: 'Peinture de Façades (Alpinisme)', description: 'Peinture et réhabilitation de façades et immeubles par alpinisme industriel. Plus rapide, économique et sans échafaudage.' },
                { name: 'Plomberie', description: 'Réparation de fuites, installation de robinets, toilettes et systèmes d\'eau.' },
                { name: 'Électricité', description: 'Installations électriques, prises, éclairage et tableaux électriques.' },
                { name: 'Menuiserie', description: 'Montage de meubles, réparation de portes, fenêtres et travaux en bois.' },
                { name: 'Réparations générales', description: 'Petites et grandes réparations pour maintenir votre maison en parfait état.' },
                { name: 'Entretien', description: 'Services d\'entretien préventif pour propriétés et copropriétés.' },
                { name: 'Nettoyage', description: 'Nettoyage domestique, après-travaux, de bureaux et espaces commerciaux.' },
                { name: 'Jardinage', description: 'Entretien de jardins, taille d\'arbres et systèmes d\'irrigation.' },
                { name: 'Déménagements', description: 'Déménagements résidentiels et commerciaux. Transport, emballage et montage.' },
                { name: 'Informatique', description: 'Réparation d\'ordinateurs, réseaux Wi-Fi et maison intelligente.' },
                { name: 'Serrurerie', description: 'Serrures, portails, grilles, aluminium et ouverture de portes urgente.' },
                { name: 'Climatisation', description: 'Installation, entretien et réparation de climatisation et chauffage.' },
                { name: 'Rénovations', description: 'Rénovation de cuisines, salles de bains, sols et travaux généraux.' },
                { name: 'Stores et volets', description: 'Réparation et installation de stores, volets, moustiquaires et auvents.' },
                { name: 'Décoration d\'intérieur', description: 'Rideaux, papier peint, éclairage décoratif, moulures et home staging.' },
                { name: 'Piscines', description: 'Nettoyage, entretien et réparation de piscines. Traitement de l\'eau, filtres, pompes et revêtements.' }
            ],
            advantages_title: 'Pourquoi nous choisir ?',
            advantages: [
                { name: 'Expérience prouvée', description: 'Plus de 5 ans d\'expérience avec professionnalisme et dévouement.' },
                { name: 'Qualité garantie', description: 'Garantie sur tous les travaux réalisés. Satisfaction assurée.' },
                { name: 'Réponse rapide', description: 'Devis en 24h. Disponibilité pour les urgences.' },
                { name: 'Prix justes', description: 'Devis transparents sans surprises. Meilleur rapport qualité-prix.' }
            ],
            testimonials_title: 'Avis',
            google_review_source: 'Avis Google',
            google_new: 'NOUVEAU',
            reviews_count: '9 avis',
            view_google_reviews: 'Voir les avis sur Google',
            faq_title: 'Questions Fréquentes',
            faqs: [
                { question: 'Quels services proposez-vous ?', answer: 'Nous proposons une large gamme de services incluant peinture, plomberie, électricité, menuiserie, réparations générales, entretien, nettoyage, jardinage, déménagements, informatique, serrurerie, climatisation, rénovations, stores et volets, décoration d\'intérieur et piscines.' },
                { question: 'Combien de temps pour recevoir un devis ?', answer: 'Nous répondons généralement avec un devis dans les 24 heures. Pour les situations urgentes, nous faisons notre possible pour répondre le jour même.' },
                { question: 'Vos professionnels sont-ils certifiés ?', answer: 'Oui, tous nos professionnels sont qualifiés et possèdent les certifications nécessaires pour réaliser les travaux en toute sécurité et qualité.' },
                { question: 'Travaillez-vous le week-end ?', answer: 'Oui, nous travaillons le samedi sur rendez-vous. Pour les urgences, nous sommes disponibles les dimanches et jours fériés.' },
                { question: 'Offrez-vous une garantie sur les travaux ?', answer: 'Oui, nous offrons une garantie sur tous les travaux réalisés. La durée de garantie varie selon le type de service.' },
                { question: 'Quelle est votre zone de couverture ?', answer: 'Nous couvrons toute la zone du Grand Lisbonne et ses environs, y compris Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas et d\'autres localités.' }
            ],
            contact_title: 'Contactez-nous',
            contact_subtitle: 'Nous sommes prêts à vous aider. Demandez votre devis gratuit.',
            social_cta: 'Suivez-nous et découvrez nos réalisations',
            footer_rights: 'Faz de Tudo PT. Tous droits réservés.',
            wa_message: 'Bonjour ! Je souhaiterais demander un devis.',
            wa_greeting: 'Comment puis-je vous aider ?',
            wa_placeholder: 'Écrivez un message...'
        }
    };

    function t(key) { return T[currentLang][key] || T.pt[key] || ''; }

    function getServiceWhatsAppUrl(serviceName) {
        const text = `Olá, quero um orçamento para ${serviceName}`;
        return `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(text)}`;
    }

    function populateServiceModals() {
        const services = T[currentLang].services;
        SERVICE_CATEGORIES.forEach(cat => {
            const list = document.getElementById(`modal-${cat.id}-list`);
            const title = document.getElementById(`modal-${cat.id}-title`);
            if (title) title.textContent = t(cat.titleKey);
            if (!list) return;
            list.innerHTML = cat.serviceIndices.map(i => {
                const s = services[i];
                if (!s) return '';
                const waUrl = getServiceWhatsAppUrl(s.name);
                return `
                    <div class="service-modal-item" role="button" tabindex="0" aria-expanded="false">
                        <div class="service-modal-item-icon">
                            <i class="${ICON_MAP[SERVICE_ICONS[i]] || 'fa-solid fa-wrench'}" aria-hidden="true"></i>
                        </div>
                        <div class="service-modal-item-body">
                            <h4>${s.name}</h4>
                            <p>${s.description}</p>
                            <div class="contact-options">
                                <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn-contact wa">
                                    <i class="fa-brands fa-whatsapp" aria-hidden="true"></i> WhatsApp
                                </a>
                                <a href="tel:+${CONFIG.whatsapp}" class="btn-contact call">
                                    <i class="fa-solid fa-phone" aria-hidden="true"></i> Ligar
                                </a>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        });
    }

    function renderServiceCategories() {
        const grid = document.getElementById('services-categories');
        if (!grid) return;
        grid.innerHTML = SERVICE_CATEGORIES.map(cat => `
            <button type="button" class="category-card" data-category="${cat.id}" aria-haspopup="dialog">
                <div class="category-card-icon">
                    <i class="${ICON_MAP[cat.icon] || 'fa-solid fa-wrench'}" aria-hidden="true"></i>
                </div>
                <h3>${t(cat.titleKey)}</h3>
                <p>${t(cat.descKey)}</p>
                <span class="category-card-cta">${t('cat_view_services')} <i class="fa-solid fa-arrow-right" aria-hidden="true"></i></span>
            </button>
        `).join('');
        populateServiceModals();
    }

    function openServiceModal(categoryId) {
        const modal = document.getElementById(`modal-${categoryId}`);
        if (!modal) return;
        closeServiceModals();
        modal.classList.add('active');
        modal.removeAttribute('hidden');
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('modal-open');
    }

    function closeServiceModals() {
        document.querySelectorAll('.service-modal').forEach(modal => {
            modal.classList.remove('active');
            modal.setAttribute('hidden', '');
            modal.setAttribute('aria-hidden', 'true');
        });
        document.querySelectorAll('.service-modal-item.show-contacts').forEach(card => {
            card.classList.remove('show-contacts');
            card.setAttribute('aria-expanded', 'false');
        });
        document.body.classList.remove('modal-open');
    }

    function toggleServiceCardContacts(card) {
        const isOpen = card.classList.toggle('show-contacts');
        card.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }

    function setupServiceModals() {
        const categories = document.getElementById('services-categories');
        if (categories && !categories.dataset.bound) {
            categories.dataset.bound = 'true';
            categories.addEventListener('click', e => {
                const card = e.target.closest('[data-category]');
                if (card) openServiceModal(card.dataset.category);
            });
        }

        document.querySelectorAll('.service-modal').forEach(modal => {
            if (modal.dataset.bound) return;
            modal.dataset.bound = 'true';

            modal.addEventListener('click', e => {
                if (e.target === modal) closeServiceModals();
            });

            const dialog = modal.querySelector('.service-modal-dialog');
            if (dialog) {
                dialog.addEventListener('click', e => e.stopPropagation());
            }

            const list = modal.querySelector('.service-modal-list');
            if (list && !list.dataset.contactsBound) {
                list.dataset.contactsBound = 'true';
                list.addEventListener('click', e => {
                    if (e.target.closest('.btn-contact')) return;
                    const card = e.target.closest('.service-modal-item');
                    if (card) toggleServiceCardContacts(card);
                });
                list.addEventListener('keydown', e => {
                    if (e.key !== 'Enter' && e.key !== ' ') return;
                    const card = e.target.closest('.service-modal-item');
                    if (!card || e.target.closest('.btn-contact')) return;
                    e.preventDefault();
                    toggleServiceCardContacts(card);
                });
            }
        });

        document.querySelectorAll('[data-close-modal]').forEach(el => {
            if (el.dataset.bound) return;
            el.dataset.bound = 'true';
            el.addEventListener('click', e => {
                e.stopPropagation();
                closeServiceModals();
            });
        });

        if (!document.body.dataset.modalEscape) {
            document.body.dataset.modalEscape = 'true';
            document.addEventListener('keydown', e => {
                if (e.key === 'Escape') closeServiceModals();
            });
        }
    }

    function renderAdvantages() {
        const grid = document.getElementById('advantages-grid');
        if (!grid) return;
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
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                    spaceBetween: 30
                }
            }
        });
    }

    function renderTestimonials() {
        const wrapper = document.getElementById('testimonials-swiper-wrapper');
        const summary = document.getElementById('testimonials-summary');
        const link = document.getElementById('google-reviews-link');
        if (!wrapper) return;

        const lang = T[currentLang];
        const { googleReviews } = CONFIG;

        if (summary) {
            summary.innerHTML = `
                <div class="reviews-aggregate fade-in">
                    <span class="reviews-score">${googleReviews.rating.toFixed(1)}</span>
                    <div class="reviews-stars" aria-label="${googleReviews.rating} / 5">${renderStars(googleReviews.rating)}</div>
                    <span class="reviews-count">${lang.reviews_count}</span>
                    <span class="reviews-google" aria-hidden="true"><i class="fab fa-google"></i></span>
                </div>
            `;
        }

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

        if (link) {
            link.href = googleReviews.url;
            link.textContent = lang.view_google_reviews;
        }

        requestAnimationFrame(() => initReviewsSwiper());
    }

    function renderFAQ() {
        const list = document.getElementById('faq-list');
        if (!list) return;
        list.innerHTML = T[currentLang].faqs.map((f, i) => `
            <div class="faq-item fade-in">
                <button class="faq-question" aria-expanded="false" aria-controls="faq-answer-${i}">
                    ${f.question}
                    <i class="fa-solid fa-chevron-down"></i>
                </button>
                <div class="faq-answer" id="faq-answer-${i}">
                    <div class="faq-answer-inner">${f.answer}</div>
                </div>
            </div>
        `).join('');
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
        if (emailText) emailText.textContent = CONFIG.email;
        const addressText = document.getElementById('footer-address-text');
        if (addressText) addressText.textContent = CONFIG.address;
    }

    function renderFooterServices() {
        const list = document.getElementById('footer-services-list');
        if (!list) return;
        const services = T[currentLang].services || T.pt.services;
        list.innerHTML = services.map(s =>
            `<li><a href="#services">${s.name}</a></li>`
        ).join('');
    }

    function setupLinks() {
        const waNum = CONFIG.whatsapp;
        const waMsg = encodeURIComponent(t('wa_message'));

        ['header-phone', 'btn-call', 'cta-phone', 'footer-phone'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.href = `tel:${CONFIG.phone}`;
        });

        ['btn-quote', 'cta-quote'].forEach(id => {
            const el = document.getElementById(id);
            if (el) el.href = `https://wa.me/${waNum}?text=${waMsg}`;
        });

        const emailEl = document.getElementById('footer-email');
        if (emailEl) emailEl.href = `mailto:${CONFIG.email}`;

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
            const msg = (input && input.value.trim()) || t('wa_message');
            const url = `https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`;
            window.open(url, '_blank', 'noopener');
            if (input) input.value = '';
            widget.classList.remove('open');
        }

        btn.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); toggleChat(); });
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
        renderServiceCategories();
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
            const btn = e.target.closest('.lang-option');
            if (!btn) return;
            const lang = btn.dataset.lang;
            if (lang === currentLang) {
                setLangOpen(false);
                return;
            }
            dropdown.querySelectorAll('.lang-option').forEach(o => o.classList.remove('active'));
            btn.classList.add('active');
            const info = LANGS[lang];
            if (info) {
                flag.src = info.flag;
                label.textContent = info.label;
            }
            setLangOpen(false);
            applyLanguage(lang);
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

    function init() {
        applyLanguage('pt');
        setupFAQListeners();
        setupHeader();
        setupLangSwitcher();
        setupWhatsAppChat();
        setupServiceModals();
        const yearEl = document.getElementById('year');
        if (yearEl) yearEl.textContent = new Date().getFullYear();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
