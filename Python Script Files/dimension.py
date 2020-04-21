# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np 

import os

print (os.getcwd() )
# for file in os.listdir(cwd):
#     if file.startswith("file"):
#         print("File \"{}\" is located at \"{}\"".format(file, os.path.join(cwd, file)))




# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("weatherhistory.csv") 

#data.head()
print(data)
