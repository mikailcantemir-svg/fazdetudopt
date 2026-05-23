#!/usr/bin/env python3
"""Generate SEO service landing pages from the Faz de Tudo PT template."""
# NOTA: servico-recuperar-casa.html foi adicionado manualmente; não regenerar com este script antigo (*-lisboa.html).

from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent

# slug, service_name, h1_title, meta_description, detail_html (inner HTML for "O que fazemos")
SERVICES = [
    (
        "pinturas-lisboa.html",
        "Pinturas",
        "Pinturas Interiores e Exteriores Profissionais",
        "Precisa de pintores em Lisboa? Pintura interior e exterior com preparação de superfícies, primários e acabamentos duradouros. Orçamento grátis!",
        "<p>Executamos pintura de paredes, tetos, portas e caixilharias com materiais de qualidade, proteção do mobiliário e acabamentos uniformes. Tratamos humidades pontuais, fissuras e lixagem antes da aplicação das tintas adequadas a cada divisão.</p>",
    ),
    (
        "pintura-fachadas-alpinismo-lisboa.html",
        "Pintura de Fachadas em Alpinismo",
        "Pintura de Fachadas e Prédios em Alpinismo Industrial",
        "Pintura de fachadas com alpinismo industrial em Lisboa, Cascais e Setúbal. Sem andaimes, mais rápido e económico. Orçamento grátis!",
        """<p>Especializamo-nos em <strong>alpinismo industrial (trabalho em cordas)</strong> para pintura, impermeabilização e reabilitação de fachadas sem montagem de andaimes.</p>
        <ul>
            <li><strong>Poupança de até 40%</strong> face a soluções tradicionais com estruturas fixas.</li>
            <li><strong>Rapidez:</strong> acesso a qualquer zona do edifício no próprio dia.</li>
            <li><strong>Segurança:</strong> menos incómodo para moradores e menor risco de acessos indevidos.</li>
        </ul>
        <p>Tratamos fissuras, lavagem de alta pressão, primários e repintura completa em condomínios, moradias e edifícios comerciais expostos à maresia na linha de Cascais.</p>""",
    ),
    (
        "canalizacoes-lisboa.html",
        "Canalizações",
        "Canalizador e Serviços de Canalização Urgente",
        "Canalizador em Lisboa: fugas, desentupimentos, autoclismos, torneiras e sanitas. Atendimento rápido na Grande Lisboa. Orçamento grátis!",
        "<p>Reparamos fugas visíveis e ocultas, substituímos torneiras, sifões, autoclismos e tubagens danificadas. Realizamos desentupimentos de lavatórios, sanitas, cozinhas e ralos com equipamento adequado e diagnóstico preciso da origem do problema.</p>",
    ),
    (
        "eletricidade-lisboa.html",
        "Electricidade",
        "Eletricista Certificado para Casa e Negócio",
        "Eletricista em Lisboa: tomadas, iluminação, quadros eléctricos e avarias urgentes. Grande Lisboa e Margem Sul. Orçamento grátis!",
        "<p>Instalamos e reparamos circuitos, tomadas, interruptores, iluminação LED e quadros eléctricos. Resolvemos disjuntores a disparar, falhas de energia e atualizamos instalações antigas para maior segurança e conformidade.</p>",
    ),
    (
        "carpintaria-lisboa.html",
        "Carpintaria",
        "Carpintaria e Montagem de Móveis ao Domicílio",
        "Carpinteiro em Lisboa: montagem de móveis, portas, janelas e trabalhos em madeira. Serviço preciso com garantia. Orçamento grátis!",
        "<p>Montamos móveis modulados e por medida, ajustamos portas e janelas que raspam ou não fecham, colocamos puxadores, corrediças e reparamos estruturas em madeira interiores e exteriores.</p>",
    ),
    (
        "reparacoes-gerais-lisboa.html",
        "Reparações Gerais",
        "Reparações Gerais e Faz-Tudo ao Domicílio",
        "Handyman em Lisboa para reparações gerais na casa ou empresa. Uma equipa, várias soluções. Orçamento grátis na Grande Lisboa!",
        "<p>Somos o seu faz-tudo de confiança: fixação de prateleiras e TVs, pequenas reparações, selagem de juntas, ajustes diversos e lista de tarefas pendentes resolvida numa única visita.</p>",
    ),
    (
        "manutencao-lisboa.html",
        "Manutenção",
        "Manutenção Preventiva e Reparações para Condomínios",
        "Manutenção de edifícios e habitações em Lisboa: preventiva, reparações e lavagem de telhados e pátios. Orçamento grátis!",
        "<p>Planos de manutenção periódica para condomínios e particulares, inspeção de telhados, calhas, fachadas e zonas comuns, com intervenção rápida antes de pequenos problemas se tornarem obras caras.</p>",
    ),
    (
        "limpezas-lisboa.html",
        "Limpezas",
        "Limpezas Domésticas e Pós-Obra Profissionais",
        "Empresa de limpezas em Lisboa: doméstica, pós-obra, escritórios e espaços comerciais. Equipas experientes. Orçamento grátis!",
        "<p>Limpeza profunda ou de manutenção com produtos adequados a cada superfície. Pós-obra com remoção de pó de construção, resíduos e brilho final para entrega da casa ou loja pronta a habitar.</p>",
    ),
    (
        "jardinagem-lisboa.html",
        "Jardinagem",
        "Jardinagem e Manutenção de Jardins em Lisboa",
        "Jardinagem em Lisboa: poda, relva, rega e manutenção de espaços exteriores. Cascais, Sintra e Margem Sul. Orçamento grátis!",
        "<p>Poda de árvores e arbustos, corte de relva, tratamento de sebes, limpeza de terrenos e instalação ou reparação de sistemas de rega automática.</p>",
    ),
    (
        "mudancas-lisboa.html",
        "Mudanças",
        "Mudanças Residenciais e Comerciais com Embalagem",
        "Mudanças em Lisboa e Margem Sul: transporte, embalagem e montagem de mobília. Equipa cuidadosa. Orçamento grátis!",
        "<p>Organizamos mudanças completas ou parciais, com proteção de móveis, desmontagem e remontagem, transporte seguro e apoio na distribuição nos novos espaços.</p>",
    ),
    (
        "informatica-lisboa.html",
        "Informática",
        "Assistência Informática e Redes Wi-Fi ao Domicílio",
        "Informática em Lisboa: reparação de PCs, Wi-Fi, impressoras e smart home. Atendimento ao domicílio. Orçamento grátis!",
        "<p>Diagnosticamos computadores lentos ou infetados, configuramos redes Wi-Fi estáveis, impressoras em rede e dispositivos inteligentes para casa e pequenos escritórios.</p>",
    ),
    (
        "serralharia-lisboa.html",
        "Serralharia",
        "Serralharia e Abertura de Portas Urgente 24h",
        "Serralheiro em Lisboa: fechaduras, portões, grades e abertura de portas urgente. Grande Lisboa. Orçamento grátis!",
        "<p>Substituímos cilindros e fechaduras, reparamos portões e portas de garagem, instalamos grades e resolvemos situações de porta trancada com discrição e rapidez.</p>",
    ),
    (
        "climatizacao-lisboa.html",
        "Climatização",
        "Instalação e Reparação de Ar Condicionado (AVAC)",
        "AVAC e ar condicionado em Lisboa: instalação, manutenção e reparação. Aquecimento e climatização. Orçamento grátis!",
        "<p>Instalamos splits e multisplit, efetuamos cargas de gás, limpeza de filtros, reparação de avarias e manutenção preventiva para maior eficiência energética.</p>",
    ),
    (
        "remodelacoes-lisboa.html",
        "Remodelações",
        "Remodelações de Cozinhas, Casas de Banho e Obras Gerais",
        "Remodelações em Lisboa: cozinhas, casas de banho, pavimentos e obras por medida. Equipa completa. Orçamento grátis!",
        "<p>Coordenamos obras de remodelação com canalização, electricidade, revestimentos e acabamentos, com cronograma claro e orçamento transparente do início ao fim.</p>",
    ),
    (
        "reparacao-estores-lisboa.html",
        "Estores e Persianas",
        "Reparação e Instalação de Estores e Persianas",
        "Reparação de estores e persianas em Lisboa: fitas, motores, toldos e mosquiteiras. Serviço rápido. Orçamento grátis!",
        "<p>Substituímos fitas e lâminas, reparamos mecanismos, motores eléctricos e instalamos estores novos ou mosquiteiras em janelas e varandas.</p>",
    ),
    (
        "decoracao-interiores-lisboa.html",
        "Decoração de Interiores",
        "Decoração de Interiores e Home Staging",
        "Decoração de interiores em Lisboa: cortinas, papel de parede, iluminação e home staging. Orçamento grátis!",
        "<p>Apoiamos na escolha de cortinados, papel de parede, iluminação decorativa, molduras e pequenos detalhes que transformam a estética da sua casa ou imóvel para venda.</p>",
    ),
    (
        "manutencao-piscinas-lisboa.html",
        "Piscinas",
        "Manutenção e Limpeza de Piscinas Profissional",
        "Manutenção de piscinas em Lisboa e Margem Sul: tratamento de água, filtros, bombas e revestimentos. Orçamento grátis!",
        "<p>Limpeza regular, equilíbrio químico da água, revisão de filtros e bombas, deteção de fugas e reparação de revestimentos para piscinas sempre prontas a usar.</p>",
    ),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-PT">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{service_name} em Lisboa e Margem Sul | Faz de Tudo PT</title>
    <meta name="description" content="Precisa de especialistas em {service_name}? O Faz de Tudo oferece soluções rápidas com garantia na Grande Lisboa, Cascais e Setúbal. Peça já o seu orçamento grátis!">
    <link rel="canonical" href="https://www.fazdetudo.pt/{slug}">

    <meta property="og:title" content="{service_name} | Faz de Tudo PT">
    <meta property="og:description" content="{meta_description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.fazdetudo.pt/{slug}">
    <meta property="og:image" content="https://www.fazdetudo.pt/logo.png">

    <link rel="icon" type="image/png" href="/logo.png">
    <link rel="apple-touch-icon" href="/logo.png">

    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Service",
      "serviceType": "{service_name}",
      "description": "{meta_description}",
      "provider": {{
        "@type": "HomeAndConstructionBusiness",
        "name": "Faz de Tudo PT",
        "image": "https://www.fazdetudo.pt/logo.png",
        "telephone": "+351932504112",
        "priceRange": "$$",
        "address": {{
          "@type": "PostalAddress",
          "addressLocality": "Lisboa",
          "addressCountry": "PT"
        }}
      }},
      "areaServed": [
        {{ "@type": "AdministrativeArea", "name": "Lisboa" }},
        {{ "@type": "AdministrativeArea", "name": "Cascais" }},
        {{ "@type": "AdministrativeArea", "name": "Estoril" }},
        {{ "@type": "AdministrativeArea", "name": "Sintra" }},
        {{ "@type": "AdministrativeArea", "name": "Almada" }},
        {{ "@type": "AdministrativeArea", "name": "Setúbal" }}
      ]
    }}
    </script>
