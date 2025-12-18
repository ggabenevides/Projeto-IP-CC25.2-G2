import pygame
import math
from coletaveis.base import Base
from coletaveis.base import (
    sprites_coletaveis
)

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
