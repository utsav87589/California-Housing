import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


### function to split the data globally (cleanest earliest split)
def split_data_global(df) : 

    train, valid = train_test_split(df, test_size = 0.25, random_state = 35)

    train = train.reset_index(drop = True)
    valid = valid.reset_index(drop = True)

    return train, valid


### function to split the data locally (train/test split)
def split_data_locally(df, target_feature) : 

    X = df.drop(target_feature, axis = 1)
    y = df[target_feature]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42, test_size = 0.25)

    return X_train, X_test, y_train, y_test