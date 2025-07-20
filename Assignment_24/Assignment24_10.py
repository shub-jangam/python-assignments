import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}

sns.boxplot(data=data['English'], color='lightcoral')
plt.title('Boxplot of English Marks')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()