import pandas as pd
import numpy as np


### function to track the number of nan values before and after the fix
def track_nan(df, df_copy) : 

        nan_report = pd.concat(
        [df.isna().sum(), df_copy.isna().sum()],
        axis=1,
        keys=["after_fix", "before_fix"]
    )
        
        return nan_report