"""
Categorias de Produtos.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Protocol(ABC):
    """
    Interface visitor.
    """

    def calculateTaxesForBook(self, book: Book) -> float:
        pass

    def calculateTaxesForFood(self, food: Food) -> float:
        pass

    def calculateTaxesForSmartphone(self, smartphone: Smartphone) -> float:
        pass

    def calculateTaxesForComputer(self, computer: Computer) -> float:
        pass


class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def getPriceWithTaxes(self, visitor: Protocol) -> float:
        pass


class Book(Product):
    def __init__(self, price: float):
        super(Book, self).__init__(name='Book', price=price)

    def getPriceWithTaxes(self, visitor: Protocol):
        return visitor.calculateTaxesForBook(self)


class Food(Product):
    def __init__(self, price: float):
        super(Food, self).__init__(name='Food', price=price)

    def getPriceWithTaxes(self, visitor: Protocol):
        return visitor.calculateTaxesForFood(self)


class Smartphone(Product):
    def __init__(self, price: float):
        super(Smartphone, self).__init__(name='Smartphone', price=price)

    def getPriceWithTaxes(self, visitor: Protocol):
        return visitor.calculateTaxesForSmartphone(self)


class Computer(Product):
    def __init__(self, price: float):
        super(Computer, self).__init__('Computer', price)

    def getPriceWithTaxes(self, visitor: Protocol):
        return visitor.calculateTaxesForComputer(self)
