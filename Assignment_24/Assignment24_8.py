import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Name' : ['Amit', 'Sagar','Pooja'],
    'Math':[85,90,78],
    'Science' :[92,88,80],
    'English': [75,85,88]
    
}

plt.figure(figsize=(10, 6))

plt.hist(data['Math'], bins=5, alpha=0.5, label='Math')

plt.xlabel('Scores')
plt.ylabel('Number of Students')
plt.title('Histogram of Subject Scores')
plt.legend()

# Show the plot
plt.show()
