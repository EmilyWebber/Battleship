import pandas as pd 

class Board:

    def __init__(self, x_range, y_range, filler):
        assert x_range == y_range
        self.x_range = x_range
        self.y_range = y_range
        self.filler = filler
        b = self.create_board()
        self.board = b
        
    def is_hit(self, x, y):
        return self.board.loc[y, x] == 'S'
        
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

    def get_board(self):
        return self.board
    
    def get_ship_dimentions(self, ship_type, x, y, direction):
        x2, y2 = x, y

        ships = {'carrier':5, 'battleship':4, 'cruiser':3, 'submarine':3, 'destroyer':2}
        assert ship_type in list(ships.keys())
        assert direction in ['up', 'right']

        length = ships[ship_type]

        if direction == 'up':
            y2 += length - 1
        elif direction == 'right':
            x2 += length - 1

        return x, x2, y, y2
    
    def add_ship(self, ship_type, x, y, direction ):
        '''
        Make sure this is done from a 0 index space
        '''
        
        board = self.board

        x1, x2, y1, y2 = self.get_ship_dimentions(ship_type, x, y, direction)

        up = (x1 == x2)

        # direction is up, select a column
        if up:
            rows = []
            col = 'x_{}'.format(x1)
            for y in range(y1, y2+1):
                rows.append('y_{}'.format(y))
            space = board.loc[rows, col]

        # direction is right, select a row
        elif y1 == y2:
            row = 'y_{}'.format(y1)
            col_1 = 'x_{}'.format(x1)
            col_2 = 'x_{}'.format(x2)
            space = board.loc[row, col_1:col_2]

        for each in space.values:
            if each != 0:
                b.print_board()
                return 'Please try a different spot! This one is taken.'

        if up:
            board.loc[rows, col] = 'S'

        else:

            board.loc[row, col_1:col_2] = 'S'
            
        self.board = board

        return 