from abc import ABC, abstractmethod
from iterator_interface import Iterator

class IterableCollection(ABC):
    @abstractmethod
    def createIterator(self) -> Iterator:
        pass

    @abstractmethod
    def addItem(self, item):
        pass