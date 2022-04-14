from bridge import *

class PC(Platform):
    def __init__(self, implementation:Product, external_memory:int, operational_system:str, favorite=False):
        self.implementation = implementation
        self.external_memory = external_memory
        self.operational_system = operational_system
        self.favorite = favorite

    def checkPlatform(self):
        for i in self.implementation.platforms:
            print(i)
            # Implementar. se i == 'all' return True, else if i == self.operational_system return True, else return False

    def toPlay(self):
        if checkPlatform():
            print(f'Playing {self.implementation.name} in Desktop {self.operational_system}')
        else:
            print('Error! Unsupported platform.')

    def toggleFavorite(self):
        self.favorite = not self.favorite

class Playstation(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str, achievements=False, psn_sync=False):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = achievements
        self.psn_sync = psn_sync

    # Implementar
    def checkPlatform(self):
        pass

    def toPlay(self):
        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def syncWithPsnPlus(self):
        self.psn_sync = True

class Xbox(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str, achievements=False, gamepass_sync=False):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = achievements
        self.gamepass_sync = gamepass_sync

    def checkPlatform(self):
        pass

    def toPlay(self):
        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def syncWithGamePass(self):
        self.gamepass_sync = True

class Nintendo(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str, achievements=False, cloud_save=False):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = achievements
        self.cloud_save = cloud_save

    def checkPlatform(self):
        pass

    def toPlay(self):
        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def toggleCloudSave(self):
        self.cloud_save = not self.cloud_save

class SteamDeck(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str, achievements=False, favorite=False):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = achievements
        self.favorite = favorite

    def checkPlatform(self):
        pass

    def toPlay(self):
        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def toggleFavorite(self):
        self.favorite = not self.favorite

