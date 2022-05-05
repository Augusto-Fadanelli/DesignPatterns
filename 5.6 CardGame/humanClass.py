from compositeDP import Component

class Human(Component):
    def operation(self) -> str:
         return 'Human'

class Knight(Component):
    '''
    Docstring:
    Human subclass
    '''
    def operation(self) -> str:
        return 'Knight'

class Templar(Component):
    '''
    Docstring:
    Knight leaf
    '''
    def __init__(self):
        self._atk = 10
        self._def = 10

    def description(self):
        return 'Descrição da carta em português\nNão esqueça das quebras de linha'

    def operation(self) -> str:
        return 'Templar'

class Paladin(Component):
    '''
    Docstring:
    Knight leaf
    '''
    def operation(self) -> str:
        return 'Paladin'

class Assassin(Component):
    '''
    Docstring:
    Human subclass
    '''
    def operation(self) -> str:
        return 'Assassin'

class Ninja(Component):
    '''
    Docstring:
    Assassin leaf
    '''
    def operation(self) -> str:
        return 'Ninja'

class StealthKiller(Component):
    '''
    Docstring:
    Assassin leaf
    '''
    def operation(self) -> str:
        return 'Stealth Killer'

class Fighter(Component):
    '''
    Docstring:
    Human leaf
    '''
    def operation(self) -> str:
        return 'Fighter'