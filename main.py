import pygame 
from pygame.locals import *
from sys import exit
import os
import math

pygame.init() 
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal')

altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)

tela = pygame.display.set_mode(dimensoes_tela)
original_bg_image = pygame.image.load(os.path.join('assets', 'cenario', 'passarela.png')).convert()
bg_image = pygame.transform.scale(original_bg_image, dimensoes_tela)
bg_width = bg_image.get_width()

tiles = math.ceil(largura_tela / bg_width) + 1
buff_ativo = False
debuff_ativo = False
tempo_ativo = 0
relogio = pygame.time.Clock()
run = True
scroll = 0

while run:  # loop principal
        delta_time = relogio.tick(30) / 1000.0  # tempo decorrido em segundos

        for event in pygame.event.get():  # fechar a janela do jogo
            if event.type == QUIT:
                run = False
                pygame.quit()
                exit()

        # desenhando o cenário
        for i in range(0, tiles):
            tela.blit(bg_image, (i * bg_width + scroll, 0))
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

        pygame.display.update()           