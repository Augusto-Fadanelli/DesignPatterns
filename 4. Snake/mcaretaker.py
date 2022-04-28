from cmemento import *
from obj import Snake

class Caretaker():
    def __init__(self, originator:Snake):
        self._mementos = []
        self._originator = originator

    def backup(self, snakePosX, snakePosY):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save(snakePosX, snakePosY))

    def undo(self):
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'Caretaker: Restoring state to: {memento.getName()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()