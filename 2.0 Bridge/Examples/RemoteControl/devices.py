from bridge import Device

class TV(Device):
    def getName(self):
        return self.name

    def setPower(self, power_status):
        self.power_status = power_status

    def getPower(self):
        return self.power_status

    def setVolume(self, new_volume):
        self.volume = new_volume

    def getVolume(self):
        return self.volume

class Radio(Device):
    def getName(self):
        return self.name

    def setPower(self, power_status):
        self.power_status = power_status

    def getPower(self):
        return self.power_status

    def setVolume(self, new_volume):
        self.volume = new_volume

    def getVolume(self):
        return self.volume

class Light(Device):
    def getName(self):
        return self.name

    def setPower(self, power_status):
        self.power_status = power_status

    def getPower(self):
        return self.power_status

    def setVolume(self, new_volume):
        self.volume = new_volume

    def getVolume(self):
        return self.volume
