# -*- coding: utf-8 -*-
"""Sonar rock vs mine project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ml965l3ZO-Rby0F42MvID4T5y_DnhGGg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'/content/drive/MyDrive/Machine Learning Projects/Sonar rock vs mine project/sonar data.csv')

df.head()

df.info()

df.shape

df.info()

df['R'].value_counts()

""" M -> Mine   
 R -> Rock
"""

df.groupby('R').mean()

# X and y
X = df.drop('R',axis=1)
y = df['R']

from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

print(X)

print(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_train.shape, X_test.shape

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Modelling
#Training the logistic regression model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train,y_train)

#Predicting New Result
y_pred = classifier.predict(X_test)
y_pred

#Evaluating the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

#Accuracy of model
#from sklearn.metrics import accuracy_score
#print('Accuracy of my model on testing set :' ,accuracy_score(y_test,y_pred))

#This is to get the Models Accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

#This is to get the Classification Report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
cr

# Training the Random Forest Classification model on the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
#classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)