import pandas as pd
import numpy as np


### function to check the nunique and the value_counts for the categorical columns
def get_nunique_value_counts(df, col) : 

    print(f"{df[col].nunique()} \n{df[col].value_counts()}")