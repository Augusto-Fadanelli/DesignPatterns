from compositeDP import *

class Spell(Composite):
    def operation(self) -> str:
        return super().operation(name='Spell')

class FireRain(Leaf):
    '''
    Docstring:
    Spell leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Fire Rain')

class TrailOfDead(Leaf):
    '''
    Docstring:
    Spell leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Trail of Dead')

class HealingSpell(Composite):
    '''
    Docstring:
    Spell branch
    '''
    def operation(self) -> str:
        return super().operation(name='Healing Spell')

class Esculapio(Leaf):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Esculápio')

class NightHerbs(Leaf):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Night Herbs')

