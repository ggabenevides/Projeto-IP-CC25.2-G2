import pygame
from pygame.locals import *
from sys import exit
import math
import random

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
    cores_coletaveis
)
from coletaveis.banana import efeito_banana
from coletaveis.camera import (
    efeito_camera,
    iniciar_flash,
    desenhar_flash
)
from coletaveis.rosa import efeito_rosa

pygame.init()
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal')

# inicializando variáveis
altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)

tela = pygame.display.set_mode(dimensoes_tela)
relogio = pygame.time.Clock()
run = True

# configurando cenário
bg_image, bg_width, tiles, scroll = iniciar_passarela(
    dimensoes_tela,
    largura_tela
)

# definindo distância
distancia_pixels = 0
pixels_por_metro = 20
meta_metros = 300

# dicionários com os contadores (coletáveis temporários - amarelo: bananas; ciano: câmera; rosa: flores)
contadores = {
    (255, 200, 0): 0,   # amarelo
    (0, 255, 255): 0,   # ciano
    (220, 0, 255): 0    # rosa
}

fonte = pygame.font.SysFont(None, 28)

coletaveis = []

for _ in range(3):
    alturas_ocupadas = [c["rect"].y for c in coletaveis]
    xs_ocupados = [c["rect"].x for c in coletaveis]
    cor = random.choice(cores_coletaveis)
    coletaveis.append(
        gerar_coletavel(
            cor,
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

    # movimentação dos coletáveis
    for coletavel in coletaveis:
        coletavel["rect"].x -= vel_coletavel

        if coletavel["rect"].right < 0:
            alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
            xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
            coletavel.update(
                gerar_coletavel(
                    random.choice(cores_coletaveis),
                    alturas_ocupadas,
                    xs_ocupados,
                    largura_tela
                )
            )

    gisele_rect = get_rect()

    # colisões
    for coletavel in coletaveis:
        if gisele_rect.colliderect(coletavel["rect"]):
            if coletavel["cor"] == (255, 200, 0):
                efeito_banana(contadores)

            elif coletavel["cor"] == (0, 255, 255):
                efeito_camera(contadores)
                iniciar_flash(largura_tela, altura_tela)

            else:
                efeito_rosa(contadores)

            alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
            xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
            coletavel.update(
                gerar_coletavel(
                    random.choice(cores_coletaveis),
                    alturas_ocupadas,
                    xs_ocupados,
                    largura_tela
                )
            )

    # mostrando os contadores na tela
    for coletavel in coletaveis:
        pygame.draw.rect(tela, coletavel["cor"], coletavel["rect"])

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
        (100, 100, 100),
        (fundo_x, fundo_y, fundo_largura, fundo_altura),
        2
    )

    margin_x = fundo_x + 10

    texto_distancia = fonte.render(f"{distancia_metros} m", True, (0, 0, 0))
    tela.blit(texto_distancia, (margin_x, fundo_y + 45))

    for cor in cores_coletaveis:
        pygame.draw.rect(tela, cor, (margin_x, fundo_y + 10, 20, 20))
        texto = fonte.render(str(contadores[cor]), True, (0, 0, 0))
        tela.blit(texto, (margin_x + 25, fundo_y + 10))
        margin_x += 65

    # flash do paparazzi
    desenhar_flash(tela, dimensoes_tela)

    # fim do jogo
    if distancia_metros >= meta_metros:
        run = False

    pygame.display.update()
