from abc import ABC, abstractmethod
from datetime import datetime


class Memento(ABC):
    """
    Docstring:
    Interface
    """

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getDate(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = str(datetime.now())[:19]

    def getState(self):
        return self._state

    def getName(self):
        return f'{self._date} / ({self._state[0:9]}...)'

    def getDate(self):
        return self._date


class Originator:
    _state = None

    def __init__(self, state: str):
        self._state = state
        print(f'Originator: Initial state: {self._state}')

    def operation(self):
        self._state = input('Say something: ')
        print(f'Originator: State has changed to: {self._state}')

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento):
        self._state = memento.getState()
        print(f'Originator: State has changed to: {self._state}')


class Caretaker:
    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'Caretaker: Restoring state to: {memento.getName()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self):
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.getName())


if __name__ == '__main__':
    originator = Originator('In a hole in the ground there lived a hobbit.')
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.operation()

    caretaker.backup()
    originator.operation()

    caretaker.backup()
    originator.operation()

    caretaker.backup()
    originator.operation()

    print()
    caretaker.show_history()

    print('\nClient: rollback!\n')
    caretaker.undo()

    print('\nClient: rollback again!\n')
    caretaker.undo()

    print()
    caretaker.show_history()
