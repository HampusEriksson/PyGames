
from snakeconst import *
import time
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def draw_window(WIN, score, *spritegroups):
    WIN.fill(0)

    score_text = SCORE_FONT.render(
        "Score: " + str(score), 1, WHITE)
    WIN.blit(score_text, (10, 10))

    for group in spritegroups:
        group.draw(WIN)
        
    pygame.display.update()

def main():
    score = 0
    clock = pygame.time.Clock()
    game_over = False

    bodygroup, applegroup, headgroup = (pygame.sprite.Group() for _ in range(3))

    apple = Apple()
    applegroup.add(apple)
    apple.move()
    print(len(applegroup))

    head = Snakepart(color=PINK)
    headgroup.add(head)

    while not game_over:
        clock.tick(FPS)

        if head.collide(applegroup):
            apple.move()

            head.speed *= 1.02
            score +=1
            part = Snakepart()
            bodygroup.add(part)

        newpos = [head.rect.center] + [x.rect.center for x in bodygroup]

        if len(bodygroup) >= 1:
            for i, part in enumerate(bodygroup):
                part.rect.center = newpos[i]

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



        draw_window(WIN, score, bodygroup, applegroup, headgroup)


if __name__ == "__main__":
    main()
