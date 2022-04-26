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

## Deployment
<hr>

1. Create a new app on the Heroku dashboard.
2. Add the python buildpack, followed by the node.js buildpack.
3. Head to the deploy section and connect the battleships repository to Heroku.
4. Selecting the 'master' branch, deploy the app.

## Credits
<hr>

- Code institute for the template to allow the mock terminal.
