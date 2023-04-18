# gui

import pygame
import sys
from time import sleep
from game import Game

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60

SIZE = WIDTH, HEIGHT = 600, 600
SQ_SIZE = SQ_WIDTH, SQ_HEIGHT = WIDTH // 3, HEIGHT // 3

class Gui:
    def __init__(self):
        self.game = None
        self.game_over_time = None
        pygame.init()
        self.WIN = pygame.display.set_mode(SIZE)

    def play(self):
        self.WIN.fill(WHITE)
        self.draw_init_screen()
        while True:
            pygame.time.Clock().tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x < WIDTH // 2:
                        self.game = Game('O')
                    else:
                        self.game = Game('X')
                    self.mainloop()

            pygame.display.update()

    def mainloop(self):
        self.WIN.fill(WHITE)
        while True:
            pygame.time.Clock().tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game.current_player == self.game.player_symbol and event.button == 1:
                        x, y = event.pos
                        i, j = y // (SQ_HEIGHT), x // (SQ_WIDTH)
                        self.game.make_move(i, j)

            if self.game.current_player != self.game.player_symbol and not self.game.gameover:
                self.game.make_move(*self.game.get_ai_move())

            self.draw_board()
            pygame.display.update()
            if self.game_over_time is None:
                self.draw_gameover()
            else:
                if pygame.time.get_ticks() - self.game_over_time > 2000:
                    self.game_over_time = None
                    self.game = None
                    self.play()

    def draw_init_screen(self):
        font = pygame.font.SysFont('comicsans', 100)
        text = font.render('Tic Tac Toe', 1, BLACK)
        self.WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 - text.get_height() // 2))

        # O button
        pygame.draw.circle(self.WIN, BLACK, (WIDTH // 2 - 100, HEIGHT // 2), 50)

        # X button
        pygame.draw.line(self.WIN, BLACK, (WIDTH // 2 + 100 - 50, HEIGHT // 2 - 50), (WIDTH // 2 + 100 + 50, HEIGHT // 2 + 50), 5)
        pygame.draw.line(self.WIN, BLACK, (WIDTH // 2 + 100 + 50, HEIGHT // 2 - 50), (WIDTH // 2 + 100 - 50, HEIGHT // 2 + 50), 5)

    def draw_board(self):
        pygame.draw.line(self.WIN, BLACK, (SQ_WIDTH, 0), (SQ_WIDTH, 3*SQ_HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (2*SQ_WIDTH, 0), (2*SQ_WIDTH, 3*SQ_HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (0, SQ_HEIGHT), (3*SQ_WIDTH, SQ_HEIGHT), 5)
        pygame.draw.line(self.WIN, BLACK, (0, 2*SQ_HEIGHT), (3*SQ_WIDTH, 2*SQ_HEIGHT), 5)

        for i in range(3):
                for j in range(3):
                    if self.game.BOARD[i][j] == 'X':
                        self.draw_x(i, j)
                    elif self.game.BOARD[i][j] == 'O':
                        self.draw_o(i, j)

    def draw_x(self, i, j):
        pygame.draw.line(self.WIN, BLACK, (j * SQ_WIDTH + SQ_WIDTH//4, i * SQ_HEIGHT + SQ_HEIGHT//4), (j * SQ_WIDTH + 3*SQ_WIDTH//4, i * SQ_HEIGHT + 3*SQ_HEIGHT//4), 5)
        pygame.draw.line(self.WIN, BLACK, (j * SQ_WIDTH + 3*SQ_WIDTH//4, i * SQ_HEIGHT + SQ_HEIGHT//4), (j * SQ_WIDTH + SQ_WIDTH//4, i * SQ_HEIGHT + 3*SQ_HEIGHT//4), 5)

    def draw_o(self, i, j):
        min_size = min(SQ_WIDTH, SQ_HEIGHT)
        pygame.draw.circle(self.WIN, BLACK, (j * SQ_WIDTH + SQ_WIDTH//2, i * SQ_HEIGHT + SQ_HEIGHT//2), min_size//4, 5)

    def draw_text(self, text):
        size = SQ_HEIGHT//2
        font = pygame.font.SysFont('Arial', size)
        text = font.render(text, True, RED)
        tesxt_rect = text.get_rect()
        tesxt_rect.center = (WIDTH//2, HEIGHT//2)
        self.WIN.blit(text, tesxt_rect)

    def draw_gameover(self):
        if self.game.gameover:
            if self.game.check_win():
                self.draw_text(f'{self.game.current_player} won!')
            elif self.game.check_draw():
                self.draw_text('Draw!')

            pygame.display.update()

            if self.game_over_time is None:
                self.game_over_time = pygame.time.get_ticks()
