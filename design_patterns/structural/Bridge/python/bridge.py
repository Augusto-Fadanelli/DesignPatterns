from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def operationImpA(self):
        pass

    @abstractmethod
    def operationImpB(self):
        pass


class Abstraction(ABC):
    def __init__(self, implementation: Implementor):
        self.implementation = implementation

    def operationA(self):
        pass

    def operationB(self):
        pass


class RefinedAbstractionA(Abstraction):
    def __init__(self, implementation: Implementor):
        self.implementation = implementation

    def operationC(self):
        pass


class RefinedAbstractionB(Abstraction):
    def __init__(self, implementation: Implementor):
        self.implementation = implementation

    def operationD(self):
        pass


class ConcreteImplementorA(Implementor):
    def operationImpA(self):
        pass

    def operationImpB(self):
        pass


class ConcreteImplementorB(Implementor):
    def operationImpA(self):
        pass

    def operationImpB(self):
        pass


if __name__ == '__main__':
    imp = ConcreteImplementorA()
    abst = RefinedAbstractionA(imp)
