import pygame

WIDTH, HEIGHT = 1200,675
FPS = 60

BUTTONNAMES = []
WHITE = (255, 255, 255)
PINK = (255, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Button():
    def __init__(self, color, y, cost, value, text=''):
        self.color = color
        self.x = (WIDTH*3) // 4
        self.y = y
        self.width = WIDTH // 5
        self.height = HEIGHT // 12
        self.text = text
        self.font = pygame.font.SysFont('comicsans', 800//HEIGHT)
        self.cost = cost
        self.value = value


    def draw(self, win):

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
        text = self.font.render(self.text, 1, (0, 0, 0))
        win.blit(text,
                 (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isClicked(self, pos):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:

                return True

        return False

    def isOver(self, pos):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.color  = PINK
                return

        self.color = WHITE