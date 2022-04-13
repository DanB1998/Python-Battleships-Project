board = []

for x in range(8):
        board.append(' _ ' * 8)

def print_game_board(board):
    print(" 1  2  3  4  5  6  7  8")
    for x in board:
        print(x)

def main():
    """
    Run the program
    """
    print_game_board(board)
    

print('Welcome to Python battleships')
main()
