from compositeDP import *

class Potion(Composite):
    def operation(self) -> str:
        return super().operation(name='Potion')

class CurePotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Porção para recuperar HP, feita pelos melhores Druidas de todo o mundo'

    def operation(self) -> str:
        return super().operation(name='Potion of Cure')

class WeaknessPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Uma porção que causa fraqueza em todos aqueles que beberem ou inalarem\n'
        'podendo ser o fim da vida daquele que estiver no caminho'

    def operation(self) -> str:
        return super().operation(name='Potion of Weakness')

class StrengthPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Também conhecida como Força de Hércules essa porção é\n'
        'capaz de aumentar a força de seu usuário em 2x'

    def operation(self) -> str:
        return super().operation(name='Potion of Strength')

class PoisonPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Veneno da criatura mais perigosa do mundo, apenas o ato de\n'
        'buscar e preparar essa porção torna ela a mais perigosa.'

    def operation(self) -> str:
        return super().operation(name='Potion of Poison')