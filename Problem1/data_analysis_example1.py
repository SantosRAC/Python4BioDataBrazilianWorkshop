# Several simple tests, such as
## importing libraries
## reading table
## reading content of directories
## reading, manipulating pandas DataFrame
##

# TODO: Check all name of objects, variables, etc. then translate all to Portuguese or English
        ## During the workshop the variable names will be in Portuguese, to facilitate communication
        #  English is another barrier - this is why I am writing everything in Portuguese in the wiki


import pandas as pd # Importing python library called 'pandas'
import os # Used to check files in directory
import Bio # Importing biopython

print(os.listdir()) # Lists files in the current dir (it works either on Windows 10 or on Ubuntu 14.04)

print(pd.read_table('nmeth.1226-S3.txt')) # Reading gene expression data with "read_table" function of pandas

# Importing the table with gene expression data for:
tabelaExpressaoMouseBrain = pd.read_table('nmeth.1226-S3.txt') # Mouse brain
tabelaExpressaoMouseLiver = pd.read_table('nmeth.1226-S4.txt') # Mouse liver
tabelaExpressaoMouseMuscle = pd.read_table('nmeth.1226-S5.txt') # Mouse muscle

# TODO: allow python to import the same tables as Excel files (more usual to biologists)
# 

tabelaAnotacaoCamundongo = pd.read_table('gene_result.txt') # Importing the table with annotation (from NCBI)

print(tabelaExpressaoMouseBrain) # Printing the pandas DataFrame with gene expression data
                       ## Python will limit number of lines shown

print(tabelaExpressaoMouseBrain.shape) # Printing a tuple representing the dimensionality of the DataFrame.
print(tabelaExpressaoMouseBrain.size) # Printing the number of elements in the NDFrame

print(tabelaExpressaoMouseBrain.columns) # Printing the columns of the DataFrame

print(tabelaExpressaoMouseBrain['gene']) # Retrieving information of a column by dict-like notation

print(tabelaExpressaoMouseBrain.gene) # Retrieving information of a column by attribute

print(tabelaExpressaoMouseBrain.ix[1]) # Retrieving information from column 1

print(tabelaExpressaoMouseBrain.ix[[1, 2]]) # Retrieving information from column 1 and 2
                                 ## It is done by giving method ix a list with the row indexes

print(tabelaExpressaoMouseBrain.ix[[40, 401]]) # Retrieving information from column 40 and 401

del tabelaExpressaoMouseBrain['gid']  # Deleting the column with GI (we will not need this information)

print(tabelaExpressaoMouseBrain) # Printing the DataFrame with gene expression data
                       ## after deleting the column with GI

print(tabelaExpressaoMouseBrain.shape) # Printing a tuple representing the dimensionality of the gene expression dataFrame after removing one column
print(tabelaExpressaoMouseBrain.size) # Printing the number of elements in the gene expression DataFrame after removing one column

print(tabelaExpressaoMouseBrain.T) # Tranposing the results

print(tabelaExpressaoMouseBrain.values) # Printing only the values in the DataFrame

# Example of sum of values of same index in different pandas series
S1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a','c','d','e'])
S2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a','c','e','f','g'])

print(S1)
print(S2)

print(S1+S2)

# Filtering DataFrame based on gene name (column "gene")
print("Brain: ",tabelaExpressaoMouseLiver[tabelaExpressaoMouseLiver['gene'].isin(['Myf6','Myf5'])])
print("Muscle: ",tabelaExpressaoMouseMuscle[tabelaExpressaoMouseMuscle['gene'].isin(['Myf6','Myf5'])])
print("Liver: ",tabelaExpressaoMouseBrain[tabelaExpressaoMouseBrain['gene'].isin(['Myf6','Myf5'])])

# df['A'].isin([3, 6])
