import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data = {
    'marks' : [45,67,88,32,76]
}

df = pd.DataFrame(data)
print(df)
# Interpolate missing values in 'col1'
result = df.where(df['marks']>50)
df_replaced = result.replace(np.nan,'fail')

print(df_replaced)
