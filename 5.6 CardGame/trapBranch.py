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
        return 'Enormes rochas de fogo caindo do céu e atigindo o campo de batalha.\n'
        'Sempre olhe para cima se não quiser ser atigindo.'

    def operation(self) -> str:
        return super().operation(name='Meteor Rain')

class Necromancy(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def description(self):
        return 'A magia proibida está escrita no necromante, capaz de ressuscitar\n'
        'uma legião de mortos-vivo. Além disso todos irão obedecer sua ordens.'

    def operation(self) -> str:
        return super().operation(name='Necromancy')

class AlternateReality(Leaf):
    '''
    Docstring:
    Trap leaf
    '''
    def description(self):
        return 'Com esse feitiço tudo a sua volta muda ao seu bel-prazer,\n'
        'simplesmente o poder mais forte de todo o jogo'

    def operation(self) -> str:
        return super().operation(name='Alternate Reality')

class Madness(Leaf):
    '''
    Docstring:
    Trap Leaf
    '''
    def description(self):
        return 'Faça seus inimigos materem uns aos outros com esssa carta,\n'
        'todos afetados com essa magia estão a beira da loucara máxima'

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
        return 'Armadinha terrestre feita para capturar e matar seus inimigos destraidos,\n'
        'uma vez colocada em jogo ela é capaz acabar com varios adversarios.'

    def operation(self) -> str:
        return super().operation(name='Thorns')

class LightStatue(Leaf):
    '''
    Docstring:
    Terrestrial leaf
    '''
    def description(self):
        return 'Essa estátua é capaz de cegar e desorientar varios adversarios\n'
        'sendo considerada uma dor de cabeça caso veja ela no campo de batalha'

    def operation(self) -> str:
        return super().operation(name='Light Statue')

