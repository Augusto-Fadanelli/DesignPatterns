from compositeDP import Component

class Land(Component):
    def operation(self) -> str:
        return 'Land'

class FlatLand(Component):
    '''
    Docstring:
    Land leaf
    '''

    def description(self):
        return 'Campo vasto e plano sem arvores ou qualquer outro obstaculo.\n'
        'Um lugar ideal para uma guerra com varios combatentes'

    def operation(self) -> str:
        return 'Flat Land'

class Hell(Component):
    '''
    Docstring:
    Land leaf
    '''

    def description(self):
        return 'Lugar onde as forças do mal predominam e podem fazer o que quiser.\n' 
        'Se seu inimigo for um deles, então tome cuidado ao enfrenta-lo nesse lugar'

    def operation(self) -> str:
        return 'Hell'

class Forest(Component):
    '''
    Docstring:
    Land leaf
    '''

    def description(self):
        return 'Uma floresta de vegetação fechada. Não se encante com a beleza do lugar\n'
        'pois pode a ver criaturas e aarmadinhas pronto para captura-lo'

    def operation(self) -> str:
        return 'Forest'
