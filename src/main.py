import pygame
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
        self.apple = Apple(5, 5)
        self.game = Game()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        self.score()

        pygame.display.set_caption('SnakePyGame')
        self._running = True

        self._image_surf = pygame.image.load("../static/green-square.png").convert()
        self._apple_surf = pygame.image.load("../static/apple.png").convert()

    def score(self):
        self._font = pygame.font.SysFont(None, 30)
        self._display_surf.blit(self._font.render('Hello!', True, (255, 0, 0)), (200, 100))
        pygame.display.update()
        # pygame.font.init()
        # self._myfont = pygame.font.SysFont(None, 30)
        # self._label = self._myfont.render("Score:", True, (255,255,0))
        # self._textrect = self._label.get_rect()
        # self._textrect.centerx = screen.get_rect().centerx
        # self._textrect.centery = screen.get_rect().centery
        #
        # screen.fill((255,255,255))
        # screen.blit(self._label, self._textrect)
        # print("TEXT")
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.player.update()

        #snake eat apple
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2, 9) * 44
                self.apple.y = randint(2, 9) * 44
                self.player.length += 1

        for i in range(2, self.player.length):
             if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                 print("You lose! Collision: ")
                 print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                 print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                 exit(0)

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while(self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                self.on_event(event)
            if (keys[K_RIGHT]):
                self.player.moveRight()

            if (keys[K_LEFT]):
                self.player.moveLeft()

            if (keys[K_UP]):
                self.player.moveUp()

            if (keys[K_DOWN]):
                self.player.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False
                print "QUIT1"

            self.score()
            self.on_loop()
            self.on_render()

            sleep(50.0 / 1000.0);
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()