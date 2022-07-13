from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

#Colleague conhece sua interface Mediator
#Colleague não conhece outros objetos
class Colleague(ABC):
    
    def __init__(self) -> None:
        self.name = str
    
    @abstractmethod
    def broadcast(self, msg: str) -> None: pass
    
    #@abstractmethod
    # def direct(self, msg: str) -> None: pass

