# game logic

import random
class Game:
    def __init__(self, player_symbol) -> None:
        self.player_symbol = player_symbol
        self.oponent_symbol = 'X' if player_symbol == 'O' else 'O'
        self.current_player = 'O'
        self.gameover = False
        self.BOARD = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

        if self.oponent_symbol == 'O':
            self.make_move(*self.random_move())

    def check_win(self):
        for i in range(3):
            if self.BOARD[i][0] == self.BOARD[i][1] == self.BOARD[i][2] != ' ':
                return True
            elif self.BOARD[0][i] == self.BOARD[1][i] == self.BOARD[2][i] != ' ':
                return True
        if self.BOARD[0][0] == self.BOARD[1][1] == self.BOARD[2][2] != ' ':
            return True
        elif self.BOARD[0][2] == self.BOARD[1][1] == self.BOARD[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.BOARD[i][j] == ' ':
                    return False
        return True
    
    def update_board(self):
        if self.check_win() or self.check_draw():
            self.gameover = True
        else:
            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def make_move(self, i, j):
        if self.BOARD[i][j] == ' ' and not self.gameover:
            self.BOARD[i][j] = self.current_player
            self.update_board()
            return True
        return False
    
    def random_move(self):
        moves = self.get_valid_moves()
        return random.choice(moves)
    
    def get_ai_move(self):
        def minimax(is_maximizing):
            moves = self.get_valid_moves()
            if self.check_win() and is_maximizing:
                return -1 - len(moves)
            elif self.check_win() and not is_maximizing:
                return 1 + len(moves)
            elif self.check_draw():
                return 0
            
            if is_maximizing:
                best_score = -float('inf')
                for move in moves:
                    self.BOARD[move[0]][move[1]] = self.oponent_symbol
                    score = minimax(False)
                    self.BOARD[move[0]][move[1]] = ' '
                    best_score = max(score, best_score)
                return best_score
            else:
                best_score = float('inf')
                for move in moves:
                    self.BOARD[move[0]][move[1]] = self.player_symbol
                    score = minimax(True)
                    self.BOARD[move[0]][move[1]] = ' '
                    best_score = min(score, best_score)
                return best_score
            
        best_score = -float('inf')
        best_move = None
        for move in self.get_valid_moves():
            self.BOARD[move[0]][move[1]] = self.oponent_symbol
            score = minimax(False)
            self.BOARD[move[0]][move[1]] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move            

    def get_valid_moves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.BOARD[i][j] == ' ':
                    moves.append((i, j))
        return moves
    