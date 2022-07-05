
from command import Command

class SimplesComando(Command):

    def __init__(self, solicitacao):
        self._solicitacao = solicitacao
    
    def setSimplesComando(self, solicitacao):
        self._solicitacao = solicitacao

    def executar(self):
        print(f"Estou executando um simples comando de {self._solicitacao}") 

