from objeto import ObjetoInterface
from proxy import Substituindo


class ObjetoConexaoProxy(ObjetoInterface):
    def MetodoAbstrato():
        return super().interface()


class Importacao(Substituindo):
    def mostrandoMoedas():
        return super().importacao()


class Conversao(Substituindo):
    def convertendoMoeda():
        return super().conversao()
