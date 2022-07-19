from abc import abstractmethod

from chamaAPI import ConverterMoeda

# from main import Menu


class adaptando:
    @abstractmethod
    def get_moedaInicial(self):
        return super().get_moedaInicial

    @abstractmethod
    def get_valor(self):
        return super().get_valor

    @abstractmethod
    def get_moedaFinal(self):
        return super().get_moedaFinal


class adaptandoVisualizacao(ConverterMoeda):
    def visualizarTudo(self):
        return super().show_currencies()


if __name__ == '__main__':
    pessoa = ConverterMoeda('95cb7a414c4d5c073632')
    print(pessoa.transforme_currency('USD', 1, 'BRL'))
