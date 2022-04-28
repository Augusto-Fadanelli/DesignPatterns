import pygame
from pygame.locals import *
from random import randint
from cmemento import *

# Variáveis globais
g_snake_size = 30

class Portal():
    def __init__(self):
        self.pos_x = []
        self.pos_y = []
        self.radius = 0

    def setPos(self, x, y):
        if len(self.pos_x) > 3:
            del self.pos_x[0]
            del self.pos_y[0]

        self.pos_x.append(x)
        self.pos_y.append(y)

    def getPosX(self, i):
        if len(self.pos_x) > i:
            return self.pos_x[i]
        return -100

    def getPosY(self, i):
        if len(self.pos_y) > i:
            return self.pos_y[i]
        return -100

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def closePortal(self):
        if len(self.pos_x) > 0:
            del self.pos_x[len(self.pos_x)-1]
            del self.pos_y[len(self.pos_y)-1]

class Food():
    def __init__(self):
        self.eat_sound = pygame.mixer.Sound('eat_sound.wav')
        self.pos_x = 0
        self.pos_y = 0
        self.radius = 0

    def setPos(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def setRadius(self, r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def playSong(self):
        self.eat_sound.play()

class Snake():
    def __init__(self):
        self.teleport_sound = pygame.mixer.Sound('teleport_sound.wav')
        self.rect_size = 0  # Tamanho de cada quadrado que compõe a snake
        self.snake_x = 0
        self.snake_y = 0
        self.snake_speed = 0
        self.control_x = 0
        self.control_y = 0
        self.snake_size = g_snake_size # Tamanho inicial da snake
        self.is_dead = False

        self.snake_list = []
        self.head_list = []

    def save(self, snakePosX, snakePosY):
        self._state = [snakePosX, snakePosY]
        return ConcreteMemento(self._state)

    def restore(self, memento: ConcreteMemento):
        self._state = memento.getState()
        self.snake_x = self._state[0]
        self.snake_y = self._state[1]
        self.teleport_sound.play()
        print(f'Originator: State has changed to: {self._state}')

    def originator_start(self):
        # Originator
        self._state = [self.snake_x, self.snake_y] # Posição da snake
        self.save(self._state[0], self._state[1])

    def setIsDead(self, dead:bool):
        self.is_dead = dead

    def getIsDead(self):
        return self.is_dead

    def setRectSize(self, size):
        self.rect_size = size

    def getRectSize(self):
        return self.rect_size

    def setSize(self, size):
        self.snake_size = size

    def getSize(self):
        return self.snake_size

    def setSnakeList(self, snake_list:list):
        self.snake_list = snake_list

    def addToSnakeList(self, a):
        self.snake_list.append(a)

    def setHeadList(self, head_list:list):
        self.head_list = head_list

    def getHeadList(self):
        return self.head_list

    def setPos(self, x, y):
        self.snake_x = x
        self.snake_y = y

    def getPosX(self):
        return self.snake_x

    def getPosY(self):
        return self.snake_y

    def setSpeed(self, speed):
        self.snake_speed = speed

    def getSpeed(self):
        return self.snake_speed

    def setControl(self, x, y):
        self.control_x = x
        self.control_y = y

    def getControlX(self):
        return self.control_x

    def getControlY(self):
        return self.control_y

    def checkCollision(self):
        if self.snake_list.count(self.head_list) > 1:
            return True
        return False

    def growthSnake(self, screen):
        if len(self.snake_list) > self.snake_size:
            del self.snake_list[0]
        for pos in self.snake_list:
            pygame.draw.rect(screen, (0,255,0), (pos[0], pos[1], self.rect_size, self.rect_size))
