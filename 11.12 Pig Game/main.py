# pip install pygame

import pygame
from pygame.locals import *
from sys import exit
import random

class angryPig(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
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
        self.current = 0
        self.image = self.sprites[self.current]
        # self.image = pygame.transform.scale(self.image, (128*3, 64*3)) # Aumenta o tamanho da imagem

        self.rect = self.image.get_rect()
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
    pygame.display.set_caption('Angry Pig')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    while True:
        clock.tick(30)
        screen.fill((220,230,230))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_q:
                    posX = random.randint(1, screen_width)
                    posY = random.randint(1, screen_height)
                    pig = angryPig(posX, posY)
                    all_sprites.add(pig)

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()