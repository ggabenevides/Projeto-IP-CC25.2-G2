from coletaveis.base import Base
from coletaveis.base import (
    sprites_coletaveis
)
class Banana(Base):
    
    def efeito_banana(contadores):
        contadores[sprites_coletaveis[2]] = 0 # a banana faz ela perder todas as rosas
        contadores[sprites_coletaveis[0]] += 1
