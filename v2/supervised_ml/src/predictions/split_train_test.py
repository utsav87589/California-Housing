import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


### function to split the train and the test data
def split_train_test(df, target_feature) : 

    X = df.drop(target_feature, axis = 1)
    y = df[target_feature]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

    return X_train, X_test, y_train, y_test


### function to verify the split by veryfying the shape 
def verify_split(X_train, y_train, X_test, y_test) : 

    print(f"X_train : {X_train.shape} :: y_train : {y_train.shape} \nX_test : {X_test.shape} :: y_test : {y_test.shape}")

