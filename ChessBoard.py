import numpy as np

# Create an 8x8 numpy array filled with 'x'
chess_board = np.full((8, 8), 'x', dtype=str)

# Fill the array with alternating '1's and 'x's to create a chessboard pattern
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            chess_board[i][j] = '1'

# Print the chess board
for row in chess_board:
    print('  '.join(row))
