from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def getNext(self):
        pass

    @abstractmethod
    def hasMore(self) -> bool:
        pass
