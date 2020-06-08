from utils import sudoku_generator as sg

puzzle = None
obj = None
def generate_sudoku():
    global obj,puzzle
    obj = sg.SudokuGenerator(9,"moderate")
    puzzle = obj.create_base_puzzle()
    puzzle = obj.generate_puzzle_challenge(puzzle)
    print("Challenge: ")
    obj.print_puzzle(puzzle)

def solve_sudoku():
    global obj, puzzle
    print("Solution: ")
    if obj.sudoku_solver.does_solution_exists(puzzle):
        print(*puzzle,sep='\n')
    else:
        print("No solution exists")

if __name__ == "__main__":
    generate_sudoku()
    solve_sudoku()