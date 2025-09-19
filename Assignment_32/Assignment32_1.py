import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier

def predictRealFakeNewsArticle(fakeNewsArticlePath,realNewsArticlePath):

    # load the data
    fake_df =pd.read_csv(fakeNewsArticlePath)
    real_df = pd.read_csv(realNewsArticlePath)

    # Check the missing values before addeing lable
    print("Check of Missing values")
    print(fake_df.isnull().sum())
    print(50* "--")

    print("Check of Missing values")
    print(real_df.isnull().sum())
    print(50* "--")

    # drop unnessary columns
    fake_df = fake_df.drop(columns=['subject','date','title'])
    real_df = real_df.drop(columns=['subject','date','title'])

    # Set Lable for Fake and real df
    fake_df['lable'] = 0
    real_df ['lable'] = 1
    
    #Create dataset
    df = pd.concat([fake_df, real_df], ignore_index=True, axis=0)
    
    print("print Dataset Dimension " , df.shape)
    print(50* "--")
    print(df.head())
    print(50* "--")
 
    # preprocessing the text
    df['text'] = df['text'].apply(preprocess)

    X = df['text']  # Use just the cleaned text column
    Y = df['lable']

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Fit TF-IDF on training text, transform both train and test
    tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
    x_train_tfidf = tfidf.fit_transform(x_train)
    x_test_tfidf = tfidf.transform(x_test)    

    #Train the model - LogisticRegression
    model1 = LogisticRegression(max_iter=1000)
    model2 = DecisionTreeClassifier(random_state=42)
        
    voting_clf_hard = VotingClassifier(estimators=[
        ('lr', model1),('nb', model2)],
        voting='hard')
    
    voting_clf_soft = VotingClassifier(estimators=[
        ('lr', model1),('nb', model2)], voting='soft')
    
    voting_clf_hard.fit(x_train_tfidf, y_train)
    y_pred_hard = voting_clf_hard.predict(x_test_tfidf)

    print("Hard Voting Classifier Accuracy:", accuracy_score(y_test, y_pred_hard))
    print(classification_report(y_test, y_pred_hard))

    voting_clf_soft.fit(x_train_tfidf, y_train)
    y_pred_soft = voting_clf_soft.predict(x_test_tfidf)

    print("Soft Voting Classifier Accuracy:", accuracy_score(y_test, y_pred_soft))
    print(classification_report(y_test, y_pred_soft))
    
# Basic text cleaning function
def preprocess(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'\W', ' ', text)  # Remove non-word characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    return text.strip()

def main():
    predictRealFakeNewsArticle(fakeNewsArticlePath="Fake.csv",realNewsArticlePath="True.csv")

if __name__ == "__main__":
    main()