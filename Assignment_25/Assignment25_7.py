import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    'Age' : [18,22,25,30,35]
}

df = pd.DataFrame(data)
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

print(df)

