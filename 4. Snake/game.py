import pygame
from pygame.locals import *
from sys import exit
from random import randint

g_snake_size = 30

class Food():
    def __init__(self):
        self.eat_song = pygame.mixer.Sound('eat_song.wav')
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
        self.eat_song.play()

class Snake():
    def __init__(self):
        self.rect_size = 0  # Tamanho de cada quadrado que compõe a snake
        self.snake_x = 0
        self.snake_y = 0
        self.snake_speed = 0
        self.control_x = 0
        self.control_y = 0
        self.snake_size = g_snake_size # Tamanho inicial da snake

        self.snake_list = []
        self.head_list = []

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
        self.snake_x = x - self.rect_size // 2
        self.snake_y = y - self.rect_size // 2

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

class PlayGame():
    def __init__(self, snake:Snake, food:Food):
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.snake = snake
        self.snake.setRectSize(self.screen_width // 32)
        self.snake.setSpeed(self.screen_width // 128)

        self.clock = pygame.time.Clock()

        #self.score = 0
        self.font_score = pygame.font.SysFont('Arial', 40, True, True)
        self.font_game_over = pygame.font.SysFont('Arial', 20, True, True)

        self.food = food
        self.food.setRadius(self.screen_width // 64)

        self.__reloadGame()
        self.__conf()
        self.__loop()

    def __reloadGame(self):
        self.snake.setPos(self.screen_width // 2, self.screen_height // 2)
        self.snake.setControl(self.snake.getSpeed(), 0)
        self.score = 0
        self.food.setPos(randint(self.food.getRadius() * 2, self.screen_width - self.food.getRadius() * 2),
                         randint(self.food.getRadius() * 2, self.screen_height - self.food.getRadius() * 2)
                         )
        self.snake.setSize(g_snake_size)
        self.snake.setSnakeList([]) # Zera a lista
        self.snake.setHeadList([]) # Zera a lista

    # Configurações da janela que não estão em loop
    def __conf(self):
        #pygame.init()
        pygame.display.set_caption('Snake')

    def __loop(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((255,255,255))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                # Controles e Movimento da snake
                if event.type == KEYDOWN:
                    if event.key == K_a:
                        if not self.snake.getControlX() == self.snake.getSpeed(): # Impede a snake de inverter a direção
                            self.snake.setControl(-self.snake.getSpeed(), 0)
                    if event.key == K_d:
                        if not self.snake.getControlX() == -self.snake.getSpeed(): # Impede a snake de inverter a direção
                            self.snake.setControl(self.snake.getSpeed(), 0)
                    if event.key == K_w:
                        if not self.snake.getControlY() == self.snake.getSpeed(): # Impede a snake de inverter a direção
                            self.snake.setControl(0, -self.snake.getSpeed())
                    if event.key == K_s:
                        if not self.snake.getControlY() == -self.snake.getSpeed(): # Impede a snake de inverter a direção
                            self.snake.setControl(0, self.snake.getSpeed())

            self.snake.setPos(
                self.snake.getPosX() + self.snake.getControlX(),
                self.snake.getPosY() + self.snake.getControlY()
            )

            # Snake Shape
            snake_head = pygame.draw.rect(self.screen, (0,255,0), (
                self.snake.getPosX(), self.snake.getPosY(),
                self.snake.getSize(), self.snake.getSize()
            ))

            # Food Shape
            food = pygame.draw.circle(self.screen, (255,0,0), (self.food.getPosX(), self.food.getPosY()), self.food.getRadius())

            # Colisões
            if snake_head.colliderect(food):
                self.food.setPos(randint(self.food.getRadius() * 2, self.screen_width - self.food.getRadius() * 2),
                                 randint(self.food.getRadius()*2, self.screen_height - self.food.getRadius()*2)
                                 )
            self.score += 1
            self.food.playSong()

            self.snake.setHeadList([self.snake.getPosX(), self.snake.getPosY()])
            self.snake.addToSnakeList(self.snake.getHeadList())

            # Se a snake colidir consigo mesma
            if self.snake.checkCollision():
                message_game_over = 'Game Over! Press R to play again'
                formatted_game_over = self.font_game_over.render(message_game_over, True, (0,0,0))
                pos_message_game_over = formatted_game_over.get_rect()

                while True:
                    self.screen.fill(255,255,255)
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        if event.type == KEYDOWN:
                            if event.key == K_r:
                                self.__reloadGame()

                pos_message_game_over.center = (self.screen_width//2, self.screen_height//2)
                self.screen.blit(formatted_game_over, pos_message_game_over)
                pygame.display.update()

            # Se a snake sair da tela
            if self.snake.getPosX() < 0:
                self.snake.setPos(
                    self.screen_width, self.snake.getPosY()
                )
            elif self.snake.getPosX() > self.screen_width:
                self.snake.setPos(
                    0, self.snake.getPosY()
                )
            if self.snake.getPosY() < 0:
                self.snake.setPos(
                    self.snake.getPosX(), self.screen_height
                )
            elif self.snake.getPosY() > self.screen_height:
                self.snake.setPos(
                    self.snake.getPosX(), 0
                )

            self.snake.setSize(self.score + g_snake_size)
            self.snake.growthSnake(self.screen)

            # Score
            message_score = f'Score: {self.score}'
              # (text, anti-aliasing, (R,G,B))
            formatted_score = self.font_score.render(message_score, False, (0,0,0))
            self.screen.blit(formatted_score, (450, 40))

            pygame.display.update()

if __name__ == '__main__':
    pygame.init()
    player1 = Snake()
    food = Food()
    play = PlayGame(player1, food)