import random
import pygame

pygame.font.init()

WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
PINK = (255, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (40, 100, 20)
APPLESIZE = 50
UNITSIZE = 30
SCORE_FONT = pygame.font.SysFont("comicsans", 40)

FPS = 60


class Snakepart(pygame.sprite.Sprite):
    def __init__(self, center, color=GREEN, direction=(0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((UNITSIZE, UNITSIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.direction = direction
        self.speed = 5

    def update(self):
        self.rect.x += self.direction[0] * UNITSIZE // 5
        self.rect.y += self.direction[1] * UNITSIZE // 5

        if self.rect.left > WIDTH:
            self.rect.right = 0

        if self.rect.right < 0:
            self.rect.left = WIDTH

        if self.rect.bottom < 0:
            self.rect.top = HEIGHT

        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

    def collide(self, spritegroup):
        if pygame.sprite.spritecollide(self, spritegroup, False):
            print("Collision")
            return True


class Apple(pygame.sprite.Sprite):
    def __init__(self, color=RED):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((APPLESIZE, APPLESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self):
        print("moving")
        self.rect.x, self.rect.y = random.randrange(
            0 + UNITSIZE, WIDTH - UNITSIZE
        ), random.randrange(0 + UNITSIZE, HEIGHT - UNITSIZE)
