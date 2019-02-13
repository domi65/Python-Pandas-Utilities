# v10
# copy to your .ipynb notebook: 
# from pandasutils import *

# example: if you import some of functions, note no brackets after name, like here:
# from gc_utils import sigmoid, relu, dictionary_to_vector

# Optional (I assume numpy and pandas are already imported):
# import numpy as np
# import pandas as pd

# df_basic_info() is a function in pandasutils module, that shows Basic Information about a dataframe:
def df_basic_info(df):
    print('----shape (rows, columns)= ')
    print(df.shape) #(rows, columns)
    print('----index=')
    print(df.index) #Describe index
    print('----columns, Describe DataFrame columns=')
    print(df.columns) #Describe DataFrame columns
    print('----info=')
    print(df.info()) #Info on DataFrame
    print('----count, Number of non-NA values=')
    print(df.count()) #Number of non-NA values
    print()
    return
    
# Summary Statistics
def df_summary_stat(df):
    print('----Sum of values=')
    print(df.sum()) #Sum of values
    print('----Cumulative sum of values=')
    print(df.cumsum()) #Cummulative sum of values
    print('----Minimum/maximum values=')
    print(df.min()/df.max()) #Minimum/maximum values
    print('----Minimum/Maximum index value=')
    print(df.idxmin()/df.idxmax()) #Minimum/Maximum index value
    print('----Summary statistics=')
    print(df.describe()) #Summary statistics
    print('----Mean of values=')
    print(df.mean()) #Mean of values
    print('----Median of values=')
    print(df.median()) #Median of values
    print()
    return
    