# Several simple tests, such as
## importing libraries
## reading table
## reading content of directories
##
##

import pandas as pd # Importing python library called 'pandas'
import os # Used to check files in directory
import Bio # Importing biopython

os.listdir() # Lists files in the current dir (Windows 10)

pd.read_table('nmeth.1226-S3.txt') # Convert text data into a DataFrame

tabelaExpressao = pd.read_table('nmeth.1226-S3.txt') # Importing the table with gene expression

