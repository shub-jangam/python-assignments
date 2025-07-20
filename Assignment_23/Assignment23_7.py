import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)
print(df)

df['Total'] = df['Math'] +df['Science']+ df['English']

# plt.figure(figsize=(8,4))
# plt.plot(df['Name'] , df['Total'])
# plt.xlabel("Names for Student ")
# plt.ylabel("total marks")
# plt.grid(True)
# plt.show()


sns.barplot(x=df['Name'], y=df['Total'])
plt.title('Basic Bar Plot with Seaborn')
plt.show()