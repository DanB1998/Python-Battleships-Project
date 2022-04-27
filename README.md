# Python Battleships Game

In this project I will be building a battleship game in python, playable in the terminal. This project uses code institutes template to allow this game to be played in a mock terminal when deployed on Heroku.

The player will battle against a computer and will have to sink all of the computers ships before its sinks theirs.

## User stories

* User's want to have a fun and interactive game to play.

* User's want the application to hand any areas to prevent a bad user experience.

* User's want feedback and from the game so they can monitor game progress. They also want to know if they win or lose.

## Features
<hr>

A list of all of the features in this battleship terminal game, and an overview of what they are and do.

### Starting Terminal
<hr>
The starting terminal is what the user will see when they land on the page. The first prompt for user input will ask for the user's name, which will  be stored in the player board instance of the class 'UserBoard' 


### Computer board randomisation
<hr>

Computer board has randomly generated ships placed onto it. The board is hidden from the user as the ships positions are stored in the `ships` list instance in the UserBoard class.

To prevent a ship being placed on top of another this code block executes and checks if the randomised coordinate has already been appended to the `ships` list.

```
col, row = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
while (col, row) in self.ships:
    col, row = random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)
self.store_ships(col, row)
```
If the coordinates are already inside the `ships list` the while loop will identify this and repeat until it finds coordinates that are not inside of the `ships list`.

### Input validation
<hr> 
Input validation is extremely important in a game which is taking input from a player. There are a couple of ways my game prevents incorrect or illegal inputs:
<br></br>

1. Using while loops
    To prevent either player from inputting a guess twice. A for loop is used in the `start game()` function. An example of the for loop can be seen here:
```
col, row = computer_board.user_guess()
while (col, row) in computer_board.guesses:
        print("You've already guessed here! Try again")
        col, row = computer_board.user_guess()
```
The while loop checks the new guess against the boards own `guesses = []` list, and if their is a duplicate guess, the while loop will repeat until the player inputs a guess that is unique.
<br></br>

2. Using `Try and Except` statements
    The `Try and Except` statements used on the input for the row and the column were the main forms of input validation in this game
```
while True:
    try:
        user_col = int(input("\nSelect column: "))
        if user_col < 0 or user_col > self.board_size-1:
            print("Number is outside of range")
        else:
            break
    except ValueError:
        print("Please enter a number")
```
In this `Try and Except` statement the `Try` will execute until the input is an integer as it is wrapped in a for loop that is always True. When an integer is entered it will then progress onto the `if / else` statement which will check that if input is outside the board range.

Only when both of these instances conclude that the input is valid the loop will then break and do the same for the other coordinate. Once both are validated the row and column values will be returned.

### The Data Model
<hr>

The data model used is the UserBoard class. This class stores:

1. The size of the board
2. The number of ships on the board
3. The player
4. The guesses used on that board
5. The ships position on the board

Here is a look at the classes methods with collapsed functions.

*INSERT SS OF CLASS*

The methods allow the board to assign any relevant information to itself, and also append inputted/received guesses or ship positions for future reference. This made it easy to construct the start game function as a lot of the information is stored or easily obtained inside the UserBoard class.

### Future Features
<hr>

* Ability to choose size and orientation of ships

## Testing
<hr>

### Manual testing
<hr>

I tested the input validation by inputting many different incorrect data types.
Test cases:

1. Inputting nothing
2. Inputting an integer that is outside of the boards range
3. Inputting a coordinate I have already guessed
4. Inputting a string

Results from test cases:

1. Pass - when inputting nothing the program asks for a number to be given, and asks the user to retry.
2. Pass - When inputting an integer that is outside the range, the program asks for a number inside the range.
3. Pass - When inputting a previous guess the program notifies the user and asks them to try again.
4. Pass - When inputting a string the program asks for an integer to be given, and asks the user to retry.

### User Stories Testing
<hr>

* User's want to have a fun and interactive game to play.

The game allows multiple inputs that are validated that can control the size and length of the game, the challenge against the computer and the guessing unknown tiles adds to the fun.

* User's want the application to hand any areas to prevent a bad user experience.

All inputs are validated and if they do not pass then the program will ask for a new input, to prevent any disruption in the user experience

* User's want feedback and from the game so they can monitor game progress. They also want to know if they win or lose.

The round end gives an update of the score and the current board that each player has. Also once one of the players hits all the ships the game will announce a winner.

### Validator testing
<hr>

There were no errors when passing the code through the PEP8 validator at http://pep8online.com/

## Deployment
<hr>
Please note that at the time of deployment for this project, heroku was not allowing links to github due to some for of security issue, so deployment of this app was pushed through the console.
Here are the steps to deploying this way.

1. Create a new app on the Heroku dashboard.
2. Add the python buildpack, followed by the node.js buildpack.
3. Head to the console of the repository in gitpod.
4. login to heroku through the console using `heroku login -i`
5. Run command `heroku git:remote -a python-battleships-game`
6. Push changes using `git push heroku main`


## Solved Bugs
<hr>

Bug  #1:

Computer was generating ships outside of the board range and I could not understand why I could not find all of the ships.

Bug #1 solved: 
I solved this bug by running the program a few times whilst printing the ships list     belonging to the board.

`print(computer_board.ships)` 

After doing this I realised that some of the ships were positioned outside of the board size (you could also guess 1 too far as this issue was global). The problem was an indexing problem, and once I changed `board_size` to `board_size-1` globally I had no further issues.

## Credits
<hr>

- [Code institute](https://codeinstitute.net/) for the template to allow the mock terminal.

- [Code institute](https://codeinstitute.net/) for the Data model and structure of the Class. Referenced below:

```
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
```