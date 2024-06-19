import random
import numpy as np

def generate_sudoku(difficulty=''):
    def is_valid(board, row, col, num):
        # Check if the number is already in the current row
        if num in board[row]:
            return False
        
        # Check if the number is already in the current column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check if the number is already in the current 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(box_row_start, box_row_start + 3):
            for j in range(box_col_start, box_col_start + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def solve(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == "":
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if solve(board):
                                return True
                            else:
                                board[i][j] = ""
                    return False
        return True
    
    # Start with a blank board
    board = [["" for _ in range(9)] for _ in range(9)]
    
    # Solve the board to get a completed Sudoku solution
    solve(board)
    
    # Now create the difficulty by removing numbers based on percentage
    total_cells = 9 * 9
    if difficulty == 'easy':
        zero_percentage = 0.45
    elif difficulty == 'hard':
        zero_percentage = 0.60
    elif difficulty == 'expert':
        zero_percentage = 0.75
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'hard', or 'expert'.")
    
    num_zeros = int(total_cells * zero_percentage)
    positions = list(range(total_cells))
    random.shuffle(positions)
    
    for i in range(num_zeros):
        row = positions[i] // 9
        col = positions[i] % 9
        board[row][col] = ""
    
    return board

# Example usage:
