# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 05:56:57 2019

@author: PlayGOD
"""

import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
concept = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

def train1(con,tar):
    specific_h = con[0].copy()
    general_h=[['?' for _ in range(len(specific_h))] 
    for _ in range(len(specific_h))]
    
    for i,val in enumerate(con):
        if tar[i].lower() == 'yes':
            for x in range(len(specific_h)):
                if(val[x] != specific_h[x]):
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        else:
            for x in range(len(specific_h)):
                if val[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x]='?'
                    
        print("Iteration["+ str(i+1) + "]")
        print("Specific: "+str(specific_h))
        print("General: "+str(general_h)+"\n\n")
    
    general_h =[general_h[i] for i, val in enumerate(general_h) if val!= ['?' for x in range(len(specific_h))]]
    return specific_h, general_h

specific , general = train1(concept,target)
print("Final hypothesis: ")
print("Specific hypothesis: " +str(specific))
print("General hypothses: "+ str(general))