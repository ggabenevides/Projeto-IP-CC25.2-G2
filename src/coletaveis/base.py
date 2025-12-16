import pygame
import random

tamanho_coletavel = 30

alturas_coletaveis = [565, 480, 460]
distancia_minima_x = 250
cores_coletaveis = [(255, 200, 0), (0, 255, 255), (220, 0, 255)]

def gerar_coletavel(cor, alturas_ocupadas, xs_ocupados, largura_tela):
    alturas_disponiveis = [h for h in alturas_coletaveis if h not in alturas_ocupadas]
    if not alturas_disponiveis:
        altura = random.choice(alturas_coletaveis)
    else:
        altura = random.choice(alturas_disponiveis)

    tentativas = 0
    while True:
        x = random.randint(largura_tela + 200, largura_tela + 900)
        if all(abs(x - outro_x) >= distancia_minima_x for outro_x in xs_ocupados):
            break
        tentativas += 1
        if tentativas > 10:
            break

    return {
        "rect": pygame.Rect(x, altura, tamanho_coletavel, tamanho_coletavel),
        "cor": cor
    }
