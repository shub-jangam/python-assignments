import pandas as pd
data = {
    'Salary' :[25000, 27000, 29000, 31000, 50000, 100000]
}

df =  pd.DataFrame(data)
print(df)

Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
iqr = Q3 - Q1

lower_bound = Q1 - 1.5 * iqr
upper_bound = Q3 + 1.5 * iqr

outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print(outliers)
