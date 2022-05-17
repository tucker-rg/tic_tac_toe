#note: does not run
#trying to make a gui for tic tac Toe

from tkinter import *
from tkinter.ttk import *

board = [['_','_','_'],['_','_','_'],['_','_','_']]
rows = {'top' : 0, 'middle' : 1, 'bottom' : 2}
columns = {'left' : 0, 'middle' : 1, 'right' : 2}

root = Tk()
root.geometry('128x128')
root.title('Tic Tac Tucker')

frame = Frame(root)
frame.pack()

def pick_a_spot(mark, row, column):
    global board
    board[row][column] = mark

#figure out how to bind commands and pass them variable args
top_left = Button(frame, text = board[0][0], command = lambda: pick_a_spot('X', 0, 0))
top_middle = Button(frame, text = board[0][1])
top_right = Button(frame, text = board[0][2])
middle_left = Button(frame, text = board[1][0])
middle_middle = Button(frame, text = board[1][1])
middle_right = Button(frame, text = board[1][2])
bottom_left = Button(frame, text = board[2][0])
bottom_middle = Button(frame, text = board[2][1])
bottom_right = Button(frame, text = board[2][2])

top_left.grid(row = 0, column = 0)
top_middle.grid(row = 0, column = 1)
top_right.grid(row = 0, column = 2)
middle_left.grid(row = 1, column = 0)
middle_middle.grid(row = 1, column = 1)
middle_right.grid(row = 1, column = 2)
bottom_left.grid(row = 2, column = 0)
bottom_middle.grid(row = 2, column = 1)
bottom_right.grid(row = 2, column = 2)

def player_turn(turn_num):
    '''prompts basic string input from user to determine their move'''
    if turn_num % 2 == 1:
        marker = 'X'
    else:
        marker = 'O'
    row = get_position(marker, 'row', rows, 'top, middle, bottom')
    column = get_position(marker, 'column', columns, 'left, middle, right')
    if check_move(row, column):
        print('\n* * * that spot is taken * * *\n')
        player_turn(turn_num)
    else:
        board[rows[row]][columns[column]] = marker
        print_board(board)
        check_win((board, rotate_board(board)), turn_num)

def check_move(x_axis, y_axis):
    '''see if move is already taken'''
    if board[rows[x_axis]][columns[y_axis]] != '_':
        return True
    else:
        pass

def check_win(board_names, turn_num):
    '''so many functions for checking if someone has won! this one combines the subfunctions'''
    for i in board_names:
        check_rows(i)
        check_diagonal(i)
    if turn_num >= 9:
            print('stalemate')
            quit()
    else:
        pass

def check_rows(board_name):
    '''check for 3 in a row across a list'''
    for x in board_name:
        if x[0] == x[1] and x[0] == x[2]:
            if x[0] != '_':
                end_game(x[0])
            else:
                pass
        else:
            pass

def rotate_board(board_name):
    '''fixed with some help from stackoverflow'''
    new_board = list(zip(*reversed(board)))
    return new_board

def check_diagonal(board_name):
    '''I'm sure there is a neater way to do this by shuffling the board and reusing the check_rows function'''
    if board_name[0][0] == board_name[1][1] and board_name[0][0] == board_name[2][2]:
        if board_name[0][0] != '_':
            end_game(board_name[0][0])
        else:
            pass
    else:
        pass

def end_game(mark):
    '''announce the winner'''
    print(f'\nPlayer {mark} wins')
    quit()

#get rid of old main() contents. You can't have two main loops lol.
def main():
    '''this is the game'''
    turn = 0
    print("\nWelcome to Tic-Tac-Toe\nX goes first")
    while True:
        root.mainloop()
        turn += 1
        player_turn(turn)

main()
