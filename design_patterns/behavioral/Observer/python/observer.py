# Código retirado de https://refactoring.guru/pt-br/design-patterns/observer/python/example

from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    '''
    Interface.
    Declara métodos para gerenciar os subscribers.
    '''

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        '''
        Anexa um observer ao Subject.
        '''
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        '''
        Remove um observer do Subject.
        '''
        pass

    @abstractmethod
    def notify(self) -> None:
        '''
        Notifica todos os observers sobre um evento.
        '''
        pass

class ConcreteSubject(Subject):
    '''
    Sujeito ou Publisher.
    '''

    _state: int = None # Armazena o estado do sujeito
    _observers: List[Observer] = []

    def getState(self):
        return self._state

    def attach(self, observer: Observer):
        print('Subject: Anexado um observer.')
        self._observers.append(observer)

    def detach(self, observer: Observer):
        print('Subject: Removido um observer')
        self._observers.remove(observer)

    def notify(self):
        '''
        Aciona o update em cada subscriber.
        '''

        print('Subject: Notificando observers...')
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        '''
        Alguma lógica de negócios que aciona os updates.
        '''

        print('\nSubject: Estou fazendo algo importante...')
        self._state = randrange(0, 10)

        print(f'Subject: Meu estado foi mudado para {self._state}.')
        self.notify()

class Observer(ABC):
    '''
    Interface.
    Declara o método update usado pelos subjects.
    '''

    @abstractmethod
    def update(self, subject: Subject) -> None:
        '''
        Recebe atualizações do subject.
        '''
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Subject):
        if subject.getState() < 3:
            print('ConcreteObserverA: Reagiu ao evento.')

class ConcreteObserverB(Observer):
    def update(self, subject: Subject):
        if subject.getState() == 0 or subject.getState() >= 2:
            print('ConcreteObserverB: Reagiu ao evento.')

if __name__ == '__main__':
    # Client code

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a) # Anexa observer_a à lista de observers

    observer_b = ConcreteObserverB()
    subject.attach(observer_b) # Anexa observer_b à lista de observers

    # Muda o estado do subject
    subject.some_business_logic()
    subject.some_business_logic()

    print()
    subject.detach(observer_a) # Remove observer_a da lista de observers

    # Muda o estado do subject
    subject.some_business_logic()

