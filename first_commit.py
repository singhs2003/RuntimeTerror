!/usr/bin/env python

#------------------------------------------------------------
#PATIENT MONITORING SYSTEM
#MADE BY SAKSHAM SINGH, MAIT
#        ISHAAN SANGWAN, MAIT
#DATE: 22/12/22
#---------------------------------------------------------

""" This code cleans the data set we got from kaggle" of over a 1000 records""

import pandas as pd
import numpy as np

data=pd.read_excel('dataset.xlsx')

data.shape

data.isnull().sum()

data.describe()

data['heart rate']=data['heart rate'].fillna(data['heart rate'].mean()) 
data['Pulse']=data['Pulse'].fillna(data['Pulse'].mean())
data['temperature']=data['temperature'].fillna(data['temperature'].mean())
data['Systolic blood pressure']=data['Systolic blood pressure'].fillna(data['Systolic blood pressure'].mean())
data['Diastolic blood pressure']=data['Diastolic blood pressure'].fillna(data['Diastolic blood pressure'].mean())
data['Respiratory rate']=data['Respiratory rate'].fillna(data['Respiratory rate'].mean())
data['SP O2']=data['SP O2'].fillna(data['SP O2'].mean())
data['PH']=data['PH'].fillna(data['PH'].mean())
data['PCO2']=data['PCO2'].fillna(data['PCO2'].mean())
data['outcome']=data['outcome'].fillna(data['outcome'].min())


data.isnull().sum()

X=data.drop('outcome',axis=1)
Y=data['outcome']
