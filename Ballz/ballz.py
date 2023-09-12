from constants import *
import pygame
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ballz")

game = Game(screen)


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game.draw()
    pygame.display.update()


pygame.quit()