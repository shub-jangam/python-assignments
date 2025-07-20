import pandas as pd
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)
df['Total'] = df['Math'] +df['Science']+ df['English']

# Add a new column named 'Price'
df['Status'] = ['Pass' if x > 250 else 'fail' for x in df['Total']]

print("Number student pass ",len(df.loc[df['Status'] == 'Pass']))

