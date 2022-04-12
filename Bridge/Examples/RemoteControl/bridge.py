from abc import ABC, abstractmethod

class Device(ABC):
    '''
    Docstring:
    Classe Implementor
    '''
    def __init__(self, power_status):
        self.power_status = power_status

    @abstractmethod
    def setPower(self):
        pass

    @abstractmethod
    def getPower(self):
        pass

class RemoteControl(ABC):
    '''
    Docstring:
    Classe Abstraction
    '''
    def __init__(self, device: Device):
        self.device = device

    def togglePower(self):
        pass

