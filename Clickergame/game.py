from constants import *
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clickergame")

def drawpokemon(win, pokemon):
    win.blit(

        pokemon

        ,
        (
            random.randrange(WIDTH // 4, (WIDTH * 3) // 4),
            random.randrange(HEIGHT // 4, (HEIGHT * 3) // 4),
        ),
    )
    
def draw(win, buttons, plantedtrees):
    x = plantedtrees
    win.fill(0)
    for button in buttons:
        button.draw(win)
    while True:
        if x - 100 > 0:
            x-=100
            drawpokemon(win, TURTWIG)
        if x - 10 > 0:
            x -= 10
            drawpokemon(win, MEW)
            

        if x - 1 >= 0:
            x -= 1
            drawpokemon(win, EEVEE)
        
        if x <= 0:
            break

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    buttons = []
    pokemons = 0

    for i, button in enumerate(BUTTONNAMES):
        buttons.append(Button(button, (i + 1) * (HEIGHT // 12), i * 10, i * 100))

    counter = 0

    while True:
        clock.tick(FPS)

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
            
        counter += 1
        if counter % FPS == 0:
            pokemons += 1
            draw(WIN, buttons, pokemons)


if __name__ == "__main__":
    main()
