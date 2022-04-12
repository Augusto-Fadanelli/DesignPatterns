from bridge import Device

class TV(Device):
    def __init__(self, power_status):
        self.power_status = power_status

    def setPower(self):
        pass

    def getPower(self):
        pass

class Radio(Device):
    def __init__(self, power_status):
        self.power_status = power_status

    def setPower(self):
        pass

    def getPower(self):
        pass

class Light(Device):
    def __init__(self, power_status):
        self.power_status = power_status

    def setPower(self):
        pass

    def getPower(self):
        pass