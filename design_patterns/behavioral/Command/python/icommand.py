from abc import ABC, abstractmethod


class ICommand(ABC):
    """Interface de Comando"""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
