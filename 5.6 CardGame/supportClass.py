from compositeDP import Component

class Support(Component):
    def operation(self) -> str:
        return 'Support'

class Divine(Component):
    '''
    Docstring:
    Support subclass
    '''
    def operation(self) -> str:
        return 'Divine'

class Cleric(Component):
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
        return 'Cleric'

class Druid(Component):
    '''
    Docstring:
    Divine subclass
    '''
    def operation(self) -> str:
        return 'Druid'

class Ninfa(Component):
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
        return 'Ninfa'