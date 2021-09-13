import pygame
import os
from threeconst import *
import numpy as np
import time

pygame.font.init()
pygame.init()

# Skapar ett fönster
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three in row")


def draw_window(board, buttons):
    for button in buttons:
        button.draw(WIN)

    pygame.display.update()

def checkwin(buttons):
    if buttons[0].text == buttons[1].text and buttons[0].text == buttons[2].text:
        pygame.quit()

    elif buttons[0].text == buttons[3].text and buttons[0].text == buttons[6].text:
        pygame.quit()

    elif buttons[6].text == buttons[7].text and buttons[6].text == buttons[8].text:
        pygame.quit()

    elif buttons[2].text == buttons[5].text and buttons[2].text == buttons[8].text:
        pygame.quit()

    elif buttons[0].text == buttons[4].text and buttons[0].text == buttons[8].text:
        pygame.quit()

    elif buttons[6].text == buttons[4].text and buttons[6].text == buttons[2].text:
        pygame.quit()


def main():
    buttons = []
    clock = pygame.time.Clock()
    run = True
    board = np.zeros((BOARD_SIZE, BOARD_SIZE))
    print(board)
    turn = 0

    for x in range(3):
        for y in range(3):
            print("Adding button")

            buttons.append(Button(WHITE, x*150, y*150, 145, 145))


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                for button in buttons:
                    if button.isOver(pygame.mouse.get_pos(),PLAYERMARKS[turn % 2]):
                        turn += 1
                        #checkwin(buttons)

        draw_window(board, buttons)


    main()


if __name__ == "__main__":
    main()
