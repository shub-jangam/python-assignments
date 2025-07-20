import pandas as pd
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)


df['Total'] = df['Math'] +df['Science']+ df['English']
print("Existing DF")
print(df)

print("Sorted DF in Decending Order")
df_sorted =df.sort_values(by= ('Total'), ascending= False)
print(df_sorted)