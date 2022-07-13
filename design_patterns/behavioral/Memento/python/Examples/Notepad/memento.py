from abc import ABC, abstractmethod

class Memento(ABC):
    '''
    Docstring:
    Interface
    '''
    @abstractmethod
    def getText(self):
        pass

class ConcreteMemento(Memento):
    def __init__(self, state:str):
        self.__state = state

    def getState(self):
        return self.__state

class Originator():
    __state = None
    def __init__(self, state:str):
        self.__state = state
        print(f'Originator: Initial state: {self.__state}')


