import pygame

WIDTH, HEIGHT = 600,600
FPS = 60
BOARD_SIZE = 5

WHITE = (255, 255, 255)
PINK = (255, 200, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

PLAYERMARKS = ["X", "O"]

def flip(array):
    newarray = [[[] for x in range(len(array))] for x in range(len(array))]
    for row in range(len(array)):
        for col in range(len(array)):
            newarray[col][row] = array[row][col]

    return newarray

class Button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = pygame.font.SysFont('comicsans', 800//BOARD_SIZE)


    def draw(self, win):

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':

            text = self.font.render(self.text, 1, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))


    def isClicked(self, pos, text):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if self.text == "":
                    self.text = text
                return True

        return False

    def isOver(self, pos):

        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                self.color  = PINK
                return

        self.color = WHITE

WHITE if () else BLACK