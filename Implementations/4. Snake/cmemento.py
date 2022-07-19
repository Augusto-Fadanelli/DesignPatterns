from abc import ABC, abstractmethod
from datetime import datetime


class Memento(ABC):
    """
    Docstring:
    Interface
    """

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getDate(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def getState(self):
        return self._state

    def getName(self):
        return f'{self._date} / ({self._state[0:9]})'

    def getDate(self):
        return self._date
