import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}
df = pd.DataFrame(data)


result = df.loc[df['Name'] == 'Amit']
marks = result.drop(columns=['Name'])


plt.plot(result['Name'],marks, linestyle = 'dotted')
plt.show()