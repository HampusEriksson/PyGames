import pygame
from snakeconst import *
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
    score = 0
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    apple = Apple()
    all_sprites.add(apple)
    game_over = False
    head = Snakepart()
    all_sprites.add(head)
    apple.move()
    body = []

    while not game_over:
        clock.tick(FPS)


        if head.collide(apple):
            apple.move()
            part = Snakepart()
            all_sprites.add(part)
            body.append(part)
            head.speed *= 1.02
            score +=1

        newpos = [head.rect.center] + [x.rect.center for x in body]

        if len(body) >= 1:
            for i in range(len(body)):
                body[i].rect.center = newpos[i]

        head.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    head.direction = (0,-1) if head.direction != (0,1) else head.direction
                if event.key == pygame.K_a:
                    head.direction = (-1,0) if head.direction != (1,0) else head.direction
                if event.key == pygame.K_s:
                    head.direction = (0,1) if head.direction != (0,-1) else head.direction
                if event.key == pygame.K_d:
                    head.direction = (1,0) if head.direction != (-1,0) else head.direction



        draw_window(WIN, all_sprites)


if __name__ == "__main__":
    main()
