import pygame
import os
from threeconst import *
import numpy as np

pygame.font.init()

# Skapar ett fönster
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three in row")


def draw_window(board):

    pygame.display.update()


def main():
    board = []
    clock = pygame.time.Clock()
    run = True
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    print(board)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window(board)


    main()


if __name__ == "__main__":
    main()
