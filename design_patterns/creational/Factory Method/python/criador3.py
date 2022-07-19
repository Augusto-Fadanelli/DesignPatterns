from produto import MinhaCadeira


class CadeiraPequena(MinhaCadeira):
    def __init__(self):
        self.height = 25
        self.width = 30
        self.depth = 20

    def get_dimensao(self):
        return {
            'Altura': self.height,
            'Largura': self.width,
            'Profundidade': self.depth,
        }
