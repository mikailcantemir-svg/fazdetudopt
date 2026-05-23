#!/usr/bin/env python3
"""Generate servico-*.html landing pages from template-servico.html."""

import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "template-servico.html").read_text(encoding="utf-8")

SERVICES = [
    {
        "slug": "servico-pinturas.html",
        "service_name": "Pinturas",
        "page_title": "Pinturas Interiores e Exteriores em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Pinturas em Lisboa, Cascais e Setúbal: interiores, exteriores, primários e acabamentos profissionais. Orçamento grátis com a Faz de Tudo PT.",
        "h1": "Pinturas Interiores e Exteriores Profissionais",
        "wa_message": "Olá! Gostaria de pedir um orçamento para pinturas.",
        "body": """
                <p>Procura <strong>pintores em Lisboa</strong>, na <strong>Margem Sul</strong> ou em <strong>Cascais</strong>? A <strong>Faz de Tudo PT</strong> executa pintura residencial e comercial com planeamento, proteção de mobiliário e tintas adequadas a cada ambiente.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Trabalhamos em apartamentos, moradias, lojas e escritórios em Lisboa, Oeiras, Sintra, Almada e Setúbal. Preparamos superfícies com lixagem, tratamento de humidades pontuais, primários e duas demãos de acabamento quando necessário.</p>
                <p>Pintamos paredes, tetos, portas, rodapés e pequenas áreas exteriores, sempre com orçamento transparente antes de iniciar a obra.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-pintura-fachadas-alpinismo.html",
        "service_name": "Pintura de Fachadas em Alpinismo",
        "page_title": "Pintura de Fachadas em Alpinismo em Lisboa e Cascais | Faz de Tudo PT",
        "meta_description": "Pintura de fachadas com alpinismo industrial em Lisboa, Cascais e Setúbal. Sem andaimes, mais rápido e económico. Orçamento grátis Faz de Tudo PT.",
        "h1": "Pintura de Fachadas e Prédios em Alpinismo Industrial",
        "wa_message": "Olá! Gostaria de um orçamento para pintura de fachadas em alpinismo.",
        "body": """
                <p>A reabilitação de fachadas em <strong>Lisboa</strong>, <strong>Cascais</strong> e na <strong>Margem Sul</strong> não precisa de custos elevados com andaimes. Utilizamos <strong>alpinismo industrial (trabalho em cordas)</strong> para pintar, impermeabilizar e reparar edifícios com segurança.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Intervimos em condomínios, moradias e edifícios comerciais com lavagem de alta pressão, tratamento de fissuras, primários e repintura completa. A solução é especialmente vantajosa em zonas costeiras como Cascais e Estoril, expostas à maresia.</p>
                <ul>
                    <li><strong>Poupança de até 40%</strong> face a montagem de andaimes tradicionais.</li>
                    <li><strong>Rapidez:</strong> acesso a qualquer ponto do edifício no próprio dia.</li>
                    <li><strong>Segurança:</strong> menos estruturas fixas na fachada durante a noite.</li>
                </ul>
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
                </ul>""",
    },
    {
        "slug": "servico-canalizacoes.html",
        "service_name": "Canalizações",
        "page_title": "Canalizador e Canalizações Urgentes em Lisboa | Faz de Tudo PT",
        "meta_description": "Canalizador em Lisboa e Margem Sul: fugas, desentupimentos, autoclismos e torneiras. Atendimento rápido em Cascais e Setúbal. Orçamento grátis.",
        "h1": "Canalizador e Serviços de Canalização Urgente",
        "wa_message": "Olá! Gostaria de pedir um orçamento para canalizações.",
        "body": """
                <p>Problemas de água em casa ou no negócio exigem resposta imediata. Somos especialistas em <strong>canalizações em Lisboa</strong>, <strong>Setúbal</strong>, <strong>Almada</strong> e <strong>Cascais</strong>, com diagnóstico claro e reparação duradoura.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Reparamos fugas visíveis e ocultas, substituímos torneiras, sifões, autoclismos e troços de tubagem danificados. Efetuamos <strong>desentupimentos</strong> em lavatórios, sanitas, cozinhas e ralos com equipamento profissional.</p>
                <p>Atendemos urgências em apartamentos, moradias, restaurantes e escritórios em toda a Grande Lisboa e Margem Sul.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-electricidade.html",
        "service_name": "Electricidade",
        "page_title": "Eletricista em Lisboa, Cascais e Margem Sul | Faz de Tudo PT",
        "meta_description": "Eletricista em Lisboa e Setúbal: tomadas, iluminação, quadros eléctricos e avarias urgentes. Serviço certificado. Orçamento grátis.",
        "h1": "Eletricista Certificado para Casa e Negócio",
        "wa_message": "Olá! Gostaria de pedir um orçamento para electricidade.",
        "body": """
                <p>Precisa de um <strong>eletricista em Lisboa</strong>, na <strong>Margem Sul</strong> ou em <strong>Cascais</strong>? Resolvemos avarias, melhoramos a segurança da instalação e modernizamos a iluminação com orçamento claro.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Instalamos tomadas, interruptores, candeeiros e circuitos dedicados. Reparamos quadros eléctricos, disjuntores a disparar e falhas de energia. Atualizamos instalações antigas para maior fiabilidade em habitações e pequenos comércios.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-carpintaria.html",
        "service_name": "Carpintaria",
        "page_title": "Carpintaria e Montagem de Móveis em Lisboa | Faz de Tudo PT",
        "meta_description": "Carpinteiro em Lisboa, Cascais e Setúbal: montagem de móveis, portas e janelas. Serviço preciso ao domicílio. Orçamento grátis.",
        "h1": "Carpintaria e Montagem de Móveis ao Domicílio",
        "wa_message": "Olá! Gostaria de pedir um orçamento para carpintaria.",
        "body": """
                <p>A <strong>carpintaria em Lisboa</strong> e na <strong>Margem Sul</strong> exige precisão e experiência. Montamos móveis, ajustamos portas e executamos pequenas obras em madeira com acabamento profissional.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Montagem de móveis IKEA e por medida, reparação de portas que raspam, colocação de puxadores, corrediças e pequenas estruturas em madeira interiores e exteriores.</p>
                <p>Atendemos particulares e empresas em Cascais, Sintra, Oeiras, Almada e Setúbal.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-reparacoes-gerais.html",
        "service_name": "Reparações Gerais",
        "page_title": "Handyman e Reparações Gerais em Lisboa | Faz de Tudo PT",
        "meta_description": "Faz-tudo em Lisboa, Cascais e Setúbal: reparações gerais na casa ou empresa. Uma visita, várias soluções. Orçamento grátis.",
        "h1": "Reparações Gerais e Faz-Tudo ao Domicílio",
        "wa_message": "Olá! Gostaria de pedir um orçamento para reparações gerais.",
        "body": """
                <p>O seu <strong>handyman em Lisboa</strong> e na <strong>Margem Sul</strong> para listas de tarefas pendentes. Fixamos, ajustamos e reparamos o que impedem o dia-a-dia de funcionar bem.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Fixação de prateleiras, TVs e cortinados, pequenas reparações de paredes, silicone, ajuste de portas e intervenções rápidas em apartamentos, moradias e lojas em Cascais e Setúbal.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-manutencao.html",
        "service_name": "Manutenção",
        "page_title": "Manutenção de Edifícios e Habitações em Lisboa | Faz de Tudo PT",
        "meta_description": "Manutenção preventiva em Lisboa e Margem Sul: condomínios, telhados e fachadas. Lavagem alta pressão. Orçamento grátis Faz de Tudo PT.",
        "h1": "Manutenção Preventiva e Reparações para Condomínios",
        "wa_message": "Olá! Gostaria de pedir um orçamento para manutenção.",
        "body": """
                <p>A <strong>manutenção em Lisboa</strong>, <strong>Cascais</strong> e <strong>Setúbal</strong> evita obras caras. Planos periódicos para condomínios, frações e comércio com relatório claro do que foi verificado.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Inspeção de telhados, calhas e fachadas, pequenas reparações, <strong>lavagem de alta pressão</strong> de pátios, telhados e zonas comuns, e intervenção rápida quando surge uma avaria.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-limpezas.html",
        "service_name": "Limpezas",
        "page_title": "Limpezas Profissionais em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Limpezas em Lisboa, Cascais e Setúbal: doméstica, pós-obra e escritórios. Equipas experientes. Orçamento grátis.",
        "h1": "Limpezas Domésticas e Pós-Obra Profissionais",
        "wa_message": "Olá! Gostaria de pedir um orçamento para limpezas.",
        "body": """
                <p><strong>Limpezas em Lisboa</strong> e na <strong>Margem Sul</strong> com produtos adequados a cada superfície. Regular, pontual ou pós-obra — adaptamos a equipa ao seu espaço.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Limpeza profunda de casas e apartamentos, pós-obra com remoção de pó de construção, limpeza de escritórios e lojas em Cascais, Sintra, Almada e Setúbal.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-jardinagem.html",
        "service_name": "Jardinagem",
        "page_title": "Jardinagem e Manutenção de Jardins em Lisboa | Faz de Tudo PT",
        "meta_description": "Jardinagem em Lisboa, Cascais e Setúbal: poda, relva e rega. Espaços exteriores sempre apresentáveis. Orçamento grátis.",
        "h1": "Jardinagem e Manutenção de Jardins",
        "wa_message": "Olá! Gostaria de pedir um orçamento para jardinagem.",
        "body": """
                <p><strong>Jardinagem em Lisboa</strong>, <strong>Cascais</strong> e <strong>Margem Sul</strong> para moradias, condomínios e espaços comerciais. Mantemos o exterior apresentável o ano inteiro.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Corte de relva, poda de árvores e sebes, limpeza de terrenos, manutenção de relvados e instalação ou reparação de rega automática.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-mudancas.html",
        "service_name": "Mudanças",
        "page_title": "Mudanças Residenciais em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Mudanças em Lisboa, Cascais e Setúbal com embalagem e montagem. Equipa cuidadosa. Orçamento grátis Faz de Tudo PT.",
        "h1": "Mudanças Residenciais e Comerciais com Embalagem",
        "wa_message": "Olá! Gostaria de pedir um orçamento para mudanças.",
        "body": """
                <p><strong>Mudanças em Lisboa</strong> e na <strong>Margem Sul</strong> sem stress. Organizamos transporte, proteção de mobiliário e montagem na nova casa ou loja.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Mudanças completas ou parciais, desmontagem e remontagem de móveis, embalagem de fragis e apoio na distribuição em Sintra, Cascais, Almada e Setúbal.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-informatica.html",
        "service_name": "Informática",
        "page_title": "Assistência Informática em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Informática ao domicílio em Lisboa e Setúbal: PCs lentos, Wi-Fi e impressoras. Orçamento grátis Faz de Tudo PT.",
        "h1": "Assistência Informática e Redes Wi-Fi",
        "wa_message": "Olá! Gostaria de pedir um orçamento para informática.",
        "body": """
                <p><strong>Assistência informática em Lisboa</strong>, <strong>Cascais</strong> e <strong>Setúbal</strong> para casa e pequenos escritórios. Diagnóstico claro e solução no local sempre que possível.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Reparação de computadores lentos ou com vírus, configuração de Wi-Fi e impressoras em rede, smart home básica e recuperação de dados quando viável.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-serralharia.html",
        "service_name": "Serralharia",
        "page_title": "Serralharia e Abertura de Portas em Lisboa | Faz de Tudo PT",
        "meta_description": "Serralheiro em Lisboa e Margem Sul: fechaduras, portões e abertura urgente. Cascais e Setúbal. Orçamento grátis.",
        "h1": "Serralharia e Abertura de Portas Urgente",
        "wa_message": "Olá! Gostaria de pedir um orçamento para serralharia.",
        "body": """
                <p><strong>Serralharia em Lisboa</strong>, <strong>Cascais</strong> e <strong>Setúbal</strong> com resposta rápida. Fechaduras, portões, grades e situações de porta trancada.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Substituição de cilindros e fechaduras, reparação de portões de garagem, instalação de grades e abertura de portas com discrição e profissionalismo.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-climatizacao.html",
        "service_name": "Climatização",
        "page_title": "Instalação de Ar Condicionado e Climatização em Lisboa | Faz de Tudo PT",
        "meta_description": "AVAC e ar condicionado em Lisboa, Cascais e Setúbal: instalação, manutenção e reparação. Orçamento grátis Faz de Tudo PT.",
        "h1": "Instalação e Reparação de Ar Condicionado (AVAC)",
        "wa_message": "Olá! Gostaria de pedir um orçamento para climatização.",
        "body": """
                <p><strong>Climatização em Lisboa</strong> e na <strong>Margem Sul</strong> para conforto térmico o ano inteiro. Instalamos, damos manutenção e reparamos sistemas de ar condicionado e aquecimento.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Instalação de splits e multisplit, carga de gás, limpeza de filtros, reparação de avarias e manutenção preventiva para maior eficiência em apartamentos, moradias e lojas em Cascais e Setúbal.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-remodelacoes.html",
        "service_name": "Remodelações",
        "page_title": "Remodelações e Obras em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Remodelações em Lisboa e Setúbal: cozinhas, casas de banho e pavimentos. Equipa completa. Orçamento grátis.",
        "h1": "Remodelações de Cozinhas, Casas de Banho e Obras",
        "wa_message": "Olá! Gostaria de pedir um orçamento para remodelações.",
        "body": """
                <p><strong>Remodelações em Lisboa</strong>, <strong>Cascais</strong> e <strong>Setúbal</strong> com coordenação de canalização, electricidade e acabamentos. Um interlocutor único do orçamento à entrega.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Renovação de cozinhas e casas de banho, substituição de pavimentos, pequenas e médias obras com cronograma e preço fechado sempre que possível.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-estores-persianas.html",
        "service_name": "Estores e Persianas",
        "page_title": "Reparação de Estores e Persianas em Lisboa | Faz de Tudo PT",
        "meta_description": "Estores e persianas em Lisboa e Margem Sul: reparação, motores e toldos. Serviço rápido. Orçamento grátis.",
        "h1": "Reparação e Instalação de Estores e Persianas",
        "wa_message": "Olá! Gostaria de pedir um orçamento para estores e persianas.",
        "body": """
                <p><strong>Estores e persianas em Lisboa</strong>, <strong>Cascais</strong> e <strong>Setúbal</strong> — fitas gastas, motores avariados ou instalação nova. Intervenção rápida em janelas e varandas.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Substituição de fitas e lâminas, reparação de mecanismos e motores eléctricos, mosquiteiras, toldos e estores novos em apartamentos e moradias.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-decoracao-interiores.html",
        "service_name": "Decoração de Interiores",
        "page_title": "Decoração de Interiores em Lisboa e Cascais | Faz de Tudo PT",
        "meta_description": "Decoração de interiores em Lisboa e Setúbal: cortinas, papel de parede e home staging. Orçamento grátis.",
        "h1": "Decoração de Interiores e Home Staging",
        "wa_message": "Olá! Gostaria de pedir um orçamento para decoração de interiores.",
        "body": """
                <p><strong>Decoração de interiores em Lisboa</strong> e na <strong>Margem Sul</strong> para valorizar a sua casa ou preparar um imóvel para venda em Cascais e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Cortinados, papel de parede, iluminação decorativa, molduras, pequenas alterações de layout e home staging com acabamento cuidado.</p>
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
                </ul>""",
    },
    {
        "slug": "servico-piscinas.html",
        "service_name": "Piscinas",
        "page_title": "Manutenção de Piscinas em Lisboa e Margem Sul | Faz de Tudo PT",
        "meta_description": "Manutenção de piscinas em Lisboa, Cascais e Setúbal: tratamento de água, filtros e bombas. Orçamento grátis Faz de Tudo PT.",
        "h1": "Manutenção e Limpeza de Piscinas Profissional",
        "wa_message": "Olá! Gostaria de pedir um orçamento para manutenção de piscinas.",
        "body": """
                <p><strong>Manutenção de piscinas em Lisboa</strong>, <strong>Cascais</strong>, <strong>Margem Sul</strong> e <strong>Setúbal</strong> para água cristalina o ano inteiro. Moradias, condomínios e espaços de lazer.</p>
                <h2>O que fazemos nesta área:</h2>
                <p>Limpeza regular, equilíbrio químico, revisão de filtros e bombas, deteção de fugas e reparação de revestimentos. Planos de manutenção semanal ou quinzenal disponíveis.</p>
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
                </ul>""",
    },
]


