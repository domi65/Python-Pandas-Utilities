# copy to your .ipynb notebook: from pandasutils import *
# example: if you import some of functions, note no brackets after name, like here:
#     from gc_utils import sigmoid, relu, dictionary_to_vector

# Optional (I assume numpy and pandas are already imported):
# import numpy as np
# import pandas as pd

# df_basic_info() is a function in pandasutils module, that shows Basic Information about a dataframe:
def df_basic_info(df):
    print('shape (rows, columns)= ', df.shape) #(rows, columns)
    print()
    print('index=', df.index) #Describe index
    print()
    print('columns, Describe DataFrame columns=', df.columns) #Describe DataFrame columns
    print()
    print('info=', df.info()) #Info on DataFrame
    print()
    print('count, Number of non-NA values=', df.count()) #Number of non-NA values
    print()
    return
    
