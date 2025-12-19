# Gisele Bündchen VS As Forças do Mal

## Descrição do projeto

### Sinopse
Nossa *übermodel* está de volta!

Após anos afastada das passarelas, **Gisele Bündchen** tem uma nova missão — *o desfile de encerramento da turma de IP 2025.2*.

Mas há um detalhe: modelos invejosas realizaram um complô para sabotar o evento e dispersaram **cascas de banana** pelo caminho.

Ajude Gisele a driblar os obstáculos escorregadios e os ***paparazzi***, que a ofuscam enlouquecidamente com seus flashes, enquanto tenta coletar as **rosas** lançadas na passarela.

***Atenção:** basta uma única banana para abalar sua reputação e zerar as rosas coletadas.*

Será que a musa consegue manter-se imune a quedas no *catwalk* e honrar o estrelato?

### Objetivo
Conduzir Gisele pelo desfile, driblando as cascas de banana e os flashes dos *paparazzi*, para coletar o máximo de rosas possível antes do fim da passarela.

### Mecânica e fases
O jogo consiste em uma única fase, com **velocidade progressiva** a cada ciclo de 10 segundos: desfilar ao longo de 700 metros de passarela, esquivando-se das **cascas de banana** e das **câmeras**, e acumulando as **rosas** dispersas pelo percurso.

Os três tipos de coletáveis têm os seguintes efeitos:

**· Casca de banana:** Zerar a contagem de rosas. Se coletadas 3, encerra-se o jogo — **game over**.\
**· Câmera:** Ofuscar a tela durante 0,3 segundo. Se coletadas 3, encerra-se o jogo — **game over**.\
**· Rosa:** Somar pontos ao relatório final do jogo.

## Participantes do projeto
· Beatriz Araújo Ciríaco do Rêgo Barros (bacrb)\
· Gabriela Tavares Benevides (gtb)\
· Marcela Parahym Xavier Lins (mpxl)\
· Sofia Avallone Sakovitz (sas3)

## Organização e desenvolvimento do jogo
A execução do projeto foi repartida entre o grupo tendo em vista não apenas sua eficiência, mas também as preferências de cada integrante e a colaboração mútua.
Foram realizadas reuniões presenciais e assíncronas para planejar o processo, firmar metas e avaliar o progresso.

## Divisão de tarefas

| Integrante(s)               | Tarefa                |
------------------------------|-----------------------|
| Beatriz Araújo Ciríaco do Rêgo Barros | · Arte e implementação das telas de:<br>&emsp;- início;<br>&emsp;- _game over_;<br>&emsp;- vitória. |
| Gabriela Tavares Benevides | · Cenários e a implementação desses códigos;<br>· *Sprites* (personagem principal e coletáveis);<br>· Sons;<br>· Organização do código (repositório + modularização). |
| Marcela Parahym Xavier Lins | · Desenvolvimento do código principal;<br>· Refinamento de detalhes gráficos;<br>· Relatório final (README.md). |
| Sofia Avallone Sakovitz | · Desenvolvimento do código principal;<br>· Slides da apresentação. |

## Arquitetura do projeto
````
PROJETO/
|-- assets/                   # Recursos estáticos do projeto
|   |-- cenario/              # Imagens usadas para o cenário
|   |-- fonte/                # Fonte utilizada para os textos
|   |-- sprites/              # Sprites utilizadas
|   |   |-- coletaveis/       # Sprites: coletáveis
|   |   |-- gisele/           # Sprites: personagem
|   |-- sons/                 # Música e efeitos sonoros utilizados no jogo
|   |-- telas de transição    # PNGs das telas inicial e final, além de seus botões
|-- src/                      # Código fonte do projeto
|   |-- cenarios/             # Definição das telas e da interface gráfica
|   |   |-- desfile.py        # Lógica de renderização da tela do desfile
|   |   |-- tela_inicial.py   # Lógica da tela inicial e seus botões
|   |   |-- tela_final.py     # Lógica da tela final, mensagens e botões
|   |-- coletaveis/           # Módulo para coletáveis do jogo
|   |   |-- banana.py         # Coletável: casca de banana
|   |   |-- base.py           # Classe-mãe para coletáveis
|   |   |-- camera.py         # Coletável: câmera
|   |   |-- rosa.py           # Coletável: rosa
|   |-- personagens/          # Módulo para personagens do jogo
|   |   |-- gisele.py         # Personagem: Gisele
|   |-- main.py               # Arquivo principal do projeto
|-- .gitignore                # Identificação de quais arquivos devem ser ignorados no controle de versão, deixando o repositório mais limpo
|-- README.md                 # Arquivo informativo do projeto
````

## Galeria do projeto
### Tela inicial
<img width="1128" height="915" alt="image" src="https://github.com/user-attachments/assets/82efbbf6-5494-430b-95ff-46d510fef414" /><br>
### Cenário principal
<img width="1128" height="915" alt="image" src="https://github.com/user-attachments/assets/60c1d5bf-98a7-49ee-8383-2b49988edd8b" /><br>
### Cenário de chegada
<img width="1128" height="915" alt="image" src="https://github.com/user-attachments/assets/0baf2f86-ea2c-41e0-91c7-0f6211fe507d" /><br>
### Tela de vitória
<img width="1128" height="915" alt="image" src="https://github.com/ggabenevides/Projeto-IP-CC25.2-G2/blob/41476e97e0fc659f0e50f0a3d590fd6b981c5da4/assets/telas%20de%20transi%C3%A7%C3%A3o/tela_vitoria.png" /><br>
### Tela de derrota
<img width="1128" height="915" alt="image" src="https://github.com/ggabenevides/Projeto-IP-CC25.2-G2/blob/eda11ebeef343aef042f358ebe430e04632d4105/assets/telas%20de%20transi%C3%A7%C3%A3o/tela_derrota.png" />


