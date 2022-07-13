# Código retirado de https://refactoring.guru/pt-br/design-patterns/chain-of-responsibility/python/example

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    '''
    Interface.
    Declara um método para construir a corrente de handlers.
    Também declara um método para executar uma solicitação.
    '''

    @abstractmethod
    def setNext(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    '''
    O comportamento padrão de encadeamento (setar o próximo objeto da corrente) pode ser
    implementado dentro de uma classe Handler base.
    '''

    _next_handler: Handler = None

    def setNext(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == 'Banana':
            return f"Monkey: I'll eat the {request}!"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == 'Nut':
            return f"Monkey: I'll eat the {request}!"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any):
        if request == 'MeatBall':
            return f"Dog: I'll eat the {request}!"
        else:
            return super().handle(request)

def clientCode(handler: Handler):
    for food in ['Nut', 'Banana', 'Cup of coffee']:
        print(f'\nClient: Who wants a {food}?')
        result = handler.handle(food)
        if result:
            print(f' {result}', end='')
        else:
            print(f' {food} was left untouched.', end='')

if __name__ == '__main__':
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.setNext(squirrel).setNext(dog)

    print('Chain: Monkey > Squirrel > Dog')
    clientCode(monkey)
    print()

    print('Subchain: Squirrel > Dog')
    clientCode(squirrel)
    print()
