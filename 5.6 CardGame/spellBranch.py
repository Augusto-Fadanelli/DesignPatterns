from compositeDP import *

class Spell(Composite):
    def operation(self) -> str:
        return super().operation(name='Spell')

class FireRain(Leaf):
    '''
    Docstring:
    Spell leaf
    '''
    def description(self):
        return 'A melhor legião de elfos arqueiros se juntam se para\n'
        'criar a tão temida chuva de flechas, sendo bem utilida ela é capaz de dizimar um exercito'

    def operation(self) -> str:
        return super().operation(name='Fire Rain')

class TrailOfDead(Leaf):
    '''
    Docstring:
    Spell leaf
    '''
    def description(self):
        return 'Um poder tão forte nas maão certas pode decidir o destino de uma\n'
        'batalha, com apenas um jesto voceê é capaz de invocar os mortos para lutar ao seu lado'

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
    def description(self):
        return 'Com o poder divino os clerigos irão ajuda-lo a recuperar vida'

    def operation(self) -> str:
        return super().operation(name='Esculápio')

class NightHerbs(Leaf):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def description(self):
        return 'Um poder de cura conjurado pelos melhores druidas que irão ajudar em sua batalha'

    def operation(self) -> str:
        return super().operation(name='Night Herbs')

