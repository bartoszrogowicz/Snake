from random import randint
from time import sleep
class Player:
    x = []
    y = []
    step = 50
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        #set snake on start
        self.x.append(randint(2, 9) * self.step)
        self.y.append(randint(4, 5) * self.step)
        #self.x.append(250)
        #self.y.append(250)
        for i in range(1, 2000):
            self.x.append(-100)
            self.y.append(-100)

        #init pos for non colision
        self.x[1] = 1 * self.step
        self.x[2] = 2 * self.step

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                #print "self.x[" + str(i) + "] = self.x[" + str(i - 1) + "]"
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step

            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
