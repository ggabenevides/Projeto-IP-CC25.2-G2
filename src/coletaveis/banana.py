from coletaveis.base import Base
base_engine = Base()
class Banana(Base):
    
    def efeito_banana(contadores):
        contadores['rosa'] = 0 # a banana faz ela perder todas as rosas
        contadores['banana'] += 1
