
from abc import ABC, abstractmethod
from typing import Dict


class ICommand(ABC):
    """ Interface de Comando """    
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class Ligth:
    """ RECEIVER """
    
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = "Default color"
        self.intensity = 100  

    def on(self) -> None:
        print(f"Ligth {self.name} in {self.room_name} is now ON")

    def off(self) -> None:
        print(f"Ligth {self.name} in {self.room_name} is now OFF")

    def charge_color(self, color) -> None:
        self.color = color
        print(f"Ligth {self.name} in {self.room_name} is now {self.color}")

class LigthOnCommand(ICommand):
    """ Comando Concreto """
    def __init__(self, ligth: Ligth) -> None:
        self.ligth = ligth 
    
    def execute(self) -> None:
        self.ligth.on

    def undo(self) -> None:
        self.ligth.off

class RemoteController:
    """ Invoker """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()

if __name__ == "__main__":
    
    bedroom_ligth = Ligth("Room Ligth", "Room")
    bathroom_ligth = Ligth("Room Bath", "Bath")

    bedroom_ligth_on = LigthOnCommand(bedroom_ligth)
    bathroom_ligth_on = LigthOnCommand(bathroom_ligth)

    remote = RemoteController()
    remote.button_add_command('Primeiro', bedroom_ligth_on)

    remote.button_pressed('Primeiro_Botao')