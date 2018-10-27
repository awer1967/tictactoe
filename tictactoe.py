"""Tictactoe module"""

def cl_screen() :
    """Clear screen function"""
    # Clear the screen before squares drawing
    print('\n'*100)

def replay() :
    """Replay function
    """
    # Asking for replay if you want to play again
    choice = input(' Do You want to play again ? Press Y to continue, any other key to quit. ').upper()
    return choice=='Y'

#The main play cycle here

while True:
    cl_screen()
    if not replay():
        break