from prototype import Prototype
import copy
import time

class SummonerElf(Prototype):
    def __init__(self, age, defense, attack):
        super().__init__()
        time.sleep(4)
        self.age = age
        self.defense = defense
        self.attack = attack
        # Atributo exclusivo da classe Elfo Invocador
        self.powerNature = 60
        
    def description(self):
        return 'Elfos invocadores necessitam de muita magia para realizar seus feitos, \n' \
        'mas em contrapartida estes feitos são Grandiosos. Invocam seres de qualquer tipo, \n' \
        'desde um inseto até um mamute ou coisa maior.'

    def clone(self):
        return copy.deepcopy(self)