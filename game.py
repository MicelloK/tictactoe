# game logic

current_player = 'O'
gameover = False

BOARD = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def check_win():
    global current_player
    for i in range(3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] != ' ':
            return True
        elif BOARD[0][i] == BOARD[1][i] == BOARD[2][i] != ' ':
            return True
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != ' ':
        return True
    elif BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != ' ':
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] == ' ':
                return False
    return True

def update_board():
    global current_player
    global gameover
    if check_win() or check_draw():
        gameover = True
    else:
        current_player = 'X' if current_player == 'O' else 'O'

def make_move(i, j):
    global current_player
    global gameover
    if BOARD[i][j] == ' ' and not gameover:
        BOARD[i][j] = current_player
        update_board()
        return True
    return False
