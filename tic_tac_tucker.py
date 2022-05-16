#a tic-tac-toe game that we can pair program with!

board = [['_','_','_'],['_','_','_'],['_','_','_']]
rows = {'top' : 0, 'middle' : 1, 'bottom' : 2}
columns = {'left' : 0, 'middle' : 1, 'right' : 2}

def print_board(board_name):
    '''display boardstate to player'''
    print('')
    for i in range(3):
        print(' '.join(board_name[i]))
    print('')

def get_position(player, choice, axis, options):
    '''asks user to make a move'''
    position = input(f'Player {player}, choose a {choice}: ({options}) ').lower()
    if position in axis:
        return position
    else:
        print('\n* * * I didn\'t understand. Choose again * * * \n')
        position = get_position(player, choice, axis, options)
        return position

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
        end_game(board_name[0][0])
    else:
        pass

def end_game(mark):
    '''announce the winner'''
    print(f'\nPlayer {mark} wins')
    quit()

def main():
    '''this is the game'''
    turn = 0
    print("\nWelcome to Tic-Tac-Toe\nX goes first")
    print_board(board)
    while True:
        turn += 1
        player_turn(turn)

main()
