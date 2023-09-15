from ballz_constants import *
import pygame
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ballz")

game = Game(screen)


run = True
balls_moving = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == MOUSEBUTTONUP and balls_moving == False:
            balls_moving = True
            pos = pygame.mouse.get_pos()
            dx = pos[0] - SCREEN_WIDTH / 2
            dy = pos[1] - (SCREEN_HEIGHT - 50)
            distance = max(1, pygame.math.Vector2(dx, dy).length())
            direction = (dx / distance, dy / distance)
            for ball in game.balls:
                ball.direction = direction
                ball.moving = True
                ball.update()
                pygame.time.delay(10)
            
    if all(ball.moving == False for ball in game.balls) and balls_moving == True:
        balls_moving = False
        game.level_up()

            

    for ball in game.balls:
        ball.update()

    game.draw()
    pygame.display.update()

    if any(tile for tile in game.tiles if tile.y >= SCREEN_HEIGHT):
        run = False
        print("Game Over")
        print("Level:", game.level)
        print("Tiles:", len(game.tiles))
        print("Balls:", len(game.balls))


pygame.quit()