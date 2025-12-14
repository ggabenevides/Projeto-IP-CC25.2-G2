import pygame 
from pygame.locals import *
from sys import exit
import os
import math

pygame.init() 
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal')

bg_image = pygame.image.load(os.path.join('assets', 'cenario', 'passarela.png'))
bg_width = bg_image.get_width()

altura_tela = 690
largura_tela = 1300
dimensoes_tela = (largura_tela, altura_tela)
tela = pygame.display.set_mode(dimensoes_tela)
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
            scroll -= 20
            tempo_ativo += 1
            if tempo_ativo >= 100:
                buff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 10

        if debuff_ativo:
            buff_ativo = False
            scroll -= 1
            tempo_ativo += 1
            if tempo_ativo >= 100:
                debuff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 10

        # reset scroll do cenario
        if abs(scroll) > bg_width:
            scroll = 0            