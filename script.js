(() => {
    'use strict';

    let currentLang = 'pt';

    const CONFIG = {
        phone: '+351 932504112',
        phone_display: '932 504 112',
        whatsapp: '351932504112',
        email: 'geral@fazdetudo.pt',
        address: 'Lisboa, Portugal'
    };

    const SERVICE_ICONS = [
        'paint-roller', 'faucet-drip', 'bolt', 'hammer', 'screwdriver-wrench',
        'gear', 'broom', 'leaf', 'truck', 'laptop', 'lock', 'temperature-half',
        'house-chimney', 'blinds', 'couch', 'water-ladder'
    ];

    const ADVANTAGE_ICONS = ['award', 'shield-halved', 'clock', 'euro-sign'];

    const LANGS = {
        pt: { label: 'Português', flag: 'https://flagcdn.com/w20/pt.png' },
        en: { label: 'English', flag: 'https://flagcdn.com/w20/gb.png' },
        es: { label: 'Español', flag: 'https://flagcdn.com/w20/es.png' },
        fr: { label: 'Français', flag: 'https://flagcdn.com/w20/fr.png' },
        de: { label: 'Deutsch', flag: 'https://flagcdn.com/w20/de.png' },
        nl: { label: 'Nederlands', flag: 'https://flagcdn.com/w20/nl.png' },
        it: { label: 'Italiano', flag: 'https://flagcdn.com/w20/it.png' },
        ru: { label: 'Русский', flag: 'https://flagcdn.com/w20/ru.png' }
    };

    const ICON_MAP = {
        'paint-roller': 'fa-solid fa-paint-roller',
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
            services: [
                { name: 'Pinturas', description: 'Interior e exterior. Preparação de superfícies, primários e acabamentos de qualidade.' },
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
            testimonials_title: 'O que dizem os nossos clientes',
            testimonials: [
                { text: 'Excelente serviço! Pintaram toda a minha casa em tempo recorde e com uma qualidade impecável. Recomendo vivamente.', name: 'Maria Santos', location: 'Lisboa' },
                { text: 'Muito profissionais e de confiança. Resolveram vários problemas de canalização numa só visita. Óptima comunicação.', name: 'João Silva', location: 'Sintra' },
                { text: 'Trabalho impecável na instalação elétrica do meu apartamento. Preços justos e muito profissionais.', name: 'António Ferreira', location: 'Cascais' }
            ],
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
            services: [
                { name: 'Painting', description: 'Interior and exterior. Surface preparation, primers and quality finishes.' },
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
            testimonials_title: 'What our clients say',
            testimonials: [
                { text: 'Excellent service! They painted my entire house in record time and with impeccable quality. Highly recommend.', name: 'Maria Santos', location: 'Lisbon' },
                { text: 'Very professional and reliable. Fixed multiple plumbing issues in one visit. Great communication.', name: 'João Silva', location: 'Sintra' },
                { text: 'Impeccable work on the electrical installation of my apartment. Fair prices and very professional.', name: 'António Ferreira', location: 'Cascais' }
            ],
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
            services: [
                { name: 'Pinturas', description: 'Interior y exterior. Preparación de superficies, imprimaciones y acabados de calidad.' },
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
            testimonials_title: 'Lo que dicen nuestros clientes',
            testimonials: [
                { text: '¡Excelente servicio! Pintaron toda mi casa en tiempo récord y con una calidad impecable. Lo recomiendo encarecidamente.', name: 'Maria Santos', location: 'Lisboa' },
                { text: 'Muy profesionales y de confianza. Resolvieron varios problemas de fontanería en una sola visita. Excelente comunicación.', name: 'João Silva', location: 'Sintra' },
                { text: 'Trabajo impecable en la instalación eléctrica de mi apartamento. Precios justos y muy profesionales.', name: 'António Ferreira', location: 'Cascais' }
            ],
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
            services: [
                { name: 'Peinture', description: 'Intérieur et extérieur. Préparation des surfaces, apprêts et finitions de qualité.' },
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
            testimonials_title: 'Ce que disent nos clients',
            testimonials: [
                { text: 'Excellent service ! Ils ont peint toute ma maison en un temps record et avec une qualité impeccable. Je recommande vivement.', name: 'Maria Santos', location: 'Lisbonne' },
                { text: 'Très professionnels et fiables. Ont résolu plusieurs problèmes de plomberie en une seule visite. Excellente communication.', name: 'João Silva', location: 'Sintra' },
                { text: 'Travail impeccable sur l\'installation électrique de mon appartement. Prix justes et très professionnels.', name: 'António Ferreira', location: 'Cascais' }
            ],
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
            footer_rights: 'Faz de Tudo PT. Tous droits réservés.',
            wa_message: 'Bonjour ! Je souhaiterais demander un devis.',
            wa_greeting: 'Comment puis-je vous aider ?',
            wa_placeholder: 'Écrivez un message...'
        },
        de: {
            nav_home: 'Startseite', nav_services: 'Dienstleistungen', nav_about: 'Über uns', nav_contact: 'Kontakt',
            footer_links: 'Links',
            hero_title: 'Ihr zuverlässiger Handwerker in Portugal',
            hero_subtitle: 'Malerarbeiten, Sanitär, Elektrik, Schreinerei und vieles mehr. Professioneller Service mit Qualitätsgarantie.',
            hero_btn_quote: 'Kostenloses Angebot',
            hero_btn_call: 'Jetzt anrufen',
            services_title: 'Unsere Dienstleistungen',
            services_subtitle: 'Komplettlösungen für Ihr Zuhause oder Büro',
            services: [
                { name: 'Malerarbeiten', description: 'Innen und außen. Oberflächenvorbereitung, Grundierungen und hochwertige Anstriche.' },
                { name: 'Sanitär', description: 'Leckreparatur, Installation von Armaturen, Toiletten und Wassersystemen.' },
                { name: 'Elektrik', description: 'Elektroinstallationen, Steckdosen, Beleuchtung und Schaltschränke.' },
                { name: 'Schreinerei', description: 'Möbelmontage, Tür- und Fensterreparatur, Holzarbeiten.' },
                { name: 'Allgemeine Reparaturen', description: 'Kleine und große Reparaturen für ein perfektes Zuhause.' },
                { name: 'Wartung', description: 'Vorbeugende Wartungsdienste für Immobilien und Wohnanlagen.' },
                { name: 'Reinigung', description: 'Haushalts-, Nachrenovierungs-, Büro- und Gewerbereinigung.' },
                { name: 'Gartenarbeit', description: 'Gartenpflege, Baumschnitt und Bewässerungssysteme.' },
                { name: 'Umzüge', description: 'Privat- und Gewerbeumzüge. Transport, Verpackung und Montage.' },
                { name: 'IT-Services', description: 'Computerreparatur, WLAN-Netzwerke und Smart Home.' },
                { name: 'Schlosserei', description: 'Schlösser, Tore, Gitter, Aluminium und Notöffnung von Türen.' },
                { name: 'Klimaanlagen', description: 'Installation, Wartung und Reparatur von Klimaanlagen und Heizungen.' },
                { name: 'Renovierungen', description: 'Küchen-, Bad-, Boden-Renovierungen und allgemeine Bauarbeiten.' },
                { name: 'Rollläden & Jalousien', description: 'Reparatur und Installation von Rollläden, Jalousien, Insektenschutz und Markisen.' },
                { name: 'Inneneinrichtung', description: 'Vorhänge, Tapeten, dekorative Beleuchtung, Zierleisten und Home Staging.' },
                { name: 'Schwimmbäder', description: 'Reinigung, Wartung und Reparatur von Pools. Wasseraufbereitung, Filter, Pumpen und Auskleidungen.' }
            ],
            advantages_title: 'Warum uns wählen?',
            advantages: [
                { name: 'Bewährte Erfahrung', description: 'Über 5 Jahre Erfahrung mit Professionalität und Engagement.' },
                { name: 'Garantierte Qualität', description: 'Garantie auf alle durchgeführten Arbeiten. Zufriedenheit gesichert.' },
                { name: 'Schnelle Antwort', description: 'Angebote innerhalb von 24h. Verfügbarkeit für Notfälle.' },
                { name: 'Faire Preise', description: 'Transparente Angebote ohne Überraschungen. Bestes Preis-Leistungs-Verhältnis.' }
            ],
            testimonials_title: 'Was unsere Kunden sagen',
            testimonials: [
                { text: 'Hervorragender Service! Sie haben mein ganzes Haus in Rekordzeit und mit tadelloser Qualität gestrichen. Sehr empfehlenswert.', name: 'Maria Santos', location: 'Lissabon' },
                { text: 'Sehr professionell und zuverlässig. Haben mehrere Sanitärprobleme in einem Besuch gelöst. Hervorragende Kommunikation.', name: 'João Silva', location: 'Sintra' },
                { text: 'Tadellose Arbeit bei der Elektroinstallation meiner Wohnung. Faire Preise und sehr professionell.', name: 'António Ferreira', location: 'Cascais' }
            ],
            faq_title: 'Häufig gestellte Fragen',
            faqs: [
                { question: 'Welche Handwerker-Dienste bieten Sie an?', answer: 'Wir bieten ein breites Spektrum an Dienstleistungen an: Malerarbeiten, Sanitär, Elektrik, Schreinerei, allgemeine Reparaturen, Wartung, Reinigung, Gartenarbeit, Umzüge, IT, Schlosserei, Klimaanlagen, Renovierungen, Rollläden und Jalousien, Inneneinrichtung und Schwimmbäder.' },
                { question: 'Wie lange dauert es, ein Angebot zu erhalten?', answer: 'Normalerweise antworten wir innerhalb von 24 Stunden mit einem Angebot. Bei dringenden Situationen bemühen wir uns, noch am selben Tag zu antworten.' },
                { question: 'Sind Ihre Fachkräfte zertifiziert?', answer: 'Ja, alle unsere Fachkräfte sind qualifiziert und besitzen die notwendigen Zertifizierungen für sichere und qualitativ hochwertige Arbeit.' },
                { question: 'Arbeiten Sie am Wochenende?', answer: 'Ja, wir arbeiten samstags nach Vereinbarung. Für Notfälle sind wir auch sonntags und an Feiertagen verfügbar.' },
                { question: 'Bieten Sie Garantie auf durchgeführte Arbeiten?', answer: 'Ja, wir bieten Garantie auf alle durchgeführten Arbeiten. Die Garantiezeit variiert je nach Art der Dienstleistung.' },
                { question: 'Was ist Ihr Einzugsgebiet?', answer: 'Wir decken den gesamten Großraum Lissabon und Umgebung ab, einschließlich Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas und weitere Orte.' }
            ],
            contact_title: 'Kontaktieren Sie uns',
            contact_subtitle: 'Wir sind bereit zu helfen. Fordern Sie Ihr kostenloses Angebot an.',
            footer_rights: 'Faz de Tudo PT. Alle Rechte vorbehalten.',
            wa_message: 'Hallo! Ich möchte ein Angebot anfordern.',
            wa_greeting: 'Wie kann ich Ihnen helfen?',
            wa_placeholder: 'Schreiben Sie eine Nachricht...'
        },
        nl: {
            nav_home: 'Home', nav_services: 'Diensten', nav_about: 'Over ons', nav_contact: 'Contact',
            footer_links: 'Links',
            hero_title: 'Uw betrouwbare klusjesman in Portugal',
            hero_subtitle: 'Schilderwerk, loodgieterij, elektriciteit, timmerwerk en nog veel meer. Professionele service met kwaliteitsgarantie.',
            hero_btn_quote: 'Gratis offerte aanvragen',
            hero_btn_call: 'Bel nu',
            services_title: 'Onze diensten',
            services_subtitle: 'Complete oplossingen voor uw huis of kantoor',
            services: [
                { name: 'Schilderwerk', description: 'Binnen en buiten. Oppervlaktevoorbereiding, primers en kwaliteitsafwerkingen.' },
                { name: 'Loodgieterij', description: 'Lekreparatie, installatie van kranen, toiletten en watersystemen.' },
                { name: 'Elektriciteit', description: 'Elektrische installaties, stopcontacten, verlichting en schakelkasten.' },
                { name: 'Timmerwerk', description: 'Meubelmontage, reparatie van deuren, ramen en houtwerk.' },
                { name: 'Algemene reparaties', description: 'Kleine en grote reparaties om uw huis in perfecte staat te houden.' },
                { name: 'Onderhoud', description: 'Preventieve onderhoudsdiensten voor woningen en appartementen.' },
                { name: 'Schoonmaak', description: 'Huishoudelijke, na-bouw, kantoor- en commerciële ruimtereiniging.' },
                { name: 'Tuinieren', description: 'Tuinonderhoud, boomsnoeien en irrigatiesystemen.' },
                { name: 'Verhuizingen', description: 'Residentiële en commerciële verhuizingen. Transport, verpakking en montage.' },
                { name: 'IT-diensten', description: 'Computerreparatie, Wi-Fi-netwerken en smart home.' },
                { name: 'Slotenmakerij', description: 'Sloten, poorten, hekken, aluminium en noodopening van deuren.' },
                { name: 'Airconditioning', description: 'Installatie, onderhoud en reparatie van airconditioning en verwarming.' },
                { name: 'Renovaties', description: 'Renovatie van keukens, badkamers, vloeren en algemene bouwwerken.' },
                { name: 'Rolluiken & zonwering', description: 'Reparatie en installatie van rolluiken, jaloezieën, horren en luifels.' },
                { name: 'Interieurontwerp', description: 'Gordijnen, behang, decoratieve verlichting, lijsten en home staging.' },
                { name: 'Zwembaden', description: 'Reiniging, onderhoud en reparatie van zwembaden. Waterbehandeling, filters, pompen en bekleding.' }
            ],
            advantages_title: 'Waarom ons kiezen?',
            advantages: [
                { name: 'Bewezen ervaring', description: 'Meer dan 5 jaar ervaring met professionaliteit en toewijding.' },
                { name: 'Gegarandeerde kwaliteit', description: 'Garantie op alle uitgevoerde werkzaamheden. Tevredenheid verzekerd.' },
                { name: 'Snelle reactie', description: 'Offertes binnen 24 uur. Beschikbaar voor noodgevallen.' },
                { name: 'Eerlijke prijzen', description: 'Transparante offertes zonder verrassingen. Beste prijs-kwaliteitverhouding.' }
            ],
            testimonials_title: 'Wat onze klanten zeggen',
            testimonials: [
                { text: 'Uitstekende service! Ze hebben mijn hele huis in recordtijd en met onberispelijke kwaliteit geschilderd. Sterk aanbevolen.', name: 'Maria Santos', location: 'Lissabon' },
                { text: 'Zeer professioneel en betrouwbaar. Hebben meerdere loodgietersproblemen in één bezoek opgelost. Uitstekende communicatie.', name: 'João Silva', location: 'Sintra' },
                { text: 'Onberispelijk werk aan de elektrische installatie van mijn appartement. Eerlijke prijzen en zeer professioneel.', name: 'António Ferreira', location: 'Cascais' }
            ],
            faq_title: 'Veelgestelde Vragen',
            faqs: [
                { question: 'Welke klusjesdiensten bieden jullie aan?', answer: 'Wij bieden een breed scala aan diensten aan, waaronder schilderwerk, loodgieterij, elektriciteit, timmerwerk, algemene reparaties, onderhoud, schoonmaak, tuinieren, verhuizingen, IT, slotenmakerij, airconditioning, renovaties, rolluiken en zonwering, interieurontwerp en zwembaden.' },
                { question: 'Hoe lang duurt het om een offerte te ontvangen?', answer: 'Normaal gesproken reageren we binnen 24 uur met een offerte. Bij urgente situaties doen we ons best om dezelfde dag te reageren.' },
                { question: 'Zijn uw vakmensen gecertificeerd?', answer: 'Ja, al onze vakmensen zijn gekwalificeerd en beschikken over de nodige certificeringen om veilig en kwalitatief werk te leveren.' },
                { question: 'Werken jullie in het weekend?', answer: 'Ja, we werken op zaterdag op afspraak. Voor noodgevallen zijn we ook op zondag en feestdagen beschikbaar.' },
                { question: 'Bieden jullie garantie op uitgevoerd werk?', answer: 'Ja, we bieden garantie op alle uitgevoerde werkzaamheden. De garantieperiode varieert afhankelijk van het type dienst.' },
                { question: 'Wat is uw dekkingsgebied?', answer: 'We dekken de hele regio Groot-Lissabon en omgeving, inclusief Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas en andere locaties.' }
            ],
            contact_title: 'Neem contact op',
            contact_subtitle: 'We staan klaar om te helpen. Vraag uw gratis offerte aan.',
            footer_rights: 'Faz de Tudo PT. Alle rechten voorbehouden.',
            wa_message: 'Hallo! Ik zou graag een offerte aanvragen.',
            wa_greeting: 'Hoe kan ik u helpen?',
            wa_placeholder: 'Schrijf een bericht...'
        },
        it: {
            nav_home: 'Home', nav_services: 'Servizi', nav_about: 'Chi siamo', nav_contact: 'Contatto',
            footer_links: 'Link',
            hero_title: 'Il vostro tuttofare di fiducia in Portogallo',
            hero_subtitle: 'Pittura, idraulica, elettricità, falegnameria e molto altro. Servizio professionale con garanzia di qualità.',
            hero_btn_quote: 'Preventivo gratuito',
            hero_btn_call: 'Chiama ora',
            services_title: 'I nostri servizi',
            services_subtitle: 'Soluzioni complete per la vostra casa o ufficio',
            services: [
                { name: 'Pittura', description: 'Interni ed esterni. Preparazione superfici, primer e finiture di qualità.' },
                { name: 'Idraulica', description: 'Riparazione perdite, installazione rubinetti, sanitari e impianti idrici.' },
                { name: 'Elettricità', description: 'Impianti elettrici, prese, illuminazione e quadri elettrici.' },
                { name: 'Falegnameria', description: 'Montaggio mobili, riparazione porte, finestre e lavori in legno.' },
                { name: 'Riparazioni generali', description: 'Piccole e grandi riparazioni per mantenere la casa in perfette condizioni.' },
                { name: 'Manutenzione', description: 'Servizi di manutenzione preventiva per proprietà e condomini.' },
                { name: 'Pulizia', description: 'Pulizia domestica, post-ristrutturazione, uffici e spazi commerciali.' },
                { name: 'Giardinaggio', description: 'Manutenzione giardini, potatura alberi e sistemi di irrigazione.' },
                { name: 'Traslochi', description: 'Traslochi residenziali e commerciali. Trasporto, imballaggio e montaggio.' },
                { name: 'Informatica', description: 'Riparazione computer, reti Wi-Fi e smart home.' },
                { name: 'Fabbro', description: 'Serrature, cancelli, grate, alluminio e apertura porte urgente.' },
                { name: 'Climatizzazione', description: 'Installazione, manutenzione e riparazione di condizionatori e riscaldamento.' },
                { name: 'Ristrutturazioni', description: 'Ristrutturazione cucine, bagni, pavimenti e lavori generali.' },
                { name: 'Tapparelle e persiane', description: 'Riparazione e installazione di tapparelle, persiane, zanzariere e tende da sole.' },
                { name: 'Design d\'interni', description: 'Tende, carta da parati, illuminazione decorativa, cornici e home staging.' },
                { name: 'Piscine', description: 'Pulizia, manutenzione e riparazione di piscine. Trattamento acqua, filtri, pompe e rivestimenti.' }
            ],
            advantages_title: 'Perché sceglierci?',
            advantages: [
                { name: 'Esperienza comprovata', description: 'Oltre 5 anni di esperienza con professionalità e dedizione.' },
                { name: 'Qualità garantita', description: 'Garanzia su tutti i lavori eseguiti. Soddisfazione assicurata.' },
                { name: 'Risposta rapida', description: 'Preventivi entro 24h. Disponibilità per le urgenze.' },
                { name: 'Prezzi giusti', description: 'Preventivi trasparenti senza sorprese. Miglior rapporto qualità-prezzo.' }
            ],
            testimonials_title: 'Cosa dicono i nostri clienti',
            testimonials: [
                { text: 'Servizio eccellente! Hanno dipinto tutta la mia casa in tempi record e con qualità impeccabile. Lo consiglio vivamente.', name: 'Maria Santos', location: 'Lisbona' },
                { text: 'Molto professionali e affidabili. Hanno risolto diversi problemi idraulici in una sola visita. Ottima comunicazione.', name: 'João Silva', location: 'Sintra' },
                { text: 'Lavoro impeccabile sull\'impianto elettrico del mio appartamento. Prezzi giusti e molto professionali.', name: 'António Ferreira', location: 'Cascais' }
            ],
            faq_title: 'Domande Frequenti',
            faqs: [
                { question: 'Quali servizi di tuttofare offrite?', answer: 'Offriamo un\'ampia gamma di servizi tra cui pittura, idraulica, elettricità, falegnameria, riparazioni generali, manutenzione, pulizia, giardinaggio, traslochi, informatica, fabbro, climatizzazione, ristrutturazioni, tapparelle e persiane, design d\'interni e piscine.' },
                { question: 'Quanto tempo ci vuole per ricevere un preventivo?', answer: 'Di solito rispondiamo con un preventivo entro 24 ore dal primo contatto. Per situazioni urgenti, facciamo il possibile per rispondere in giornata.' },
                { question: 'I vostri professionisti sono certificati?', answer: 'Sì, tutti i nostri professionisti sono qualificati e possiedono le certificazioni necessarie per eseguire i lavori in sicurezza e con qualità.' },
                { question: 'Lavorate nei fine settimana?', answer: 'Sì, lavoriamo il sabato su appuntamento. Per le emergenze, siamo disponibili anche la domenica e nei giorni festivi.' },
                { question: 'Offrite garanzia sui lavori eseguiti?', answer: 'Sì, offriamo garanzia su tutti i lavori eseguiti. Il periodo di garanzia varia in base al tipo di servizio.' },
                { question: 'Qual è la vostra area di copertura?', answer: 'Copriamo tutta la zona della Grande Lisbona e dintorni, inclusi Cascais, Sintra, Oeiras, Amadora, Loures, Almada, Odivelas e altre località.' }
            ],
            contact_title: 'Contattateci',
            contact_subtitle: 'Siamo pronti ad aiutarvi. Richiedete il vostro preventivo gratuito.',
            footer_rights: 'Faz de Tudo PT. Tutti i diritti riservati.',
            wa_message: 'Ciao! Vorrei richiedere un preventivo.',
            wa_greeting: 'Come posso aiutarla?',
            wa_placeholder: 'Scrivi un messaggio...'
        },
        ru: {
            nav_home: 'Главная', nav_services: 'Услуги', nav_about: 'О нас', nav_contact: 'Контакт',
            footer_links: 'Ссылки',
            hero_title: 'Ваш надёжный мастер в Португалии',
            hero_subtitle: 'Покраска, сантехника, электрика, столярные работы и многое другое. Профессиональный сервис с гарантией качества.',
            hero_btn_quote: 'Бесплатная смета',
            hero_btn_call: 'Позвонить',
            services_title: 'Наши услуги',
            services_subtitle: 'Комплексные решения для вашего дома или офиса',
            services: [
                { name: 'Покраска', description: 'Внутренние и наружные работы. Подготовка поверхностей, грунтовки и качественная отделка.' },
                { name: 'Сантехника', description: 'Ремонт протечек, установка кранов, унитазов и систем водоснабжения.' },
                { name: 'Электрика', description: 'Электромонтаж, розетки, освещение и электрощиты.' },
                { name: 'Столярные работы', description: 'Сборка мебели, ремонт дверей, окон и работы по дереву.' },
                { name: 'Общий ремонт', description: 'Мелкий и крупный ремонт для поддержания дома в идеальном состоянии.' },
                { name: 'Техобслуживание', description: 'Профилактическое обслуживание объектов недвижимости и кондоминиумов.' },
                { name: 'Уборка', description: 'Домашняя уборка, послестроительная, офисов и коммерческих помещений.' },
                { name: 'Садоводство', description: 'Уход за садом, обрезка деревьев и системы полива.' },
                { name: 'Переезды', description: 'Жилые и коммерческие переезды. Транспортировка, упаковка и сборка.' },
                { name: 'IT-услуги', description: 'Ремонт компьютеров, сети Wi-Fi и умный дом.' },
                { name: 'Слесарные работы', description: 'Замки, ворота, решётки, алюминий и аварийное вскрытие дверей.' },
                { name: 'Кондиционирование', description: 'Установка, обслуживание и ремонт кондиционеров и отопления.' },
                { name: 'Ремонт помещений', description: 'Ремонт кухонь, ванных комнат, полов и общие строительные работы.' },
                { name: 'Жалюзи и ставни', description: 'Ремонт и установка жалюзи, ставней, москитных сеток и навесов.' },
                { name: 'Дизайн интерьера', description: 'Шторы, обои, декоративное освещение, молдинги и хоум-стейджинг.' },
                { name: 'Бассейны', description: 'Чистка, обслуживание и ремонт бассейнов. Обработка воды, фильтры, насосы и облицовка.' }
            ],
            advantages_title: 'Почему выбирают нас?',
            advantages: [
                { name: 'Проверенный опыт', description: 'Более 5 лет опыта с профессионализмом и преданностью делу.' },
                { name: 'Гарантия качества', description: 'Гарантия на все выполненные работы. Удовлетворение обеспечено.' },
                { name: 'Быстрый ответ', description: 'Сметы в течение 24ч. Доступность для экстренных случаев.' },
                { name: 'Справедливые цены', description: 'Прозрачные сметы без сюрпризов. Лучшее соотношение цены и качества.' }
            ],
            testimonials_title: 'Что говорят наши клиенты',
            testimonials: [
                { text: 'Отличный сервис! Покрасили весь мой дом в рекордные сроки и с безупречным качеством. Настоятельно рекомендую.', name: 'Maria Santos', location: 'Лиссабон' },
                { text: 'Очень профессиональные и надёжные. Решили несколько проблем с сантехникой за один визит. Отличная коммуникация.', name: 'João Silva', location: 'Синтра' },
                { text: 'Безупречная работа по электромонтажу в моей квартире. Справедливые цены и очень профессионально.', name: 'António Ferreira', location: 'Кашкайш' }
            ],
            faq_title: 'Часто задаваемые вопросы',
            faqs: [
                { question: 'Какие услуги мастера вы предлагаете?', answer: 'Мы предлагаем широкий спектр услуг: покраска, сантехника, электрика, столярные работы, общий ремонт, техобслуживание, уборка, садоводство, переезды, IT, слесарные работы, кондиционирование, ремонт помещений, жалюзи и ставни, дизайн интерьера и бассейны.' },
                { question: 'Сколько времени занимает получение сметы?', answer: 'Обычно мы отвечаем со сметой в течение 24 часов после первого обращения. В срочных ситуациях стараемся ответить в тот же день.' },
                { question: 'Ваши специалисты сертифицированы?', answer: 'Да, все наши специалисты квалифицированы и имеют необходимые сертификаты для безопасного и качественного выполнения работ.' },
                { question: 'Работаете ли вы по выходным?', answer: 'Да, мы работаем по субботам по предварительной записи. В экстренных случаях доступны по воскресеньям и праздникам.' },
                { question: 'Предоставляете ли вы гарантию на выполненные работы?', answer: 'Да, мы предоставляем гарантию на все выполненные работы. Срок гарантии зависит от типа услуги.' },
                { question: 'Какова ваша зона обслуживания?', answer: 'Мы обслуживаем весь район Большого Лиссабона и окрестности, включая Кашкайш, Синтру, Оэйраш, Амадору, Лоуреш, Алмаду, Одивелаш и другие населённые пункты.' }
            ],
            contact_title: 'Свяжитесь с нами',
            contact_subtitle: 'Мы готовы помочь. Запросите бесплатную смету.',
            footer_rights: 'Faz de Tudo PT. Все права защищены.',
            wa_message: 'Здравствуйте! Хотел бы запросить смету.',
            wa_greeting: 'Чем могу помочь?',
            wa_placeholder: 'Напишите сообщение...'
        }
    };

    function t(key) { return T[currentLang][key] || T.pt[key] || ''; }

    function renderServices() {
        const grid = document.getElementById('services-grid');
        if (!grid) return;
        const services = T[currentLang].services;
        grid.innerHTML = services.map((s, i) => `
            <div class="service-card fade-in">
                <div class="service-icon">
                    <i class="${ICON_MAP[SERVICE_ICONS[i]] || 'fa-solid fa-wrench'}"></i>
                </div>
                <h3>${s.name}</h3>
                <p>${s.description}</p>
            </div>
        `).join('');
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

    function renderTestimonials() {
        const grid = document.getElementById('testimonials-grid');
        if (!grid) return;
        grid.innerHTML = T[currentLang].testimonials.map(tm => {
            const initials = tm.name.split(' ').map(w => w[0]).join('').slice(0, 2);
            return `
                <div class="testimonial-card fade-in">
                    <p class="testimonial-text">${tm.text}</p>
                    <div class="testimonial-author">
                        <div class="testimonial-avatar">${initials}</div>
                        <div class="testimonial-info">
                            <strong>${tm.name}</strong>
                            <span>${tm.location}</span>
                        </div>
                    </div>
                </div>
            `;
        }).join('');
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
        renderServices();
        renderFooterServices();
        renderAdvantages();
        renderTestimonials();
        renderFAQ();
        renderFAQSchema();
        setupLinks();
        requestAnimationFrame(() => setupScrollAnimations());
    }

    function setupLangSwitcher() {
        const toggle = document.getElementById('lang-toggle');
        const dropdown = document.getElementById('lang-dropdown');
        const flag = document.getElementById('lang-flag');
        const label = document.getElementById('lang-label');
        if (!toggle || !dropdown) return;

        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            const isOpen = dropdown.classList.contains('open');
            dropdown.classList.toggle('open', !isOpen);
            toggle.classList.toggle('open', !isOpen);
            toggle.setAttribute('aria-expanded', !isOpen);
        });

        dropdown.addEventListener('click', (e) => {
            const btn = e.target.closest('.lang-option');
            if (!btn) return;
            const lang = btn.dataset.lang;
            if (lang === currentLang) {
                dropdown.classList.remove('open');
                toggle.classList.remove('open');
                return;
            }
            dropdown.querySelectorAll('.lang-option').forEach(o => o.classList.remove('active'));
            btn.classList.add('active');
            const info = LANGS[lang];
            if (info) { flag.src = info.flag; label.textContent = info.label; }
            dropdown.classList.remove('open');
            toggle.classList.remove('open');
            toggle.setAttribute('aria-expanded', 'false');
            applyLanguage(lang);
        });

        document.addEventListener('click', () => {
            dropdown.classList.remove('open');
            toggle.classList.remove('open');
            toggle.setAttribute('aria-expanded', 'false');
        });
    }

    function setupHeader() {
        const header = document.getElementById('header');
        const toggle = document.getElementById('menu-toggle');
        const nav = document.getElementById('nav');
        window.addEventListener('scroll', () => header.classList.toggle('scrolled', window.scrollY > 20));
        toggle.addEventListener('click', () => { toggle.classList.toggle('active'); nav.classList.toggle('active'); });
        nav.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => { toggle.classList.remove('active'); nav.classList.remove('active'); });
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
        const yearEl = document.getElementById('year');
        if (yearEl) yearEl.textContent = new Date().getFullYear();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
