from bridge import *


class BasicRemoteControl(RemoteControl):
    """
    Docstring
    Controle remoto genérico com volume
    """

    def volumeUp(self):
        if self.device.getVolume() <= 95:
            self.device.setVolume(self.device.getVolume() + 5)

    def volumeDown(self):
        if self.device.getVolume() >= 5:
            self.device.setVolume(self.device.getVolume() - 5)


class TouchControl(RemoteControl):
    pass
