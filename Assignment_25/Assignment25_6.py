import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Grade' : ['A+','B','A','C','B+']
}

df = pd.DataFrame(data)
mapping = {'A+': 'Excellent', 'A': 'Very Good', 'B+':'Good','B':'Average','C':'Poor'}
df['Grade'] = df['Grade'].replace(mapping)
print(df)

