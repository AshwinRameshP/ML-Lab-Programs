# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 06:39:12 2019

@author: PlayGOD
"""
import numpy as np
import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
names=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','heartdisease']
heartDisease=pd.read_csv('heart.csv',names=names)
heartDisease=heartDisease.replace('?',np.nan)
model=BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),('exand','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),('heartdisease','thalach'),('heartdiseae','chol')])
model.fit(heartDisease,estimator=MaximumLikelihoodEstimator)
HeartDisease_infer=VariableElimination(model)
q=HeartDisease_infer.query(variables=[])
