# Gisele Bundchen VS As Forças do Mal

## Descrição do projeto

### Sinopse
Nossa *übermodel* está de volta! Após anos afastada da passarela, **Gisele Bündchen** tem uma nova missão: *o desfile de encerramento da turma de IP 2025.2*.\
Mas há um detalhe: modelos invejosas realizaram um complô para sabotar o evento e dispersaram **cascas de banana** pelo caminho.\
Ajude Gisele a driblar os obstáculos escorregadios e os ***paparazzi***, que enlouquecidamente a ofuscam com seus *flashes*, enquanto tenta coletar as **rosas** lançadas na passarela.\
_Atenção:_ basta uma única banana para abalar sua reputação e zerar as rosas coletadas.\
Será que nossa musa consegue manter-se imune a quedas no *catwalk* e honrar o estrelato?

### Objetivo
Conduzir Gisele pelo desfile, driblando as cascas de banana e os *flashes* dos *paparazzi*, para coletar o máximo de rosas possível antes do fim da passarela.

### Mecânica e fases
O jogo consiste em uma única fase, com **velocidade progressiva** a cada ciclo de 10 segundos: desfilar ao longo de 700 metros de passarela, esquivando-se das **cascas de banana** e das **câmeras**, e acumulando as **rosas** dispersas pelo percurso.

Os três tipos de coletáveis têm os seguintes efeitos:

**· Casca de banana:** Zerar a contagem de rosas. Se coletadas mais de 3, encerra-se o jogo — **game over**.\
**· Câmera:** Ofuscar a tela durante 0,3 segundo. Se coletadas mais de 3, encerra-se o jogo — **game over**.\
**· Rosa:** Somar pontos ao relatório final do jogo.

## Participantes do projeto
· Beatriz de Araújo Ciríaco do Rêgo Barros <bacrb>\
· Gabriela Tavares Benevides <gtb>\
· Marcela Parahym Xavier Lins <mpxl>\
· Sofia Avallone Sakovitz <sas3>

## Organização e desenvolvimento do jogo
A execução do projeto foi repartida entre o grupo tendo em vista não apenas sua eficiência, mas também as preferências de cada integrante e a colaboração mútua.
Foram realizadas reuniões presenciais e assíncronas para planejar o processo, firmar metas e avaliar o progresso.

## Divisão de tarefas

| Integrante(s)               | Tarefas               |
------------------------------|-----------------------|
| Beatriz de Araújo Ciríaco do Rêgo Barros | Tela de início e tela final |
| Gabriela Tavares Benevides | Personagens, sons, cenários e coletáveis |
| Marcela Parahym Xavier Lins, Sofia Avallone Sakovitz | Código principal |

## Arquitetura do projeto - CONCLUIR

## Galeria do projeto - CONCLUIR

## Ferramentas e bibliotecas utilizadas

| Ferramenta | Justificativa                                                                      |
|------------|------------------------------------------------------------------------------------|
| VS Code    | Ambiente de desenvolvimento integrado (IDE) adotado no projeto por oferecer desempenho consistente, robusto e eficiente para Python, com capacidade de integrar-se nativamente ao Git — atributos substanciais para a equipe. |
| Pygame     | Requisito do projeto, Pygame é uma biblioteca consolidada para jogos 2D em Python. Ofertou uma gama de funcionalidades caras à elaboração do código e à lapidação da dinâmica implementada.|
| Math       | Biblioteca designada ao uso de funções e constantes matemáticas aplicadas a certas dinâmicas do jogo. Seu uso otimizou significativamente a implementação de certos efeitos. |
| Random     | Analogamente a Math, foi crucial para certos trechos do código, especialmente na atribuição randômica de coletáveis. Biblioteca padrão de Python. |
| Os         | Módulo útil ao carregamento de arquivos por seu caminho. Biblioteca padrão de Python. |
| Sys        | Utilizada na interação com o sistema operacional para o encerramento do programa. Biblioteca padrão de Python. |
| Github     | Plataforma basilar para a estruturação do projeto de forma coesa e colaborativa. Viabilizou o trabalho em equipe, o gerenciamento de tarefas e a hospedagem do código e dos arquivos utilizados. |        

## Desafios e lições aprendidas
# Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
Errou-se em subestimar, a princípio, a dimensão das tarefas necessárias e a possibilidade de surgirem percalços ao longo da jornada.
O redirecionamento do projeto primário, auxiliado pelos *checkpoints*, mostrou-se uma necessidade, mas, ao fim, também um aprendizado.  

# Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
O maior desafio foi, certamente, o gerenciar o tempo e conciliar demandas internas — que, muitas vezes, exigiam a aquisição de novas habilidades — e externas.
Para isso, alinhar as expectativas inicias ao que era passível de execução no tempo e nas condições disponíveis foi fundamental.
Adaptaram-se, assim, as ideias originais para que resultassem em um projeto factível, focado em contemplar com sucesso os requisitos listados,
mas ainda instigante e conectado com os interesses e a criatividade do grupo.

# Quais as lições aprendidas durante o projeto?
Para além das lições relativas à programação, o projeto foi enriquecedor no aprendizado do trabalho em grupo: a divisão de tarefas, a comunicação entre a equipe,
o compromisso com as metas estabelecidas e o entendimento de que colaborar requer, sobretudo, disciplina, parcimônia e compreensão para que se alcance o resultado almejado.

## Conceitos da disciplina aplicados

### Classes
A classes deram forma ao código. Por elas, os elementos do código puder ser representados como objetos — a exemplo de `Base`,
classe-mãe para os coletáveis, que lhes atribuía os *sprites* e a formatação desejada.

### Funções
As funções também foram de grande relevância no projeto: organizaram os blocos de ação relativos à mecânica de jogo de forma concisa e eficiente.
`atualizar_fisica()`, `atualizar_animacao()` e `pular()`, por exemplo, modularizaram a classe da personagem.

### Laços de repetição
Em `main`, foi o *loop* `while` que garantiu a execução contínua do jogo, com dados, coletáveis e cenários atualizados.
Já os *loops* `for` foram indispensáveis à dinâmica aplicada aos coletáveis, tanto em sua geração quanto em sua contabilização.

### Dicionários
Usaram-se dicionários, especialmente, na implementação dos `contadores` e dos atributos retornados por `gerar_coletavel()`.

### Condicionais
Amplamente utilizadas no código, determinaram o encadeamento de eventos, as condições para execuçãod as classes, a movimentação de Gisele e o controle da aceleração e da saída do jogo.

### Listas
O uso de listas, como `alturas_coletaveis`, embora moderado, auxiliou a definição de constantes de posicionamento dos coletáveis na tela.

### Tuplas
Tuplas foram primordiais para o estabelecimento de constantes para armazenar dados de posicionamento na tela e das cores utilizadas segundo padrão RGB.

## Como jogar

**1. Configuração do ambiente**\
Antes de jogar, é preciso verificar a instalação de **Python 3.x** e, uma vez acessada a pasta do projeto, executar, no terminal:\
````pip install -r requirements.txt````

**2. Execução do jogo**\
Após o primeiro passo, deve-se iniciar o arquivo `main`:\
````python main.py````

**3. Controles do jogo**
Para controlar o jogo, podem-se usar os seguintes comandos:

| Entrada                          | Ação                      |
|----------------------------------|---------------------------|
| `Setas` ou `W/A/S/D` ou `Espaço` | Movimentar a personagem   |
| `Enter`                          | Começar ou confirmar      |
| `ESC`                            | Voltar ao menu            |
| `Mouse`                          | Clicar nos botões da tela |

