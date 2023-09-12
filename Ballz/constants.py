import pygame

class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.balls = [Ball(self)]
        self.tiles = []
        self.level = 1

    def draw(self):
        for ball in self.balls:
            ball.draw(self.screen)
        for tile in self.tiles:
            tile.draw(self.screen)

    def add_ball(self):
        self.balls.append(Ball(self))

class Tiles:
    def __init__(self, x, y, number, game) -> None:
        self.x = x
        self.y = y
        self.number = number
        self.rect = pygame.Rect(x, y, 50, 50)
        self.game = game

    def draw(self, screen):
        pygame.draw.rect(screen, (155, 155, 155), self.rect)

class Ball:
    def __init__(self, game) -> None:
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 50
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        self.game = game

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000
