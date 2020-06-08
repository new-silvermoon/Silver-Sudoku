import math
from random import randint
from utils.sudoku_solver import SudokuSolver

class SudokuGenerator:
    puzzle_size = None
    difficulty = None
    sudoku_solver = None

    def __init__(self,puzzle_size,difficulty="easy"):
        self.puzzle_size = puzzle_size
        self.difficulty = difficulty
        self.sudoku_solver = SudokuSolver(self.puzzle_size)

    def create_base_puzzle(self):

        puzzle = [[0 for _ in range(self.puzzle_size)] for _ in range(self.puzzle_size)]

        for i in range(self.puzzle_size):
            for j in range(self.puzzle_size):
                puzzle[i][j] = int((i * math.sqrt(self.puzzle_size) + int(i / math.sqrt(self.puzzle_size)) + j) % self.puzzle_size) + 1

        seed = randint(8,15)

        for _ in range(seed):
            puzzle = self.shuffle_puzzle(puzzle)

        return puzzle

    def generate_puzzle_challenge(self,puzzle):
        grid_size = self.puzzle_size * self.puzzle_size
        removal_count = {
            "easy": ((int(grid_size / 2) - int(grid_size / 10)), 0),
            "moderate": (int(grid_size), int(grid_size / 15)),
            "difficult": (int(grid_size), int(grid_size / 10))
        }

        item_removal_limit1 = removal_count[self.difficulty][0]
        item_removal_limit2 = removal_count[self.difficulty][1]

        puzzle = self.remove_values(puzzle, 1, item_removal_limit1)
        if item_removal_limit2 != 0:
            puzzle = self.remove_values(puzzle, 2, item_removal_limit2)

        return puzzle


    def remove_values(self, puzzle, type, item_removal_limit=35):
        if type == 1:
            removed_items_count = 0
            for _ in range(self.puzzle_size * 500):
                i = randint(0, self.puzzle_size - 1)
                j = randint(0, self.puzzle_size - 1)
                temp = puzzle[i][j]
                if temp == 0:
                    continue
                puzzle[i][j] = 0
                if len(self.sudoku_solver.generate_all_possible_values(i, j, puzzle)) != 1:
                    puzzle[i][j] = temp
                else:
                    removed_items_count += 1
                if removed_items_count == item_removal_limit:
                    return puzzle

            return puzzle
        elif type == 2:
            removed_items_count = 0
            for i in range(self.puzzle_size):
                for j in range(self.puzzle_size):
                    if (puzzle[i][j] == 0):
                        continue
                    temp = puzzle[i][j]
                    puzzle[i][j] = 0
                    temp_puzzle = [[ele for ele in row] for row in puzzle]
                    if not self.sudoku_solver.does_solution_exists(temp_puzzle):
                        puzzle[i][j] = temp
                    else:
                        removed_items_count += 1
                    if removed_items_count == item_removal_limit:
                        return puzzle
            return puzzle




    def shuffle_puzzle(self, puzzle):
        old_value = -1
        new_value = -1

        while(old_value == new_value):
            old_value = randint(1, self.puzzle_size)
            new_value = randint(1, self.puzzle_size)

        for i in range(self.puzzle_size):
            for j in range(self.puzzle_size):
                if (puzzle[i][j] == old_value):
                    puzzle[i][j] = new_value
                elif (puzzle[i][j] == new_value):
                    puzzle[i][j] = old_value

        mSize = int(math.sqrt(self.puzzle_size))
        if (mSize > 1):
            old_row_index = -1
            new_row_index = -1
            while (old_row_index == new_row_index):
                old_row_index = randint(1, mSize)
                new_row_index = randint(1, mSize)
            multiplier = randint(0, mSize - 1)
            old_row_index += (multiplier * mSize)
            new_row_index += (multiplier * mSize)
            puzzle[old_row_index - 1], puzzle[new_row_index - 1] = puzzle[new_row_index - 1], puzzle[
                old_row_index - 1]
            puzzle = [[x[i] for x in puzzle] for i in range(self.puzzle_size)]
            old_row_index -= (multiplier * mSize)
            new_row_index -= (multiplier * mSize)
            multiplier = randint(0, mSize - 1)
            old_row_index += (multiplier * mSize)
            new_row_index += (multiplier * mSize)
            puzzle[old_row_index - 1], puzzle[new_row_index - 1] = puzzle[new_row_index - 1], puzzle[
                old_row_index - 1]

        return puzzle

    def print_puzzle(self,puzzle):
        for row in puzzle:
            print(row)




