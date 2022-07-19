from __future__ import annotations

from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def hasMore(self) -> bool:
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection: ConcreteCollection):
        self._collection = collection
        self._iteration_state = None

    def getNext(self):
        pass

    def hasMore(self):
        pass


class IterableCollection(ABC):
    @abstractmethod
    def createIterator(self) -> Iterator:
        pass


class ConcreteCollection(IterableCollection):
    def createIterator(self):
        pass


if __name__ == '__main__':
    print('ok!')
