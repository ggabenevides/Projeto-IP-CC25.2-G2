import pygame
import math

flash = False
flash_raio = 0
flash_velocidade = 25
flash_raio_max = 0
flash_tempo_tela_total = 0
flash_duracao_tela_total = 30


def efeito_camera(contadores):
    contadores[(0, 255, 255)] += 1


def iniciar_flash(largura_tela, altura_tela):
    global flash, flash_raio, flash_raio_max, flash_tempo_tela_total
    flash = True
    flash_raio = 0
    flash_raio_max = int(math.hypot(largura_tela, altura_tela))
    flash_tempo_tela_total = 0


def desenhar_flash(tela, dimensoes_tela):
    global flash, flash_raio, flash_tempo_tela_total

    if not flash:
        return

    flash_surface = pygame.Surface(dimensoes_tela, pygame.SRCALPHA)

    if flash_raio < flash_raio_max:
        flash_raio += flash_velocidade
        pygame.draw.circle(
            flash_surface,
            (255, 255, 255, 255),
            (dimensoes_tela[0] // 2, dimensoes_tela[1] // 2),
            flash_raio
        )
    else:
        flash_surface.fill((255, 255, 255))
        flash_tempo_tela_total += 1

        if flash_tempo_tela_total >= flash_duracao_tela_total:
            flash = False

    tela.blit(flash_surface, (0, 0))
