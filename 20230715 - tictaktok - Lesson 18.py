import pygame
import random

width = 300
height = 300
fps = 30
blue = 34, 0, 255
red = 255, 3, 3
green = 0, 255, 0
white = 255, 255, 255
field = [["", "", ""], ["", "", ""], ["", "", ""]]
game_over = False
win = None

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("TicTacToe")
run = True


def draw_grid():
    pygame.draw.line(window, red, (100, 0), (100, 300), 3)
    pygame.draw.line(window, red, (200, 0), (200, 300), 3)
    pygame.draw.line(window, red, (0, 100), (300, 100), 3)
    pygame.draw.line(window, red, (0, 200), (300, 200), 3)


def draw_symbols():
    for i in range(3):
        for j in range(3):
            symbol = field[i][j]
            if symbol == "X":
                pygame.draw.line(window, red, (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(window, red, (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)
            elif symbol == "O":
                pygame.draw.circle(window, red, (j * 100 + 50, i * 100 + 50), 40, 3)


def check_winner(a):
    global win
    flag_win = False
    for i in field:
        if i.count(a) == 3:
            flag_win = True
            win = [[0, field.index(i)], [1, field.index(i)], [2, field.index(i)]]
    for j in range(3):
        if field[0][j] == field[1][j] == field[2][j] == a:
            flag_win = True
            win = [[j, 0], [j, 1], [j, 2]]
    if field[0][0] == field[1][1] == field[2][2] == a:
        flag_win = True
        win = [[0, 0], [1, 1], [2, 2]]
    if field[2][0] == field[1][1] == field[0][2] == a:
        flag_win = True
        win = [[2, 0], [1, 1], [0, 2]]
    return flag_win


def get_grid_position(pos):
    row = pos[1] // 100
    col = pos[0] // 100
    return row, col


def check_cell(pos):
    row, col = get_grid_position(pos)
    return field[row][col] == ""


clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            row, col = mouse_pos[1] // 100, mouse_pos[0] // 100
            if field[row][col] == "":
                field[row][col] = "X"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while field[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                field[x][y] = "O"
            player_win = check_winner("X")
            comp_win = check_winner("O")
            draw_win = field[0].count("X") + field[0].count("O") + field[1].count("X") + field[1].count("O") + field[
                2].count("X") + field[2].count("O")
            if comp_win or player_win or draw_win == 9:
                game_over = True
                if comp_win:
                    pygame.display.set_caption("The computer has won")
                elif player_win:
                    pygame.display.set_caption("You have won")
                elif draw_win == 9:
                    pygame.display.set_caption("It's a draw")

    window.fill(white)
    draw_grid()
    draw_symbols()
    if win is not None:
        pygame.draw.rect(window, green, (win[0][0] * 100, win[0][1] * 100, 100, 100))
        pygame.draw.rect(window, green, (win[1][0] * 100, win[1][1] * 100, 100, 100))
        pygame.draw.rect(window, green, (win[2][0] * 100, win[2][1] * 100, 100, 100))
    draw_symbols()
    pygame.display.flip()

pygame.quit()
