import pandas as pd
import numpy as np


### function to load the data based on the given path
def load_data(df_path) :
 
     df = pd.read_csv(df_path)

     return df

### function to check the nan values in the dataset
def get_nan(df) : 

     return df.isna().sum()


### function to check the shape
def get_shape(df) : 

     return df.shape


### function to check the info
def get_info(df) : 

     return df.info()