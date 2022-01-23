"""
A simple game of battleships run in the terminal.
"""
from random import randint


board = []

for x in range(5):
    board.append([" O"] * 5)


def print_board(board):
    """
    Print out game board in the terminal
    """
    for row in board:
        print(" ".join(row))


print("Let's Play")
print_board(board)


def random_row(board):
    """
    A function to generate a random row selection
    """
    return randint(0, len(board[0]) - 1)


def random_col(board):
    """
    A function to generate a random column selection
    """
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

for guess in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("You've sunk the battleship")
        break
    else:
        if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Your guess is outside the board")

        elif board[guess_row][guess_col] == "X":
            print("You've already guessed that one!")

        else:
            print("Miss!")
            board[guess_row][guess_col] = "X"
