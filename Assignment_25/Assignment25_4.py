import pandas as pd
data = {
    'dept' : ['HR', 'IT','Finance', 'HR', 'IT'],
}

df =  pd.DataFrame(data)
print(df)
df_encoded = pd.get_dummies(df, columns=['dept'])
print(df_encoded)