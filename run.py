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
        self.guesses = []
        self.ships = []


    def print_board(self):
        """
        Prints the current board passed to it
        """
        print("\n   0 1 2 3 4")
        row_no = 0
        for row in self.board:
            print(row_no, "|" + "|".join(row) + "|")
            row_no += 1

    def store_guesses(self, col, row):
        """
        This method will store the guesses made by the board owner
        """
        self.guesses.append((col, row))

    
    def plant_ships(self, num_ships, board_size):
    """
    Plants ships randomly for the computer's board
    """
    time.sleep(1)
    print("\nThe computer has planted it's ships")
    for x in range(num_ships):
        self.x_coord, self.y_coord = random.randint(0, board_size-1), random.randint(0, board_size-1)
        while (self.x_coord, self.y_coord) in self.guesses:
            self.x_coord, self.y_coord = random.randint(0, board_size-1), random.randint(0, board_size-1)
        self.x_coord, self.y_coord.append(guesses)
    return self.board


def setup_game():
    """
    Sets up the game to play
    """
    board_size = 5
    num_ships = 3
    name = "Susan"

    player_board = UserBoard(board_size, num_ships, "Computer", type="player")
    computer_board = UserBoard(board_size, num_ships, name, type="computer")

    plant_ships(computer_board, num_ships, board_size)
    plant_ships(player_board, num_ships, board_size)
    
    start_game(player_board, computer_board)


def start_game(player_board, computer_board):
    pass


if __name__ == '__main__':
    setup_terminal()
    setup_game()
