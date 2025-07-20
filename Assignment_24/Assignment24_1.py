import pandas as pd
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)
print(df)

df['Math'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

print(df)