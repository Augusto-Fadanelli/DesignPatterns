from bridge import Product

class Game(Product):
    def __init__(self, name, description, price, discount, size, developer:str, minimum_requirements:list, recommended_requirements:list, genre:list, platforms='all'):
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.size = size
        self.developer = developer
        self.minimum_requirements = minimum_requirements
        self.recommended_requirements = recommended_requirements
        self.genre = genre
        self.platforms = platforms

    def printMinimumRequirements(self):
        print(self.minimum_requirements)

    def printRecommendedRequirements(self):
        print(self.recommended_requirements)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

class Software(Product):
    def __init__(self, name, description, price, discount, size, developer:str, minimum_requirements:list, recommended_requirements:list, platforms='all'):
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.size = size
        self.developer = developer
        self.minimum_requirements = minimum_requirements
        self.recommended_requirements = recommended_requirements
        self.platforms = platforms

    def printMinimumRequirements(self):
        print(self.minimum_requirements)

    def printRecommendedRequirements(self):
        print(self.recommended_requirements)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

class Soundtrack(Product):
    def __init__(self, name, description, price, discount, size, track_listing:list, artist:str, genre:str, platforms='all'):
        self.name = name
        self.description = description
        self.price = price
        self.discount = discount
        self.size = size
        self.track_listing = track_listing
        self.artist = artist
        self.genre = genre
        self.platforms = platforms

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

