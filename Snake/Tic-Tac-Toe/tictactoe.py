import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

run = True
clicked = False

# Define variables
# Line width
LINE_WIDTH = 15
BOARD_SIZE = 3

x_img = pygame.transform.scale(pygame.image.load('x.png'), (SCREEN_WIDTH//BOARD_SIZE, SCREEN_HEIGHT//BOARD_SIZE))
o_img = pygame.transform.scale(pygame.image.load('o.png'), (SCREEN_WIDTH//BOARD_SIZE, SCREEN_HEIGHT//BOARD_SIZE))


def draw_grid():
    bg = (255, 255, 200)
    grid_color = (23, 145, 135)
    screen.fill(bg)

    for x in range(1,BOARD_SIZE):
        pygame.draw.line(screen, grid_color, (0, SCREEN_HEIGHT*x/BOARD_SIZE), (SCREEN_WIDTH, SCREEN_HEIGHT*x/BOARD_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, grid_color, (SCREEN_WIDTH*x/BOARD_SIZE,0), (SCREEN_WIDTH*x/BOARD_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

def draw_symbols():
    for ri, row in enumerate(board):
        for ci, col in enumerate(row):
            if col == 1:
                screen.blit(x_img, (int(ci*(SCREEN_WIDTH/BOARD_SIZE) + (SCREEN_WIDTH/(BOARD_SIZE*2)) - x_img.get_width()/2), int(ri*(SCREEN_HEIGHT/BOARD_SIZE) + (SCREEN_HEIGHT/(BOARD_SIZE*2)) - x_img.get_height()/2)))
            if col == -1:
                screen.blit(o_img, (int(ci*(SCREEN_WIDTH/BOARD_SIZE) + (SCREEN_WIDTH/(BOARD_SIZE*2)) - o_img.get_width()/2), int(ri*(SCREEN_HEIGHT/BOARD_SIZE) + (SCREEN_HEIGHT/(BOARD_SIZE*2)) - o_img.get_height()/2)))
def check_win():
    if any(abs(sum(row)) == BOARD_SIZE for row in board):
        return True
    # Check columns
    if any(abs(sum(row)) == BOARD_SIZE for row in zip(*board)):
        return True
    if abs(sum(board[i][i] for i in range(BOARD_SIZE))) == BOARD_SIZE:
        return True
    if abs(sum(board[i][BOARD_SIZE-1-i] for i in range(BOARD_SIZE))) == BOARD_SIZE:
        return True
    return False
def draw_winner():
    font = pygame.font.Font(None, 100)
    text = font.render("Player 1 wins!" if player == -1 else "Player 2 wins!", True, (255, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
board = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)]
player = 1

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            print(pos)
            if board[pos[1]*BOARD_SIZE//SCREEN_HEIGHT][pos[0]*BOARD_SIZE//SCREEN_WIDTH] == 0:
                board[pos[1]*BOARD_SIZE//SCREEN_HEIGHT][pos[0]*BOARD_SIZE//SCREEN_WIDTH] = player
                player *= -1
                print(board)
    draw_grid()
    draw_symbols()
    if check_win():
        
        draw_winner()
        run = False
    
    pygame.display.update()

# Keep the pygame window open



