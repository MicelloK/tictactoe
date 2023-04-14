# gui

import pygame
import sys

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60

class Gui:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.WIN = pygame.display.set_mode((600, 600))
        self.run = True

    def mainloop(self):
        while self.run:
            pygame.time.Clock().tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        i, j = y // 200, x // 200
                        self.game.make_move(i, j)

            self.draw_board()
            self.draw_gameover()
            pygame.display.flip()

        pygame.quit()

    def draw_board(self):
        self.WIN.fill(WHITE)
        pygame.draw.line(self.WIN, BLACK, (200, 0), (200, 600), 5)
        pygame.draw.line(self.WIN, BLACK, (400, 0), (400, 600), 5)
        pygame.draw.line(self.WIN, BLACK, (0, 200), (600, 200), 5)
        pygame.draw.line(self.WIN, BLACK, (0, 400), (600, 400), 5)

        for i in range(3):
                for j in range(3):
                    if self.game.BOARD[i][j] == 'X':
                        self.draw_x(i, j)
                    elif self.game.BOARD[i][j] == 'O':
                        self.draw_o(i, j)

    def draw_x(self, i, j):
        pygame.draw.line(self.WIN, BLACK, (j * 200 + 50, i * 200 + 50), (j * 200 + 150, i * 200 + 150), 5)
        pygame.draw.line(self.WIN, BLACK, (j * 200 + 150, i * 200 + 50), (j * 200 + 50, i * 200 + 150), 5)

    def draw_o(self, i, j):
        pygame.draw.circle(self.WIN, BLACK, (j * 200 + 100, i * 200 + 100), 50, 5)

    def draw_text(self, text, color, size, x, y):
        font = pygame.font.SysFont('Arial', size)
        text = font.render(text, True, color)
        self.WIN.blit(text, (x, y))

    def draw_gameover(self):
        if self.game.gameover:
            if self.game.check_win():
                self.draw_text(f'{self.game.current_player} won!', RED, 100, 150, 250)
            elif self.game.check_draw():
                self.draw_text('Draw!', RED, 100, 250, 250)



# colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# SIZE = WIDTH, HEIGHT = 600, 600
# WIN = pygame.display.set_mode(SIZE)
# run = True

# def mainloop():
#     global run
#     pygame.init()

#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 sys.exit()

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     x, y = event.pos
#                     i, j = y // 200, x // 200
#                     make_move(i, j)

#         draw_board()
        
#         draw_gameover()
#         pygame.display.flip()

#     pygame.quit()

# def draw_board():
#     WIN.fill(WHITE)
#     pygame.draw.line(WIN, BLACK, (200, 0), (200, 600), 5)
#     pygame.draw.line(WIN, BLACK, (400, 0), (400, 600), 5)
#     pygame.draw.line(WIN, BLACK, (0, 200), (600, 200), 5)
#     pygame.draw.line(WIN, BLACK, (0, 400), (600, 400), 5)

#     for i in range(3):
#             for j in range(3):
#                 if BOARD[i][j] == 'X':
#                     draw_x(i, j)
#                 elif BOARD[i][j] == 'O':
#                     draw_o(i, j)

# def draw_x(i, j):
#     pygame.draw.line(WIN, BLACK, (j * 200 + 50, i * 200 + 50), (j * 200 + 150, i * 200 + 150), 5)
#     pygame.draw.line(WIN, BLACK, (j * 200 + 150, i * 200 + 50), (j * 200 + 50, i * 200 + 150), 5)

# def draw_o(i, j):
#     pygame.draw.circle(WIN, BLACK, (j * 200 + 100, i * 200 + 100), 50, 5)

# def draw_text(text, color, size, x, y):
#     font = pygame.font.SysFont('Arial', size)
#     text = font.render(text, True, color)
#     WIN.blit(text, (x, y))

# def draw_gameover():
#     if check_win():
#         draw_text(f'{current_player} wins!', RED, 100, 100, 100)
#     elif check_draw():
#         draw_text('Draw!', RED, 100, 100, 100)
