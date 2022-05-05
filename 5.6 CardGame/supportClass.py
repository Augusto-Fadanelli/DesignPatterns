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
    def operation(self) -> str:
        return 'Ninfa'