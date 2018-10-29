"""Tictactoe module"""


def cl_screen():
    """Clear screen function"""
    # Clear the screen before squares drawing
    print('\n'*100)


def display_board(board):

    """Print board on a command line"""
    # Print the game board on command line with filled boxes
    cl_screen()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


def replay():
    """Replay function
    """
    # Asking for replay if you want to play again
    choice = input(' Do You want to play again ? Press Y to continue, '
                   'any other key to quit. ').upper()
    return choice == 'Y'

# The main play cycle here

while True:
    # Define an list for the board and fill it in with spaces
    THE_BOARD = [' '] * 10
    display_board(THE_BOARD)
    if not replay():
        cl_screen()
        break
