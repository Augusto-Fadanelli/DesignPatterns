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
        return 'Um mago que se rendeu as práticas do lado do mal e se corrompeu apenas\n'
        'por mais poder. Em um campo de batalha não se pode substimar seus poderes'

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
        return 'Extremamente podereso e sabio, sempre querendo ajudar e com boas intençoes.\n' 
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
        return 'Um mago sombrio já pode ser um problema no seu caminho agora um feiticeiro\n'
        'sombrio é um poblema dobrado, eles são tão poderesos que podem mudar a realidade ao seu bem prazer'

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
        return 'Feiticeiros nascem com o dom da magia diferentes dos magos, e esses poderes\n' 
        'são extremamente enormes quando seus usuarios passsam por um rigoroso treinamento.\n' 
        'Não seja inimigos deles se você ainda quer viver'

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
        return 'São uma espécie de elfo Negro, mas só se transformam em Animais. \n' 
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
        return 'São elfos que necessita de muita magia para realizar seus feitos, \n' 
        'mas em benefícios estes feitos são Grandiosos. Invocam seres de qualquer tipo \n' 
        'desde um Inseto até um mamute ou coisa maior.'

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
        return 'Exímios atiradores no uso do arco, sua determinação a uma única arma destacam eles como grandes guerreiros \n' 
        'Sua capacidade de disparar uma grande quantidade de flechas o torna capaz de \n'
        'matar seu inimigo antes que ele consiga se aproximar.'

    def operation(self) -> str:
        return super().operation(name='Elf Archer')
