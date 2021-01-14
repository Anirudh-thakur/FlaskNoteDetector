import pandas as pd
import numpy as np 

df = pd.read_csv('BankNote_Authentication.csv')
print(df.head())

#Independent variables (All except last)
X = df.iloc[:,:-1]
#Dependent variable (only last)
Y = df.iloc[:,-1]

print(X.head())
print(Y.head())

#Splitting test and train data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

#implement random forest classifier 
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train,Y_train)

#Prediction 
y_pred=classifier.predict(X_test)

#Accuracy 
from sklearn.metrics import accuracy_score
score = accuracy_score(Y_test,y_pred)
print(score)

#Saving classifier in pickle file 
import pickle
pickle_out = open("classifier.pkl","wb")
pickle.dump(classifier,pickle_out)
pickle_out.close()
print(classifier.predict([[1,2,3,4]]))