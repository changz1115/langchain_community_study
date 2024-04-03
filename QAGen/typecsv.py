import pandas as pd
df = pd.read_csv('D:/project/langchain_community_study/QAGen/Data.csv', sep=',')
# df = pd.read_table('D:/project/langchain_community_study/QAGen/Data.csv')
print(df.head())
# print(df._data[0])
print(df.columns.tolist())

df.head() #默认显示前10行
df.tail() #默认显示后10行

print('print(df.values)')
print(df.values)
print(df['question'].values[1])