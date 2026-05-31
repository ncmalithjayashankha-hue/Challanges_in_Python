import pandas as pd

df = pd.read_csv("employees.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df['Salary'].mean())
print()
print(df['Department'] == 'IT')
print()
print(df.sort_values(by='Salary', ascending=False))
print()
print(df.loc[df["Salary"].idxmin()])
print()
df['Bonus'] =  df['Salary'] *0.1
print(df)
