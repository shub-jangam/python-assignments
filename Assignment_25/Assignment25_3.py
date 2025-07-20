import pandas as pd
data = {
    'city' : ['Pune', 'Mumbai','Delhi', 'Pune', 'Delhi'],
}

df =  pd.DataFrame(data)
print(df)

df['city'] = pd.factorize(df['city'])[0]

print(df)