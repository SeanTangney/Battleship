"""
A simple game of battleships run in the terminal.
"""
from random import randint


board = []

for x in range(5):
    board.append([" O"] * 5)


def print_board():
    """
    Print out game board in the terminal
    """
    for row in board:
        print(" ".join(row))


# Game Instructions
print("\n-=-=-BATTLESHIP-=-=-\n")
print("How to play:")
print("* A battleship has been randomly placed on the board.")
print("* The objective is to target it with your coordinates to hit it.")
print("* You have four tries to find it! ")
print("* Previous missed attempts are displayed on the board with an X ")
print("* Enter your coordinates (from 1-5) below\n  Best of Luck!!\n")
print_board()


def random_row():
    """
    A function to generate a random row selection
    """
    return randint(0, len(board))


def random_col():
    """
    A function to generate a random column selection
    """
    return randint(0, len(board))


# Generate random row and col and assign it to variables
ship_row = random_row()
ship_col = random_col()


# Validate users input to see if its a hit, miss or invalid input type
SHOT = 0
for guess in range(5):
    while True:
        try:
            guess_row = int(input("\nGuess Row: "))
            guess_col = int(input("\nGuess Column: "))

            if guess_row == ship_row and guess_col == ship_col:
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                print(" You've sunk the battleship")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("          You Win!\n")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                break
            else:
                if((guess_row < 1 or guess_row > 5) or
                        (guess_col < 1 or guess_col > 5)):
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    print("Your guess is outside the board")
                    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                elif board[guess_row - 1][guess_col - 1] == " X":
                    print("You've already guessed that one!")

                else:
                    print("\n-=-=-")
                    print("Miss!")
                    print("-=-=-\n")
                    SHOT += 1
                    board[guess_row - 1][guess_col - 1] = " X"
                    print("Guess " + str(SHOT) + " out of 5.\n")
                    print_board()
                    if SHOT == 5:
                        print("\n-=-=-=-=-=-=-=-=-=-=-")
                        print("\n     Game Over")
                        print("\nBetter Luck Next Time")
                        print("\n-=-=-=-=-=-=-=-=-=-=-")
                    break
        except Exception():
            print("Invalid entry")
