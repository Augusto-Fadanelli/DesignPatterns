from abc import ABC, abstractmethod

class Device(ABC):
    '''
    Docstring:
    Interface Implementor
    Implements
    '''
    def __init__(self, name: str, power_status: bool):
        self.name = name
        self.power_status = power_status
        self.volume = 10

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def setPower(self, power_status):
        pass

    @abstractmethod
    def getPower(self) -> bool:
        pass

    @abstractmethod
    def setVolume(self):
        pass

    @abstractmethod
    def getVolume(self) -> int:
        pass

class RemoteControl(ABC):
    '''
    Docstring:
    Classe Abstraction
    Herança/Extends
    '''
    def __init__(self, device: Device):
        self.device = device

    def togglePower(self):
        self.device.setPower(not self.device.getPower())

