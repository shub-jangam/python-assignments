import pandas as pd
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)
print(df)
df['Gender'] = ['Male' ,'Male', 'Female']

df_encoded = pd.get_dummies(df, columns=['Gender'], drop_first=True)
print(df_encoded)