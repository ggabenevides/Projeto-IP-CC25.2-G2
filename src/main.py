import pygame
from pygame.locals import *
from sys import exit
import math
import random
import os

# inicializando variáveis
relogio = pygame.time.Clock()
run = True
altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)

pygame.init()
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal')
tela = pygame.display.set_mode(dimensoes_tela)

# cenário
original_bg_image = pygame.image.load(
    os.path.join('assets', 'cenario', 'passarela.png')
).convert()

# gisele
gisele_frames = [
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
]

# coletáveis
sprites_coletaveis = [
    pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'cascaDeBanana.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'flash.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'rosa.png')).convert_alpha(),
]

#-----------#
#  CLASSES  #  
#-----------#

# CLASSE: Desfile
class Desfile:
    
    def iniciar_passarela(dimensoes_tela, largura_tela):
        bg_image = pygame.transform.scale(original_bg_image, dimensoes_tela)
        bg_width = bg_image.get_width()
        tiles = math.ceil(largura_tela / bg_width) + 1
        scroll = 0

        return bg_image, bg_width, tiles, scroll

# CLASSE: Gisele
class Gisele:

    gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in gisele_frames]

    def __init__(self):
        self.frame_idx = 0
        self.frame_timer = 0.0
        self.frame_interval = 0.06

        self.player_x = 120
        self.chao = 525
        self.player_y = self.chao

        self.vel_y = 0
        self.gravidade = 1
        self.pulando = False

    def atualizar_fisica(self): # VERIFICAR APLICAÇÃO DE SELF E SELF
        global player_y, vel_y, pulando

        vel_y += self.gravidade
        player_y += vel_y

        if player_y >= self.chao:
            player_y = self.chao
            vel_y = 0
            pulando = False

    def atualizar_animacao(self, delta_time): # VERIFICAR APLICAÇÃO DE SELF
        global frame_timer, frame_idx

        if not pulando:
            frame_timer += delta_time
            if frame_timer >= self.frame_interval:
                frame_timer = 0
                frame_idx = (frame_idx + 1) % len(gisele_frames)
        else:
            frame_idx = 1

    def pular():
        global vel_y, pulando
        if not pulando:
            vel_y = -14
            pulando = True

    def desenhar(self, tela): # VERIFICAR APLICAÇÃO DE SELF
        tela.blit(gisele_frames[frame_idx], (self.player_x, player_y))

    def get_rect(self): # VERIFICAR APLICAÇÃO DE SELF
        return pygame.Rect(self.player_x, player_y, 80, 80)

# CLASSE: Base
class Base:

    def __init__(self):

        self.tamanho_coletavel = 40
        self.alturas_coletaveis = [565, 480, 460]
        self.distancia_minima_x = 250
        sprites_coletaveis = [pygame.transform.scale(img, (self.tamanho_coletavel, self.tamanho_coletavel)) for img in sprites_coletaveis]

    def gerar_coletavel(self, sprite_coletavel, alturas_ocupadas, xs_ocupados, largura_tela):  # VERIFICAR APLICAÇÃO DE SELF
        alturas_disponiveis = [h for h in self.alturas_coletaveis if h not in alturas_ocupadas]
        if not alturas_disponiveis:
            altura = random.choice(self.alturas_coletaveis)
        else:
            altura = random.choice(alturas_disponiveis)

        tentativas = 0
        while True:
            x = random.randint(largura_tela + 200, largura_tela + 900)
            if all(abs(x - outro_x) >= self.distancia_minima_x for outro_x in xs_ocupados):
                break
            tentativas += 1
            if tentativas > 10:
                break

        return {
            "rect": pygame.Rect(x, altura, self.tamanho_coletavel, self.tamanho_coletavel),
            "coletavel": sprite_coletavel,
        }

# CLASSE: Banana
class Banana(Base):
    
    def efeito_banana(contadores):
        contadores[sprites_coletaveis[2]] = 0
        contadores[sprites_coletaveis[0]] += 1

