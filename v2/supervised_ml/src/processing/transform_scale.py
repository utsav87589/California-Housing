import pandas as pd
import numpy as np
from scipy.stats import boxcox
import joblib


### function to apply thr boxcox transformation
def apply_transform_boxcox(df, cols) : 

    for col in cols : 

        df[col], parameter = boxcox(df[col] + 1)

### function to remove the additional outliers i.e. between 3 standard deviation to the right and left for the boxcox column
def remove_outliers(df, cols) : 

    for col in cols : 

        mean = df[col].mean()
        std = df[col].std()

        upper_limit = mean + (3*std)
        lower_limit = mean - (3*std)

        df[col] = df[col].apply(lambda x : upper_limit if x > upper_limit else x)
        df[col] = df[col].apply(lambda x : lower_limit if x < lower_limit else x)


### function to scale the data and save the scaler on the train data.
# def apply_scaler(df, cols, scaler_path = None) : 
