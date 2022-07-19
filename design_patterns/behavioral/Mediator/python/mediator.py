from abc import ABC, abstractmethod

from colleague import Colleague


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, person: Colleague, msg: str) -> None:
        pass

    # @abstractmethod
    # def direct(self, sender: Colleague, receiver: str, msg: str) -> None: pass
