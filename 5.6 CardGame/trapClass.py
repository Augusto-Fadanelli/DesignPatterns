from compositeDP import Component

class Trap(Component):
    def operation(self) -> str:
        return 'Trap'

class MeteorRain(Component):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return 'Meteor Rain'

class Necromancy(Component):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return 'Necromancy'

class AlternateReality(Component):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return 'Alternate Reality'

class Madness(Component):
    '''
    Docstring:
    Trap Leaf
    '''
    def operation(self) -> str:
        return 'Madness'

class Terrestrial(Component):
    '''
    Docstring:
    Trap subclass
    '''
    def operation(self) -> str:
        return 'Terrestrial'

class Thorns(Component):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def operation(self) -> str:
        return 'Thorns'

class LightStatue(Component):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def operation(self) -> str:
        return 'Light Statue'

