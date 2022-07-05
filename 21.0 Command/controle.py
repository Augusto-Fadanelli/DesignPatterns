
from command import Command

class Controle:
    
    def enviarComandoSimples(self, command: Command):
        self.comandoSimples = command

    def enviarComandoComplexo(self, command: Command):
        self.comandoComplexo = command

    def fazer(self):
        print("OK, vou executar para você")
        if(self.comandoSimples is Command):
            self.comandoSimples.executar()

        if(self.comandoComplexo is Command):
            self.comandoComplexo.executar()

