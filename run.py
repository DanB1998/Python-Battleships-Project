import random
from setup import setup_terminal
import time


class UserBoard:
    """
    Will allow boards to be printed using the
    print_current_board method
    """
    def __init__(self, board_size, num_ships, name):
        self.board = [["~"] * board_size for i in range(board_size)]
        self.board_size = board_size
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships = []

    def store_ships(self, col, row):
        """
        This method will store the guesses made by the board owner
        """
        self.ships.append((col, row))
        if self.name != "Computer":
            self.board[col][row] = "O"

    def print_board(self):
        """
        Prints the current board passed to it
        """
        print(f"\n{self.name}'s Board ")
        print("   0 1 2 3 4")
        row_no = 0
        for row in self.board:
            print(row_no, "|" + "|".join(row) + "|")
            row_no += 1

    def guess(self, col, row):
        """
        Will compare the guess to the self's board
        """
        self.guesses.append((col, row))
        self.board[col][row] = "X"

        if (col, row) in self.ships:
            self.board[col][row] = "#"
            return "Hit"
        else:
            return "Miss"

    def user_guess(self):
        """
        Will initiate the user guess
        """
        while True:
            try:
                user_col = int(input("\nSelect column: "))
                if user_col < 0 or user_col > self.board_size-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                user_row = int(input("Select row: "))
                if user_row < 0 or user_row > self.board_size-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")
        return user_col, user_row

    def plant_ships(self):
        """
        Plants randomly for the computer's board
        """
        col, row = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
        while (col, row) in self.ships:
            col, row = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
        self.store_ships(col, row)

    def computer_guess(self):
        """
        randomises a guess to use as the computers guess
        """
        

def setup_game():
    """
    Sets up the game to play
    """
    global num_ships

    board_size = 5
    num_ships = 3
    name = "Susan"

    player_board = UserBoard(board_size, num_ships, name)
    computer_board = UserBoard(board_size, num_ships, "Computer")

    for i in range(num_ships):
        computer_board.plant_ships()
        player_board.plant_ships()

    start_game(player_board, computer_board)


def start_game(player_board, computer_board):
    """
    Starts the game
    """
    print("Here are the boards, good luck")
    player_board.print_board()
    computer_board.print_board()
    print("\nIts time to play, you're guessing first. Choose a coordinate\n")
    player_hits = 0
    comp_hits = 0
    print(player_board.ships)
    print(computer_board.ships)
    while player_hits < num_ships and comp_hits < num_ships:
        col, row = computer_board.user_guess()
        check = computer_board.guess(col, row)
        if check == "Hit":
            player_hits += 1
            print("You sunk a battleship")
        else:
            print("You missed a battleship")


if __name__ == '__main__':
    # setup_terminal()
    setup_game()
