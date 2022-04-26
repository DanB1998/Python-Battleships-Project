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


def plant_ships(self, num_ships, board_size):
    """
    Plants ships randomly for the computer's board
    """
    time.sleep(1)
    print("\nThe computer has planted it's ships")
    for x in range(num_ships):
        self.x_coord, self.y_coord = random.randint(0, board_size-1), random.randint(0, board_size-1)
        while self.board[self.x_coord][self.y_coord] == 'O':
            self.x_coord, self.y_coord = random.randint(0, board_size-1), random.randint(0, board_size-1)
        self.board[self.x_coord][self.y_coord] = 'O'
    return self.board

def user_plant_ships(self, num_ships):
    """
    Lets the user select where their ships will go.
    """
    print("""
\nSo, Where would you like to plant your ships?
\nShips are only 1x1, so only 1 set of coordinates is needed for each
""")
    for x in range(num_ships):
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
    


if __name__ == '__main__':
    setup_terminal()
    setup_game()
