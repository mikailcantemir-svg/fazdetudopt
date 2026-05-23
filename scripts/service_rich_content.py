# -*- coding: utf-8 -*-
"""Unique service-rich-text bodies for all servico-*.html pages."""
# servico-recuperar-casa.html: HTML principal mantido manualmente; entrada abaixo para apply-rich-text futuro.

ZONES_LI = """
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Lisboa</strong> (Arroios, Benfica, Campo de Ourique, Alvalade, Lumiar, Belém, Parque das Nações)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Loures e Odivelas</strong> (Sacavém, Moscavide, Camarate, Santa Iria de Azóia, Bucelas)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Sintra e Amadora</strong> (Queluz, Agualva-Cacém, Rio de Mouro, Mem Martins, Massamá, Mafra, Ericeira)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Cascais e Oeiras</strong> (Estoril, Carcavelos, Parede, Carnaxide, Algés, Paço de Arcos, São Domingos de Rana)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Vila Franca de Xira</strong> (Alverca, Póvoa de Santa Iria, Alhandra, Castanheira do Ribatejo)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Margem Sul</strong> (Almada, Costa da Caparica, Seixal, Amora, Corroios, Barreiro, Moita, Montijo, Alcochete)</li>
                    <li><i class="fa-solid fa-location-dot" aria-hidden="true"></i> <strong>Setúbal e Sesimbra</strong> (Azeitão, Palmela, Quinta do Anjo)</li>"""

ZONES_BLOCK = """
                <h2>Zonas de Atendimento Rápido</h2>
                <p>Deslocamo-nos rapidamente até à sua porta nas seguintes localizações:</p>
                <ul class="service-zones-grid">""" + ZONES_LI + """
                </ul>"""

ZONES_SECTION_LISBOA_SETUBAL = """
                <h2>Zonas de Atendimento na Grande Lisboa e Setúbal:</h2>
                <p>Deslocamo-nos rapidamente até à sua porta nas seguintes localizações:</p>
                <ul class="service-zones-grid">""" + ZONES_LI + """
                </ul>"""

