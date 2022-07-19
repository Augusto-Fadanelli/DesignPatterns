from abc import ABC, abstractmethod


class Product(ABC):
    """
    Docstring:
    Interface Implementor
    """

    @abstractmethod
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        size: int,
        platforms='all',
    ):   # size in MB
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getPrice(self) -> float:
        pass


class Platform(ABC):
    """
    Docstring:
    Classe Abstraction
    """

    def __init__(self, implementation: Product, external_memory: int):
        self.implementation = implementation
        self.external_memory = external_memory

    def checkFreeSpace(self):
        # Se a memória interna livre do dispositivo for menor que o tamanho do produto
        if self.external_memory < self.implementation.size:
            return False
        return True

    @abstractmethod
    def toPlay(self):
        pass
