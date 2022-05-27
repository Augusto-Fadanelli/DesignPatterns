
from abc import ABC

class MachineVending(ABC):
    
    def __init__(self, salgado, doce, bebidas):
        self.salgado = salgado
        self.doce = doce
        self.bebidas = bebidas


class Salgados(MachineVending):
    