# CLASSE: Câmera
class Camera(Base):

    def __init__(self):
        self.flash = False
        self.flash_raio = 0
        self.flash_velocidade = 25
        self.flash_raio_max = 0
        self.flash_tempo_tela_total = 0
        self.flash_duracao_tela_total = 30

    def efeito_camera(contadores):
        contadores[sprites_coletaveis[1]] += 1

    def iniciar_flash(largura_tela, altura_tela):
        global flash, flash_raio, flash_raio_max, flash_tempo_tela_total
        flash = True
        flash_raio = 0
        flash_raio_max = int(math.hypot(largura_tela, altura_tela))
        flash_tempo_tela_total = 0

    def desenhar_flash(self, tela, dimensoes_tela): # VERIFICAR APLICAÇÃO DE SELF
        global flash, flash_raio, flash_tempo_tela_total

        if not flash:
            return

        flash_surface = pygame.Surface(dimensoes_tela, pygame.SRCALPHA)

        if flash_raio < flash_raio_max:
            flash_raio += self.flash_velocidade
            pygame.draw.circle(
                flash_surface,
                (255, 255, 255, 255),
                (dimensoes_tela[0] // 2, dimensoes_tela[1] // 2),
                flash_raio
            )
        else:
            flash_surface.fill((255, 255, 255))
            flash_tempo_tela_total += 1

            if flash_tempo_tela_total >= self.flash_duracao_tela_total:
                flash = False

        tela.blit(flash_surface, (0, 0))

# CLASSE: Rosa
class Rosa(Base):
    from coletaveis.base import (
    sprites_coletaveis
    )

    def efeito_rosa(contadores):
        contadores[sprites_coletaveis[2]] += 1

#--------#
#  main  #
#--------#

def main():

    # importando funções da mecânica de jogo
    from cenarios.desfile import iniciar_passarela
    from personagens.gisele import (
        atualizar_fisica,
        atualizar_animacao,
        pular,
        desenhar,
        get_rect
    )
    from coletaveis.base import (
        gerar_coletavel,
        sprites_coletaveis
    )
    from coletaveis.banana import efeito_banana
    from coletaveis.camera import (
        efeito_camera,
        iniciar_flash,
        desenhar_flash
    )
    from coletaveis.rosa import efeito_rosa

    # configurando cenário
    bg_image, bg_width, tiles, scroll = iniciar_passarela(
        dimensoes_tela,
        largura_tela
    )

    # definindo distância
    distancia_pixels = 0
    pixels_por_metro = 20
    meta_metros = 700

    # dicionários com os contadores
    contadores = {
        sprites_coletaveis[0]: 0,   # banana
        sprites_coletaveis[1]: 0,   # câmera
        sprites_coletaveis[2]: 0    # rosa
    }

    fonte = pygame.font.SysFont(None, 28)

    coletaveis = []

    for _ in range(3):
        alturas_ocupadas = [c["rect"].y for c in coletaveis]
        xs_ocupados = [c["rect"].x for c in coletaveis]
        sprite_coletavel = random.choice(sprites_coletaveis)
        coletaveis.append(
            gerar_coletavel(
                sprite_coletavel,
                alturas_ocupadas,
                xs_ocupados,
                largura_tela
            )
        )

    vel_coletavel = 7

    # loop principal
    while run:
        delta_time = relogio.tick(30) / 1000.0 # tempo decorrido em segundos

        for event in pygame.event.get(): # fechar a janela do jogo
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN: # identificar o w ou a seta do pulo
                if event.key == K_w or event.key == K_UP:
                    pular()

        # chamando as funções de gisele
        atualizar_fisica()
        atualizar_animacao(delta_time)

        # desenhando o cenário
        for i in range(tiles):
            tela.blit(bg_image, (i * bg_width + scroll, 0))

        scroll -= 7
        if abs(scroll) > bg_width:
            scroll = 0

        # incrementando a distância percorrida
        distancia_pixels += 7
        distancia_metros = distancia_pixels // pixels_por_metro

        # acelerando o jogo a cada 100 metros
        if distancia_metros != 0 and distancia_metros % 100 == 0:
            vel_coletavel += 2
            pixels_por_metro += 5.7

        # movimentação dos coletáveis
        for coletavel in coletaveis:
            coletavel["rect"].x -= vel_coletavel

            if coletavel["rect"].right < 0:
                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
                coletavel.update(
                    gerar_coletavel(
                        random.choice(sprites_coletaveis),
                        alturas_ocupadas,
                        xs_ocupados,
                        largura_tela
                    )
                )

        gisele_rect = get_rect()

        # colisões
        for coletavel in coletaveis:
            if gisele_rect.colliderect(coletavel["rect"]):
                if coletavel["coletavel"] == sprites_coletaveis[2]:
                    efeito_rosa(contadores)
                else:
                    if coletavel["coletavel"] == sprites_coletaveis[0]:
                        efeito_banana(contadores)
                    elif coletavel["coletavel"] == sprites_coletaveis[1]:
                        efeito_camera(contadores)
                        iniciar_flash(largura_tela, altura_tela)

                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
                coletavel.update(
                    gerar_coletavel(
                        random.choice(sprites_coletaveis),
                        alturas_ocupadas,
                        xs_ocupados,
                        largura_tela
                    )
                )

        # mostrando os contadores na tela
        for coletavel in coletaveis:
            tela.blit(coletavel["coletavel"], (coletavel["rect"]))

        # mostrando gisele na tela
        desenhar(tela)

        # fundo cinza para exibir coletáveis e metragem
        fundo_x = 20
        fundo_y = 20
        fundo_largura = 250
        fundo_altura = 70

        pygame.draw.rect(
            tela,
            (180, 180, 180),
            (fundo_x, fundo_y, fundo_largura, fundo_altura)
        )
        pygame.draw.rect(
            tela,
            (126, 77, 113),
            (fundo_x, fundo_y, fundo_largura, fundo_altura),
            4
        )

        margin_x = fundo_x + 10

        texto_distancia = fonte.render(f"{distancia_metros} m", True, (0, 0, 0))
        tela.blit(texto_distancia, (margin_x, fundo_y + 45))

        for sprite in sprites_coletaveis:
            tela.blit(sprite, (margin_x + 5, fundo_y + 5, 20, 20))
            texto = fonte.render(str(contadores[sprite]), True, (0, 0, 0))
            tela.blit(texto, (margin_x + 50, fundo_y + 20))
            margin_x += 65

        # flash do paparazzi
        desenhar_flash(tela, dimensoes_tela)

        # fim do jogo
        if contadores[sprites_coletaveis[0]] >= 4 or contadores[sprites_coletaveis[1]] >= 4:
            run = False
        elif distancia_metros >= meta_metros:
            run = False

        pygame.display.update()
