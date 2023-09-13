import pygame, random
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 1000
TILE_SIZE = SCREEN_WIDTH // 8

class Game:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.balls = [Ball(self)]
        self.tiles = []
        self.level = 1
        self.add_tiles()

    def draw(self):
        self.screen.fill(0)

        for ball in self.balls:
            ball.draw(self.screen)
        for tile in self.tiles:
            tile.draw(self.screen)

    def add_ball(self):
        self.balls.append(Ball(self))

    def level_up(self):
        self.level += 1
        for tile in self.tiles:
            tile.move_down()
        self.add_tiles()

    def add_tiles(self):
        for i in range(8):
            if random.random() < 0.8:
                self.tiles.append(Tiles(i * TILE_SIZE, TILE_SIZE//2, self))




class Tiles:
    def __init__(self, x, y, game) -> None:
        self.x = x
        self.y = y
        self.number = random.randint(game.level, game.level+5)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.game = game
        self.font = pygame.font.SysFont('Arial', 25)

    def draw(self, screen):
        pygame.draw.rect(screen, (155, 155, 155), self.rect)
        self.game.screen.blit(self.font.render(str(self.number), True, (255,0,0)), (self.x + TILE_SIZE//2, self.y+TILE_SIZE//2))

    def move_down(self):
        self.y += TILE_SIZE
        self.rect.y = self.y

class Ball:
    def __init__(self, game) -> None:
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 50
        self.rect = pygame.Rect(self.x, self.y, 25, 25)
        self.game = game
        self.moving = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
    def reset_position(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 50
        self.rect.x = self.x
        self.rect.y = self.y
    def update(self):
        if self.moving == True:
            self.x += self.direction[0]
            self.y += self.direction[1]
            self.rect.x = self.x
            self.rect.y = self.y
            # Check for collision with walls
            if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
                self.direction = (-self.direction[0], self.direction[1])
            if self.rect.top <= 0:
                self.direction = (self.direction[0], -self.direction[1])
            # Reset ball if it hits the bottom
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.moving = False
                self.reset_position()

            # Check for collision with tiles
            for tile in self.game.tiles:
                if self.rect.colliderect(tile.rect):
                    tile.number -= 1
                    if tile.number <= 0:
                        # Remove tile
                        self.game.tiles.remove(tile)

                    self.direction = (self.direction[0], -self.direction[1])
                    break



