from coletaveis.base import (
    sprites_coletaveis
)

def efeito_banana(contadores):
    contadores[sprites_coletaveis[2]] = 0
    contadores[sprites_coletaveis[0]] += 1
