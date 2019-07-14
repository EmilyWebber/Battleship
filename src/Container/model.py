#  Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  
#  Licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License.
#  A copy of the License is located at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  or in the "license" file accompanying this file. This file is distributed 
#  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
#  express or implied. See the License for the specific language governing 
#  permissions and limitations under the License.

from __future__ import print_function

import argparse
import os
import pandas as pd

# from sklearn.externals import joblib

def create_features(board):
    '''
    Given a square board, generates features from the board. Returns a pandas data frame
    '''
    # make sure the board is a square 
    assert len(board) == len(board[0])

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
        
def add_vanilla_labels(df):
    df['Miss'] = 0
    df.insert(0, 'Hit', [0 for i in range(df.shape[0])])
    return df

def main():
    parser = argparse.ArgumentParser()

    # Sagemaker specific arguments. Defaults are set in the environment variables.
    parser.add_argument('--output-data-dir', type=str, default=os.environ['SM_OUTPUT_DATA_DIR'])
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])

    args = parser.parse_args()

    # Take the set of files and read them all into a single pandas dataframe
    input_files = [ os.path.join(args.train, file) for file in os.listdir(args.train) ]

    board = [ pd.read_csv(file, header=None, engine="python").values for file in input_files ]
    
    df = create_features(board[0])
    
    df = add_vanilla_labels(df)
    
    output_file = os.path.join(args.model_dir, "board_as_features.csv") 
    
    df.to_csv(output_file, index=False, header=False)

    # Print the coefficients of the trained classifier, and save the coefficients
#     joblib.dump(clf, os.path.join(args.model_dir, "model.joblib"))

def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    df = pd.read_csv(os.path.join(model_dir, "board_as_features.csv"))
    return clf            

                     
if __name__ == '__main__':    
    main()

