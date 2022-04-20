import random

PLAYER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
COMPUTER_BOARD = [["~"] * BOARD_SIZE for i in range(BOARD_SIZE)]
BOARD_SIZE = 6
NUMBER_OF_SHIPS = 3


class UserBoard:
    """
    Will allow boards to be printed using the
    print_current_board method
    """
    def __init__(self, board):
        self.board = board

    def print_current_board(self):
        print("   0 1 2 3 4 5")
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
        for x in range(NUMBER_OF_SHIPS):
            self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE), random.randint(0, BOARD_SIZE)
            while True:
                if (self.board[self.x_coord][self.y_coord] == 'O'):
                    self.x_coord, self.y_coord = random.randint(0, BOARD_SIZE), random.randint(0, BOARD_SIZE)
                    return True
                else:
                    self.board[self.x_coord][self.y_coord] = 'O'
                    return False


    def place_ships(self):
        pass


def rungame():
    """
    This function will take the player through
    the introduction and explain the rules.
    """
    print("---------------------------------------------------------")
    print("Welcome to Python Battleships")
    print("Beat the computer by finding it's ships before it sinks yours!")
    print("There are 3 ships in total, you will guess first!")
    print("---------------------------------------------------------\n")
    UserBoard(PLAYER_BOARD).print_current_board()


if __name__ == '__main__':
    rungame()