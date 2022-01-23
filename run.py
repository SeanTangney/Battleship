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


print("\n-=-=-BATTLESHIP-=-=-\n")
print("How to play:")
print("* A battleship has been randomly placed on the board.")
print("* You have four tries to find it! ")
print("* Enter your coordinates (from 1-5) below\nBest of Luck!!\n")
print_board(board)


def random_row(board):
    """
    A function to generate a random row selection
    """
    return randint(1, len(board) + 1)


def random_col(board):
    """
    A function to generate a random column selection
    """
    return randint(1, len(board) + 1)


ship_row = random_row(board)
ship_col = random_col(board)

for guess in range(4):
    guess_row = int(input("\nGuess Row: "))
    guess_col = int(input("\nGuess Column: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("You've sunk the battleship")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        break
    else:
        if(guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("Your guess is outside the board")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        elif board[guess_row][guess_col] == " X":
            print("You've already guessed that one!")

        else:
            print("\n-=-=-")
            print("Miss!")
            print("-=-=-\n")
            board[guess_row][guess_col] = " X"

        print("Guess " + str(guess + 1) + " out of 5.\n")
        print_board(board)

    if guess >= 5:
        print("\n-=-=-=-=-=-")
        print("Game over!")
        print("-=-=-=-=-=-\n")

