class Item:
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'Item(nome={self.name}, valor={self.value})'


class Cart:
    def __init__(self):
        self.items = []

    def addItem(self, item: Item):
        self.items.append(item)

    def totalValue(self):
        sum = 0
        for item in self.items:
            sum += item.value

        return sum

    def getItems(self):
        return self.items
