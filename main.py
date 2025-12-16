import pygame 
from pygame.locals import *
from sys import exit
import os
import math
import random

pygame.init() 
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal') # nome do jogo

# inicializando variáveis
altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)
buff_ativo = False
debuff_ativo = False
tempo_ativo = 0
relogio = pygame.time.Clock()
run = True
scroll = 0

# configurando cenario
tela = pygame.display.set_mode(dimensoes_tela)
original_bg_image = pygame.image.load(os.path.join('assets', 'cenario', 'passarela.png')).convert()
bg_image = pygame.transform.scale(original_bg_image, dimensoes_tela)
bg_width = bg_image.get_width()
tiles = math.ceil(largura_tela / bg_width) + 1 # variavel para o mecanismo de rolagem infinita da tela

# colocando gisele no cenário
gisele_frames = [
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_2.png')).convert_alpha(),
]

gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in gisele_frames]

frame_idx = 0
frame_timer = 0.0
frame_interval = 0.06

player_x = 120
chao = 525 # altura de gisele
player_y = chao

vel_y = 0
gravidade = 1
pulando = False

# distância a ser percorrida (finitude do jogo)
distancia_pixels = 0

pixels_por_metro = 20
meta_metros = 300

# coletáveis (temporários - amarelo: bananas; ciano: câmera; rosa: flores)
tamanho_coletavel = 30

alturas_coletaveis = [565, 480, 460]
distancia_minima_x = 250
cores_coletaveis = [(255, 200, 0), (0, 255, 255), (220, 0, 255)]

# contadores (dicionário que a chave é a cor)
contadores = {
    (255, 200, 0): 0,
    (0, 255, 255): 0,
    (220, 0, 255): 0
}

fonte = pygame.font.SysFont(None, 28)

def gerar_coletavel(cor, alturas_ocupadas, xs_ocupados):
    alturas_disponiveis = [h for h in alturas_coletaveis if h not in alturas_ocupadas]
    if not alturas_disponiveis:
        altura = random.choice(alturas_coletaveis)
    else:
        altura = random.choice(alturas_disponiveis)

    tentativas = 0
    while True:
        x = random.randint(largura_tela + 200, largura_tela + 900)
        if all(abs(x - outro_x) >= distancia_minima_x for outro_x in xs_ocupados):
            break
        tentativas += 1
        if tentativas > 10:
            break

    return {
        "rect": pygame.Rect(x, altura, tamanho_coletavel, tamanho_coletavel),
        "cor": cor
    }

coletaveis = []

for i in range(3):
    alturas_ocupadas = [c["rect"].y for c in coletaveis]
    xs_ocupados = [c["rect"].x for c in coletaveis]

    cor = random.choice(cores_coletaveis)
    coletaveis.append(gerar_coletavel(cor, alturas_ocupadas, xs_ocupados))

vel_coletavel = 7

# variáveis do flash da câmera
flash = False
flash_raio = 0
flash_velocidade = 25
flash_raio_max = int(math.hypot(largura_tela, altura_tela))
flash_tela_total = 0
flash_duracao_tela_total = 30

