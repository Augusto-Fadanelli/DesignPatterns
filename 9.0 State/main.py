"""
Permitir que um objeto altere seu comportamento quando seu estado interno for alterado.
O objeto aparecerá para alterar sua classe.
"""

"""Criar uma maquina de alimento que vende doces e salgados automatica,
apenas inserir a moeda e a maquina devolve o alimento que voce escolheu.
Mas a maquina so vai liberar o alimento se for pago corretamente.
"""

import abc


class Context:
    """
    Definir a interface de interesse para os clientes.
    Manter uma instância de uma subclasse ConcreteState que define o
    Estado atual.
    """

    def __init__(self, state):
        self._state = state

    def solicitacao(self):
        self._state.handle()


class State(metaclass=abc.ABCMeta):
    """
    Defina uma interface para encapsular o comportamento associado a um
    estado particular do Contexto.
    """

    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):
    """
    Implemente um comportamento associado a um estado do Contexto.
    """

    def handle(self):
        pass


class ConcreteStateB(State):
    """
    Implemente um comportamento associado a um estado do Contexto.
    """

    def handle(self):
        pass


def main():
    concrete_state_a = ConcreteStateA()
    context = Context(concrete_state_a)
    context.solicitação()


if __name__ == "__main__":
    main()