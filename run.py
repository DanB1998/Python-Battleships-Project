import random


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
            self.board[row][col] = "O"

    def store_guesses(self, col, row):
        """
        This method will store the guesses made by the board owner
        """
        self.guesses.append((col, row))

    def print_board(self):
        """
        Prints the current board passed to it
        """
        print(f"\n{self.name}'s Board ")
        if board_size == 4:
            print("   0 1 2 3")
        elif board_size == 5:
            print("   0 1 2 3 4")
        else:
            print("   0 1 2 3 4 5")
        row_no = 0
        for row in self.board:
            print(row_no, "|" + "|".join(row) + "|")
            row_no += 1

    def guess(self, col, row):
        """
        Will compare the guess to the self's board
        """
        self.guesses.append((col, row))
        self.board[row][col] = "X"

        if (col, row) in self.ships:
            self.board[row][col] = "#"
            return "Hit"
        else:
            return "Miss"

    def user_guess(self):
        """
        Will initiate the user guess and validate it
        """
        while True:
            try:
                user_col = int(input("\nGuess a column: "))
                if user_col < 0 or user_col > self.board_size-1:
                    print("Number is outside of range")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        while True:
            try:
                user_row = int(input("Guess a row: "))
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
        col = random.randint(0, self.board_size-1)
        row = random.randint(0, self.board_size-1)
        while (col, row) in self.ships:
            col = random.randint(0, self.board_size-1)
            row = random.randint(0, self.board_size-1)
        self.store_ships(col, row)

    def computer_guess(self):
        """
        randomises a guess to use as the computers guess
        """
        comp_col = random.randint(0, self.board_size-1)
        comp_row = random.randint(0, self.board_size-1)

        return comp_col, comp_row


def name_validation(value):
    """
    Will validate the setup inputs
    """
    if len(value) > 8 or len(value) < 4:
        return True
    else:
        return False


def board_validation(value):
    """
    Will validate the setup inputs
    """
    if value == 4:
        return False
    elif value == 5:
        return False
    elif value == 6:
        return False
    else:
        return True


def ship_validation(value):
    """
    Validates ship input
    """
    if value == 2:
        return False
    elif value == 3:
        return False
    elif value == 4:
        return False
    else:
        return True


def player_win():
    """
    Code runs when the player wins
    """
    print("Oh wait... you've sank all of their ships!")
    print("Congratulations, You won against the computer")
    play_again()


def computer_win():
    """
    Code runs when the computer wins
    """
    print("Oh wait... your ships are gone")
    print("Unfortunately, You lost against the computer")
    play_again()


def play_again():
    """
    Play again function
    """
    print("""
Thanks for playing, play again by clicking the run program button above
""")


def end_round(player_board, computer_board, hits, hits2):
    """
    Shows the game state after each guess by the computer and the player
    """
    print("\nThats the end of this round")
    print("Lets take a look at the boards\n")
    player_board.print_board()
    computer_board.print_board()
    print(f"""
{player_board.name}'s score: {hits}, {computer_board.name}'s score: {hits2}
Onto the next round. Good luck!
""")


def setup_game():
    """
    Sets up the game to play
    """
    global num_ships
    global board_size

    print("""
______________________________________________________________
WELCOME TO THE PYTHON BATTLESHIPS TERMINAL GAME
SINK THE COMPUTERS SHIPS BEFORE IT SINKS YOURS
\nINPUT IS COLUMN FIRST THEN ROW
TOP LEFT COORDINATE IS (0,0)
\nRUNNING SETUP.... PLEASE FOLLOW THE PROMPTS
______________________________________________________________
""")

    print("Enter a name, please ensure it is 4-8 characters long")
    name = input("Your name: ")
    while name_validation(name):
        print("Please ensure name is 4-8 characters long")
        name = input("Your name: ")

    print(f"\nWelcome {name}!")
    while True:
        try:
            board_size = int(input("""
Enter a board size, this must be between 4 and 6:
"""))
            if board_validation(board_size):
                print("Number is outside of range")
            else:
                break
        except ValueError:
            print("Please enter a number")

    while True:
        try:
            num_ships = int(input("""
Enter amount of ships each, between 2 and 4:
"""))
            if ship_validation(num_ships):
                print("Number is outside of range")
            else:
                break
        except ValueError:
            print("Please enter a number")

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
    print("Here are the boards, good luck!")
    # Print the boards
    player_board.print_board()
    computer_board.print_board()
    print("\nIts time to play, you're guessing first. Choose a coordinate")
    # Create hits variables to be able to track a win or loss
    player_hits = 0
    comp_hits = 0
    while player_hits < num_ships and comp_hits < num_ships:
        # Users guess
        col, row = computer_board.user_guess()
        while (col, row) in computer_board.guesses:
            print("You've already guessed here! Try again")
            col, row = computer_board.user_guess()
        check = computer_board.guess(col, row)
        print(f"\nYou guessed {col}, {row}")
        if check == "Hit":
            player_hits += 1
            print("You sunk a battleship")
        else:
            print("You missed a battleship")
        # Computers guess
        col, row = player_board.computer_guess()
        while (col, row) in player_board.guesses:
            col, row = computer_board.computer_guess()
        check = player_board.guess(col, row)
        print(f"Computer guessed {col}, {row}")
        # Checking for a hit
        if check == "Hit":
            comp_hits += 1
            print("Computer sunk a battleship")
        else:
            print("Computer missed a battleship")
        # Ending the round
        end_round(player_board, computer_board, player_hits, comp_hits)
    if player_hits == num_ships:
        player_win()
    elif comp_hits == num_ships:
        computer_win()


if __name__ == '__main__':
    setup_game()
