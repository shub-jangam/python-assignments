import pandas as pd
data = {
    'Name' : ['A','B','C'],
    'Age' :[21.0,22.0,23.0]
}

df =  pd.DataFrame(data)
print(df)
df['Age'] = df['Age'].astype(int)

print(df)