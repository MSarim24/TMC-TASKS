import pandas as pd
import numpy as np

df = pd.read_csv("dirty_cafe_sales.csv")

print(df.isna().sum())

copy = df.copy()

copy.info()

objectscol =  copy.select_dtypes(include=['object','string']).columns
numcols = copy.select_dtypes(include='number').columns

print(copy[objectscol].mode())

copy[numcols] = copy[numcols].apply(pd.to_numeric,errors='coerce')
copy[numcols] = copy[numcols].fillna(copy[numcols].mean())
copy[objectscol] = copy[objectscol].fillna(copy[objectscol].mode().iloc[0])

print(copy.isna().sum())
print(copy)

print(copy.duplicated().sum())
copy = copy.drop_duplicates(keep='first')

