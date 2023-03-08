from constants import constants


class CheckValues:

    def check_if_box_available(self, list_values_indices, index_row, index_column):
        if list_values_indices[index_row][index_column] == 0:
            return False
        else:
            return True

    # start the checks
    def check_values_horizontally(self, board, value, index_row):
        # check on what column we are
        for j in range(0, len(board)):
            if board[index_row][j] == value:
                return True
        return False

    def check_values_vertically(self, board, value, index_column):
        for i in range(0, len(board)):
            if board[i][index_column] == value:
                return True
        return False

    def check_values_box(self, value, board, index_row, index_column):
        # to see the box we need to check , we divide the current row/column by 3 and the result is then multiplied by 3
        row = int(index_row / 3) * 3
        column = int(index_column / 3) * 3  # this always gives us the first cell of a box
        # we know then that we just to check 2 rows left and 2 columns down
        for i in range(row, row + 3):
            for j in range(column, column + 3):
                if board[i][j] == value:
                    return True
        return False

    def compute_checks(self, board, value, index_row, index_col):
        check1 = self.check_values_horizontally(board, value, index_row)
        check2 = self.check_values_vertically(board, value, index_col)
        check3 = self.check_values_box(value, board, index_row, index_col)
        if check1 or check2 or check3:
            return True
        return False

    def get_rows(self, board):
        list_rows = []
        for i in range(0, 9):
            list_row = board[i]
            list_rows.append(list_row)
        return list_rows

    def get_columns(self, board):
        list_columns = []
        list_column = []
        index_col = 0
        while index_col < 9:
            for i in range(0, 9):
                val = board[i][index_col]
                list_column.append(val)
            index_col += 1
            list_column_copy = list_column.copy()
            list_columns.append(list_column_copy)
            list_column.clear()
        return list_columns

    def get_blocks(self, board):
        list_boxes = []
        list_box1 = []
        list_box2 = []
        list_box3 = []
        list_box4 = []
        list_box5 = []
        list_box6 = []
        list_box7 = []
        list_box8 = []
        list_box9 = []
        for i in range(0, 9):
            for j in range(0, 9):
                if i < 3:
                    if j < 3:
                        list_box1.append(board[i][j])
                    elif j < 6:
                        list_box2.append(board[i][j])
                    elif j < 9:
                        list_box3.append(board[i][j])
                elif i < 6:
                    if j < 3:
                        list_box4.append(board[i][j])
                    elif j < 6:
                        list_box5.append(board[i][j])
                    elif j < 9:
                        list_box6.append(board[i][j])
                elif i < 9:
                    if j < 3:
                        list_box7.append(board[i][j])
                    elif j < 6:
                        list_box8.append(board[i][j])
                    elif j < 9:
                        list_box9.append(board[i][j])
        list_boxes.append(list_box1)
        list_boxes.append(list_box2)
        list_boxes.append(list_box3)
        list_boxes.append(list_box4)
        list_boxes.append(list_box5)
        list_boxes.append(list_box6)
        list_boxes.append(list_box7)
        list_boxes.append(list_box8)
        list_boxes.append(list_box9)
        return list_boxes

    def check_board_is_complete(self, board):
        list_rows = self.get_rows(board)
        list_columns = self.get_columns(board)
        list_boxes = self.get_blocks(board)

        for list_r in list_rows:
            if len(set(list_r)) != len(constants.DIGITS) or 0 in list_r:
                return False
        for list_r in list_columns:
            if len(set(list_r)) != len(constants.DIGITS) or 0 in list_r:
                return False
        for list_r in list_boxes:
            if len(set(list_r)) != len(constants.DIGITS) or 0 in list_r:
                return False
        return True
