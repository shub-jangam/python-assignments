import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import seaborn as sns
from seaborn import countplot
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score, confusion_matrix

def breastCancerPreditor(filePath):
    df = pd.read_csv(filePath)
    print("print Dataset Dimension " , df.shape)
    print(50* "--")
    print(df.head())
    print(50* "--")
    
    df = df.drop(columns=['CodeNumber'])

    print("Check of Missing values")
    print(df.isnull().sum())
    print(50* "--")


    print("Stat describe")
    print(df.describe())
    print(50* "--")
    
    # figure()
    # target = "CancerType"
    # countplot(data = df, x = target).set_title("Subscribe VS Not Subscribe")
    # show()

    print("Check of Missing values")
    print(df.isnull().sum())
    print(50* "--")

    dummy_values = ['?']
    print("Dummy value counts per column:")
    dummy_columns = []
    for col in df.columns:
        if df[col].dtype == 'object':
            dummies = df[col].isin(dummy_values)
            count = dummies.sum()
            if count > 0:
                dummy_columns.append(col)
                print(f"{col}: {count} dummy values") 

    # Less Number of rows so deleteting the row
    for col in dummy_columns:
        dummy_index = df[df[col] == '?'].index
        df = df.drop(dummy_index)
    
    print(50* "--")

    X = df.drop('CancerType', axis=1)
    Y = df['CancerType']

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)

    print("Random Forest Classifier")
    rfc_model = RandomForestClassifier(n_estimators=150, max_depth= 7, random_state=42)
    rfc_model.fit(x_train,y_train)
    rfc_pred = rfc_model.predict(x_test)
    print("Accuracy is : ",accuracy_score(y_test,rfc_pred)*100)

    print("Gradient Boosting Classifier")
    # Initialize the model
    gbc_model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    gbc_model.fit(x_train, y_train)
    gbc_pred = gbc_model.predict(x_test)
    accuracy = accuracy_score(y_test, gbc_pred)
    print(f"Accuracy: {accuracy:.2f}")

    print("DecisionTreeClassifier")
    dtc_model = DecisionTreeClassifier(max_depth=3, random_state=42)
    dtc_model.fit(x_train,y_train)
    dtc_pred = dtc_model.predict(x_test)
    print("Accuracy is : ",accuracy_score(y_test,dtc_pred)*100)

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Decision Tree confusion matrix
    sns.heatmap(confusion_matrix(y_test, rfc_pred), annot=True, fmt='d', cmap='Blues', ax=ax[0])
    ax[0].set_title("Decision Tree Confusion Matrix")
    ax[0].set_xlabel("Predicted")
    ax[0].set_ylabel("Actual")

    # Gradient Boosting confusion matrix
    sns.heatmap(confusion_matrix(y_test, gbc_pred), annot=True, fmt='d', cmap='Greens', ax=ax[1])
    ax[1].set_title("Gradient Boosting Confusion Matrix")
    ax[1].set_xlabel("Predicted")
    ax[1].set_ylabel("Actual")

    plt.tight_layout()
    plt.show()


def main():
    breastCancerPreditor(filePath= "breast-cancer-wisconsin.csv")

if __name__ == "__main__":
    main()