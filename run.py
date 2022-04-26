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
                guess_col = int(input("\nGuess column: "))
                if guess_col < 0 or guess_col > BOARD_SIZE-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                guess_row = int(input("\nGuess row: "))
                if guess_row < 0 or guess_row > BOARD_SIZE-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        return guess_col, guess_row


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
    player_hits = 0
    computer_hits = 0
    while player_hits < 3 and computer_hits < 3:
        user_guess_col, user_guess_row = Battleships(computer_hidden_board).user_guess()
        while computer_display_board[user_guess_row][user_guess_col] == "X":
            print("You have already guessed this area")
            user_guess_col, user_guess_row = Battleships(computer_hidden_board).user_guess()
        # Check if the users guess is where a ship is positioned
        if computer_hidden_board[user_guess_row][user_guess_col] == "O":
            player_hits += 1
            print("You hit a battleship!")
            computer_display_board[user_guess_row][user_guess_col] = "#"
        else:
            print("You missed a battleship")
            computer_display_board[user_guess_row][user_guess_col] = "X"
        
        comp_guess_col, comp_guess_row = ComputerHandler(player_board).generate_guess()
        while player_board[comp_guess_row][comp_guess_col] == "X":
            comp_guess_col, comp_guess_row = ComputerHandler(player_board).generate_guess()
        # Check computer guess against player board
        if player_board[comp_guess_row][comp_guess_col] == "O":
            computer_hits += 1
            print("Computer hit a battleship!")
            player_board[comp_guess_row][comp_guess_col] = "#"
        else:
            print("Computer missed a battleship")
            player_board[comp_guess_row][comp_guess_col] = "X"
        # Prints computer board to user after updating the users guess
        UserBoard(computer_display_board).print_current_board()
        UserBoard(player_board).print_current_board()

    print('end')


if __name__ == '__main__':
    # setup()
    rungame()