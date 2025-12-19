import pygame
from pygame.locals import *
from sys import exit
import random
import os

# inicializando pygame + criando tela + inicializando variáveis globais + acelerando gradualmente jogo
altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)
pygame.init()    
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal')
tela = pygame.display.set_mode(dimensoes_tela)
relogio = pygame.time.Clock()
ACELERAR = pygame.USEREVENT + 1
pygame.time.set_timer(ACELERAR, 10000)

# importando classes
from cenarios.desfile import Desfile
from personagens.gisele import Gisele
from coletaveis.base import Base
from coletaveis.banana import Banana
from coletaveis.camera import Camera
from coletaveis.rosa import Rosa

# instanciando objetos para acessar a classe
base_engine = Base()
gisele = Gisele()
banana = Banana()
camera = Camera()

# carregando imagens
FONTE_HUD = pygame.font.Font(os.path.join('assets', 'fonte', 'fonte.ttf'), 20)
HUD_BG = pygame.image.load(os.path.join('assets', 'cenario', 'placa_contadores1.png')).convert_alpha()
HUD_BG = pygame.transform.scale(HUD_BG, (250, 110))
LINHA_CHEGADA = pygame.image.load(os.path.join('assets', 'cenario', 'passarela_chegada.png')).convert_alpha()
LINHA_CHEGADA = pygame.transform.scale(LINHA_CHEGADA, dimensoes_tela)

def main():

    global run 
    run = True
    finalizando = False
    scroll_final = 0

    # configurando cenário
    bg_image, bg_width, tiles, scroll = Desfile.iniciar_passarela(dimensoes_tela, largura_tela)

    # definindo distância
    distancia_pixels = 0
    pixels_por_metro = 20
    meta_metros = 500

    # dicionários com os contadores
    contadores = {
        "banana": 0,   
        "camera": 0,   
        "rosa": 0    
    }

    coletaveis = []

    for _ in range(3):
        alturas_ocupadas = [c["rect"].y for c in coletaveis]
        xs_ocupados = [c["rect"].x for c in coletaveis]
        sprite_coletavel = random.choice(base_engine.sprites_coletaveis)
        coletaveis.append(
            base_engine.gerar_coletavel(
                sprite_coletavel,
                alturas_ocupadas,
                xs_ocupados,
                largura_tela
            )
        )

    vel_coletavel = 7

    # loop principal
    while run:
        # variaveis locais
        delta_time = relogio.tick(30) / 1000.0 # tempo decorrido em segundos
        meta_metros = 500
        tela.fill((0,0,0))

        for event in pygame.event.get(): 
            if event.type == QUIT: # fechar a janela do jogo
                pygame.quit()
                exit()

            if event.type == KEYDOWN: # identificar o w ou a seta do pulo ou espaço
                if event.key == K_w or event.key == K_UP or event.key == K_SPACE:
                    gisele.pular()

            if event.type == ACELERAR and vel_coletavel < 20:
                vel_coletavel += 1

        # chamando as funções de gisele
        gisele.atualizar_fisica()
        gisele.atualizar_animacao(delta_time)

        if not finalizando:
            for i in range(tiles):
                tela.blit(bg_image, (i * bg_width + scroll, 0))
            scroll -= (7 + vel_coletavel)
            if abs(scroll) > bg_width:
                scroll = 0
        else:
            # estado de finalização: o cenário para de rodar em loop
            # e desenhamos a passarela de chegada deslizando uma única vez
            tela.blit(LINHA_CHEGADA, (0, 0))/
            
            if largura_tela + scroll_final > 0:
                scroll_final -= 7 # velocidade da linha entrando na tela
                scroll -= vel_coletavel
            
            gisele.player_x += 5

            if gisele.player_x >= largura_tela:
                 run = False # fim do jogo / tela de vitória

        scroll -= vel_coletavel
        if abs(scroll) > bg_width:
            scroll = 0

        # incrementando a distância percorrida
        distancia_pixels += 7
        distancia_metros = distancia_pixels // pixels_por_metro

        # movimentação dos coletáveis
        if not finalizando:
            for coletavel in coletaveis:
                coletavel["rect"].x -= vel_coletavel

                if coletavel["rect"].right < 0:
                    alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                    xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
                    coletavel.update(
                        base_engine.gerar_coletavel(
                            random.choice(base_engine.sprites_coletaveis),
                            alturas_ocupadas,
                            xs_ocupados,
                            largura_tela
                        )
                    )

            gisele_rect = gisele.get_rect()

        # colisões
        for coletavel in coletaveis:
            if gisele_rect.colliderect(coletavel["rect"]):
                if coletavel["coletavel"] == base_engine.sprites_coletaveis[2]:
                    Rosa.efeito_rosa(contadores)
                else:
                    if coletavel["coletavel"] == base_engine.sprites_coletaveis[0]:
                        Banana.efeito_banana(contadores)
                    elif coletavel["coletavel"] == base_engine.sprites_coletaveis[1]:
                        Camera.efeito_camera(contadores)
                        camera.iniciar_flash(largura_tela, altura_tela)

                alturas_ocupadas = [c["rect"].y for c in coletaveis if c != coletavel]
                xs_ocupados = [c["rect"].x for c in coletaveis if c != coletavel]
                coletavel.update(
                    base_engine.gerar_coletavel(
                        random.choice(base_engine.sprites_coletaveis),
                        alturas_ocupadas,
                        xs_ocupados,
                        largura_tela
                    )
                )

        # mostrando os contadores na tela
        for coletavel in coletaveis:
            tela.blit(coletavel["coletavel"], (coletavel["rect"]))

        # mostrando gisele na tela
        gisele.desenhar(tela)

        # HUD 
        fundo_x = 20
        fundo_y = 20
        fundo_largura = 250
        fundo_altura = 90
        fonte = pygame.Font((os.path.join('assets', 'fonte', 'fonte.ttf')), 20)

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

        margin_x = fundo_x + 20

        texto_distancia = FONTE_HUD.render(f"{distancia_metros} m", True, (0, 0, 0))
        tela.blit(texto_distancia, (margin_x, fundo_y + 55))

        icones = ["banana", "camera", "rosa"]
        for i, sprite in enumerate(base_engine.sprites_coletaveis):
            tela.blit(sprite, (margin_x, 25))
            nome_item = icones[i]
            texto = FONTE_HUD.render(str(contadores[nome_item]), True, (0, 0, 0))
            tela.blit(texto, (margin_x + 45, 30))
            margin_x += 65

        # flash do paparazzi
        camera.desenhar_flash(tela, dimensoes_tela)

        # fim do jogo
        if contadores["banana"] >= 3 or contadores["camera"] >= 3:
            run = False
            perdeu = True
            # tela de game over
        elif distancia_metros >= meta_metros-50:
            finalizando = True

        pygame.display.update()

# chamando função principal
if __name__ == "__main__":
    main()
