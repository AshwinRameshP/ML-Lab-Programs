# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:44:06 2019

@author: PlayGOD
"""

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


#load dataset-iris
iris=datasets.load_iris()
print("Loaded Iris dataset..")

xTrain,xTest,yTrain,yTest=train_test_split(iris.data,iris.target,test_size=0.1)
print("Splitting dataset into test & train sets..")
print("Size of training data and label :",xTrain.shape,yTrain.shape)
print("Size of testing data and label :",xTest.shape,yTest.shape)

for i in range(len(iris.target_names)):
    print("Label ",i ,"-",iris.target_names[i])

classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(xTrain,yTrain)
ypred=classifier.predict(xTest)

print("Results of classification using knn with n=1")

for r in range(len(xTest)):
    print("Sample ",xTest[r],"-Actual Label:",yTest[r]," Predicted Label:",ypred[r])

print("Classification Accuracy is ",classifier.score(xTest,yTest))

