import sys
from solver.solve_game import SolveGame
from game_preparing.number_creator import CreateNumbers
from excel_writer.excel_writer import ExcelWriter

sys.setrecursionlimit(10000)


class GamePlay:

    def __init__(self):
        self.number_creator = CreateNumbers()
        self.excel_wr = ExcelWriter()
        self.solver = SolveGame()

    def execute(self):
        board_values = self.number_creator.generate_random_numbers_board()
        board_values = self.number_creator.complete_list(board_values)
        self.excel_wr.write_to_file(board_values)
        self.number_creator.generate_back_zeroes(board_values)
        answer = self.excel_wr.check_if_file_closed()
        if answer == "Y" or "y":
            final_board = self.solver.check_if_sudoku_solved(board_values)
            self.excel_wr.write_solution_to_file(final_board)

