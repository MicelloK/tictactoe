# game logic

class Game:
    def __init__(self) -> None:
        self.current_player = 'O'
        self.gameover = False
        self.BOARD = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

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
