import pygame 

pygame.init()

class Item:
    def __init__(self, imagem, som, tipo):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = imagem
        self.som = som
        self.quantidade_visivel = 0
        self.quantidade_visivel_max = 3
        self.tipo = tipo
        
    def spawn(self):
        if self.quantidade_visivel < self.quantidade_visivel_max:
            # aparece na tela em uma posição permitida

    def colisao(self):
        # soma um ao contador 
        # desaparece
        

