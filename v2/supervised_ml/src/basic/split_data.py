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


### function to verify the split by checking the shape for the global split
def check_global_split(train, valid) : 

    print(f"train shape : {train.shape} :: valid shape : {valid.shape}")


### function to verify the split by checkin the shape for the local split
def check_local_split(X_train, X_test, y_train, y_test) : 
    print(f"{X_train.shape} : {y_train.shape} :: {X_test.shape} : {y_test.shape}")