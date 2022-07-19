class Ligth:
    """RECEIVER"""

    def __init__(self, name: str, room_name: str):
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self):
        print(f'A luz {self.name} que está {self.room_name} está ON')

    def off(self):
        print(f'A luz {self.name} que está {self.room_name} está OFF')

    def charge_color(self, color):
        self.color = color
        print(
            f'A luz {self.name} que está {self.room_name} tem a cor {self.color}'
        )
