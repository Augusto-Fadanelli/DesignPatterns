from compositeDP import Component

class Heavenly(Component):
    def operation(self) -> str:
        return 'Heavenly'

class Magician(Component):
    '''
    Docstring:
    Heavenly subclass
    '''
    def operation(self) -> str:
        return 'Magician'

class DarkMagician(Component):
    '''
    Docstring:
    Magician leaf
    '''
    def operation(self) -> str:
        return 'Dark Magician'

class LightMagician(Component):
    '''
    Docstring:
    Magician leaf
    '''
    def operation(self) -> str:
        return 'Light Magician'

class Sorcerer(Component):
    '''
    Docstring:
    Heavenly subclass
    '''
    def operation(self) -> str:
        return 'Sorcerer'

class DarkSorcerer(Component):
    '''
    Docstring:
    Sorcerer leaf
    '''
    def operation(self) -> str:
        return 'Dark Sorcerer'

class LightSorcerer(Component):
    '''
    Docstring:
    Sorcerer leaf
    '''
    def operation(self) -> str:
        return 'Light Sorcerer'

class Elf(Component):
    '''
    Docstring:
    Heavenly subclass
    '''
    def operation(self) -> str:
        return 'Elf'

class ShapeshifterElf(Component):
    '''
    Docstring:
    Elf leaf
    '''
    def operation(self) -> str:
        return 'Shapeshifter elf'

class SummonerElf(Component):
    '''
    Docstring:
    Elf leaf
    '''
    def operation(self) -> str:
        return 'Summoner Elf'

class elfArcher(Component):
    '''
    Docstring:
    Elf leaf
    '''
    def operation(self) -> str:
        return 'Elf Archer'
