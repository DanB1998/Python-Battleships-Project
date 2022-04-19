from random import randint

player_board = []
computer_board = []
board_length = 4
number_of_ships = 3
player_hits = 0
computer_hits = 0


def make_game_board(board):
    """
    Making the game board
    """
    for i in range(board_length):
        board.append('O ' * board_length)


def print_game_board(board):
    """
    Showing the game board
    """
    for row in board:
        print("".join(row))


def plant_ships_player():
    """
    Plants the ships for the computers board
    """
    global ps1_pos, ps2_pos, ps3_pos, player_positions
    ps1_pos = [randint(0, board_length-1), randint(0, board_length-1)]
    ps2_pos = [randint(0, board_length-1), randint(0, board_length-1)]
    ps3_pos = [randint(0, board_length-1), randint(0, board_length-1)]

    while True:
        if ps1_pos == ps2_pos:
            ps1_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        elif ps2_pos == ps3_pos:
            ps2_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        elif ps1_pos == ps3_pos:
            ps3_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        else:
            break

    player_positions = [ps1_pos, ps2_pos, ps3_pos]
    print(player_positions)


def plant_ships_computer():
    """
    Plants the ships for the computers board
    """
    cs1_pos = [randint(0, board_length-1), randint(0, board_length-1)]
    cs2_pos = [randint(0, board_length-1), randint(0, board_length-1)]
    cs3_pos = [randint(0, board_length-1), randint(0, board_length-1)]

    global computer_positions

    while True:
        if cs1_pos == cs2_pos:
            cs1_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        elif cs2_pos == cs3_pos:
            cs2_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        elif cs1_pos == cs3_pos:
            cs3_pos = [randint(0, board_length-1), randint(0, board_length-1)]
        else:
            break

    computer_positions = [cs1_pos, cs2_pos, cs3_pos]


def run_game():
    """
    Function that will run the game
    """
    make_game_board(player_board)
    make_game_board(computer_board)
    plant_ships_player()
    plant_ships_computer()
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
                f"You missed the Ocean, the max size is {board_length-1}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def computer_turn():
    """
    Computer guess
    """
    global computer_guess
    computer_guess = [randint(0, board_length-1), randint(0, board_length-1)]
    print(f"Computer guessed {computer_guess}")
    check_for_hit_computer()


def check_for_hit():
    """
    Checks for hits when data is validated
    """
    global hits
    if [user_entry_row, user_entry_col] in player_positions:
        print("You hit a battleship \n")
        update_board_hit(player_board, user_entry_row, user_entry_col)
    else:
        print("You missed my battleship \n")
        update_board_miss(player_board, user_entry_row, user_entry_col)

    computer_turn()


def check_for_hit_computer():
    """
    checks for a hit from the computer
    """
    if computer_guess in computer_positions:
        print("Computer hit a battleship \n")
        update_board_hit(computer_board, computer_guess[0], computer_guess[1])
    else:
        print("Computer missed a battleship \n")
        update_board_miss(computer_board, computer_guess[0], computer_guess[1])

    round_end()


def update_board_hit(board, entry_row, entry_col):
    """
    Will update the board with a hit
    """
    update_hit = board[entry_col].split()
    update_hit[entry_row] = "#"
    updated_row = " ".join(update_hit)
    board[entry_col] = updated_row


def update_board_miss(board, entry_row, entry_col):
    """
    Will update the board with a hit
    """
    update_miss = board[entry_col].split()
    update_miss[entry_row] = "X"
    updated_row = " ".join(update_miss)
    board[entry_col] = updated_row


def round_end():
    """
    End the round by showing the state of the game
    """
    print("------------------------------------------------")
    print("At the end of the round your board:\n")
    print_game_board(player_board)
    print("Computer's board:\n")
    print_game_board(computer_board)
    print("------------------------------------------------")
    check_win()


def check_win():
    """
    Checks for a win to end the game
    """
    if player_hits == number_of_ships:
        print("\nYou Win")
    elif computer_hits == number_of_ships:
        print("\nYou lose")
    else:
        guess()


def main():
    """
    Main functions
    """
    print("---------------------------------------------------------")
    print("Welcome to Python Battleships")
    print("Beat the computer by finding it's ships before it sinks yours!")
    print("There are 3 ships in total, you will guess first!")
    print("---------------------------------------------------------")
    run_game()


# Calling main function
main()
