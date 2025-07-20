import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)

result = df.loc[df['Name'] == 'Sagar']
print(result)
marks = result.drop(columns=['Name'])

plt.pie(marks, labels = marks.columns)
plt.show() 
