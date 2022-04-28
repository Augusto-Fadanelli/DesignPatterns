import pygame
from pygame.locals import *
from sys import exit
from random import randint

from cmemento import *
from obj import *
from mcaretaker import *

# Variáveis globais
g_snake_size = 30

class PlayGame():
    def __init__(self, snake:Snake, food:Food, portal:Portal, caretaker:Caretaker):
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

        self.portal = portal
        self.portal.setRadius(self.screen_width // 40)

        self.food = food
        self.food.setRadius(self.screen_width // 64)

        self.caretaker = caretaker

        self.__reloadGame()
        self.snake.originator_start()
        pygame.display.set_caption('Snake')
        self.__loop()

    def __reloadGame(self):
        self.snake.setPos(self.screen_width // 2 - self.snake.getRectSize() // 2, self.screen_height // 2 - self.snake.getRectSize() // 2)
        self.snake.setControl(self.snake.getSpeed(), 0)
        self.score = 0
        self.food.setPos(randint(self.food.getRadius() * 2, self.screen_width - self.food.getRadius() * 2),
                         randint(self.food.getRadius() * 2, self.screen_height - self.food.getRadius() * 2)
                         )
        self.snake.setSize(g_snake_size)
        self.snake.setSnakeList([]) # Zera a lista
        self.snake.setHeadList([]) # Zera a lista
        self.snake.setIsDead(False)

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
                    # Save/Load
                    if event.key == K_k:
                        #self.save(self.snake.getPosX(), self.snake.getPosY())
                        self.caretaker.backup(self.snake.getPosX(), self.snake.getPosY())
                        self.portal.setPos(self.snake.getPosX(), self.snake.getPosY())
                    if event.key == K_l:
                     #   self.restore()
                        self.caretaker.undo()
                        self.portal.closePortal()

            self.snake.setPos(
                self.snake.getPosX() + self.snake.getControlX(),
                self.snake.getPosY() + self.snake.getControlY()
            )

            # Snake Shape
            snake_head = pygame.draw.rect(self.screen, (0,255,0), (
                self.snake.getPosX(), self.snake.getPosY(),
                self.snake.getRectSize(), self.snake.getRectSize()
            ))

            # Portal Shape
            portal = pygame.draw.circle(self.screen, (0,0,255), (self.portal.getPosX(0), self.portal.getPosY(0)), self.portal.getRadius())
            portal = pygame.draw.circle(self.screen, (0,0,255), (self.portal.getPosX(1), self.portal.getPosY(1)), self.portal.getRadius())
            portal = pygame.draw.circle(self.screen, (0,0,255), (self.portal.getPosX(2), self.portal.getPosY(2)), self.portal.getRadius())

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

                self.snake.setIsDead(True)
                while self.snake.getIsDead():
                    self.screen.fill((255,255,255))
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
    portal = Portal()

    caretaker = Caretaker(player1)
    play = PlayGame(player1, food, portal, caretaker) # Originator

