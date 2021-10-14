import random

import pygame

WIDTH, HEIGHT = 1200, 675
FPS = 60

BUTTONNAMES = []
TREENAMES = ["tree", "eucalyptus"]
WHITE = (255, 255, 255)
PINK = (255, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

MEW = pygame.image.load("Assets/mew.png")
MEW = pygame.transform.scale(MEW,(int(MEW.get_width()*0.2), int(MEW.get_height()*0.2)))

EEVEE = pygame.image.load("Assets/eevee.png")
EEVEE = pygame.transform.scale(EEVEE,(int(EEVEE.get_width()*0.2), int(EEVEE.get_height()*0.2)))

TURTWIG = pygame.image.load("Assets/turtwig.png")
TURTWIG = pygame.transform.scale(TURTWIG,(int(TURTWIG.get_width()*0.2), int(TURTWIG.get_height()*0.2)))

class Button:
    def __init__(self, image, y, cost, value):
        self.width = WIDTH // 5
        self.height = HEIGHT // 12
        self.regimage = pygame.transform.scale(
            pygame.image.load("Assets/" + image + ".png"), (self.width, self.height)
        )
        self.bigimage = pygame.transform.scale(
            pygame.image.load("Assets/" + image + ".png"), (int(self.width*1.1), int(self.height*1.1))
        )
        self.image = self.bigimage
        self.x = (WIDTH * 3) // 4
        self.y = y
        self.font = pygame.font.SysFont("comicsans", 800 // HEIGHT)
        self.cost = cost
        self.value = value

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def isClicked(self, pos):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:

                return True

        return False

    def isOver(self, pos):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if (pos[0] > self.x and pos[0] < self.x + self.width) and (pos[1] > self.y and pos[1] < self.y + self.height):
            self.image = self.bigimage
        else:
            self.image = self.regimage

        self.color = WHITE
