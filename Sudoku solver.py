def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    empty_cell = find_empty_cell(grid)
    if empty_cell is None:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0

    return False

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()

# Example Sudoku grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(grid):
    print("Sudoku solved:")
    print_grid(grid)
else:
    print("No solution exists.")


  

