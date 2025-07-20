import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

data = {
    'marks' : [85,np.nan,90, np.nan,95]
}

df = pd.DataFrame(data)
print(df)
df['marks'] = df['marks'].interpolate()
print(df)

