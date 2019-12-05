# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:39:34 2019

@author: PlayGOD
"""
import csv

hypo=['%','%','%','%','%','%']
with open('train.csv') as csv_file:
    readcsv=csv.reader(csv_file,delimiter=',')
    data=[]
    print("\nThe given training examples are:")
    for row in readcsv:
        print(row)
        if row[len(row)-1].upper()=="YES":
            data.append(row)
print("\nThe positive examples are:")
for x in data:
    print(x)
print("\n")
TotalExamples=len(data)
d=len(data[0])-1

print("The steps of the Find-s algorithm are\n",hypo)

for j in range(d):
    hypo[j]=data[0][j]  #initializing
for i in range(TotalExamples):
    for k in range(d):
        if(hypo[k]!=data[i][k]):
            hypo[k]='?'
            
    print(hypo)
print("The maximally specific Find-s hypothesis for the given training example is")
print(hypo)
