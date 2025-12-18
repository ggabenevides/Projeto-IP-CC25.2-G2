from coletaveis.base import Base

class Rosa(Base):

    def efeito_rosa(contadores):
        contadores[Base.sprites_coletaveis[2]] += 1
