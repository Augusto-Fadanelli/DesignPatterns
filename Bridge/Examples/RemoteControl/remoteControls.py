from bridge import *

class BasicRemoteControl(RemoteControl):
    def __init__(self, device: Device):
        self.device = device

class TouchControl(RemoteControl):
    def __init__(self, device: Device):
        self.device = device
