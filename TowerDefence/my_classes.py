import pygame, math
from constants import *
class Game:

    def __init__(self, screen) -> None:
        self.tiles = []
        self.screen = screen
        self.enemies = []


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
        print(dist, PATH_COORDINATES.index(self.target), PATH_COORDINATES[PATH_COORDINATES.index(self.target) + 1])
        if dist == 0.0:
            print("Byter target")
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
        