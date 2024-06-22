def validate_sudoku(board):
    def is_valid_group(group):
        """Check if a group (row, column, or sub-grid) contains no duplicates of digits 1-9."""
        seen = set()
        for value in group:
            if value != "":
                if value in seen:
                    return False
                seen.add(value)
        return True

    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False

    # Check columns
    for col in range(9):
        if not is_valid_group([board[row][col] for row in range(9)]):
            return False

    # Check 3x3 sub-grids
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            group = []
            for i in range(3):
                for j in range(3):
                    group.append(board[box_row + i][box_col + j])
            if not is_valid_group(group):
                return False

    return True