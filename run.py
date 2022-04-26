import random
from setup import setup
import time

BOARD_SIZE = 5
COMPUTER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
COMPUTER_HIDDEN_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
PLAYER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
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
        print(board)
        print("\n   0 1 2 3 4")
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

    def user_input(self):
        """
        Will initiate the user guess
        """
        while True:
            try:
                user_col = int(input("\nSelect column: "))
                if user_col < 0 or user_col > BOARD_SIZE-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                user_row = int(input("Select row: "))
                if user_row < 0 or user_row > BOARD_SIZE-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        return user_col, user_row

    def user_plant_ships(self):
        """
        Lets the user select where their ships will go.
        """
        print("""
\nSo, Where would you like to plant your ships?
\nShips are only 1x1, so only 1 set of coordinates is needed for each
""")
        for x in range(NUMBER_OF_SHIPS):
            time.sleep(2.5)
            print(f"\nShip {x+1} location?")
            ship_col, ship_row = Battleships(PLAYER_BOARD).user_input()
            while PLAYER_BOARD[ship_row][ship_col] == "O":
                time.sleep(1)
                print("\nYou have already chosen this area, try again")
                ship_col, ship_row = Battleships(PLAYER_BOARD).user_input()
            PLAYER_BOARD[ship_row][ship_col] = "O"
            print(f"""
You planted a ship on {ship_col}, {ship_row}
\nHere is a look at your board
""")        
            time.sleep(2)
            UserBoard(PLAYER_BOARD).print_current_board()


class ComputerHandler:
    """
    A class that will handle the computer and non-player related processes
    """
    def __init__(self, board):
        self.board = board

    def generate_guess(self):
        """
        Generates coordinates to use as computer guess
        """
        gen_col = random.randint(0, BOARD_SIZE-1)
        gen_row = random.randint(0, BOARD_SIZE-1)

        return gen_col, gen_row

    def plant_ships(self):
        """
        Plants ships randomly for the computer's board
        """
        time.sleep(1)
        print("\nThe computer has planted it's ships")
        for x in range(NUMBER_OF_SHIPS):
            self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
            while self.board[self.x_coord][self.y_coord] == 'O':
                self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE-1), random.randint(0, BOARD_SIZE-1)
            self.board[self.x_coord][self.y_coord] = 'O'
        return self.board


def rungame():
    time.sleep(3)

    # Plant ships on the computers hidden board
    ComputerHandler(COMPUTER_HIDDEN_BOARD).plant_ships()
    time.sleep(2)
    print("\nIts time to play, you're guessing first. Choose a coordinate")
    time.sleep(2)
    # Sets the guess locally so it can be checked by the run game function
    player_hits = 0
    computer_hits = 0
    while player_hits < 3 and computer_hits < 3:
        time.sleep(2)
        user_col, user_row = Battleships(COMPUTER_HIDDEN_BOARD).user_input()
        while COMPUTER_BOARD[user_row][user_col] == "X":
            print("You have already guessed this area")
            user_col, user_row = Battleships(COMPUTER_HIDDEN_BOARD).user_input()
        # Check if the users guess is where a ship is positioned
        if COMPUTER_HIDDEN_BOARD[user_row][user_col] == "O":
            player_hits += 1
            print("You hit a battleship!")
            COMPUTER_BOARD[user_row][user_col] = "#"
        else:
            print("You missed a battleship")
            COMPUTER_BOARD[user_row][user_col] = "X"
        
        comp_guess_col, comp_guess_row = ComputerHandler(PLAYER_BOARD).generate_guess()
        while PLAYER_BOARD[comp_guess_row][comp_guess_col] == "X":
            comp_guess_col, comp_guess_row = ComputerHandler(PLAYER_BOARD).generate_guess()
        # Check computer guess against player board
        if PLAYER_BOARD[comp_guess_row][comp_guess_col] == "O":
            computer_hits += 1
            print("Computer hit a battleship!")
            PLAYER_BOARD[comp_guess_row][comp_guess_col] = "#"
        else:
            print("Computer missed a battleship")
            PLAYER_BOARD[comp_guess_row][comp_guess_col] = "X"
        # Prints computer board to user after updating the users guess
        UserBoard(COMPUTER_BOARD).print_current_board()
        UserBoard(PLAYER_BOARD).print_current_board()

    print('end')


if __name__ == '__main__':
    setup()
    rungame()