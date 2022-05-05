from compositeDP import Component

class Spell(Component):
    def operation(self) -> str:
        return 'Spell'

class FireRain(Component):
    '''
    Docstring:
    Spell leaf
    '''
    def operation(self) -> str:
        return 'Fire Rain'

class TrailOfDead(Component):
    '''
    Docstring:
    Spell leaf
    '''
    def operation(self) -> str:
        return 'Trail of Dead'

class HealingSpell(Component):
    '''
    Docstring:
    Spell subclass
    '''
    def operation(self) -> str:
        return 'Healing Spell'

class Esculapio(Component):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def operation(self) -> str:
        return 'Esculapio'

class NightHerbs(Component):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def operation(self) -> str:
        return 'Night Herbs'

