from compositeDP import *

class Trap(Composite):
    def operation(self) -> str:
        return super().operation(name='Trap')

class MeteorRain(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def description(self):
        return 'Enormes rochas de fogo caem do céu e atingem o campo de batalha.\n' \
        'Sempre olhe para cima se não quiser ser esmagado.'

    def operation(self) -> str:
        return super().operation(name='Meteor Rain')

class Necromancy(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def description(self):
        return 'A magia proibida está escrita no necromante, capaz de ressuscitar\n' \
        'uma legião de mortos-vivos. Além disso, todos irão obedecer suas ordens.'

    def operation(self) -> str:
        return super().operation(name='Necromancy')

class AlternateReality(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def description(self):
        return 'Com este feitiço, o campo de batalha será movido.\n' \
        'Essa é a sua chance de mudar o rumo do jogo.'

    def operation(self) -> str:
        return super().operation(name='Alternate Reality')

class Madness(Leaf):
    '''
    Docstring:
    Trap Leaf
    '''
    def description(self):
        return 'Faça seus inimigos matarem uns aos outros com essa carta,\n' \
        'todos os afetados com essa magia estão à beira da loucara máxima.'

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
    def description(self):
        return 'Armadilha terrestre feita para capturar e matar seus inimigos distraídos.\n' \
        'Uma vez colocada em jogo, ela é capaz acabar com vários adversarios.'

    def operation(self) -> str:
        return super().operation(name='Thorns')

class LightStatue(Leaf):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def description(self):
        return 'Essa estátua é capaz de cegar e desorientar seus adversários,\n' \
        'sendo considerada uma dor de cabeça caso seja encontrada no campo de batalha.'

    def operation(self) -> str:
        return super().operation(name='Light Statue')

