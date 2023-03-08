import sys

from constants import constants
from conditions.check_values import CheckValues


class SolveGame:

    def __init__(self):
        self.checker = CheckValues()

    '''
       1. We traverse all the keys and see what value is empty
       2. We know that the values could be from 1 to 9
       3. We check now if the value is correct to add
       4. we will redo the process (recursively) and appeal the same function,

       '''
    @staticmethod
    def get_valid_positions(board, row, column):
        list_value_rows = []
        list_value_boxes = []
        list_value_columns = []
        # get row values
        for i in range(0, 9):
            if board[row][i] != 0:
                list_value_rows.append(board[row][i])
        for i in range(0, 9):
            if board[i][column] != 0:
                list_value_columns.append(board[i][column])
        row_board = int(row / 3) * 3
        column_board = int(column / 3) * 3
        for i in range(row_board, row_board + 3):
            for j in range(column_board, column_board + 3):
                if board[i][j] != 0:
                    list_value_boxes.append(board[i][j])
        final_list_values = list(set(list_value_rows + list_value_columns + list_value_boxes))
        valid_positions = [x for x in constants.DIGITS if x not in final_list_values]
        return valid_positions

    def solve_sudoku(self, list_conversion):
        if self.checker.check_board_is_complete(list_conversion):
            return True  # this means our board is finally completed
        for i in range(0, len(list_conversion)):
            for j in range(0, len(list_conversion[i])):
                if list_conversion[i][j] == 0:
                    valid_positions = self.get_valid_positions(list_conversion, i, j)
                    for digit in valid_positions:
                        list_conversion[i][j] = digit
                        # need now to make recursive call, and we return true (it is completed)
                        is_completed = self.solve_sudoku(list_conversion)
                        if is_completed:
                            return True
                        else:
                            list_conversion[i][j] = 0
                        # we convert back the index to nothing
                    # basically there is no possibility to resolve the sudoku now, so it will continue with a new index
                    # If it is out of valid positions, it will start backtracking and deletes previous indices
                    return False
                # here we know that it cannot be completed
                # need to return where we don't find an empty space anymore
        return True

    def check_if_sudoku_solved(self, board):
        is_solved = self.solve_sudoku(board)
        if is_solved:
            print("Board is successfully completed")
            return board
        else:
            print("Sorry! We cannot solve this sudoku puzzle! Try a different one")
            sys.exit(0)
