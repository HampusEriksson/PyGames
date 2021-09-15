import random
import pygame

WIDTH, HEIGHT = 600,600
WHITE = (255, 255, 255)
PINK = (255, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (40,100,20)
UNITSIZE = 50
FPS = 60
SPEED = 5

class Pgobj(pygame.Rect):
    def __init__(self, x, y, color):
        self.color = color
        self.x = x
        self.y = y
        self.width = UNITSIZE
        self.height = UNITSIZE


    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

class Snakepart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((UNITSIZE, UNITSIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (UNITSIZE // 2, UNITSIZE // 2)
        self.direction = (0, 0)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


class Apple(Pgobj):
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, color=RED):
        super(Apple, self).__init__(x,y,color)

    def move(self):
        self.x, self.y = random.randrange(0+UNITSIZE,WIDTH-UNITSIZE), random.randrange(0+UNITSIZE,HEIGHT-UNITSIZE)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.width//2)
