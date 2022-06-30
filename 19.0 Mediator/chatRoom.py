
from mediator import Mediator
from colleague import Colleague
from typing import List

class ChatRoom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []
    
    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return
        
        print(f"{colleague.name} disse: {msg}")

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):
            return
        
        receiver_obj = List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]
        
        if not receiver_obj:
            return
        
        receiver_obj[0].direct(
            print(f"{sender.name} para {receiver_obj[0].name}: {msg}")
        )

