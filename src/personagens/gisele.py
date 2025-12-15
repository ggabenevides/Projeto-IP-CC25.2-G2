import pygame
import os

ANDANDO = [pygame.image.load(os.path.join("assets/gisele", "sprite_0.png")),
           pygame.image.load(os.path.join("assets/gisele", "sprite_1.png")),
           pygame.image.load(os.path.join("assets/gisele", "sprite_2.png"))]
PULANDO = pygame.image.load(os.path.join("assets/gisele", "sprite_1.png")) # enquanto ela não estiver tocando no chão, ela fica "parada"

class Gisele:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.andando_animacao = ANDANDO
        self.pulando_animacao = PULANDO

        self.pulando = False
        self.andando = True

    def pulo(self):




