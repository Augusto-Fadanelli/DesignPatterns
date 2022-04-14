from bridge import *

class PC(Platform):
    def __init__(self, implementation:Product, external_memory:int, operational_system:str):
        self.implementation = implementation
        self.external_memory = external_memory
        self.operational_system = operational_system
        self.favorite = False

    def toPlay(self):
        def checkPlatform():
            for i in self.implementation.platforms:
                if i == 'all' or i == self.operational_system:
                    return True
            return False

        if checkPlatform():
            print(f'Playing {self.implementation.name} in Desktop {self.operational_system}')
        else:
            print('Error! Unsupported platform.')

    def toggleFavorite(self):
        self.favorite = not self.favorite

class Playstation(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = False
        self.psn_sync = False

    def toPlay(self):
        def checkPlatform():
            for i in self.implementation.platforms:
                if i == 'all' or i == self.model:
                    return True
            return False

        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def syncWithPsnPlus(self):
        self.psn_sync = True

class Xbox(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = False
        self.gamepass_sync = False

    def toPlay(self):
        def checkPlatform():
            for i in self.implementation.platforms:
                if i == 'all' or i == self.model:
                    return True
            return False

        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def syncWithGamePass(self):
        self.gamepass_sync = True

class Nintendo(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = False
        self.cloud_save = False

    def toPlay(self):
        def checkPlatform():
            for i in self.implementation.platforms:
                if i == 'all' or i == self.model:
                    return True
            return False

        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def toggleCloudSave(self):
        self.cloud_save = not self.cloud_save

class SteamDeck(Platform):
    def __init__(self, implementation:Product, external_memory:int, model:str, version:str):
        self.implementation = implementation
        self.external_memory = external_memory
        self.model = model
        self.version = version
        self.achievements = False
        self.favorite = False

    def toPlay(self):
        def checkPlatform():
            for i in self.implementation.platforms:
                if i == 'all' or i == self.model:
                    return True
            return False

        if checkPlatform():
            print(f'Playing {self.implementation.name} in {self.model} v.{self.version}')
        else:
            print('Error! Unsupported platform.')

    def toggleAchievements(self):
        self.achievements = not self.achievements

    def toggleFavorite(self):
        self.favorite = not self.favorite

