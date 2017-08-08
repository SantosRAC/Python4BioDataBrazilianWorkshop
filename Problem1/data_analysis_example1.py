# Several simple tests, such as
## importing libraries
## reading table
## reading content of directories
##
##

import pandas as pd # Importing python library called 'pandas'
import os # Used to check files in directory
import Bio # Importing biopython

print(os.listdir()) # Lists files in the current dir (it works either on Windows 10 or on Ubuntu 14.04)

print(pd.read_table('nmeth.1226-S3.txt')) # Reading gene expression data with "read_table" function of pandas

tabelaExpressao = pd.read_table('nmeth.1226-S3.txt') # Importing the table with gene expression data
tabelaAnotacaoCamundongo = pd.read_table('gene_result.txt') # Importing the table with annotation (from NCBI)

print(tabelaExpressao) # Printing the pandas DataFrame with gene expression data
                       ## Python will limit number of lines shown

print(tabelaExpressao.shape) # Printing a tuple representing the dimensionality of the DataFrame.
print(tabelaExpressao.size) # Printing the number of elements in the NDFrame

print(tabelaExpressao.columns) # Printing the columns of the DataFrame

print(tabelaExpressao['gene']) # Retrieving information of a column by dict-like notation

print(tabelaExpressao.gene) # Retrieving information of a column by attribute

print(tabelaExpressao.ix[1]) # Retrieving information from column 1

print(tabelaExpressao.ix[[1, 2]]) # Retrieving information from column 1 and 2
                                 ## It is done by giving method ix a list with the row indexes

print(tabelaExpressao.ix[[40, 401]]) # Retrieving information from column 40 and 401

del tabelaExpressao['gid']  # Deleting the column with GI (we will not need this information)

 print(tabelaExpressao) # Printing the DataFrame with gene expression data
                       ## after deleting the column with GI

print(tabelaExpressao.shape) # Printing a tuple representing the dimensionality of the gene expression dataFrame after removing one column
print(tabelaExpressao.size) # Printing the number of elements in the gene expression DataFrame after removing one column

print(tabelaExpressao.T) # Tranposing the results

