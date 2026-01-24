import pandas as pd
import numpy as np


### function to check the number of nan values
def get_nan(df) :

    return df.isna().sum()


### function to track the number of nan values before and after the fix
def track_nan(nan_before, nan_after) : 

        nan_report = pd.concat(
        [nan_before, nan_after],
        axis=1,
        keys=["before_fix", "after_fix"]
    )
        
        return nan_report