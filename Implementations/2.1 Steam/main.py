from bridge import *
from platforms import *
from products import *
from singleton import *


def clientCode():
    pass


if __name__ == '__main__':

    # Same Instance
    login1 = Login(
        'Augusto Fadanelli', '12345678900', 'augustofadanelli@pm.me', '1234'
    )
    print(login1)
    login2 = Login.getInstance()
    print(login2)

    # Register Products
    god_of_war = Game(
        'God of War',
        'His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. It is in this harsh, unforgiving world that he must fight to survive… and teach his son to do the same.',
        199.9,
        71680,
        'Santa Monica Studio',
        [
            'Processor: Intel i5-2500k (4 core 3.3 GHz) or AMD Ryzen 3 1200 (4 core 3.1 GHz)',
            'Memory: 8 GB RAM',
            'Graphics: NVIDIA GTX 960 (4 GB) or AMD R9 290X (4 GB)',
            'DirectX: Version 11',
        ],
        [
            'Processor: Intel i5-6600k (4 core 3.5 GHz) or AMD Ryzen 5 2400 G (4 core 3.6 GHz)',
            'Memory: 8 GB RAM',
            'Graphics: NVIDIA GTX 1060 (6 GB) or AMD RX 570 (4 GB)',
            'DirectX: Version 11',
        ],
        ['Action', 'Adventure', 'RPG'],
        ['Windows 10'],
    )

    wallpaper_engine = Software(
        'Wallpaper Engine',
        'Use stunning live wallpapers on your desktop. Animate your own images to create new wallpapers or import videos/websites and share them on the Steam Workshop!',
        9.99,
        512,
        'Wallpaper Engine Team',
        [
            'Processor: 1.66 GHz Intel i5 or equivalent',
            'Memory: 1024 MB RAM',
            'Graphics: HD Graphics 4000 or above',
            'DirectX: Version 10',
        ],
        [
            'Processor: 2.0 GHz Intel i7 or equivalent',
            'Memory: 2048 MB RAM',
            'Graphics: NVIDIA GeForce GTX 660, AMD HD7870, 2 GB VRAM or above',
            'DirectX: Version 11',
        ],
        ['Windows 7', 'Windows 8', 'Windows 10'],
    )

    demeo_together_collection = Soundtrack(
        'DEMEO TOGETHER COLLECTION',
        'A game soundtrack',
        57.99,
        214,
        [
            'Where Are You? (E3 2019 Trailer Edit)',
            'Where Are You? (2022 Cinematic Trailer Edit)',
            'The Dark (2022 Video Edit)',
        ],
        'Ghostwood Empire',
        'Rock',
        ['all'],
    )

    # Same Instance
    cart1 = Cart()
    cart1.addToCart(god_of_war)
    cart1.addToCart(wallpaper_engine)
    cart1.addToCart(demeo_together_collection)
    cart2 = Cart.getInstance()
    cart2.buy()

    # Platforms
    pc1 = PC(god_of_war, 102400, 'Windows 10')
    pc1.toPlay()