## Ferramentas e bibliotecas utilizadas

| Ferramenta | Justificativa                                                                      |
|------------|------------------------------------------------------------------------------------|
| VS Code    | Ambiente de desenvolvimento integrado (IDE) adotado no projeto por oferecer desempenho consistente, robusto e eficiente para Python, com capacidade de integrar-se nativamente ao Git — atributos substanciais para a equipe. |
| Pygame     | Requisito do projeto, Pygame é uma biblioteca consolidada para jogos 2D em Python. Ofertou uma gama de funcionalidades caras à elaboração do código e à lapidação da dinâmica implementada.|
| Math       | Biblioteca designada ao uso de funções e constantes matemáticas aplicadas a certas dinâmicas do jogo. Seu uso otimizou significativamente a implementação dos efeitos. |
| Random     | Analogamente a Math, foi crucial para certos trechos do código, especialmente na atribuição randômica de coletáveis. Biblioteca padrão de Python. |
| Os         | Módulo útil ao carregamento de arquivos por seu caminho. Biblioteca padrão de Python. |
| Sys        | Utilizada na interação com o sistema operacional para o encerramento do programa. Biblioteca padrão de Python. |
| GitHub     | Plataforma basilar para a estruturação do projeto de forma coesa e colaborativa. Viabilizou o trabalho em equipe, o gerenciamento de tarefas e a hospedagem do código e dos arquivos utilizados. |
| Piskel     | Ferramenta que possibilitou o design das *sprites*. |
| Canva      | Plataforma que auxiliou o desenvolvimento das telas de transição e dos slides de apresentação do projeto. |
| PenUp      | Ferramenta de desenho digital utilizada para o design de cenário. |

## Desafios e lições aprendidas
### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
Errou-se em subestimar, a princípio, a dimensão das tarefas necessárias e a possibilidade de surgirem percalços ao longo da jornada.
O redirecionamento do projeto primário, auxiliado pelos *checkpoints*, mostrou-se uma necessidade, mas, ao fim, também um aprendizado.  

### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
O maior desafio foi, certamente, gerenciar o tempo e conciliar demandas internas — as quais, muitas vezes, exigiam a aquisição de novas habilidades — e externas.
Para isso, alinhar as expectativas iniciais ao que era passível de execução no tempo e nas condições disponíveis foi fundamental.
Adaptaram-se, assim, as ideias originais para que resultassem em um projeto factível, focado em contemplar com sucesso os requisitos listados,
mas ainda instigante e conectado com os interesses e a criatividade do grupo.

### Quais as lições aprendidas durante o projeto?
Para além das lições relativas à programação, o projeto foi enriquecedor no aprendizado do trabalho em grupo: a divisão de tarefas, a comunicação entre a equipe,
o compromisso com as metas estabelecidas e o entendimento de que colaborar requer, sobretudo, disciplina, parcimônia e compreensão para que se alcance o resultado almejado.

## Conceitos da disciplina aplicados

### Classes
A classes deram forma ao código. Graças a elas, os elementos do jogo puderam ser representados como objetos — a exemplo de `Base`,
classe-mãe para os coletáveis, que lhes atribuía os *sprites* e a formatação desejada.

### Funções
As funções também foram de grande relevância no projeto: organizaram os blocos de ação relativos à mecânica do jogo de forma concisa e eficiente.
`atualizar_fisica()`, `atualizar_animacao()` e `pular()`, por exemplo, modularizaram a classe da personagem, `Gisele`.

### Laços de repetição
Em `main`, foi o *loop* `while` que garantiu a execução contínua do jogo, com dados, coletáveis e cenários atualizados.
Já os *loops* `for` foram indispensáveis à dinâmica aplicada aos coletáveis, tanto em sua geração quanto em sua contabilização.

### Dicionários
Usaram-se dicionários, especialmente, na implementação dos `contadores` e dos atributos retornados por `gerar_coletavel()`.

### Condicionais
Amplamente utilizadas no código, determinaram o encadeamento de eventos, as condições para execução das classes, a movimentação de Gisele e o controle da aceleração e da saída do jogo.

### Listas
O uso de listas, como `alturas_coletaveis`, embora moderado, auxiliou a definição das constantes de posicionamento dos coletáveis na tela.

### Tuplas
Tuplas foram primordiais para o estabelecimento das constantes para armazenar dados de posicionamento na tela e das cores utilizadas segundo o padrão RGB.

## Como jogar

**1. Configuração do ambiente**\
Antes de jogar, é preciso verificar a instalação de **Python 3.x** e, uma vez acessada a pasta do projeto, executar, no terminal:\
````pip install -r requirements.txt````

**2. Execução do jogo**\
Após o primeiro passo, deve-se iniciar o arquivo `main`:\
````python main.py````

**3. Controles do jogo**\
Para controlar o jogo, podem-se usar os seguintes comandos:

| Entrada                          | Ação                      |
|----------------------------------|---------------------------|
| `Setas` ou `W/A/S/D` ou `Espaço` | Movimentar a personagem   |
| `Enter`                          | Começar ou confirmar      |
| `ESC`                            | Voltar ao menu            |
| `Mouse`                          | Clicar nos botões da tela |

