import random

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell

    numbers = list(range(1, 10))
    random.shuffle(numbers) 

    for num in numbers:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = ""

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == "":
                return row, col
    return None

def remove_numbers(board, num_holes):
    while num_holes > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != "":
            board[row][col] = ""
            num_holes -= 1

def generate_sudoku(difficulty='easy'):
    board = [[""] * 9 for _ in range(9)]
    
    fill_diagonal_grids(board)
    
    solve_sudoku(board)
    
    if difficulty == 'easy':
        num_holes = 40 
    elif difficulty == 'medium':
        num_holes = 50
    else:  # hard
        num_holes = 60

    remove_numbers(board, num_holes)  
    return board

def fill_diagonal_grids(board):
    for i in range(0, 9, 3):
        fill_3x3_grid(board, i, i)

def fill_3x3_grid(board, row, col):
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for i in range(3):
        for j in range(3):
            board[row + i][col + j] = numbers.pop()