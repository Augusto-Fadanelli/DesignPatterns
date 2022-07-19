"""
Calcula taxas para cada país.
Obs.: Todos os valores são hipotéticos.
"""
from categories import *


class BRTax(Protocol):
    def calculateTaxesForBook(self, book: Book):
        # Não há taxa para livros
        return book.price

    def calculateTaxesForFood(self, food: Food):
        # 10% de taxa
        return food.price + food.price * 0.1

    def calculateTaxesForSmartphone(self, smartphone: Smartphone):
        # 70% de taxa
        return smartphone.price + smartphone.price * 0.7

    def calculateTaxesForComputer(self, computer: Computer):
        # 55% de taxa
        return computer.price + computer.price * 0.55


class USTax(Protocol):
    def calculateTaxesForBook(self, book: Book):
        # Não há taxa para livros
        return book.price

    def calculateTaxesForFood(self, food: Food):
        # 15% de taxa
        return food.price + food.price * 0.15

    def calculateTaxesForSmartphone(self, smartphone: Smartphone):
        # 25% de taxa
        return smartphone.price + smartphone.price * 0.25

    def calculateTaxesForComputer(self, computer: Computer):
        # 25% de taxa
        return computer.price + computer.price * 0.25
