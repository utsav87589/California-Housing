import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import pylab
import seaborn as sns
from sklearn.preprocessing import PowerTransformer
import joblib


### function to plot the qq plot, distribution plot and the box plot for the numerical columns
def plot_graphs(df) : 

    cols = df.select_dtypes(include = ['float64'])

    for col in cols : 

        print(f"column : {col}")
        plt.figure(figsize = (12, 4))

        #---------first plot, which is a hist plot        
        plt.subplot(1, 3, 1)
        plt.title('Hist plot')
        df[col].hist()

        #----------second one, which is a qq plot
        plt.subplot(1, 3, 2)
        plt.title('QQ plot')
        stat.probplot(df[col], dist = 'norm', plot = pylab)
        
        #----------third plot, box plot
        plt.subplot(1, 3, 3)
        plt.title('Boxplot')
        sns.boxplot(df[col])

        plt.show()


### function to apply and save the boxcox transformation on the given columns and save the transformer
def apply_transform_boxcox(df, cols, path_for_transformer) : 

    boxcox = PowerTransformer(method = 'boxcox')

    for col in cols : 
        df[col + '_boxcox'] = boxcox.fit_transform(df[col])

    joblib.dump(boxcox, path_for_transformer)
