from produto import MinhaCadeira


class CadeiraGrande(MinhaCadeira):
    def __init__(self):
        self.height = 100
        self.width = 60
        self.depth = 60

    def get_dimensao(self):
        return {
            'Altura': self.height,
            'Largura': self.width,
            'Profundidade': self.depth,
        }
