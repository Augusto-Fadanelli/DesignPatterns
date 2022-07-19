from compositeDP import *


class Land(Composite):
    def operation(self) -> str:
        return super().operation(name='Land')


class FlatLand(Leaf):
    """
    Docstring:
    Land leaf
    """

    def description(self):
        return (
            'Campo vasto e plano, sem árvores ou qualquer outro obstáculo.\n'
            'Um lugar ideal para uma batalha com vários combatentes.'
        )

    def operation(self) -> str:
        return super().operation(name='Flat Land')


class Hell(Leaf):
    """
    Docstring:
    Land leaf
    """

    def description(self):
        return (
            'Lugar onde as forças do mal predominam e podem fazer o que bem quiser.\n'
            'Se seu inimigo for um deles, então tome cuidado ao enfrentá-lo nesse lugar.'
        )

    def operation(self) -> str:
        return super().operation(name='Hell')


class Forest(Leaf):
    """
    Docstring:
    Land leaf
    """

    def description(self):
        return (
            'Uma floresta de vegetação fechada. Não se encante com a beleza do lugar,\n'
            'pois podem haver criaturas e armadilhas prontas para capturá-lo.'
        )

    def operation(self) -> str:
        return super().operation(name='Forest')
