from constants import *
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickergame")


def draw(win, buttons, plantedtrees):
    x = plantedtrees
    win.fill(0)
    for button in buttons:
        button.draw(win)
    while True:
        if x - 10 > 0:
            x -= 10

            win.blit(
                pygame.transform.scale(
                    pygame.image.load("Assets/eucalyptus.png"),
                    (WIDTH // 5, HEIGHT // 12),
                ),
                (
                    random.randrange(WIDTH // 4, (WIDTH * 3) // 4),
                    random.randrange(HEIGHT // 4, (HEIGHT * 3) // 4),
                ),
            )

        if x - 1 >= 0:
            x -= 1
            win.blit(
                pygame.transform.scale(
                    pygame.image.load("Assets/tree.png"),
                    (WIDTH // 5, HEIGHT // 12),
                ),
                (
                    random.randrange(WIDTH // 4, (WIDTH * 3) // 4),
                    random.randrange(HEIGHT // 4, (HEIGHT * 3) // 4),
                ),
            )

        if x <= 0:
            break

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    buttons = []
    plantedtrees = 0
    trees = []
    for i, button in enumerate(BUTTONNAMES):
        buttons.append(Button(button, (i + 1) * (HEIGHT // 12), i * 10, i * 100))

    counter = 0

    while True:
        clock.tick(FPS)
        if counter % FPS == 0:
            plantedtrees += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isClicked(pygame.mouse.get_pos()):
                        print("Clicked")

        for button in buttons:
            button.isOver(pygame.mouse.get_pos())

        draw(WIN, buttons, plantedtrees)


if __name__ == "__main__":
    main()
