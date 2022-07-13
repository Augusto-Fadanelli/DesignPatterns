from compositeDP import *

class Human(Composite):
    def operation(self) -> str:
         return super().operation(name='Human')

class Knight(Composite):
    '''
    Docstring:
    Human branch
    '''
    def operation(self) -> str:
        return super().operation(name='Knight')

class Templar(Leaf):
    '''
    Docstring:
    Knight leaf
    '''
    def __init__(self):
        self._atk = 16
        self._def = 10

    def description(self):
        return 'Um cavaleiro Templário devoto as leis de Deus. Ele fará de tudo\n' \
        'para ganhar uma guerra, mesmo que isso custe sua vida.'

    def operation(self) -> str:
        return super().operation(name='Templar')

class Paladin(Leaf):
    '''
    Docstring:
    Knight leaf
    '''
    def __init__(self):
        self._atk = 8
        self._def = 20

    def description(self):
        return 'Um paladino se destaca pela sua força e resistência, podendo aguentar\n' \
        'vários ataques de uma só vez. Com toda certeza tê-lo em sua equipe é um passo para a vitória'

    def operation(self) -> str:
        return super().operation(name='Paladin')

class Assassin(Composite):
    '''
    Docstring:
    Human branch
    '''
    def operation(self) -> str:
        return super().operation(name='Assassin')

class Ninja(Leaf):
    '''
    Docstring:
    Assassin leaf
    '''
    def __init__(self):
        self._atk = 14
        self._def = 8

    def description(self):
        return 'Também chamado de demônio negro, esse é o ninja. Sempre faz seus ataques\n' \
        'de maneira rápida e furtiva.'

    def operation(self) -> str:
        return super().operation(name='Ninja')

class StealthKiller(Leaf):
    '''
    Docstring:
    Assassin leaf
    '''
    def __init__(self):
        self._atk = 12
        self._def = 10

    def description(self):
        return 'Um assassino sabe aproveitar a distração do inimigo para atingi-lo em pontos vitais.\n' \
        'Ótimo atirador e também um combatente corpo a corpo.'

    def operation(self) -> str:
        return super().operation(name='Stealth Killer')

class Fighter(Leaf):
    '''
    Docstring:
    Human leaf
    '''
    def description(self):
        return 'Um mestre na arte da luta sempre vai ser uma ótima escolha no campo de batalha. Caso ele\n' \
               'seja seu inimigo, sugiro que corra pois tudo que eles mais querem é ganhar e não vão\n' \
               'deixar ninguém em seu caminho'

    def operation(self) -> str:
        return super().operation(name='Fighter')