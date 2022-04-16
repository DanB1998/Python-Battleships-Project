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


# Function to get a random column for a ship
def rand_row(board):
    return randint(0, board_length-1)


# Function to get a random column for a ship
def rand_col(board):
    return randint(0, board_length-1)


# Plants the ships
def plant_ships():
    global ship1_pos
    ship1_pos = [rand_row(board), rand_col(board)]
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

    global user_entry_row
    global user_entry_col

    user_entry_row = input("Guess row: ")
    user_entry_col = input("Guess column: ")

    if (validate_input(user_entry_row) and validate_input(user_entry_col)):
        print(f"You guessed {[user_entry_row, user_entry_col]}")
        check_for_hit()
    else:
        guess()


# Input validation
def validate_input(coordinates):
    """
    A function that will validate the user's
    input numbers representing a coordinate
    """
    try:
        if(int(coordinates) > board_length-1):
            raise ValueError(
                f"You missed the Ocean, the max size is {board_length}"
            )
        elif len(coordinates) != 1:
            raise ValueError(
                f"Only 2 values needed, you gave {len(coordinates)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


# Checks for hits when data is validated
def check_for_hit():
    if (ship1_pos[1] == int(user_entry_col) and ship1_pos[0] == int(user_entry_row)):
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
