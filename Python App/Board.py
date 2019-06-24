import pandas as pd 

class Board:

    def __init__(self, x_range, y_range, filler):
        assert x_range == y_range
        self.x_range = x_range
        self.y_range = y_range
        self.filler = filler
        self.board = self.create_board()
        self.frame = self.create_features()

    def print_board(self):
        for row in self.board:
            print (row)  

    def create_board(self):
        rt = []
        for x in range(self.y_range+1):
            new_row = []
            for y in range(self.x_range+1):
                new_row.append(self.filler)
            rt.append(new_row)
        return rt

    def get_frame(self):
        return self.frame

    def get_board(self):
        return self.board


    def create_features(self):
        '''
        Given a square board, generates features from the board. Returns a pandas data frame
        '''
        board = self.board
        n_columns = len(board) + len(board[0])

        rt = []

        for y, row in enumerate(board):

            for x, col in enumerate(row):

                # add one extra column for the label 
                new_row = [0 for i in range(n_columns)]

                new_row[x] = 1
                new_row[y + len(board)] = 1

                rt.append(new_row)
        df = pd.DataFrame(rt)

        columns = []

        for c in range(n_columns):
            if c < len(board):
                str_base = "x_{}"
            else:
                str_base = 'y_{}'
                c -= len(board)
            columns.append(str_base.format(c))

        df = pd.DataFrame(rt, columns = columns)

        return df
