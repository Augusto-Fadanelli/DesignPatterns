from compositeDP import Component

class Land(Component):
    def operation(self) -> str:
        return 'Land'

class FlatLand(Component):
    '''
    Docstring:
    Land leaf
    '''
    def operation(self) -> str:
        return 'Flat Land'

class Hell(Component):
    '''
    Docstring:
    Land leaf
    '''
    def operation(self) -> str:
        return 'Hell'

class Forest(Component):
    '''
    Docstring:
    Land leaf
    '''
    def operation(self) -> str:
        return 'Forest'
