from compositeDP import *

class Heavenly(Composite):
    def operation(self) -> str:
        return super().operation(name='Heavenly')

class Magician(Composite):
    '''
    Docstring:
    Heavenly branch
    '''
    def operation(self) -> str:
        return super().operation(name='Magician')

class DarkMagician(Leaf):
    '''
    Docstring:
    Magician leaf
    '''
    def __init__(self):
        self._atk = 15
        self._def = 12

    def description(self):
        return 'Um mago que se rendeu as práticas do lado do mal, corrompendo-se por mais poder.\n' \
               'Em um campo de batalha não se pode subestimar seus poderes.'

    def operation(self) -> str:
        return super().operation(name='Dark Magician')

class LightMagician(Leaf):
    '''
    Docstring:
    Magician leaf
    '''
    def __init__(self):
        self._atk = 14
        self._def = 16

    def description(self):
        return 'Extremamente podereso, sábio e com boas intenções.\n' \
        'Esse mago usa de todo seu conhecimento para deter as forças que atarapalham o sossego dos inocentes.'

    def operation(self) -> str:
        return super().operation(name='Light Magician')

class Sorcerer(Composite):
    '''
    Docstring:
    Heavenly branch
    '''
    def operation(self) -> str:
        return super().operation(name='Sorcerer')

class DarkSorcerer(Leaf):
    '''
    Docstring:
    Sorcerer leaf
    '''
    def __init__(self):
        self._atk = 14 
        self._def = 10

    def description(self):
        return 'Um mago sombrio já pode ser um problema no seu caminho, mas um feiticeiro\n' \
        'sombrio é um poblema dobrado. Eles são tão poderesos que podem mudar a realidade ao seu bel-prazer.'

    def operation(self) -> str:
        return super().operation(name='Dark Sorcerer')

class LightSorcerer(Leaf):
    '''
    Docstring:
    Sorcerer leaf
    '''
    def __init__(self):
        self._atk = 15
        self._def = 12

    def description(self):
        return 'Feiticeiros nascem com o dom da magia, diferente dos magos. Seu poder\n' \
        'pode atingir o ápice quando seus usuarios passsam por um rigoroso treinamento.\n' \
        'Não se meta com eles se você ainda pretende viver.'

    def operation(self) -> str:
        return super().operation(name='Light Sorcerer')

class Elf(Composite):
    '''
    Docstring:
    Heavenly branch
    '''
    def operation(self) -> str:
        return super().operation(name='Elf')

class ShapeshifterElf(Leaf):
    '''
    Docstring:
    Elf leaf
    '''
    def __init__(self):
        self._atk = 14
        self._def = 17

    def description(self):
        return 'Metamorfos são uma espécie de elfo Negro, que possuem a habilidade de se transformar em Animais.\n' \
        'O Metamorfo não tem  muito sentimentalismo pela natureza, e muitas vezes até prejudica a mesma.'

    def operation(self) -> str:
        return super().operation(name='Shapeshifter Elf')

class SummonerElf(Leaf):
    '''
    Docstring:
    Elf leaf
    '''
    def __init__(self):
        self._atk = 12
        self._def = 10

    def description(self):
        return 'Elfos invocadores necessitam de muita magia para realizar seus feitos, \n' \
        'mas em contrapartida estes feitos são Grandiosos. Invocam seres de qualquer tipo, \n' \
        'desde um inseto até um mamute ou coisa maior.'

    def operation(self) -> str:
        return super().operation(name='Summoner Elf')

class ElfArcher(Leaf):
    '''
    Docstring:
    Elf leaf
    '''
    def __init__(self):
        self._atk = 15
        self._def = 9

    def description(self):
        return 'Exímios atiradores no uso do arco, sua determinação a uma única arma destacam eles como grandes guerreiros.\n' \
        'Sua capacidade de disparar uma grande quantidade de flechas o torna capaz de \n' \
        'matar seu inimigo antes que ele consiga se aproximar.'

    def operation(self) -> str:
        return super().operation(name='Elf Archer')
