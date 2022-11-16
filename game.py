import os
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        print("-------------")
        for i in range(3):
            for j in range(3):
                print('|', self.board[i*3 + j], end=' ')
            print("|\n", "-------------", sep='')

    @staticmethod
    def print_num_board():
        print("-------------")
        for i in range(3):
            for j in range(3):
                print('|', i*3 + j + 1, end=' ')
            print("|\n", "-------------", sep='')

    def empty_fields(self) -> bool:
        return ' ' in self.board

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']

    def make_move(self, player):
        move = player.get_move(self.available_moves())
        self.board[move] = player.letter
    
    def find_winner(self) -> str:
        winner = None
        # rows
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] and self.board[i*3] != ' ':
                winner = self.board[i*3]
        
        # columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != ' ':
                winner = self.board[i]
            
        # diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ':
            winner = self.board[0]
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            winner = self.board[2]

        return winner

def play(game, player1, player2):
    def next_player(player):
        return player1 if player == player2 else player2

    winner = None
    game_over = False
    curr_player = player1

    while not game_over:
        os.system('cls')
        TicTacToe.print_num_board()
        game.print_board()
        game.make_move(curr_player)
        winner = game.find_winner()
        curr_player = next_player(curr_player)
        
        if winner is not None or not game.empty_fields():
            game_over = True

    
    if winner is None:
        print("Draw")
    else:
        game.print_board()
        print("The winner is", winner)

game = TicTacToe()
p1 = HumanPlayer('O')
p2 = HumanPlayer('X')

play(game, p1, p2)
