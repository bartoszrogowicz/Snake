import pygame
import threading
from Apple import *
from pygame.locals import *
from Player import *
from Game import *
from time import sleep
from random import randint

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.player = Player(1)
        self.apple = Apple()
        self.game = Game()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('SnakePyGame')
        self._running = True

        self._image_surf = pygame.image.load("../static/green-square.png").convert()
        self._apple_surf = pygame.image.load("../static/logo.png").convert()

    def score(self, input_text, font_size, width, height):
        text = pygame.font.Font('freesansbold.ttf', font_size)
        text_surf = text.render(str(input_text), True, (255, 255, 255))
        #text_rect = text_surf.get_rect().center = (width, height)
        self._display_surf.blit(text_surf, (width,height)) #text_rect)
        pygame.display.update()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def crash(self):
        self.score("YOU LOSE!", 150, self.windowWidth / 50, self.windowHeight / 2.7)
        self.score("Your Score: " + str(self.player.length - 1), 70, (self.windowWidth / 4.2), (self.windowHeight / 1.5))

    def on_loop(self):
        self.player.update()
        apple_step = 25
        eat_flag = True
        flag = True

        #snake eat apple
        for i in range(0, self.player.length):
            if self.game.is_collision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], apple_step):
                if i != 0:
                    self.game.apple_collision(self.apple, self.player, apple_step)
                elif i == 0:
                    self.game.apple_collision(self.apple, self.player, apple_step)
                    self.player.length = self.player.length + 1

        #find collision
        for i in range(2, self.player.length):
             if self.game.is_collision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                 print("You lose! Collision: ")
                 print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                 print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                 self.crash()
                 sleep(3)
                 exit(0)

        if self.game.out_of_map(self.player.x[0], self.player.y[0], self.windowWidth, self.windowHeight):
            self.crash()
            sleep(3)
            exit(0)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        #self.score("Score: " + str(self.player.length - 1), 25, (self.windowWidth / 1.2), (self.windowHeight / 50))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        right_flag = True
        left_flag = True
        up_flag = True
        down_flag = True


        if self.on_init() is False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                self.on_event(event)

            if (keys[K_RIGHT] and right_flag):
                self.player.moveRight()
                left_flag = False
                up_flag = True
                down_flag = True

            if (keys[K_LEFT] and left_flag):
                self.player.moveLeft()
                right_flag = False
                up_flag = True
                down_flag = True

            if (keys[K_UP] and up_flag):
                self.player.moveUp()
                down_flag = False
                left_flag = True
                right_flag = True

            if (keys[K_DOWN] and down_flag):
                self.player.moveDown()
                up_flag = False
                right_flag = True
                left_flag = True

            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
            #self.score("Score: " + str(self.player.length - 1), 25, (self.windowWidth / 1.2), (self.windowHeight / 50))
            #pygame.display.update()
            sleep(50.0 / 1000.0);
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()