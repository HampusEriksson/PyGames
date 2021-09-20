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

class Snakepart(pygame.sprite.Sprite):
    def __init__(self, color=GREEN):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((UNITSIZE, UNITSIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (UNITSIZE // 2, UNITSIZE // 2)
        self.direction = (0, 0)

    def update(self):
        self.rect.x += self.direction[0]*SPEED
        self.rect.y += self.direction[1]*SPEED

    def collide(self, spritegroup):
        if type(spritegroup) != list:
            spritegroup = [spritegroup]

        if pygame.sprite.spritecollide(self,spritegroup, False):
            print("Collision")
            return True



class Apple(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH//2, y=HEIGHT//2, color=RED):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((UNITSIZE, UNITSIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (UNITSIZE // 2, UNITSIZE // 2)

    def move(self):
        print("moving")
        self.rect.x, self.rect.y = random.randrange(0+UNITSIZE,WIDTH-UNITSIZE), random.randrange(0+UNITSIZE,HEIGHT-UNITSIZE)

