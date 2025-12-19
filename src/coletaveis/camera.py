import pygame
import math
from coletaveis.base import Base

base_engine = Base()
class Camera(Base):

    def __init__(self):
        self.flash = False
        self.flash_raio = 0
        self.flash_velocidade = 25
        self.flash_raio_max = 0
        self.flash_tempo_tela_total = 0
        self.flash_duracao_tela_total = 30

    def efeito_camera(contadores):
        contadores['camera'] += 1

    def iniciar_flash(self, largura_tela, altura_tela):
        self.flash = True
        self.flash_raio = 0
        self.flash_raio_max = int(math.hypot(largura_tela, altura_tela))
        self.flash_tempo_tela_total = 0

    def desenhar_flash(self, tela, dimensoes_tela): # VERIFICAR APLICAÇÃO DE SELF
        if not self.flash:
            return

        flash_surface = pygame.Surface(dimensoes_tela, pygame.SRCALPHA)

        if self.flash_raio < self.flash_raio_max:
            self.flash_raio += self.flash_velocidade
            pygame.draw.circle(
                flash_surface,
                (255, 255, 255, 255),
                (dimensoes_tela[0] // 2, dimensoes_tela[1] // 2),
                self.flash_raio
            )
        else:
            flash_surface.fill((255, 255, 255))
            self.flash_tempo_tela_total += 1

            if self.flash_tempo_tela_total >= self.flash_duracao_tela_total:
                self.flash = False

        tela.blit(flash_surface, (0, 0))
