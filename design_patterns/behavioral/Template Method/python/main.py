from difficult import HardMode
from easy import EasyMode
from normal import NormalMode

print('Nivel Fácil')
jogadorN1 = EasyMode()
jogadorN1.firstLevel()
jogadorN1.secondLevel()

print('\n****Proximo nivel****\n')

print('Nivel Normal')
jogadorN1 = NormalMode()
jogadorN1.firstLevel()
jogadorN1.secondLevel()

print('\n****Proximo nivel****\n')

print('Nivel Dificil')
jogadorN1 = HardMode()
jogadorN1.firstLevel()
jogadorN1.secondLevel()
