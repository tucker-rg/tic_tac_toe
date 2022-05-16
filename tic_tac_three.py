#practice round 3
#structure still seems sloppy. turn count seems sloppy. still boring. dumb computer.

import random

board = [['_','_','_'],['_','_','_'],['_','_','_']]
rows = {"top" : 0, "middle" : 1, "bottom" : 2}
columns = {"left" : 0, "middle" : 1, "right" : 2}

def print_board(board_name):
    '''display boardstate to player'''
    for i in range(3):
        print(' '.join(board_name[i]))

def rotate_board(board_name):
    '''with some help from stackoverflow'''
    new_board = list(zip(*reversed(board)))
    return new_board

def check_diagonal(board_name):
    '''I'm sure there is a neater way to do this by shuffling the board and reusing the check_win function'''
    if board_name[0][0] == board_name[1][1] and board_name[0][0] == board_name[2][2]:
        check_winner(board_name[0][0])
    else:
        pass

def player_turn(turn_num):
    '''prompts basic string input from user'''
    row, column = input("choose a row (top, middle, or bottom)"), input("choose a column (left, middle, or right")
    if row not in rows or column not in columns:
        print("I didn't understand. Choose again")
        player_turn(turn_num)
    else:
        if check_move(row, column):
            print("that spot is taken")
            player_turn(turn_num)
        else:
            board[rows[row]][columns[column]] = "X"
            check_win((board, rotate_board(board)), turn_num)

def computer_turn(turn_num):
    '''it's too bad this isn't reusing the player_turn function'''
    row, column = random.choice(["top", "middle", "bottom"]), random.choice(["left", "middle", "right"])
    if check_move(row, column):
        computer_turn(turn_num)
    else:
        board[rows[row]][columns[column]] = "O"
        check_win((board, rotate_board(board)), turn_num)
        print_board(board)

def check_move(x_axis, y_axis):
    '''see if move is already taken'''
    if board[rows[x_axis]][columns[y_axis]] != "_":
        return True

def check_winner(item):
    '''see if winner is X or O'''
    if item == "X":
        print("Player wins")
        quit()
    elif item == "O":
        print("computer wins")
        quit()
    else:
        pass

def check_rows(board_name):
    '''check for 3 in a row across a list- I'm sure there is a better way'''
    for x in board_name:
        if x[0] == x[1] and x[0] == x[2]:
            check_winner(x[0])
        else:
            pass

def check_win(board_names, turn_num):
    '''so many functions for checking if someone has won! this one combines the subfunctions'''
    for i in board_names:
        check_rows(i)
        check_diagonal(i)
    if turn_num >= 9:
            print("stalemate")
            quit()

def main():
    turn = 0
    print_board(board)
    while True:
        turn += 1
        player_turn(turn)
        turn += 1
        computer_turn(turn)

main()
