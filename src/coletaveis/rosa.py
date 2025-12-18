from coletaveis.base import Base

class Rosa(Base):

    def efeito_rosa(contadores):
        contadores['rosa'] += 1
