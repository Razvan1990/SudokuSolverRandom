from game_preparing.generators import GenerateValues
from conditions.check_values import CheckValues


class CreateNumbers:

    def __init__(self):
        self.generation = GenerateValues()
        self.checker = CheckValues()

    def add_row_list(self, sign):
        my_list = []
        for i in range(0, 9):
            my_list.append(sign)
        return my_list

    def generate_back_zeroes(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == " ":
                    board[i][j] = 0

    def create_blank_list(self):
        board = []
        list_board1 = self.add_row_list(0)
        list_board2 = self.add_row_list(0)
        list_board3 = self.add_row_list(0)
        list_board4 = self.add_row_list(0)
        list_board5 = self.add_row_list(0)
        list_board6 = self.add_row_list(0)
        list_board7 = self.add_row_list(0)
        list_board8 = self.add_row_list(0)
        list_board9 = self.add_row_list(0)
        board.append(list_board1)
        board.append(list_board2)
        board.append(list_board3)
        board.append(list_board4)
        board.append(list_board5)
        board.append(list_board6)
        board.append(list_board7)
        board.append(list_board8)
        board.append(list_board9)
        return board

    def change_indices(self, index_board):
        global index_row, index_column
        if index_board == 1:
            index_row = 0
            index_column = 0
        elif index_board == 2:
            index_row = 0
            index_column = 3
        elif index_board == 3:
            index_row = 0
            index_column = 6
        elif index_board == 4:
            index_row = 3
            index_column = 0
        elif index_board == 5:
            index_row = 3
            index_column = 3
        elif index_board == 6:
            index_row = 3
            index_column = 6
        elif index_board == 7:
            index_row = 6
            index_column = 0
        elif index_board == 8:
            index_row = 6
            index_column = 3
        elif index_board == 9:
            index_row = 6
            index_column = 6
        return index_row, index_column

    def generate_random_numbers_board(self):
        # first we generate 18 values -> 2 for each box
        board_game = self.create_blank_list()
        index_board = 1
        for i in range(0, 18):
            if index_board > 9:
                index_board = 1
            index_r, index_col = self.change_indices(index_board)
            generated_row = self.generation.generate_row_column_value(index_r)
            generated_column = self.generation.generate_row_column_value(index_col)
            while self.checker.check_if_box_available(board_game, generated_row, generated_column):
                generated_row = self.generation.generate_row_column_value(index_r)
                generated_column = self.generation.generate_row_column_value(index_col)
            value = self.generation.generate_value()
            # start checking availability
            check_all = self.checker.compute_checks(board_game, value, generated_row, generated_column)
            while check_all:
                value = self.generation.generate_value()
                check_all = self.checker.compute_checks(board_game, value, generated_row, generated_column)
            board_game[generated_row][generated_column] = value
            index_board += 1
        return board_game

    def complete_list(self, board_game):
        extra_values = self.generation.pick_final_number_completed()
        for x in range(18, extra_values):
            random_column = self.generation.generate_value() - 1
            random_row = self.generation.generate_value() - 1
            while self.checker.check_if_box_available(board_game, random_row, random_column):
                random_column = self.generation.generate_value() - 1
                random_row = self.generation.generate_value() - 1
            value = self.generation.generate_value()
            check_all = self.checker.compute_checks(board_game, value, random_row, random_column)
            while check_all:
                value = self.generation.generate_value()
                check_all = self.checker.compute_checks(board_game, value, random_row, random_column)
            board_game[random_row][random_column] = value
        return board_game