</head>
<body class="service-page">

    <header class="header scrolled" id="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <img src="logo.png" alt="Faz de Tudo PT" class="logo-img">
                <span class="logo-brand">
                    <span class="logo-text">fazdetudo<em>.pt</em></span>
                    <span class="logo-tagline">HANDYMAN</span>
                </span>
            </a>
            <div class="header-actions">
                <a href="index.html" class="service-page-back"><i class="fa-solid fa-arrow-left" aria-hidden="true"></i> <span>Voltar ao Início</span></a>
                <a href="tel:+351932504112" class="btn-phone" id="header-phone">
                    <i class="fa-solid fa-phone"></i>
                    <span>932 504 112</span>
                </a>
            </div>
        </div>
    </header>

    <main class="service-page-main service-page-main--article">
        <article class="container service-article">
            <header class="service-article-header">
                <h1 class="service-article-title">{h1_title}</h1>
                <p class="service-article-lead">Serviço profissional, rápido e com garantia de satisfação.</p>
            </header>

            <div class="service-rich-text">
                <p>Se procura uma solução fiável para <strong>{service_name}</strong>, a equipa do <strong>Faz de Tudo PT</strong> garante uma intervenção de excelência. Atuamos tanto em ambientes residenciais como comerciais, resolvendo desde pequenos arranjos a projetos de maior complexidade com total transparência e eficácia.</p>

                <h2>O que fazemos nesta área:</h2>
                {detail_html}

                <h2>Zonas de Atendimento na Grande Lisboa e Setúbal:</h2>
                <p>Deslocamo-nos rapidamente até à sua porta nas seguintes localizações:</p>
                <ul class="service-zones-grid">
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Lisboa</strong> (Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Loures e Odivelas</strong> (Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Sintra e Amadora</strong> (Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Cascais e Oeiras</strong> (Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Vila Franca de Xira</strong> (Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Margem Sul</strong> (Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Setúbal e Sesimbra</strong> (Azeitão, Palmela, Quinta do Anjo)</li>
                </ul>
            </div>

            <div class="service-cta-box">
                <h3>Precisa de assistência ou quer um orçamento gratuito?</h3>
                <p>Clique abaixo para falar diretamente com o nosso técnico especialista em {service_name}.</p>
                <div class="service-cta-box-actions">
                    <a href="https://wa.me/351932504112?text={wa_text}" class="btn btn-primary btn-lg" target="_blank" rel="noopener noreferrer">
                        <i class="fa-brands fa-whatsapp"></i> Orçamento por WhatsApp
                    </a>
                    <a href="tel:+351932504112" class="btn btn-outline btn-lg service-cta-call">
                        <i class="fa-solid fa-phone"></i> Ligar: 932 504 112
                    </a>
                </div>
            </div>
        </article>
    </main>

    <footer class="footer service-page-footer service-page-footer--brand">
        <div class="container">
            <p>&copy; 2026 Faz de Tudo PT. Todos os direitos reservados. Especialistas em Reparações ao Domicílio.</p>
        </div>
    </footer>

</body>
</html>
"""


def main():
    for slug, service_name, h1_title, meta_description, detail_html in SERVICES:
        path = ROOT / slug
        wa_text = quote(f"Olá! Gostaria de pedir um orçamento para {service_name}.", safe="")
        html = TEMPLATE.format(
            slug=slug,
            service_name=service_name,
            h1_title=h1_title,
            meta_description=meta_description,
            detail_html=detail_html,
            wa_text=wa_text,
        )
        path.write_text(html, encoding="utf-8")
        print(f"wrote {slug}")


if __name__ == "__main__":
    main()
