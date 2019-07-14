'''
Inherits functions directly from Board; it's a sub-class. One way only on that functionality.
'''

import pandas as pd
import Board

class TrainingSet:
      
    def __init__(self, board):
        self.board = board
        ts = self.create_features(board.get_board().values)
        self.training_set = ts
        self.create_training_set()
        
    def get_set(self):
        return self.training_set
    
    def add_value(self, x, y, column):
        ts_df = self.training_set
        query = ts_df[ (ts_df[x] == 1) & (ts_df[y] == 1)]
        idx = int(query.index.values[0])
        ts_df.at[idx, column] = 1
#         self.training_set = ts_df
        
        return list(ts_df.iloc[idx, :].values)[:]
       
    def create_training_set(self):
        '''
        Walks through a board, finds the points where there would be a hit, and labels it. 
        '''
        b = self.board
        df = b.get_board()
        
        rt = []
        
        for y, row in df.iterrows():
    
            for x, col in row.iteritems():

                # check x and y
                if b.is_hit(x, y):

                    new_row = self.add_value(x, y, column='Hit')

                else:

                    new_row = self.add_value(x, y, column = 'Miss')
                    
                rt.append(new_row)
        self.training_set = pd.DataFrame(rt)
        
        return
        
    def create_features(self, board):
        '''
        Given a square board, generates features from the board. Returns a pandas data frame
        '''
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
        df.insert(0, 'Hit', [0 for i in range(df.shape[0])])
        df['Miss'] = 0

        return df
