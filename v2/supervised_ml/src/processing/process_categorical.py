import pandas as pd
import numpy as np


### function to check the nunique and the value_counts for the categorical columns
def get_nunique_value_counts(df, col) : 

    return f"{df.nunique()} \n{df.value_counts()}"