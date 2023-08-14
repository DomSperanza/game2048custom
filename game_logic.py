import numpy as np
import random

def initialize_game(size=4):
    board = np.zeros((size, size), dtype=int)
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(i, j) for i in range(board.shape[0]) for j in range(board.shape[1]) if board[i, j] == 0]
    i, j = random.choice(empty_cells)
    board[i, j] = random.choice([2, 4])

def slide_row(row):
    result = [0] * len(row)  # Initialize with zeros
    idx = 0

    # Combine similar tiles
    for i in range(len(row)):
        if row[i] != 0:
            if idx > 0 and row[i] == result[idx - 1]:
                result[idx - 1] += row[i]
                idx -= 1
            else:
                result[idx] = row[i]
            idx += 1

    return np.array(result)

def slide_board(board, direction):
    if direction == 'down':
        for j in range(board.shape[1]):
            board[:, j] = slide_row(board[:, j])
    elif direction == 'up':
        for j in range(board.shape[1]):
            board[:, j] = slide_row(board[::-1, j])[::-1]
    elif direction == 'left':
        for i in range(board.shape[0]):
            board[i, :] = slide_row(board[i, :])
    elif direction == 'right':
        for i in range(board.shape[0]):
            board[i, :] = slide_row(board[i, ::-1])[::-1]
    add_new_tile(board)

def is_game_over(board):
    if 0 in board:
        return False
    for direction in ['up', 'down', 'left', 'right']:
        temp_board = board.copy()
        slide_board(temp_board, direction)
        if not np.array_equal(temp_board, board):
            return False
    return True
