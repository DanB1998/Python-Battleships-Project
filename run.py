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


def plant_ships():
    global ship1_pos
    ship1_pos = [(rand_row(board), rand_col(board)]
    print(ship1_pos)


# Game Logic
def run_game():
    """
    Function that will run the game
    """
    print_game_board(board)
    guess()


# User guess
def guess():
    """
    Takes a guess from a user 
    and passes it to the validator
    """
    print("Please guess a row and a column")

    global user_guess

    user_guess = input("Guess coordinates here: ")

    if validate_user_input(user_guess):
        print(f"You guessed {user_guess}")
        check_for_hit()


# Input validation
def validate_user_input(coordinates):
    """
    A function that will validate the user's
    input as 2 numbers representing a coordinate
    """
    try:
        [int(coord) for coord in coordinates]
        if len(coordinates) != 2:
            raise ValueError(
                f"Only 2 values needed, you gave {len(coordinates)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    return coordinates


def check_for_hit():
    
    if (ship1_pos == user_guess):
        print("You hit my battleship")
    else:
        print("You missed my battleship")
    

# Main functions
def main():
    print("Welcome to Python Battleships")
    make_game_board(board)
    plant_ships()
    run_game()


# Calling main function
main()
