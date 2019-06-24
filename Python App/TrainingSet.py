import pandas as pd

class TrainingSet:
      
    def __init__(self, board):
        self.training_set = self.create_features(board)

    def get_set(self):
        return self.training_set
        
        
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
