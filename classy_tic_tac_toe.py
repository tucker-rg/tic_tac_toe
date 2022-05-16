#practice round 4
#remembering the classes where I taught classes

from math import sqrt
board = []

class GridLocation:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = "_"

    def update(self, mark):
        self.state = mark

    def status_report(self):
        return self.state


def tic_tac_board(board_name, rows, columns):
    for i in range(rows):
        for j in range(columns):
            board.append(GridLocation(i, j))

def print_board(board_name):
    '''display boardstate to player'''
    # I should be able to create the board in one move
    board_len = range(int(sqrt(len(board_name))))
    display_board = [list(list() for i in board_len) for j in board_len]
    for i in board_name:
        display_board[i.row][i.column] = i.status_report()
    for i in board_len:
        print(display_board[i])

def turn():
    #try to make something usable by player and computer

def check_game_status(board_name):
    '''see if the game is over'''
    #how do I make this pretty, and how do I do it using the row and column of each object?
    
'''
    if [0:3] are all equal
    if [3:6] are all equal
    if [6:9] are all equal
    if [::3] ''
    if [1::3] ''
    if [2::3] ''
    if [1::4] ''
    if [2:7:2] '' 
    
'''

tic_tac_board(board, 3, 3)
print_board(board)
