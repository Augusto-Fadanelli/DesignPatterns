from compositeDP import *

class Support(Composite):
    def operation(self) -> str:
        return super().operation(name='Support')

class Divine(Composite):
    '''
    Docstring:
    Support branch
    '''
    def operation(self) -> str:
        return super().operation(name='Divine')

class Cleric(Leaf):
    '''
    Docstring:
    Divine leaf
    '''
    def __init__(self):
        self._atk = 11
        self._def = 10

    def description(self):
        return 'Um excelente suporte de cura para ajudar as suas tropas,\n' \
        'podendo até mesmo morrer para salvar seus companheiros.'

    def operation(self) -> str:
        return super().operation(name='Cleric')

class Druid(Composite):
    '''
    Docstring:
    Divine branch
    '''
    def operation(self) -> str:
        return super().operation(name='Druid')

class Nymph(Leaf):
    '''
    Docstring:
    Druid leaf
    '''
    def __init__(self):
        self._atk = 11
        self._def = 7

    def description(self):
        return 'Não são tão fortes quanto os outros combatentes, porém,\n' \
        'são de grande ajuda em uma guerra, podendo curar tropas e até a si mesmo.'

    def operation(self) -> str:
        return super().operation(name='Nymph')
