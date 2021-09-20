
import pygame
from snakeconst import *
import time
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def draw_window(win, all_sprites):
    win.fill(0)

    all_sprites.draw(win)

    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    apple = Apple()
    all_sprites.add(apple)

    game_over = False
    head = Snakepart()
    all_sprites.add(head)
    apple.move()

    while not game_over:
        clock.tick(FPS)
        head.update()

        if head.collide(apple):
            apple.move()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    head.direction = (0,-1)
                if event.key == pygame.K_a:
                    head.direction = (-1,0)
                if event.key == pygame.K_s:
                    head.direction = (0,1)
                if event.key == pygame.K_d:
                    head.direction = (1,0)



        draw_window(WIN, all_sprites)


if __name__ == "__main__":
    main()
