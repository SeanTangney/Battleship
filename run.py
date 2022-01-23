
board = []

for (x) in range(5):
    board.append([" O"] * 5)

def print_board(board):
    """
    Print out game board in the terminal
    """
    for row in board:
        print(" ".join(row))
