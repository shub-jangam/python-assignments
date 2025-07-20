import pandas as pd
from sklearn.model_selection import train_test_split
data = {
    'Age' : [22,25, 47, 52, 46, 56],
    'purchased':[0,1,1,0,1,1]
}

df = pd.DataFrame(data)

x_train , x_test , y_train, y_test = train_test_split(df['Age'],df['purchased'], test_size=0.2, random_state=42)

print("x_train", )
print(x_train)
print("x_test")
print(x_test)
print("y_train")
print(y_train)
print("y_test")
print(y_test)