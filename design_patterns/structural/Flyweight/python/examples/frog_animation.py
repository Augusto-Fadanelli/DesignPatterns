# Frog sprites de https://github.com/clear-code-projects/animation
# pip install pygame

import pygame
from pygame.locals import *
from sys import exit
import random

class frog(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('frog_sprites/attack_1.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_2.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_3.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_4.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_5.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_6.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_7.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_8.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_9.png'))
        self.sprites.append(pygame.image.load('frog_sprites/attack_10.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        #self.image = pygame.transform.scale(self.image, (128*3, 64*3)) # Aumenta o tamanho da imagem

        self.rect = self.image.get_rect()
        self.rect.topleft = posX, posY

    def update(self):
        self.current += 0.3
        if self.current >= len(self.sprites):
            self.current = 0
        self.image = self.sprites[int(self.current)]
        #self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))  # Aumenta o tamanho da imagem

def objects(posX, posY):
    f = frog(posX, posY)
    return f

if __name__ == '__main__':
    pygame.init()

    screen_width = 640
    screen_height = 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Angry Pig')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    for i in range(200):
        posX = random.randint(1, screen_width)
        posY = random.randint(1, screen_height)
        f = objects(posX, posY)
        all_sprites.add(f)

    while True:
        clock.tick(30)
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()