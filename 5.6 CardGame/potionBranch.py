from compositeDP import *

class Potion(Composite):
    def operation(self) -> str:
        return super().operation(name='Potion')

class CurePotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Potion of Cure')

class WeaknessPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Potion of Weakness')

class StrengthPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Potion of Strength')

class PoisonPotion(Leaf):
    '''
    Docstring:
    Potion leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Potion of Poison')