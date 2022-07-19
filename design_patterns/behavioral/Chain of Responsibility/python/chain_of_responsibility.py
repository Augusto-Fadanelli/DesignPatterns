from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Interface.
    """

    @abstractmethod
    def setNext(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class HandlerBase(Handler):
    _next_handler: Handler = None

    def setNext(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class ConcreteHandlerA(HandlerBase):
    def handle(self, request: Any):
        if request == 'A' or request == 'All':
            print('Handler-A,', end=' ')

        return super().handle(request)


class ConcreteHandlerB(HandlerBase):
    def handle(self, request: Any):
        if request == 'B' or request == 'All':
            print('Handler-B,', end=' ')

        return super().handle(request)


class ConcreteHandlerC(HandlerBase):
    def handle(self, request: Any):
        if request == 'C' or request == 'All':
            print('Handler-C,', end=' ')

        return super().handle(request)


if __name__ == '__main__':
    handlerA = ConcreteHandlerA()
    handlerB = ConcreteHandlerB()
    handlerC = ConcreteHandlerC()

    handlerA.setNext(handlerB).setNext(handlerC)
    # handlerB.setNext(handlerC).setNext(handlerA)

    handlerA.handle('All')
    # print('\n',teste)
