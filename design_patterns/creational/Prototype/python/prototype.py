from abc import ABC, abstractmethod
import time


class Prototype(ABC):
    def __init__(self):
        # Difinindo um tempo fixo para criar um objeto
        time.sleep(4)
        self.age = None
        self.defense = None
        self.attack = None
        
    @abstractmethod
    def clone(self):
        pass  