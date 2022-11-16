class HumanPlayer:
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, available_moves) -> int:
        valid_number = True
        while valid_number:
            move = int(input(self.letter + "'s move. Enter square field: ")) - 1
            if move not in available_moves:
                print("Ops, wrong field number, try again")
            else:
                valid_number = False
        return move
        
class ComputerPlayer:
    def __init__(self, letter) -> None:
        self.letter = letter
