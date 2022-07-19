from abc import ABCMeta, abstractmethod


# Classe interface
class InternalState(metaclass=ABCMeta):
    @abstractmethod
    def changeState(self):
        pass


# CLaase para ligar o radio
class TurnedOn(InternalState):
    def changeState(self):
        print('LIGAR o dispositivo')
        return 'ON'


# Classe para desligar o radio
class TurnedOff(InternalState):
    def changeState(self):
        print('DESLIGAR o dispositivo')
        return 'OFF'


# Classe para ligar a FM do radio
class CanalFM(InternalState):
    def changeState(self):
        print('Voce esta usando o canal FM de comunicação')
        return 'FM'


# Aqui guarda o nome e estação
class MudaFM:
    def __init__(self, nome, estacao):
        self.nome = nome
        self.estacao = estacao

    def nomeEstacao(self):
        print(
            f'A emissora da radio é {self.nome} e o canal de comunicação é o {self.estacao}'
        )


# Classe para ligar o USB do radio
class CanalUSB(InternalState):
    def changeState(self):
        print('Voce esta usando o USB')
        return 'USB'


# Classe para mudar de estação da radio
class PassandoEstacao(InternalState):
    def changeState(self):
        print('Mudando de canal FM')
        return 'FM'


# Classe para mudar a faixa da musica no USB
class PassandoMusica(InternalState):
    def changeState(self):
        print('Mudando de musica')
        return 'Musica USB'


# Retorna o estado do radio
class EstadoMaquina(InternalState):
    def estado():
        return f'O estado interno do rádio está atualmente: {radio.getState()}'


# Retorna a função que esta sendo executada no momento
class FuncaoMaquina(InternalState):
    def funcaoAgora():
        return f'Afunção que o radio esta sendo executada agora: {radio.setState()}'


# Aumenta o volume
class IncreaseVolume(InternalState):
    def changeState(self):
        print('Aumentando o volume em 10')
        return '+10'


# Diminuir o volume
class DecreaseVolume(InternalState):
    def changeState(self):
        print('Diminuir o volume em 10')
        return '-10'


class RadioStation(InternalState):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, status):
        self.state = status

    def changeState(self):
        self.state = self.state.changeState()


radio = RadioStation()
print(f'O estado interno do rádio está atualmente: {radio.getState()}')

on = TurnedOn()
off = TurnedOff()

aumenta = IncreaseVolume()
diminui = DecreaseVolume()

canalFM = CanalFM()
canalUSB = CanalUSB()

passaFM = PassandoEstacao()
passaUSB = PassandoMusica()


print('\nLigando o rádio')
radio.setState(on)
radio.changeState()
print(EstadoMaquina.estado())


print('\nLigando a radio FM')
radio.setState(canalFM)
radio.changeState()
print(EstadoMaquina.estado())
passaFM.changeState()
MudaFM('Tupi', '99.9').nomeEstacao()
aumenta.changeState()

# radio.getState(off)
MudaFM('sada', '31.2').nomeEstacao()
