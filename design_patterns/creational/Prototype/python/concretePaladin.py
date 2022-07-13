from prototype import Prototype
import copy
import time

#Foi adicionado o time para representar o tempo que demora para o 
#Paladino ser produzido similar a um jogo. Isso não significa quer é o
#tempo de instanciação, e sim o tempo que representa a criação do personagem.

class Paladin(Prototype):
    def __init__(self, age, defense, attack):
        time.sleep(5)
        self.age = age
        self.defense = defense
        self.attack = attack
        #Atributo exclusivo da classe Paladino
        self.stamina = 60
        
    def description(self):
        return 'Um paladino se destaca pela sua força e resistência, podendo aguentar\n' \
        'vários ataques de uma só vez. Com toda certeza tê-lo em sua equipe é um passo para a vitória'

    def clone(self):
        return copy.deepcopy(self)  