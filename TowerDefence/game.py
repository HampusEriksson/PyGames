import pygame
from pygame.locals import *
from constants import *
from my_classes import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defence")

run = True

game = Game(screen)

def draw():
    screen.fill(WHITE)
    # Draw the grid lines
    for x in range(0, GAME_WIDTH, CELL_WIDTH):
        pygame.draw.line(screen, BLACK, (x, 0), (x, GAME_HEIGHT))
    for y in range(0, GAME_HEIGHT, CELL_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, y), (GAME_WIDTH, y))

    for tile in game.tiles:
        tile.update()

    for enemy in game.enemies:
        enemy.update()

    pygame.draw.rect(screen, BLACK, (0, GAME_HEIGHT, GAME_WIDTH, 200))

for x in range(GRID_WIDTH):
    for y in range(GRID_HEIGHT):
        if (x,y) in PATH_COORDINATES:
            game.tiles.append(Dirt(x*CELL_WIDTH, y*CELL_HEIGHT, game))
        else:
            game.tiles.append(Grass(x*CELL_WIDTH, y*CELL_HEIGHT, game))

game.enemies.append(Enemy(game))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()
    pygame.display.update()


pygame.quit()