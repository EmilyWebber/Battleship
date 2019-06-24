import pandas as pd 

class Board:

    def __init__(self, x_range, y_range, filler):
        assert x_range == y_range
        self.x_range = x_range
        self.y_range = y_range
        self.filler = filler
        self.board = self.create_board()
        self.frame = self.create_features()

    def add_ship(self, x1, x2, y1, y2):
        board = self.board
        rows = board[y1:y2]
        space = rows[x1:x2]
#         for each in space:
#             if each == 0:
#                 s
        
    def print_board(self):
        for row in self.board.values():
            print (row)  

    def create_board(self):
        rt = []
        
        for x in range(self.y_range+1):
            new_row = []
            for y in range(self.x_range+1):
                new_row.append(self.filler)
            rt.append(new_row)
            
        df = pd.DataFrame(rt)
            
        index = []
        columns = []

        for i in range(10):
            base_x = 'x_{}'.format(i)
            base_y = 'y_{}'.format(i)
            index.append(base_y)
            columns.append(base_x)

        index.reverse()

        df.index = index
        df.columns = columns
        
        return df

    def get_frame(self):
        return self.frame

    def get_board(self):
        return self.board


    def create_features(self):
        '''
        Given a square board, generates features from the board. Returns a pandas data frame
        '''
        board = self.board.values
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
