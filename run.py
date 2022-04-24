import random

BOARD_SIZE = 5
PLAYER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
COMPUTER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
NUMBER_OF_SHIPS = 3


class UserBoard:
    """
    Will allow boards to be printed using the
    print_current_board method
    """
    def __init__(self, board):
        self.board = board

    def print_current_board(self):
        """
        Prints the current board passed to it
        """
        print("   0 1 2 3 4")
        row_no = 0
        for row in self.board:
            print(row_no, "|" + "|".join(row) + "|")
            row_no += 1


class Battleships:
    """
    The battleships class will look after the ships and handle user guess
    """
    def __init__(self, board):
        self.board = board

    def plant_ships(self):
        """
        Plants ships for a given board
        """
        for x in range(NUMBER_OF_SHIPS):
            self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
            while self.board[self.x_coord][self.y_coord] == 'O':
                self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
            self.board[self.x_coord][self.y_coord] = 'O'
        return self.board

    def user_guess(self):
        """
        Will initiate the user guess
        """
        while True:
            try:
                guess_row = int(input("\nGuess row: "))
                guess_col = int(input("Guess column: "))
            except ValueError:
                print("Please enter a number")
                continue
            else:
                break

        if (validate_input(guess_row) and validate_input(guess_col)):
            print(f"You guessed {[guess_row, guess_col]} \n")
        else:
            Battleships(self).user_guess()

        return guess_row, guess_col


class ComputerHandler:
    """
    A class that will handle the computer and non-player related processes
    """
    def __init__(self, board):
        self.board = board


def validate_input(coordinates):
    """
    A function that will validate the user's
    input numbers representing a coordinate.
    """
    try:
        if coordinates > BOARD_SIZE-1:
            raise ValueError(
                f"You missed the Ocean, the max size is {BOARD_SIZE-1}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    return True


def rungame():
    """
    This function will take the player through
    the introduction and explain the rules.
    """
    computer_display_board = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    computer_hidden_board = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    player_board = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    # Game Welcome
    print("---------------------------------------------------------")
    print("Welcome to Python Battleships")
    print("Beat the computer by finding it's ships before it sinks yours!")
    print("There are 3 ships in total, you will guess first!")
    print("---------------------------------------------------------\n")
    # Prints User Board
    UserBoard(player_board).print_current_board()
    # Plant ships on the computers hidden board
    Battleships(computer_hidden_board).plant_ships()
    # Prints the computer board to see where the ships have been placed
    UserBoard(computer_hidden_board).print_current_board()
    # Sets the guess locally so it can be checked by the run game function
    hits = 0
    while hits < 3:
        user_guess_row, user_guess_col = Battleships(computer_hidden_board).user_guess()
        # Check if the users guess is where a ship is positioned
        if computer_hidden_board[user_guess_col][user_guess_row] == "O":
            hits += 1
            print("You hit a battleship!")
            computer_display_board[user_guess_col][user_guess_row] = "#"
        else:
            print("You missed a battleship")
            computer_display_board[user_guess_col][user_guess_row] = "X"
        # Prints computer board to user after updating the users guess
        UserBoard(computer_display_board).print_current_board()
    
    print('end')


if __name__ == '__main__':
    rungame()