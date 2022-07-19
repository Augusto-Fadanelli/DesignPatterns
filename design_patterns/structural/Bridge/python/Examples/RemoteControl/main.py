from bridge import *
from devices import *
from remoteControls import *


def clientCode(abstraction: RemoteControl):
    abstraction.togglePower()
    abstraction.volumeUp()


if __name__ == '__main__':
    tv1 = TV('TV LG', False)
    basic_tv_remote_control = BasicRemoteControl(tv1)

    print(f'Power status: {tv1.getPower()}')
    print(f'Volume: {tv1.getVolume()}')
    clientCode(basic_tv_remote_control)
    print(f'Volume: {tv1.getVolume()}')
    print(f'Power status: {tv1.getPower()}')

    """
    print(f'Nome: {tv1.getName()}')
    generic_control.togglePower()
    print(f'Power status: {tv1.getPower()}')
    print(f'Volume: {tv1.getVolume()}')
    generic_control.volumeUp()
    print(f'Volume: {tv1.getVolume()}')
    generic_control.volumeDown()
    generic_control.volumeDown()
    print(f'Volume: {tv1.getVolume()}')
    """
