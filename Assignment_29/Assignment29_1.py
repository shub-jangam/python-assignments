import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def predictDiabetes(filePath):
    df = pd.read_csv(filePath)
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

    print("Correlation Matrix")
    print(df.corr())

    plt.figure(figsize = (10,5))
    sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    plt.show()

    
    X = df.drop(columns = ['Outcome'])
    Y = df['Outcome']

    print(X.shape)
    print(Y.shape)
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = LogisticRegression().fit(X_train,Y_train)

    print("Training Accuracy : ")
    print(model.score(X_train,Y_train))

    print("Testing Accuracy : ")
    print(model.score(X_test,Y_test))

def main():
    predictDiabetes(filePath= "diabetes.csv")

if __name__ == "__main__":
    main()