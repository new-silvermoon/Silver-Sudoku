import math
class SudokuSolver:
    puzzle_size = None

    def __init__(self, puzzle_size):
        self.puzzle_size = puzzle_size

    def get_column_list(self, index, puzzle):
        column_list = []
        for row in puzzle:
            column_list.append(row[index])
        return column_list

    def generate_all_possible_values(self, rowIndex, colIndex, puzzle):
        row = puzzle[rowIndex]
        col = self.get_column_list(colIndex, puzzle)
        sub_grid = self.generate_sub_grid(rowIndex, colIndex, puzzle)
        possible_values_list = [x for x in range(1, self.puzzle_size + 1) if
                                ((x not in row) and (x not in col) and (x not in sub_grid))]

        return possible_values_list

    def has_empty_index(self, puzzle, l):
        for row in range(9):
            for col in range(9):
                if (puzzle[row][col] == 0):
                    l[0] = row
                    l[1] = col
                    return True
        return False

    def generate_sub_grid(self, row_index_limit, col_index_limit, puzzle):
        grid = []
        size_of_grid = int(math.sqrt(self.puzzle_size))
        row_index = 0
        col_index = 0
        while ((row_index + size_of_grid) <= row_index_limit):
            row_index += size_of_grid
        while ((col_index + size_of_grid) <= col_index_limit):
            col_index += size_of_grid
        endRowIndex = row_index + size_of_grid
        endColIndex = col_index + size_of_grid
        for i in range(row_index, endRowIndex):
            for j in range(col_index, endColIndex):
                grid.append(puzzle[i][j])
        return grid

    def does_solution_exists(self, puzzle):
        l = [0, 0]
        if (not self.has_empty_index(puzzle, l)):
            return True
        row = l[0]
        col = l[1]
        for num in range(1, self.puzzle_size + 1):
            safeList = self.generate_all_possible_values(row, col, puzzle)
            if num in safeList:
                puzzle[row][col] = num
                if (self.does_solution_exists(puzzle)):
                    return True
                puzzle[row][col] = 0
        return False
