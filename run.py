import random
from setup import setup_terminal
import time


class UserBoard:
    """
    Will allow boards to be printed using the
    print_current_board method
    """
    def __init__(self, board_size, num_ships, name, type):
        self.board = [["~"] * board_size for i in range(board_size)]
        self.board_size = board_size
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def store_ships(self, col, row):
        """
        This method will store the guesses made by the board owner
        """
        self.ships.append((col, row))

    def print_board(self, name):
        """
        Prints the current board passed to it
        """
        print(f" {name}'s Board ")
        print("\n   0 1 2 3 4")
        row_no = 0
        for row in self.board:
            print(row_no, "|" + "|".join(row) + "|")
            row_no += 1


def plant_ships(self, board_size):
    """
    Plants randomly for the computer's board
    """
    col, row = random.randint(0, board_size-1), random.randint(0, board_size-1)
    while (col, row) in self.guesses:
        col, row = random.randint(0, board_size-1), random.randint(0, board_size-1)
    self.store_ships(row, col)


def setup_game():
    """
    Sets up the game to play
    """
    board_size = 5
    num_ships = 3
    name = "Susan"

    player_board = UserBoard(board_size, num_ships, "Computer", type="player")
    computer_board = UserBoard(board_size, num_ships, name, type="computer")

    for i in range(num_ships):
        plant_ships(computer_board, board_size)
        plant_ships(player_board, board_size)

    start_game(player_board, computer_board)

    print(player_board.ships)
    print(computer_board.ships)


def start_game(player_board, computer_board):
    pass


if __name__ == '__main__':
    setup_terminal()
    setup_game()
