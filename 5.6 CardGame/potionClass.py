from compositeDP import Component

class Potion(Component):
    def operation(self) -> str:
        return 'Potion'

class CurePotion(Component):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return 'Potion of Cure'

class WeaknessPotion(Component):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return 'Potion of Weakness'

class StrengthPotion(Component):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return 'Potion of Strength'

class PoisonPotion(Component):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return 'Potion of Poison'