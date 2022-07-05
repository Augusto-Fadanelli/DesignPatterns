
from abc import ABCMeta, abstractmethod

class Command(ABCMeta):
    
    @abstractmethod
    def executar():
        pass;

