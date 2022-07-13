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
        return 'Poção para recuperar HP, feita pelos melhores Druidas de todo o mundo.'

    def operation(self) -> str:
        return super().operation(name='Potion of Cure')

class WeaknessPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Uma poção que causa fraqueza em todos àqueles que beberem ou inalarem,\n' \
        'podendo ser o fim da vida daquele que estiver no caminho.'

    def operation(self) -> str:
        return super().operation(name='Potion of Weakness')

class StrengthPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Também conhecida como Força de Hércules, essa poção é\n' \
        'capaz de aumentar a força de quem à consumir.'

    def operation(self) -> str:
        return super().operation(name='Potion of Strength')

class PoisonPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def description(self):
        return 'Um veneno extraído da criatura mais perigosa do mundo, tão logo\n' \
        'o ato de buscar e preparar essa poção pode matá-lo.'

    def operation(self) -> str:
        return super().operation(name='Potion of Poison')