"""Tictactoe module"""
import random

# Clear the screen before squares drawing
def cl_screen():
    """Clear screen function"""
    print('\n'*100)


# Print the game board on command line with filled boxes
def display_board(board):

    """Print board on a command line"""
    cl_screen()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


# Asking for replay if you want to play again
def replay():
    """Replay function
    """
    choice = input(' Do You want to play again ? Press Y to continue, '
                   'any other key to quit. ').upper()
    return choice == 'Y'


# Asking for the sign choice
def player_input():
    '''Input a sign will be used by player'''
    cl_screen()
    marker = ''
    while marker not in ['X', '0']:
        marker = input('Player 1, please, select your mark from X,0 :').upper()
    # The first player will use X , the second - 0
    # and vice versa
    if marker == 'X':
        t_result = ('X', '0')
    else:
        t_result = ('0', 'X')
    return t_result


# Put the marker in the position, defined on the board
def place_marker(board, marker, position):
    """Put a marker in a position"""
    board[position] = marker


# Check the board for the possible win
def win_check(board, mark):
    """Check for the win0"""
    return ((board[7] == mark and board[8] == mark and board[9] == mark)or
            (board[4] == mark and board[5] == mark and board[6] == mark)or
            (board[1] == mark and board[2] == mark and board[3] == mark)or
            (board[1] == mark and board[4] == mark and board[7] == mark)or
            (board[2] == mark and board[5] == mark and board[8] == mark)or
            (board[3] == mark and board[6] == mark and board[9] == mark)or
            (board[1] == mark and board[5] == mark and board[9] == mark)or
            (board[3] == mark and board[5] == mark and board[7] == mark))


# Making a choice who will have the first turn
def choose_first():
    """Who will turn first"""
    flip = random.randint(0, 1)
    if flip == 0:
        s_result = 'Player 1'
    else:
        s_result = 'Player 2'
    return s_result


# Check if the position empty .
def space_check(board, position):
    """True if empty, False if a marker is here"""
    return board[position] == ' '


# Check if the board is full
def full_board_check(board):
    """True if Full, False if not"""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Choose the position for the marker
def player_choice(board):
    """The position to put the  marker"""
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose a position 1-9 :'))
        return position





# The main play cycle here

while True:
    # INITIAL SETTINGS
    #
    # Define an list for the board and fill it in with spaces
    THE_BOARD = [' '] * 10
    # Define the marker (or the sign) will be used by each player
    PLAYER1_MARKER, PLAYER2_MARKER = player_input()

    display_board(THE_BOARD)
    if not replay():
        cl_screen()
        break
