# Script encontrado em https://refactoring.guru/pt-br/design-patterns/visitor/python/example

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor):
        visitor.visitConcreteComponentA(self)

    def exclusiveMethodOfConcreteComponentA(self):
        return 'A'

class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visitConcreteComponentB(self)

    def specialMethodOfConcreteComponentB(self):
        return 'B'

class Visitor(ABC):
    @abstractmethod
    def visitConcreteComponentA(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visitConcreteComponentB(self, element: ConcreteComponentB) -> None:
        pass

class ConcreteVisitor1(Visitor):
    def visitConcreteComponentA(self, element):
        print(f'{element.exclusiveMethodOfConcreteComponentA()} + ConcreteVisitor1')

    def visitConcreteComponentB(self, element):
        print(f'{element.specialMethodOfConcreteComponentB()} + ConcreteVisitor1')

class ConcreteVisitor2(Visitor):
    def visitConcreteComponentA(self, element):
        print(f'{element.exclusiveMethodOfConcreteComponentA()} + ConcreteVisitor2')

    def visitConcreteComponentB(self, element):
        print(f'{element.specialMethodOfConcreteComponentB()} + ConcreteVisitor2')

def clientCode(components: List[Component], visitor: Visitor):
    for component in components:
        component.accept(visitor)

if __name__ == '__main__':
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print('The client code works with all visitors via the base Visitor interface:')
    visitor1 = ConcreteVisitor1()
    clientCode(components, visitor1)

    print('It allows the same client code to work with different types of visitors:')
    visitor2 = ConcreteVisitor2()
    clientCode(components, visitor2)

