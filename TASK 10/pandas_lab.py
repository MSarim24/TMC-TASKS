import pandas as pd

df = pd.read_csv('sales.csv')

print(df[(df['Sales Channel'] == 'Online') & (df['Item Type'] == 'Baby Food')])

print(df.iloc[10:15])

print(df.head(5))

print(df.info())

print(df.describe())

print(df.dtypes)

print(df.sort_values(by='Total Profit',ascending=False).head(10))