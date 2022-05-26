# Flyweight baseado no código de https://sourcemaking.com/design_patterns/flyweight/python/1
# pip install pygame

import pygame
from pygame.locals import *
from sys import exit
import random

# Para o Flyweight
import abc

class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = HappyPig()
            self._flyweights[key] = flyweight
        return flyweight

class Flyweight(metaclass=abc.ABCMeta):
    def __init__(self):
        self.intrinsic_state = None

class HappyPig(Flyweight):
    '''
    Concrete Flyweight
    Contém valores intrínsecos, que podem ser compartilhados entre múltiplos objetos
    '''
    def __init__(self):
        self.sprites = []
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 1.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 2.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 3.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 4.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 5.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 6.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 7.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 8.png'))
        self.sprites.append(pygame.image.load('Assets/pig idle/Pig Idle 9.png'))

    def getSprites(self):
        return self.sprites

class Context(pygame.sprite.Sprite):
    '''
    Contém os dados extrínsecos
    '''
    def __init__(self, flyweight: Flyweight): # Recebe objeto com dados intrínsecos
        pygame.sprite.Sprite.__init__(self)

        self.flyweight = flyweight
        self.sprites = self.flyweight.getSprites()
        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()

    def getPos(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.rect.topleft = posX, posY

    def update(self):
        self.current += 0.3
        if self.current >= len(self.sprites):
            self.current = 0
        self.image = self.sprites[int(self.current)]
        # self.image = pygame.transform.scale(self.image, (128*3, 64*3)) # Aumenta o tamanho da imagem

if __name__ == '__main__':
    pygame.init()

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Happy Pig')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    flyweight_factory = FlyweightFactory()
    pig = flyweight_factory.get_flyweight(f'key:{0}')

    while True:
        clock.tick(30)
        screen.fill((220,230,230))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    context = Context(pig)
                    posX = random.randint(1, screen_width)
                    posY = random.randint(1, screen_height)
                    context.getPos(posX, posY)
                    all_sprites.add(context)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()