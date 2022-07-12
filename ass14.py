import schedule
import time
from sys import argv
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def Play_Predictor(path=argv[1]):
    df = pd.read_csv(path)
    label_encoder = preprocessing.LabelEncoder()

    df['Wether'] = label_encoder.fit_transform(df['Wether'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
    df['Play'] = label_encoder.fit_transform(df['Play'])


    data = pd.concat([df['Wether'],df['Temperature']],axis=1)
    target = df['Play']

    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size=0.3)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf = clf.fit(data_train,target_train)

    result = clf.predict(data_test)  

    Accuracy = accuracy_score(target_test,result)
    print("Accuracy is "+str(Accuracy*100)+"%"+" at time "+str(time.ctime()))

def main():
    print("-----Abhishek Dahiphale---")
    print("Name of the Application : "+argv[0])

    if(len(argv)!=2):
        print("Invalid Number of arguments")
        exit()

    if(argv[1]=='-h') or (argv[1]=='-H'):
        print("Help : Apllication is used for the Play prediction")
        exit()

    if(argv[1]== '-u') or (argv[1]=='-U'):
        print("Usage : Application_name CSV_FilePath ")
        exit()

    if(len(argv)==2):
        try:
            Play_Predictor(argv[1])
            """schedule.every(1).minute.do(Play_Predictor)
            while True:
                schedule.run_pending()
                time.sleep(1)"""

        except Exception as e:
            print("Error : ",e)


if __name__ == "__main__":
    main()    



