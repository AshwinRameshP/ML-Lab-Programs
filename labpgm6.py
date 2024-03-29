# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:48:24 2019

@author: CSE
"""

import pandas as pd
msg=pd.read_csv('naivetext1.csv',names=['message','label'])
print("The dimensions of dataset",msg.shape)
msg['labelnum']=msg.label.map({'pos':1,'neg':0})
X=msg.message
Y=msg.labelnum
print(X)
print(Y)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,Y)
print(xtest.shape)
print(xtrain.shape)
print(ytest.shape)
print(ytrain.shape)

from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer()
xtrain_dtm=count_vect.fit_transform(xtrain)
xtest_dtm=count_vect.transform(xtest)

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB().fit(xtrain_dtm,ytrain)
predicted=clf.predict(xtest_dtm)

from sklearn import metrics
print("Accuracy metrics")
print("Accuracy of classifier is",metrics.accuracy_score(ytest,predicted))
print("Confusion Matrix")
print(metrics.confusion_matrix(ytest,predicted))
print("Recall and Precision")
print(metrics.recall_score(ytest,predicted))
print(metrics.precision_score(ytest,predicted))
