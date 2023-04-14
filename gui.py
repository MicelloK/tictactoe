# gui

import pygame
import sys

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

FPS = 60

SIZE = WIDTH, HEIGHT = 600, 600
SQ_SIZE = SQ_WIDTH, SQ_HEIGHT = WIDTH // 3, HEIGHT // 3

class Gui:
    def __init__(self, game):
        self.game = game
        pygame.init()
        self.WIN = pygame.display.set_mode(SIZE)
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
                        i, j = y // (SQ_HEIGHT), x // (SQ_WIDTH)
                        self.game.make_move(i, j)

            self.draw_board()
            self.draw_gameover()
            pygame.display.flip()

        pygame.quit()

    def draw_board(self):
        self.WIN.fill(WHITE)
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
            font_size = SQ_HEIGHT//2
            if self.game.check_win():
                self.draw_text(f'{self.game.current_player} won!')
            elif self.game.check_draw():
                self.draw_text('Draw!')
