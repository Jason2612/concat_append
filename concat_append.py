import pandas as pd
df = pd.read_csv('data\FoodPrice_in_Turkey.csv')
df1 = df.loc[0:4999,:]
df2 = df.loc[5000:7300,:]

df3 = df.loc[1000:2000,['ProductId','Place','Month','Year','Price']]
df4 = pd.concat([df1,df2], axis=0)
df5 = pd.concat([df1,df2,df3], axis=0)
df6 = df1.append(df2)
df7 = df1.append(df3)
print(df7)