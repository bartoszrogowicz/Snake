from random import randint
class Apple:
    x = 0
    y = 0
    step = 50

    def __init__(self):
        self.x = randint(2, 9) * self.step
        self.y = randint(2, 9) * self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))