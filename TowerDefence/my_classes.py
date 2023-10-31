import pygame, math
from constants import *
class Game:

    def __init__(self, screen) -> None:
        self.tiles = []
        self.screen = screen
        self.enemies = []
        self.gold = 100
        self.bullets = []


class Tile:

    def __init__(self, x,y, game, color) -> None:
        self.x = x
        self.y = y
        self.game = game
        self.color = color
        self.rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)


    def update(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        
    
class Grass(Tile):

    def __init__(self, x, y, game) -> None:
        super().__init__(x, y, game, GREEN)
        self.tower = None

    def update(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        if self.tower:
            self.tower.update()

class Dirt(Tile):

    def __init__(self, x, y, game) -> None:
        super().__init__(x, y, game, BROWN)

    

class Enemy:

    def __init__(self,game) -> None:
        self.game = game
        self.color = (255,0,0)
        self.target = PATH_COORDINATES[1]
        self.rect = pygame.Rect(PATH_COORDINATES[0][0]*CELL_WIDTH,PATH_COORDINATES[0][1]*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)


    def update(self):
        
        dist = math.sqrt((self.rect.x-self.target[0]*CELL_WIDTH)**2 + (self.rect.y-self.target[1]*CELL_HEIGHT)**2)

        if dist == 0.0:
            self.target = PATH_COORDINATES[PATH_COORDINATES.index(self.target) + 1]

        if self.rect.x < self.target[0]*CELL_WIDTH:
            self.rect.x += 1
        elif self.rect.x > self.target[0]*CELL_WIDTH:
            self.rect.x -= 1
        elif self.rect.y < self.target[1]*CELL_HEIGHT:
            self.rect.y += 1
        elif self.rect.y > self.target[1]*CELL_HEIGHT:
            self.rect.y -= 1

        pygame.draw.rect(self.game.screen, self.color, self.rect)
        

class Tower:

    def __init__(self, x, y, game) -> None:
        self.x = x
        self.y = y
        self.game = game
        self.color = (0,0,255)
        self.rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
        self.max_cooldown = 60
        self.cooldown = self.max_cooldown

    def update(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        self.cooldown -= 1
        if self.cooldown == 0:
            self.cooldown = self.max_cooldown
            self.game.bullets.append(Bullet(self.x, self.y, self.game))


class Bullet:

    def __init__(self, x, y, game) -> None:
        self.x = x
        self.y = y
        self.game = game
        self.color = (0,0,0)
        self.rect = pygame.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)
        self.target = None

        for enemy in self.game.enemies:
            if enemy.rect.collidepoint(self.x, self.y):
                self.target = enemy

    def update(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        if self.target:
            dist = math.sqrt((self.rect.x-self.target.rect.x)**2 + (self.rect.y-self.target.rect.y)**2)
            if dist == 0.0:
                self.game.enemies.remove(self.target)
                self.game.gold += 10
                self.game.bullets.remove(self)
            else:
                self.rect.x += (self.target.rect.x - self.rect.x) / dist
                self.rect.y += (self.target.rect.y - self.rect.y) / dist
        else:
            self.game.bullets.remove(self)

