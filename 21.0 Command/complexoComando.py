
from command import Command
from receiver import Receiver

class ComplexoComando(Command):
    def __init__(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def setComplexoComando(self, receiver: Receiver, a: str, b: str):
        self._receiver = receiver
        self._a = a
        self._b = b

    def executar(self):
        self._receiver.primeiroPedido(self._a)
        self._receiver.segundoPedido(self._b)

