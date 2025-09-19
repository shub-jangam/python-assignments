import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn as sns
from seaborn import countplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import  accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def depositeSubcriptionPreditor(filePath):
    df = pd.read_csv(filePath,sep=';')
    print("print Dataset Dimension " , df.shape)
    print(50* "--")
    print(df.head())
    print(50* "--")

    print("Check of Missing values")
    print(df.isnull().sum())
    print(50* "--")

    print("Stat describe")
    print(df.describe())
    print(50* "--")
    
    columns_to_encode = ['job', 'marital', 'education', 'default', 'housing', 'loan', 
                     'contact', 'month', 'poutcome', 'y']

    le = LabelEncoder()
    for col in columns_to_encode:
        df[col] = le.fit_transform(df[col])


    figure()
    target = "y"
    countplot(data = df, x = target).set_title("Subscribe VS Not Subscribe")
    show()

    x = df.drop(columns = ['y'])
    y = df['y']

    print("Dimentiones of Target : ",x.shape)
    print("Dimentiones of Labels : ",y.shape)

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_scale, y, test_size = 0.2, random_state = 42)

    model = LogisticRegression()
    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    cm = confusion_matrix(y_test,y_pred)

    print("Accuracy is : ",accuracy)
    print("Confusion matrix : ")
    print(cm)


def main():
    depositeSubcriptionPreditor(filePath= "bank-full.csv")

if __name__ == "__main__":
    main()