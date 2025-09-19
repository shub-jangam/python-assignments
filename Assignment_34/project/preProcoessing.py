import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def preprocess_data(df):
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(df.drop('target', axis=1))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    return X_scaled, df['target']

def perform_eda(df):
    print(df.describe())
    plt.figure(figsize=(14, 10))
    corr = df.corr()
    sns.heatmap(corr, annot=False, cmap='coolwarm', fmt='.2f')
    plt.title('Feature Correlation Heatmap')
    plt.show()
