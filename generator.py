import random
from copy import deepcopy

def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if the number is already in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if the number is in the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == "":
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = ""
                return False
    return True

def remove_numbers(board, num_holes):
    holes_made = 0
    while holes_made < num_holes:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != "":
            removed_num = board[row][col]
            board[row][col] = ""
            
            # Check if the board is still valid after removing the number
            if not is_valid(board, row, col, removed_num):
                board[row][col] = removed_num
                continue
            
            holes_made += 1

def generate_sudoku(difficulty=''):
    board = [[""] * 9 for _ in range(9)]
    solve_sudoku(board)  # Fill the board with a valid solution

    # Set difficulty levels
    if difficulty == 'easy':
        num_holes = 40  # Adjust this number based on desired difficulty
    elif difficulty == 'medium':
        num_holes = 50
    else:  # hard
        num_holes = 60

    # Create a copy of the board to work with
    board_copy = deepcopy(board)
    remove_numbers(board_copy, num_holes)  # Create the puzzle by removing numbers
    return board_copy