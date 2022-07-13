from __future__ import annotations
from abc import ABC, abstractmethod
from market import Cart

class Handler(ABC):
    '''
    Interface.
    '''

    @abstractmethod
    def setNext(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, cart: Cart):
        pass

class HandlerBase(Handler):
    _next_handler: Handler = None

    def setNext(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, cart: Cart):
        if self._next_handler:
            return self._next_handler.handle(cart)

        return None

# Promoções aqui

class PromotionMoreThanTenThousand(HandlerBase):
    '''
    20% de desconto se a compra for maior que 10 mil reais.
    '''

    def handle(self, cart: Cart):
        if cart.totalValue() >= 10_000:
            return cart.totalValue() - (cart.totalValue() * 0.2)

        return super().handle(cart)

class PromotionMoreThanAThousand(HandlerBase):
    '''
    15% de desconto se a compra for maior que mil reais.
    '''

    def handle(self, cart: Cart):
        if cart.totalValue() >= 1_000:
            return cart.totalValue() - (cart.totalValue() * 0.15)

        return super().handle(cart)

class Promotion50Products(HandlerBase):
    '''
    10% de desconto para 50 ou mais produtos no carrinho.
    '''

    def handle(self, cart: Cart):
        if len(cart.getItems()) >= 50:
            return cart.totalValue() - (cart.totalValue() * 0.1)

        return super().handle(cart)

