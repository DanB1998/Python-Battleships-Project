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
    The battleships class will look after the ships
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
                guess_row = int(input("Guess row: "))
                guess_col = int(input("Guess column: "))

            except ValueError:
                print("Please enter a number")

        if (validate_input(guess_row) and validate_input(guess_col)):
            print(f"You guessed {[guess_row, guess_col]} \n")
        else:
            Battleships(self).user_guess()


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
        return False

    return True


def rungame():
    """
    This function will take the player through
    the introduction and explain the rules.
    """
    computer_hidden_board = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    player_board = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
    print("---------------------------------------------------------")
    print("Welcome to Python Battleships")
    print("Beat the computer by finding it's ships before it sinks yours!")
    print("There are 3 ships in total, you will guess first!")
    print("---------------------------------------------------------\n")
    UserBoard(player_board).print_current_board()
    Battleships(computer_hidden_board).plant_ships()
    Battleships(computer_hidden_board).user_guess()


if __name__ == '__main__':
    rungame()