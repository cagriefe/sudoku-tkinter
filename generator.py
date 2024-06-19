import random

def generate_sudoku(difficulty=''):
    grid = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
    
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
        grid[row][col] = ""
    
    return grid