# %% [markdown]

# %%
#I am separating the blocks to indicate this is all this piece of code is doing. 
#This is importing the pandas directories.
import pandas as pd


# %%
#New block to read in the file
scores_csv = 'Dataset_TAS_SRS.csv'


df = pd.read_csv(scores_csv)

#This displays a couple rows to make sure it is seeing the file properly. 
df.head(3)


# %%
#This is showing correlations for specific columns
#df[['TAS-20', 'SRS']].corr('pearson')

#This is showing correlations for all data 
#Added print around this when I turned it into a python vs jupyter 
print(df.corr('pearson'))




