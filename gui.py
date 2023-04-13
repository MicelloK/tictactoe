# gui

import pygame
import sys

from game import BOARD, current_player, check_win, check_draw, make_move

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
running = True

def mainloop():
    global running
    pygame.init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    i, j = y // 200, x // 200
                    make_move(i, j)

        screen.fill(WHITE)
        draw_board()
        for i in range(3):
            for j in range(3):
                if BOARD[i][j] == 'X':
                    draw_x(i, j)
                elif BOARD[i][j] == 'O':
                    draw_o(i, j)
        draw_gameover()
        pygame.display.flip()

    pygame.quit()

def draw_board():
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

def draw_x(i, j):
    pygame.draw.line(screen, BLACK, (j * 200 + 50, i * 200 + 50), (j * 200 + 150, i * 200 + 150), 5)
    pygame.draw.line(screen, BLACK, (j * 200 + 150, i * 200 + 50), (j * 200 + 50, i * 200 + 150), 5)

def draw_o(i, j):
    pygame.draw.circle(screen, BLACK, (j * 200 + 100, i * 200 + 100), 50, 5)

def draw_text(text, color, size, x, y):
    font = pygame.font.SysFont('Arial', size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

def draw_gameover():
    if check_win():
        draw_text(f'{current_player} wins!', RED, 100, 100, 100)
    elif check_draw():
        draw_text('Draw!', RED, 100, 100, 100)

pygame.init()
