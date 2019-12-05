# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:39:57 2019

@author: PlayGOD
"""

import csv
import math
def mean(numbers):
    return sum(numbers)/float(len(numbers))
def stddev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2)for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)
def summarize(dataset):
    summaries=[(mean(attributes),stdev(attribute))for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries
def calcProb(summary,item):
    prob=1
    for i in range(len(summary)):
        x=item[i]
        mean,stdev=summary[i]
        exponent=math.exp(-math.pow(x-mean,2)/(2*math.pow(stdev,2)))
        final=exponent/(math.sqrt(2*math.pi)*stdev)
        prob*=final
    return prob
with open('Pgm5_DS.csv') as csvFile:
    data=[line for line in csv.reader(csvFile)]