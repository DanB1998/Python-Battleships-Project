import random

PLAYER_BOARD = [["~"] * 6 for i in range(6)]
COMPUTER_BOARD = [["~"] * 6 for i in range(6)]


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