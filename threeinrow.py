import pygame
import os
from threeconst import *
import numpy as np
import time
import sys

pygame.font.init()
pygame.init()

# Skapar ett fönster
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Three in row")


def draw_window(board):
    for row in board:
        for cell in row:
            cell.draw(WIN)

    pygame.display.update()

def checkwin(board):

    for row in board:
        if row[0].text != "" and len(set([x.text for x in row])) == 1:
            return True

    for row in np.flip(board):
        if row[0].text != "" and len(set([x.text for x in row])) == 1:
            return True

    return False



def main():
    buttons = []
    clock = pygame.time.Clock()
    board = [["", "", ""], ["","",""], ["", "", ""]]
    print(board)
    turn = 0

    game_over = False

    for x in range(3):
        for y in range(3):
            print("Adding button")
            board[x][y] = Button(WHITE, x*150, y*150, 145, 145)
            #buttons.append(Button(WHITE, x*150, y*150, 145, 145))


    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:

                for row in board:
                    for cell in row:
                        if cell.isOver(pygame.mouse.get_pos(),PLAYERMARKS[turn % 2]):
                            turn += 1
                            game_over = checkwin(board)

        draw_window(board)




if __name__ == "__main__":
    main()


