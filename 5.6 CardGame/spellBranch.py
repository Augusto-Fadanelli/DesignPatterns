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
        return 'A melhor legião de elfos arqueiros junta-se para criar a tão temida chuva de flechas.\n' \
        'Sendo bem utilizada ela é capaz de dizimar um exército inteiro.'

    def operation(self) -> str:
        return super().operation(name='Fire Rain')

class TrailOfDead(Leaf):
    '''
    Docstring:
    Spell leaf
    '''
    def description(self):
        return 'Um poder tão forte nas mãos certas pode decidir o destino de uma batalha,\n' \
        'com apenas um gesto você é capaz de invocar os mortos para lutar ao seu lado.'

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
        return 'Com o poder divino os clérigos irão ajudá-lo a recuperar vida.'

    def operation(self) -> str:
        return super().operation(name='Esculápio')

class NightHerbs(Leaf):
    '''
    Docstring:
    HealingSpell leaf
    '''
    def description(self):
        return 'Um poder de cura preparado pelos melhores druidas que irão ajudar em sua batalha.'

    def operation(self) -> str:
        return super().operation(name='Night Herbs')

