#it has been years since I have written in Python.
#This is a tic-tac-toe game to practice

import random

board = [['_','_','_'],['_','_','_'],['_','_','_']]
rows = {"top" : 0, "middle" : 1, "bottom" : 2}
columns = {"left" : 0, "middle" : 1, "right" : 2}
over = False

def print_board(board):
    print(board[0])
    print(board[1])
    print(board[2])

def player_turn(turn_num):
    row = input("choose a row (top, middle, or bottom)")
    column = input("choose a column (left, middle, or right")
    if row not in rows or column not in columns:
        print("I didn't understand. Choose again")
        player_turn(turn)
    else:
        if check_move(row, column):
            print("that spot is taken")
            player_turn(turn_num)
        else:
            board[rows[row]][columns[column]] = "X"
            check_win(board, turn_num)

def computer_turn(turn_num):
    row = random.choice(["top", "middle", "bottom"])
    column = random.choice(["left", "middle", "right"])
    if check_move(row, column):
        computer_turn(turn_num)
    else:
        board[rows[row]][columns[column]] = "O"
        check_win(board, turn_num)
        print_board(board)

def check_move(a,b):
    if board[rows[a]][columns[b]] != "_":
        return True

def check_win(a, b):
    for x in a:
        if x[0] == x[1] and x[0] == x[2]:
            if x[0] == "X":
                print("Player wins")
                quit()
            elif x[0] == "O":
                print("computer wins")
                quit()
            else:
                pass
        else:
            pass
    
    for x in range(3):
        if board[0][x] == board [1][x] and board[0][x] == board[2][x]:
            if board[0][x] == "X":
                print("player wins")
                quit()
            elif board[0][x] == "O":
                print("computer wins")
                quit()
            else:
                pass
            
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == "X":
            print("player wins")
            quit()
        elif board[0][0] == "O":
            print("computer wins")
            quit()
        else:
            pass
        
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        if board[2][0] == "X":
            print("player wins")
            quit()
        elif board[2][0] == "O":
            print("computer wins")
            quit()
        else:
            pass
        
    if b >= 9:
            print("stalemate")
            quit()
        
def main():
    turn = 0
    print_board(board)
    while over == False:
        turn += 1
        player_turn(turn)
        turn += 1
        computer_turn(turn)
        
main()

        
