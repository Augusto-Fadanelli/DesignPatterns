# pip install pygame

import pygame
from pygame.locals import *
from sys import exit

# from PIL import Image
#
# def loadImage(image_name):
#     fullname = os.path.join('Assets', image_name)
#     try:
#         image = pygame.image.load(fullname)
#     except pygame.error:
#         print(f'Cannot load image: {fullname}')
#         raise SystemExit
#     return image, image.get_rect()
#
#     # Teste
#     #strip = Image.open('Assets/Pig Idle (36x30).png')
#     #sprite = strip.crop(9 * 36, 0, 36, 30)
#     # sprite = [strip.crop((9*36, 0, 36, 30)) for n in range (nb_of_sprites)]

if __name__ == '__main__':
    pygame.init()

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Angry Pig')
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # Aqui ficam os controles

        pygame.display.update()