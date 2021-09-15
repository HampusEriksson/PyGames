from threeconst import *
import sys

pygame.font.init()
pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(str(BOARD_SIZE) + " in a row")


def draw_window(board):
    for row in board:
        for cell in row:
            cell.draw(WIN)

    pygame.display.update()


def checkwin(board):

    for row in board:
        if row[0].text != "" and len(set([x.text for x in row])) == 1:
            return True

    for row in flip(board):
        if row[0].text != "" and len(set([x.text for x in row])) == 1:
            return True

    diag1 = [board[i][i].text for i in range(len(board))]
    diag2 = [board[i][len(board) - 1 - i].text for i in range(len(board))]

    if (diag1[0] != "" and len(set(diag1)) == 1) or (
        diag2[0] != "" and len(set(diag2)) == 1
    ):
        return True

    return False


def main():
    clock = pygame.time.Clock()
    board = [["" for x in range(BOARD_SIZE)] for x in range(BOARD_SIZE)]
    turn = 0

    game_over = False

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            board[row][col] = Button(
                WHITE,
                col * (WIDTH // BOARD_SIZE),
                row * (HEIGHT // BOARD_SIZE),
                WIDTH // BOARD_SIZE-3,
                HEIGHT // BOARD_SIZE-3,
            )

    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for row in board:
                    for cell in row:
                        if cell.isClicked(
                            pygame.mouse.get_pos(), PLAYERMARKS[turn % 2]
                        ):
                            turn += 1
                            game_over = checkwin(board)

        for row in board:
            for cell in row:
                cell.isOver(pygame.mouse.get_pos())

        draw_window(board)


if __name__ == "__main__":
    main()
