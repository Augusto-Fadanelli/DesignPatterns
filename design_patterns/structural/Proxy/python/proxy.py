
from api import ConverterMoeda


class Substituindo(ConverterMoeda):
    
    #Mostrando todas as moedas disponiveis
    def importacao(self):
        return super().show_currencies()
    
    #Convertendo a moeda
    def conversao(self):
        return super().transforme_currency()



if __name__ == "__main__":
    pessoa = Substituindo()
    print(pessoa.conversao("USD", 1, "BRL"))