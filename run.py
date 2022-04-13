board = []
board_length = 6

# Creating a game board
def make_game_board():
    for x in range(board_length):
        board.append(' O ' * board_length)

# Showing the game board
def print_game_board(board):
    for x in board:
        print(x)

# Function to get a random location for a ship
def rand_row(board):
    return randint(1, board_length)

def rand_col(board):
    return randint(1, board_length)



# Functions for use later
print('Welcome to Python battleships')

make_game_board()
print_game_board(board)