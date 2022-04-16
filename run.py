from random import randint

player_board = []
computer_board = []
board_length = 6
number_of_ships = 1
hits = 0
turns = 0


def make_game_board(board):
    """
    Making the game board
    """
    for x in range(board_length):
        board.append('O ' * board_length)


def print_game_board(board):
    """
    Showing the game board
    """
    for row in board:
        print("".join(row))


def plant_ships_computer():
    """
    Plants the ships
    """
    global comp_ship1_pos
    comp_ship1_pos = [randint(0, board_length), randint(0, board_length)]


def run_game():
    """
    Function that will run the game
    """
    make_game_board(player_board)
    make_game_board(computer_board)
    plant_ships(player_board)
    plant_ships(computer_board)
    print_game_board(player_board)
    guess()


def guess():
    """
    Takes a guess from a user
    and passes it to the validator
    """
    print("Please guess a row and a column: \n")

    global user_entry_row, user_entry_col

    while True:
        try:
            user_entry_row = int(input("Guess row: "))
            user_entry_col = int(input("Guess column: "))
        except ValueError:
            print("Please enter a number")
            continue
        else:
            break

    if (validate_input(user_entry_row) and validate_input(user_entry_col)):
        print(f"You guessed {[user_entry_row, user_entry_col]} \n")
        check_for_hit()
    else:
        guess()


def validate_input(coordinates):
    """
    A function that will validate the user's
    input numbers representing a coordinate
    """
    try:
        if coordinates > board_length-1:
            raise ValueError(
                f"You missed the Ocean, the max size is {board_length}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
        
    return True


def check_for_hit():
    """
    Checks for hits when data is validated
    """
    global hits
    if (ship1_pos[1] == user_entry_col and ship1_pos[0] == user_entry_row):
        hits += 1
        print("You hit a battleship \n")
        update_board_hit(player_board)
        print_game_board(player_board)
        check_win()
    else:
        print("You missed my battleship \n")
        print_game_board(player_board)
        guess()


def update_board_hit(board):
    """
    Will update the board with a hit
    """
    update_hit = board[user_entry_col].split()
    update_hit[user_entry_row] = "#"
    updated_row = " ".join(update_hit)
    board[user_entry_col] = updated_row


def update_board_miss(board):
    """
    Will update the board with a hit
    """
    update_miss = board[user_entry_col].split()
    update_miss[user_entry_row] = "X"
    updated_row = " ".join(update_miss)
    board[user_entry_col] = updated_row


def check_win():
    """
    Checks for a win to end the game
    """
    if hits == number_of_ships:
        print("\nYou Win")
    else:
        guess()


def main():
    """
    Main functions
    """
    print("Welcome to Python Battleships")
    run_game()


# Calling main function
main()
