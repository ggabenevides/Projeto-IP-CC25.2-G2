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


def main():

    # importando funções da mecânica de jogo
    from cenarios.desfile import Desfile
    from personagens.gisele import Gisele
    from coletaveis.base import Base
    from coletaveis.banana import Banana
    from coletaveis.camera import Camera
    from coletaveis.rosa import Rosa

    # configurando cenário
    bg_image, bg_width, tiles, scroll = Desfile.iniciar_passarela(
        dimensoes_tela,
        largura_tela
    )

    # definindo distância
    distancia_pixels = 0
    pixels_por_metro = 20
    meta_metros = 700

    # dicionários com os contadores
    contadores = {
        Base.sprites_coletaveis[0]: 0,   # banana
        Base.sprites_coletaveis[1]: 0,   # câmera
        Base.sprites_coletaveis[2]: 0    # rosa
    }

    fonte = pygame.font.SysFont(None, 28)

    coletaveis = []

    for _ in range(3):
        alturas_ocupadas = [c["rect"].y for c in coletaveis]
        xs_ocupados = [c["rect"].x for c in coletaveis]
        sprite_coletavel = random.choice(Base.sprites_coletaveis)
        coletaveis.append(
            Base.gerar_coletavel(
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
                    Gisele.pular()

        # chamando as funções de gisele
        Gisele.atualizar_fisica()
        Gisele.atualizar_animacao(delta_time)

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
                    Base.gerar_coletavel(
                        random.choice(Base.sprites_coletaveis),
                        alturas_ocupadas,
                        xs_ocupados,
                        largura_tela
                    )
                )

        gisele_rect = Gisele.get_rect()

        # colisões
        for coletavel in coletaveis:
            if gisele_rect.colliderect(coletavel["rect"]):
                if coletavel["coletavel"] == Base.sprites_coletaveis[2]:
                    Rosa.efeito_rosa(contadores)
                else:
                    if coletavel["coletavel"] == Base.sprites_coletaveis[0]:
                        Banana.efeito_banana(contadores)
                    elif coletavel["coletavel"] == Base.sprites_coletaveis[1]:
                        Camera.efeito_camera(contadores)
                        Camera.iniciar_flash(largura_tela, altura_tela)

                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
                coletavel.update(
                    Base.gerar_coletavel(
                        random.choice(Base.sprites_coletaveis),
                        alturas_ocupadas,
                        xs_ocupados,
                        largura_tela
                    )
                )

        # mostrando os contadores na tela
        for coletavel in coletaveis:
            tela.blit(coletavel["coletavel"], (coletavel["rect"]))

        # mostrando gisele na tela
        Gisele.desenhar(tela)

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

        for sprite in Base.sprites_coletaveis:
            tela.blit(sprite, (margin_x + 5, fundo_y + 5, 20, 20))
            texto = fonte.render(str(contadores[sprite]), True, (0, 0, 0))
            tela.blit(texto, (margin_x + 50, fundo_y + 20))
            margin_x += 65

        # flash do paparazzi
        Camera.desenhar_flash(tela, dimensoes_tela)

        # fim do jogo
        if contadores[Base.sprites_coletaveis[0]] >= 4 or contadores[Base.sprites_coletaveis[1]] >= 4:
            run = False
        elif distancia_metros >= meta_metros:
            run = False

        pygame.display.update()
