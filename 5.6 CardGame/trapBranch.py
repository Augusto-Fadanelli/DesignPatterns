from compositeDP import *

class Trap(Composite):
    def operation(self) -> str:
        return super().operation(name='Trap')

class MeteorRain(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Meteor Rain')

class Necromancy(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Necromancy')

class AlternateReality(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Alternate Reality')

class Madness(Leaf):
    '''
    Docstring:
    Trap Leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Madness')

class Terrestrial(Composite):
    '''
    Docstring:
    Trap branch
    '''
    def operation(self) -> str:
        return super().operation(name='Terrestrial')

class Thorns(Leaf):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Thorns')

class LightStatue(Leaf):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def operation(self) -> str:
        return super().operation(name='Light Statue')

