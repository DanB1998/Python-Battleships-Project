from random import randint

board = []
board_length = 6
number_of_ships = 3
hits = 0
turns = 0

# Creating a game board
def make_game_board():
    for x in range(board_length):
        board.append(' O ' * board_length)

# Showing the game board
def print_game_board(board):
    print(board)

# Function to get a random location for a ship
def rand_row(board):
    return randint(0, board_length-1)

def rand_col(board):
    return randint(0, board_length-1)

ship1_pos = [rand_row(board), rand_col(board)]

#Logic ideas
while hits < number_of_ships:
    row = 0
    col = 0
    print('Welcome to Python battleships, here is your board')
    print_game_board(board)
    print('Please choose a coordinate to attack!')
    row = int(input('Choose a row: '))
    col = int(input('Choose a column: '))

# Functions for use later
def main():
    make_game_board()

main()