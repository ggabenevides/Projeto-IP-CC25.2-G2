import pygame
import os
import math

original_bg_image = pygame.image.load(
    os.path.join('assets', 'cenario', 'passarela.png')
).convert()

class Desfile:
    
    def iniciar_passarela(dimensoes_tela, largura_tela):
        bg_image = pygame.transform.scale(original_bg_image, dimensoes_tela)
        bg_width = bg_image.get_width()
        tiles = math.ceil(largura_tela / bg_width) + 1
        scroll = 0

        return bg_image, bg_width, tiles, scroll

