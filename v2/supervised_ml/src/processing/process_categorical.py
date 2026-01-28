import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### function to check the nunique and the value_counts for the categorical columns
def get_nunique_value_counts(df, col) : 

    nunique = df[col].nunique()
    value_counts = df[col].value_counts()

    return nunique, value_counts


### function to check the categories cardionality for label based columns
def check_feature_cardionality(df, main_col, target_col) : 

    codes = df[main_col].astype('category').cat.codes
    x_jitter = codes + np.random.normal(0, 0.05, size=len(codes))

    plt.figure(figsize=(8, 4))
    plt.scatter(
        x_jitter,
        df[target_col],
        c=codes,
        alpha=0.6
    )


### function to apply the label encoding 
def apply_label_encoding(df, col, labels) : 

    df[col] = df[col].map(labels)


### function to compare the nunique and valu_counts pre, post label encoding
def nunique_value_counts_compare(df, df_copy, col) : 

    nunique_main = df[col].nunique()
    value_counts_main = df[col].value_counts()

    nunique_copy = df_copy[col].nunique()
    value_counts_copy = df_copy[col].value_counts()

    print(f"before : \nNo. of categories : {nunique_copy} \nvalue_counts : \n{value_counts_copy}")
    print(f"after : \nNo. of categories : {nunique_main} \nvalue_counts : \n{value_counts_main}")