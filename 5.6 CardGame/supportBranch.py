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
        return 'Um excelente suporte de cura, para ajudar suas tropas,\n'
        'podendo ate mesmo morrer para salvar seus companheiros'

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
        return 'Não são tão fortes quantos os outros fortes em combate, porem,\n' 
        'são de grande ajuda em uma guerra, podendo curar tropas e ate a si mesmo'

    def operation(self) -> str:
        return super().operation(name='Nymph')