def json_ld(service: dict) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "serviceType": service["service_name"],
        "description": service["meta_description"],
        "provider": {
            "@type": "HomeAndConstructionBusiness",
            "name": "Faz de Tudo PT",
            "image": "https://www.fazdetudo.pt/logo.png",
            "telephone": "+351932504112",
            "priceRange": "$$",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Lisboa",
                "addressCountry": "PT",
            },
        },
        "areaServed": [
            {"@type": "AdministrativeArea", "name": "Lisboa"},
            {"@type": "AdministrativeArea", "name": "Cascais"},
            {"@type": "AdministrativeArea", "name": "Estoril"},
            {"@type": "AdministrativeArea", "name": "Sintra"},
            {"@type": "AdministrativeArea", "name": "Almada"},
            {"@type": "AdministrativeArea", "name": "Setúbal"},
        ],
    }
    return json.dumps(data, ensure_ascii=False, indent=2)


def render_page(service: dict) -> str:
    return (
        TEMPLATE.replace("{{PAGE_TITLE}}", service["page_title"])
        .replace("{{META_DESCRIPTION}}", service["meta_description"])
        .replace("{{SLUG}}", service["slug"])
        .replace("{{OG_TITLE}}", f"{service['service_name']} | Faz de Tudo PT")
        .replace("{{H1_TITLE}}", service["h1"])
        .replace("{{SERVICE_NAME}}", service["service_name"])
        .replace("{{BODY_HTML}}", service["body"].strip())
        .replace("{{WA_TEXT}}", quote(service["wa_message"], safe=""))
        .replace("{{JSON_LD}}", json_ld(service))
    )


def main():
    import sys

    sys.path.insert(0, str(Path(__file__).parent))
    try:
        from service_rich_content import SERVICE_BODIES
    except ImportError:
        SERVICE_BODIES = {}

    slugs = []
    for service in SERVICES:
        if service["slug"] in SERVICE_BODIES:
            service = {**service, "body": SERVICE_BODIES[service["slug"]]}
        path = ROOT / service["slug"]
        path.write_text(render_page(service), encoding="utf-8")
        slugs.append(service["slug"])
        print(f"wrote {service['slug']}")
    print(f"\nTotal: {len(slugs)} pages")


if __name__ == "__main__":
    main()
