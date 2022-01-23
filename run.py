from random import randint


board = []

for (x) in range(5):
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
    return randint(0, len(board[0]) -1)

def random_col(board):
    """
    A function to generate a random column selection
    """
    return randint(0, len(board[0]) -1)
