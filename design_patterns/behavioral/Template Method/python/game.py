from abc import ABC, abstractmethod


class Game(ABC):
    """Class Abstrata"""

    def gameFase(self):
        """Template Method"""

        self.firstLevel()
        self.secondLevel()

    def soundtrack(self):
        print('Trilha dos vingadores começa')

    @abstractmethod
    def firstLevel(self):
        pass

    @abstractmethod
    def secondLevel(self):
        pass
