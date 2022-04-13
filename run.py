from random import randint

board = []
board_length = 6
number_of_ships = 3
hits = 0
turns = 0



# Making the game board
def make_game_board(board):
    for x in range(board_length):
        board.append(' O ' * board_length)

# Showing the game board
def print_game_board(board):
    for x in board:
        print(x)

# Function to get a random location for a ship
def rand_row(board):
    return randint(0, board_length-1)

def rand_col(board):
    return randint(0, board_length-1)

ship1_pos = [rand_row(board), rand_col(board)]

# Game Logic

def run_game():
    """
    Function that will run the game
    """

def validate_user_input():
    """
    A function that will validate the users input
    """

# Testing area

print("Welcome to Python Battleships")
make_game_board(board)

