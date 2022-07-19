from icommand import ICommand
from light import Ligth


class LigthOnCommand(ICommand):
    """Comando Concreto"""

    def __init__(self, ligth: Ligth):
        self.ligth = ligth

    def execute(self):
        self.ligth.on()

    def undo(self):
        self.ligth.off()