SERVICE_BODIES = {
    "servico-pinturas.html": """
                <p>A <strong>FAZDETUDO.PT</strong> é referência em <strong>pintura residencial e comercial na Grande Lisboa e Margem Sul</strong>. Trabalhamos com tintas de qualidade, proteção integral do espaço e acabamentos uniformes em Lisboa, Cascais, Sintra, Almada e Setúbal — com orçamento gratuito e prazos acordados por escrito.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Preparação profissional de superfícies: lixagem, massa corrida, primários anti-humidade e correção de imperfeições.</li>
                    <li>Pintura de interiores: paredes, tetos, portas, rodapés e divisórias com demãos controladas.</li>
                    <li>Pintura de exteriores: fachadas baixas, muros, varandas e gradeamentos com tintas resistentes ao sol e à chuva.</li>
                    <li>Proteção de mobiliário, pavimentos e caixilharias com plásticos e fitas de precisão antes de pintar.</li>
                    <li>Conselho técnico sobre cores, acabamentos mate ou acetinado e soluções anti-bolor em zonas húmidas.</li>
                    <li>Pequenas reparações de gesso cartonado e rachaduras antes do acabamento final.</li>
                    <li>Entrega limpa do espaço e remoção responsável de resíduos de obra.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-pintura-fachadas-alpinismo.html": """
                <p>Reabilitamos fachadas de edifícios em <strong>Lisboa, Cascais, Estoril e Margem Sul</strong> com <strong>alpinismo industrial (trabalho em cordas)</strong>. A FAZDETUDO.PT elimina a necessidade de andaimes caros, reduz o tempo de obra e garante acesso seguro a todos os pontos da fachada — ideal para condomínios, moradias e imóveis expostos à maresia.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Lavagem de alta pressão e descontaminação de fachadas antes da pintura.</li>
                    <li>Tratamento de fissuras, rebocos degradados e zonas com infiltrações visíveis.</li>
                    <li>Aplicação de primários, impermeabilizantes e tintas elásticas para exteriores.</li>
                    <li>Repintura completa de prédios em altura sem montagem de andaimes tradicionais.</li>
                    <li>Reparação pontual de silhares, remates e peitoris com acesso por cordas.</li>
                    <li>Trabalho certificado em altura com equipamento de proteção individual (EPI) completo.</li>
                    <li>Relatório fotográfico e orçamento detalhado para administrações de condomínio.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-canalizacoes.html": """
                <p>Quando surge uma fuga ou entupimento, precisa de um <strong>canalizador de confiança na Grande Lisboa e Margem Sul</strong>. A FAZDETUDO.PT responde com diagnóstico rigoroso, peças adequadas e reparação duradoura em Lisboa, Cascais, Almada, Seixal e Setúbal — particulares, condomínios e comércio.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Deteção e reparação de fugas visíveis e ocultas em tubagens, juntas e ligações.</li>
                    <li>Desentupimentos mecânicos e químicos controlados em sanitas, lavatórios, ralos e colunas.</li>
                    <li>Substituição de torneiras, monocomandos, sifões e flexíveis danificados.</li>
                    <li>Reparação e substituição de autoclismos, válvulas de descarga e mecanismos internos.</li>
                    <li>Instalação de louças sanitárias, bases de duche, lavatórios e ligações à rede.</li>
                    <li>Substituição de troços de tubagem em PVC, multicamada ou cobre quando necessário.</li>
                    <li>Atendimento urgente para restaurantes, escritórios e frações em condomínios.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-electricidade.html": """
                <p>A segurança elétrica da sua casa ou negócio não pode esperar. Somos especialistas em <strong>electricidade em Lisboa, Margem Sul e Cascais</strong>, com intervenções certificadas, diagnóstico de quadros e modernização de instalações antigas — sempre com orçamento claro antes de iniciar trabalhos.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Reparação de avarias: curtos-circuitos, tomadas sem corrente e disjuntores a disparar.</li>
                    <li>Instalação e substituição de tomadas, interruptores e candeeiros interiores e exteriores.</li>
                    <li>Modernização de quadros eléctricos com disjuntores diferenciais e proteção adequada.</li>
                    <li>Instalação de iluminação LED, focos encastrados e fitas de led em cozinhas e salas.</li>
                    <li>Criação de circuitos dedicados para forno, placa, ar condicionado ou aquecedor.</li>
                    <li>Deteção de sobrecargas e reorganização de circuitos em instalações antigas.</li>
                    <li>Pequenas ligações para eletrodomésticos, campainhas e equipamentos comerciais.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-carpintaria.html": """
                <p>Da montagem de um roupeiro à afinação de uma porta que não fecha, a <strong>carpintaria em Lisboa e Margem Sul</strong> exige precisão e experiência. A FAZDETUDO.PT executa trabalhos em madeira e derivados com acabamento cuidado em Cascais, Sintra, Oeiras, Almada e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Montagem profissional de móveis IKEA, MDF e mobiliário por medida.</li>
                    <li>Afinação de portas interiores que raspam, batem ou não fecham corretamente.</li>
                    <li>Colocação e substituição de rodapés, guarnições e molduras decorativas.</li>
                    <li>Instalação de prateleiras, nichos e armários fixos com nivelamento preciso.</li>
                    <li>Reparação de folhas de porta, dobradiças, corrediças e puxadores.</li>
                    <li>Pequenas estruturas em madeira para arrumação, despensas e divisórias leves.</li>
                    <li>Fixação segura de tampos, bancadas e elementos em cozinhas equipadas.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-reparacoes-gerais.html": """
                <p>O seu <strong>handyman de confiança na Grande Lisboa e Margem Sul</strong> para resolver a lista de tarefas que adia há meses. A FAZDETUDO.PT combina rapidez, ferramentas adequadas e soluções definitivas em Lisboa, Cascais, Almada e Setúbal — uma visita, vários arranjos resolvidos.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Fixação de suportes de TV, estantes, espelhos e quadros em qualquer tipo de parede.</li>
                    <li>Instalação de varões, calhas de cortinados e persianas interiores.</li>
                    <li>Montagem de móveis, camas, roupeiros e equipamento de escritório.</li>
                    <li>Reparação de fechaduras, dobradiças, puxadores e fechos de janelas.</li>
                    <li>Aplicação de silicone em bases de duche, bancadas e juntas de cozinha.</li>
                    <li>Tapamento de furos, pequenas reparações em paredes e retouches de pintura.</li>
                    <li>Pequenas tarefas eléctricas e de canalização não especializadas no mesmo dia.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-manutencao.html": """
                <p>Evite obras caras com <strong>manutenção preventiva na Grande Lisboa e Margem Sul</strong>. A FAZDETUDO.PT elabora planos periódicos para condomínios, moradias e comércio em Lisboa, Cascais, Sintra, Almada e Setúbal — com relatório do que foi verificado e corrigido.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Inspeção periódica de telhados, calhas, caleiras e ralos exteriores.</li>
                    <li>Lavagem de alta pressão em pátios, terraços, muros e entradas de garagem.</li>
                    <li>Verificação de estanquidade em juntas, silicone e pequenas infiltrações.</li>
                    <li>Reparação pontual de portões, grades, portas de garagem e ferragens.</li>
                    <li>Manutenção de espaços comuns em condomínios (lâmpadas, puxadores, fechos).</li>
                    <li>Limpeza e desobstrução preventiva de ralos e sifões antes da época de chuva.</li>
                    <li>Planos mensais ou trimestrais com preço acordado e visitas agendadas.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-limpezas.html": """
                <p>Ambientes limpos transmitem confiança e bem-estar. Prestamos <strong>serviços de limpeza profissional na Grande Lisboa e Margem Sul</strong> para casas, escritórios, lojas e condomínios em Lisboa, Cascais, Oeiras, Almada e Setúbal — com produtos adequados a cada superfície.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Limpeza profunda de apartamentos e moradias (cozinhas, casas de banho, divisões).</li>
                    <li>Limpeza pós-obra com remoção de pó de construção, rejunte e resíduos.</li>
                    <li>Limpeza de escritórios, lojas e espaços comerciais fora de horário se necessário.</li>
                    <li>Limpeza de vidros interiores e exteriores acessíveis e varandas.</li>
                    <li>Desinfeção de casas de banho, cozinhas e zonas de elevada utilização.</li>
                    <li>Limpeza de garagens, arrecadações e áreas comuns de condomínios.</li>
                    <li>Planos de limpeza semanal, quinzenal ou pontual com equipa experiente.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-jardinagem.html": """
                <p>Jardins bem tratados valorizam o imóvel e melhoram a qualidade de vida. A FAZDETUDO.PT oferece <strong>jardinagem e manutenção de exteriores na Grande Lisboa e Margem Sul</strong> — desde o corte de relva em Cascais até à poda em Sintra, Almada e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Corte e tratamento de relvados com equipamento profissional.</li>
                    <li>Poda de árvores, arbustos e sebes com segurança e recolha de resíduos verdes.</li>
                    <li>Limpeza e desbaste de terrenos, quintais e espaços abandonados.</li>
                    <li>Instalação e reparação de sistemas de rega automática.</li>
                    <li>Remoção de ervas daninhas e revitalização de canteiros.</li>
                    <li>Manutenção de jardins em moradias, condomínios e espaços comerciais.</li>
                    <li>Planos sazonais de manutenção com visitas regulares acordadas.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-mudancas.html": """
                <p>Uma mudança bem planead reduz stress e danos. A FAZDETUDO.PT realiza <strong>mudanças residenciais e comerciais na Grande Lisboa e Margem Sul</strong> com embalagem cuidada, transporte seguro e montagem no destino — Lisboa, Cascais, Sintra, Almada, Seixal e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Mudanças completas T2, T3, moradias e escritórios com equipa dedicada.</li>
                    <li>Embalagem de frágeis, louças, espelhos e equipamento eletrónico.</li>
                    <li>Desmontagem e remontagem de camas, roupeiros, mesas e estantes.</li>
                    <li>Transporte com proteção de colchões, estofos e móveis volumosos.</li>
                    <li>Mudanças parciais: só cozinha, só quartos ou armazém para garagem.</li>
                    <li>Apoio no agendamento de elevador e proteção de áreas comuns do prédio.</li>
                    <li>Orçamento fechado por volume ou por hora, conforme a sua necessidade.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-informatica.html": """
                <p>Computadores lentos, Wi-Fi instável ou impressoras offline prejudicam o seu dia. A FAZDETUDO.PT presta <strong>assistência informática ao domicílio na Grande Lisboa e Margem Sul</strong> — diagnóstico claro, soluções práticas e linguagem acessível em Lisboa, Cascais, Oeiras e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Remoção de vírus, malware e otimização de computadores lentos (Windows e Mac).</li>
                    <li>Configuração e reforço de redes Wi-Fi domésticas e de pequenos escritórios.</li>
                    <li>Instalação de impressoras, scanners e partilha em rede local.</li>
                    <li>Backup de dados importantes e recuperação básica quando viável.</li>
                    <li>Configuração de email, cloud e sincronização entre dispositivos.</li>
                    <li>Pequenas soluções de smart home: câmaras, tomadas inteligentes e campainhas.</li>
                    <li>Formação breve ao utilizador para evitar problemas recorrentes.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-serralharia.html": """
                <p>Porta trancada, fechadura avariada ou portão encravado exigem resposta imediata. Somos especialistas em <strong>serralharia e segurança na Grande Lisboa e Margem Sul</strong> — abertura de portas, substituição de cilindros e reparação de portões em Lisboa, Cascais, Almada e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Abertura de portas trancadas com técnicas não destrutivas sempre que possível.</li>
                    <li>Substituição de cilindros, canhões e fechaduras de alta segurança.</li>
                    <li>Instalação de fechaduras multiponto e reforço de portas de entrada.</li>
                    <li>Reparação de portões de garagem, motores e sistemas de corrida.</li>
                    <li>Substituição e afinação de fechaduras de armários e escritórios.</li>
                    <li>Instalação de correntes, trancas de segurança e olhais reforçados.</li>
                    <li>Atendimento urgente 24h para situações de porta fechada com chave no interior.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-climatizacao.html": """
                <p>O conforto térmico no verão e no inverno passa por um sistema AVAC bem instalado e mantido. A FAZDETUDO.PT é especialista em <strong>climatização e ar condicionado na Grande Lisboa e Margem Sul</strong> — splits, multisplit e manutenção em Lisboa, Cascais, Sintra, Almada e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Instalação de ar condicionado split e multisplit com linhas frigoríficas discretas.</li>
                    <li>Carga e verificação de gás refrigerante conforme especificações do fabricante.</li>
                    <li>Limpeza profunda de filtros, serpentinas e unidades interiores e exteriores.</li>
                    <li>Reparação de avarias: não arrefece, não aquece, ruídos ou fugas de água.</li>
                    <li>Manutenção preventiva anual para maior eficiência energética e vida útil.</li>
                    <li>Desinstalação e reposicionamento de unidades em remodelações.</li>
                    <li>Conselho sobre potência (BTU) adequada ao volume de cada divisão.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-remodelacoes.html": """
                <p>Renovar a cozinha ou a casa de banho transforma o dia a dia. A FAZDETUDO.PT coordena <strong>remodelações na Grande Lisboa e Margem Sul</strong> com um único interlocutor — do orçamento à entrega da chave — em Lisboa, Cascais, Oeiras, Almada e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Remodelação completa de cozinhas: layout, móveis, bancadas e ligações.</li>
                    <li>Renovação de casas de banho: revestimentos, louças, duche e impermeabilização.</li>
                    <li>Substituição de pavimentos: cerâmica, vinílico, madeira ou laminado.</li>
                    <li>Instalação de paredes de Pladur, tetos falsos e iluminação embutida.</li>
                    <li>Pequenas e médias obras com cronograma e preço fechado acordado.</li>
                    <li>Coordenação de canalização, electricidade e pintura na mesma obra.</li>
                    <li>Preparação de imóveis para venda ou arrendamento (remodelação leve).</li>
                </ul>""" + ZONES_BLOCK,

    "servico-recuperar-casa.html": """
                <p>Devolver vida a uma casa devoluta, herdada ou muito degradada exige método e coordenação. A FAZDETUDO.PT recupera o imóvel de ponta a ponta — estrutura, instalações e acabamentos — na Grande Lisboa e Margem Sul, com um único interlocutor e prazo fechado.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Avaliação do estado geral do imóvel: estrutura, coberturas, humidades e instalações.</li>
                    <li>Recuperação de casas herdadas, devolutas ou há muito desabitadas.</li>
                    <li>Tratamento de humidades, infiltrações e patologias das paredes.</li>
                    <li>Substituição ou recuperação de instalações elétricas e de canalização antigas.</li>
                    <li>Reabilitação de coberturas, telhados, tetos e pavimentos degradados.</li>
                    <li>Renovação completa de cozinhas e casas de banho não funcionais.</li>
                    <li>Recuperação de caixilharias, portas e janelas antigas ou apodrecidas.</li>
                    <li>Pintura, acabamentos e limpeza final para entrega da casa pronta a habitar.</li>
                    <li>Coordenação de todas as especialidades com um único interlocutor e prazo fechado.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-estores-persianas.html": """
                <p>Estores presos, fitas partidas ou motores silenciosos são problemas frequentes em apartamentos da linha de Cascais e em Lisboa. A FAZDETUDO.PT repara e instala <strong>estores, persianas e mosquiteiras na Grande Lisboa e Margem Sul</strong> com peças adequadas e garantia de funcionamento.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Substituição de fitas, lâminas e mecanismos de estores manuais.</li>
                    <li>Reparação e substituição de motores de estores eléctricos e comandos.</li>
                    <li>Desencravamento e afinação de estores que não sobem ou descem corretamente.</li>
                    <li>Instalação de estores novos em janelas e varandas.</li>
                    <li>Reparação de persianas interiores e exteriores em alumínio ou PVC.</li>
                    <li>Montagem de mosquiteiras de rolo, fixas ou plissadas.</li>
                    <li>Manutenção preventiva em condomínios com múltiplas frações.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-decoracao-interiores.html": """
                <p>Detalhes bem executados mudam a perceção de qualquer espaço. A FAZDETUDO.PT oferece <strong>decoração de interiores na Grande Lisboa e Margem Sul</strong> — cortinados, iluminação, revestimentos e home staging para habitar ou vender em Lisboa, Cascais, Sintra e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Instalação de cortinados, estores decorativos e varões duplos.</li>
                    <li>Aplicação profissional de papel de parede e painéis decorativos.</li>
                    <li>Instalação de molduras, rodatetos e elementos de acabamento.</li>
                    <li>Projeto e montagem de iluminação decorativa e ambiente.</li>
                    <li>Pequenas alterações de layout para otimizar circulação e luz natural.</li>
                    <li>Home staging para venda ou arrendamento de imóveis.</li>
                    <li>Coordenação com pintura e remodelação para resultado coerente.</li>
                </ul>""" + ZONES_BLOCK,

    "servico-piscinas.html": """
                <p>Uma piscina cristalina exige manutenção regular e equipamento em bom estado. A FAZDETUDO.PT presta <strong>manutenção de piscinas na Grande Lisboa e Margem Sul</strong> — moradias em Cascais, Sintra, Almada e condomínios em toda a região de Lisboa e Setúbal.</p>
                <h2>O que fazemos nesta área:</h2>
                <ul>
                    <li>Tratamento e equilíbrio químico da água (pH, cloro e alcalinidade).</li>
                    <li>Aspiração de fundo, limpeza de paredes e remoção de folhas e detritos.</li>
                    <li>Limpeza e manutenção de filtros, bombas e skimmers.</li>
                    <li>Reparação de fugas, fissuras em revestimentos e juntas degradadas.</li>
                    <li>Arranque de piscina na época de verão e encerramento no outono.</li>
                    <li>Substituição de lâmpadas subaquáticas e pequenos componentes.</li>
                    <li>Planos semanais ou quinzenais com preço mensal fixo.</li>
                </ul>""" + ZONES_BLOCK,
}
