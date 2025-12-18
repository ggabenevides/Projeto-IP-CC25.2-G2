import pygame
import random
import os

class Base:

    def __init__(self):

        self.sprites_coletaveis = [
            pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'cascaDeBanana.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'flash.png')).convert_alpha(),
            pygame.image.load(os.path.join('assets', 'sprites', 'coletaveis', 'rosa.png')).convert_alpha(),]

        self.tamanho_coletavel = 40
        self.alturas_coletaveis = [565, 480, 460]
        self.distancia_minima_x = 250
        self.sprites_coletaveis = [pygame.transform.scale(img, (self.tamanho_coletavel, self.tamanho_coletavel)) for img in self.sprites_coletaveis]

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