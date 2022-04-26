# Python Battleships Game

In this project I will be building a battleship game in python, playable in the terminal. This project uses code institutes template to allow this game to be played in a mock terminal when deployed on Heroku.

The player will battle against a computer and will have to sink all of the computers ships before its sinks theirs.

## Features
<hr>

A list of all of the features in this battleship terminal game, and an overview of what they are and do.

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

### Validator testing

There were no errors when passing the code through the PEP8 validator at http://pep8online.com/

## Deployment
<hr>

1. Create a new app on the Heroku dashboard.
2. Add the python buildpack, followed by the node.js buildpack.
3. Head to the deploy section and connect the battleships repository to Heroku.
4. Selecting the 'master' branch, deploy the app.

## Credits
<hr>

- Code institute for the template to allow the mock terminal.
