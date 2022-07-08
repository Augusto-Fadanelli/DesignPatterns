
from light import Ligth
from ligthOnCommand import LigthOnCommand
from remoteControlle import RemoteController

bedroom_ligth = Ligth("Room Ligth", "Room")
bathroom_ligth = Ligth("Room Bath", "Bath")

bedroom_ligth_on = LigthOnCommand(bedroom_ligth)
bathroom_ligth_on = LigthOnCommand(bathroom_ligth)

remote = RemoteController()
remote.button_add_command("Primeiro_Botao", bathroom_ligth_on)

remote.button_pressed("Primeiro_Botao")
