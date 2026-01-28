import pandas as pd
import numpy as np


### function to load the data based on the given path
def load_data(df_path) :
 
     df = pd.read_csv(df_path)

     return df

### function to check the nan values and the shape of the dataset
def get_nan_duplicates_shape(df) : 

     print(f"shape : {df.shape} \nduplicates : {df.duplicated().sum()} \nNan values : \n{df.isna().sum()}")

### function to check the info
def get_info(df) : 

     return df.info()


### function to drop the particular column
def drop_cols(df, col) : 

     df.drop(col, axis = 1, inplace = True)

### function to save the data to the given path
def save_data(df, df_path) : 

     df.to_csv(df_path, index = False)     