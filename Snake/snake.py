from snakeconst import *
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


def draw_window(WIN, score, *spritegroups):
    WIN.fill(0)

    score_text = SCORE_FONT.render("Score: " + str(score), 1, WHITE)
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

    head = Snakepart(center=(WIDTH // 2, HEIGHT // 2), color=PINK)
    headgroup.add(head)

    while not game_over:
        clock.tick(FPS)

        if head.collide(applegroup):
            apple.move()
            score += 1
            bodygroup.add(
                Snakepart(
                    center=(
                        head.rect.center[0] + UNITSIZE * head.direction[0],
                        head.rect.center[1] + UNITSIZE * head.direction[1],
                    ),
                    direction=bodygroup.sprites()[-1].direction
                    if len(bodygroup) >= 1
                    else head.direction,
                )
            )

        head.update()

        newpos = [head] + [part for part in bodygroup]

        if len(bodygroup) >= 1:
            for i, part in enumerate(bodygroup):
                part.direction = newpos[i].direction
                part.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                key_directions = {
                    pygame.K_ESCAPE: (0, 0),
                    pygame.K_w: (0, -1),
                    pygame.K_a: (-1, 0),
                    pygame.K_s: (0, 1),
                    pygame.K_d: (1, 0),
                }

                head.direction = key_directions.get(event.key, head.direction)

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

        draw_window(WIN, score, bodygroup, applegroup, headgroup)


if __name__ == "__main__":
    main()
