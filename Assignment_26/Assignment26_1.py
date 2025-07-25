import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 


def PlayPredictor(csvFilePath):
    df = pd.read_csv(csvFilePath) 
    print("Dataset loaded succesfully !! ")
    print("Dimentions of dataset is : ",df.shape)
    print(30*'-')
    print(df.head())
    
    # # Drop Column unnamed 
    df.drop(columns=['Unnamed: 0'], inplace=True)
    # print("After Droping the column")
    # print(df.head())

    # Check for Missing values 
    print(30*'-')
    print("Missing values in each column", df.isnull().sum())
    print(30*'-')


    sns.countplot(x='Temperature', hue='Play', data=df)
    plt.title("Go Out by Temperature")
    plt.show()

    sns.countplot(x='Whether', hue='Play', data=df)
    plt.title("Go Out by Temperature")
    plt.show()

    # Dataset have Text info so we need to find in Unqiue set values 
    print('Unqiue values for Each of the column : Whether') 
    Whether_list = df['Whether'].unique()
    #print(Whether_list)
    #print(30*'-')
    #print('Unqiue values for Each of the column : Temperature') 
    temp_list = df['Temperature'].unique()
    #print(temp_list)

    unique_combinations_df = df[['Whether', 'Temperature' ,'Play']].drop_duplicates()
    #print(unique_combinations_df.sort_values(by=['Whether','Temperature']))

    # Convert this Text value in to Number for machine learning models
    # lable Encoding
    df['Whether'] = pd.factorize(df['Whether'])[0]
    df['Temperature'] = pd.factorize(df['Temperature'])[0]
    mapping = {'Yes':1 ,'No':0}
    df['Play'] = df['Play'].replace(mapping)
    #print(df.head())
    # train_test_split and Modle creation 
    x = df.drop('Play', axis=1)
    y = df['Play']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    modle = KNeighborsClassifier(n_neighbors = 3)
    modle.fit(x_train,y_train)
    y_predict = modle.predict(x_test)
    accuracy = accuracy_score(y_test,y_predict)

    print("modle accuracy is" , accuracy)

    def predict_go_out(temp_input, whether_input):
        temp_mapping =  {'hot':0, 'mid' :1 ,'cool':2}
        whether_mapping = {'sunny':0,'overcast':1,'Rainy':2}
        play_mapping = {1 : 'Yes', 0 :'No'}
        temp_encoded = temp_mapping.get(temp_input)
        whether_encoded = whether_mapping.get(whether_input)
        input_data = pd.DataFrame([[whether_encoded,temp_encoded]],
                       columns=['Whether','Temperature'])
        pred = modle.predict(input_data)[0]
        return play_mapping.get(pred)
    
    print("ML modle to predict to play based on the Whether And Temperature ")
    print("Enter Temp values such as hot , mid ,cool ")
    temp = input ()
    print("Enter Temp values such as sunny , overcast ,Rainy ")  
    wether = input()
    result = predict_go_out(temp ,wether)
    print("You can play ? ", result)

    ## To Check the value of K 
    # accuracy_scores= []
    # k_range = range(1,21)
    # for i in k_range:
    #     modle = KNeighborsClassifier(n_neighbors=i)
    #     modle.fit(x_train,y_train)
    #     y_predict = modle.predict(x_test)
    #     accuracy = accuracy_score(y_test,y_predict)
    #     accuracy_scores.append(accuracy)

    # plt.figure(figsize=(10,6))
    # plt.plot(k_range ,accuracy_scores , marker= 'o',linestyle = "--")
    # plt.xlabel("Values of K")
    # plt.ylabel("Values of accuracy")
    # plt.grid(True)
    # plt.show()
    # best_k = k_range[accuracy_scores.index(max(accuracy_scores))]
    # print("Best Value of k ",best_k)
    
def main():
    PlayPredictor("Playpredictor.csv")   
if __name__ == "__main__":
    main()