while run:  # loop principal
        delta_time = relogio.tick(30) / 1000.0  # tempo decorrido em segundos

        for event in pygame.event.get():  # fechar a janela do jogo
            if event.type == QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == KEYDOWN: # identificar o w ou a seta do pulo
                if (event.key == K_w or event.key == K_UP) and not pulando:
                    vel_y = -14
                    pulando = True

        # gravidade do pulo (voltar depois de pular)
        vel_y += gravidade
        player_y += vel_y

        if player_y >= chao:
            player_y = chao
            vel_y = 0
            pulando = False

        # animação andar
        if not pulando:
            frame_timer += delta_time
            if frame_timer >= frame_interval:
                frame_timer = 0
                frame_idx = (frame_idx + 1) % len(gisele_frames)
        else:
            frame_idx = 1  # pulo com os pés juntos

        # desenhando o cenário
        for i in range(0, tiles):
            tela.blit(bg_image, (i * bg_width + scroll, 0))
                    
        # scroll background
        if buff_ativo:
            debuff_ativo = False
            scroll -= 7
            tempo_ativo += 1
            if tempo_ativo >= 100:
                buff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 7

        if debuff_ativo:
            buff_ativo = False
            scroll -= 1
            tempo_ativo += 1
            if tempo_ativo >= 100:
                debuff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 7

        # reset scroll do cenario
        if abs(scroll) > bg_width:
            scroll = 0 

        distancia_pixels += abs(7) # adicionando a distância percorrida
        distancia_metros = distancia_pixels // pixels_por_metro # "convertendo em metros"


        # movimentação dos coletáveis
        for coletavel in coletaveis:
            coletavel["rect"].x -= vel_coletavel

            if coletavel["rect"].right < 0: # aparecer os coletáveis de novo
                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]

                cor = random.choice(cores_coletaveis)
                novo = gerar_coletavel(cor, alturas_ocupadas, xs_ocupados)
                coletavel["rect"] = novo["rect"]
                coletavel["cor"] = novo["cor"]

        gisele_rect = pygame.Rect(player_x, player_y, 80, 80) # rodar coletáveis

        # momento que gisele colide com o coletável
        for coletavel in coletaveis:
            if gisele_rect.colliderect(coletavel["rect"]):
                # efeitos dos coletáveis
                if coletavel["cor"] == (255, 200, 0):  # banana
                    contadores[(220, 0, 255)] = 0  # zera as rosas
                    contadores[(255, 200, 0)] += 1 # aumenta as bananas
                elif coletavel["cor"] == (0, 255, 255):  # câmera
                    contadores[(0, 255, 255)] += 1
                    flash = True
                    flash_raio = 0
                    flash_tempo_tela_total = 0
                else:  # rosas
                    contadores[(220, 0, 255)] += 1

                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]

                cor = random.choice(cores_coletaveis)
                novo = gerar_coletavel(cor, alturas_ocupadas, xs_ocupados)
                coletavel["rect"] = novo["rect"]
                coletavel["cor"] = novo["cor"]

        for coletavel in coletaveis:
            pygame.draw.rect(tela, coletavel["cor"], coletavel["rect"])

        tela.blit(gisele_frames[frame_idx], (player_x, player_y)) # rodar gisele

        # mostrar coletáveis na tela
        fundo_x = 20
        fundo_y = 20
        fundo_largura = 250
        fundo_altura = 70

        pygame.draw.rect(tela, (180, 180, 180), (fundo_x, fundo_y, fundo_largura, fundo_altura))
        pygame.draw.rect(tela, (100, 100, 100), (fundo_x, fundo_y, fundo_largura, fundo_altura), 2)

        margin_x = fundo_x + 10

        # mostrar distância percorrida na tela
        texto_distancia = fonte.render(f"{distancia_metros} m", True, (0, 0, 0))
        tela.blit(texto_distancia, (margin_x, fundo_y + 45))

        for cor in cores_coletaveis:
            pygame.draw.rect(tela, cor, (margin_x, fundo_y + 10, 20, 20))

            texto = fonte.render(str(contadores[cor]), True, (0, 0, 0))
            tela.blit(texto, (margin_x + 25, fundo_y + 10))

            margin_x += 65

        # animação do flash
        if flash:
            flash_surface = pygame.Surface(dimensoes_tela, pygame.SRCALPHA)

            # o círculo branco crescendo
            if flash_raio < flash_raio_max:
                flash_raio += flash_velocidade
                pygame.draw.circle(
                    flash_surface,
                    (255, 255, 255, 255),
                    (largura_tela // 2, altura_tela // 2),
                    flash_raio
                )
            else: # tela toda branca
                flash_surface.fill((255, 255, 255))
                flash_tempo_tela_total += 1

                if flash_tempo_tela_total >= flash_duracao_tela_total:
                    flash = False  # termina o flash

            tela.blit(flash_surface, (0, 0))

        # fim do jogo
        if distancia_metros >= meta_metros:
            run = False 

        pygame.display.update()           