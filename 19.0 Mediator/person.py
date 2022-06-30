
from colleague import Colleague
from mediator import Mediator

class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)
    
    # def send_direct(self, receiver: str, msg: str) -> None:
    #    self.mediator.direct(self, receiver, msg)
    
    # def direct(self, msg: str) -> None:
    #    print(msg)
