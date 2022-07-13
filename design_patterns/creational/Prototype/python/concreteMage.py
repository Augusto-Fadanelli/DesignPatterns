from prototype import Prototype
import copy
import time

#Foi adicionado o time para representar o tempo que demora para o 
#Mago ser produzido similar a um jogo. Isso não significa quer é o
#tempo de instanciação, e sim o tempo que representa a criação do personagem.

class Mage(Prototype):
    def __init__(self, age, defense, attack):
        time.sleep(7)
        self.age = age
        self.defense = defense
        self.attack = attack
        #Atributo exclusivo da classe Mago
        self.mana = 100
        
    def description(self):
        return 'Extremamente podereso, sábio e com boas intenções.\n' \
        'Esse mago usa de todo seu conhecimento para deter as forças que atarapalham' \
        'o sossego dos inocentes.'

    def clone(self):
        return copy.deepcopy(self) 