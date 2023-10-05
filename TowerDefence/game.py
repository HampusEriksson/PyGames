import pygame
from pygame.locals import *
from constants import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT+200))
pygame.display.set_caption("Tower Defence")

run = True

def draw():
    screen.fill((0, 255, 0))
    # Draw the grid lines
    for x in range(0, SCREEN_WIDTH, CELL_WIDTH):
        pygame.draw.line(screen, BLACK, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, y), (SCREEN_WIDTH, y))

    for coord in PATH_COORDINATES:
        cell_x, cell_y = coord
        pygame.draw.rect(screen, BROWN, (cell_x * CELL_WIDTH, cell_y * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))
    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT, SCREEN_WIDTH, 200))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw()
    pygame.display.update()


pygame.quit()