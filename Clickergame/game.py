from constants import *
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickergame")


def draw(buttons):

    for button in buttons:
        button.draw()

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    buttons = []
    for button, i in enumerate(BUTTONNAMES):
        buttons.append(Button(RED, (i+1)*(HEIGHT // 12), i*10, i*100, button))



    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isClicked(pygame.mouse.get_pos()):
                        pass

        for button in buttons:
                button.isOver(pygame.mouse.get_pos())

        draw(buttons)


if __name__ == "__main__":
    main()
