!/usr/bin/env python

#------------------------------------------------------------
##############################################################     PATIENT MONITORING SYSTEM     #######################################################################
#MADE BY :SAKSHAM SINGH, MAIT , 2nd Yr.
#        :ISHAAN SANGWAN, MAIT , 2nd Yr.
#        :DATE: 22/12/22
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                        """ This code cleans the data set we got from kaggle of  1000+ records"""
#importing libraries.
import pandas as pd
import numpy as np

#Importing the dataset
data=pd.read_excel('dataset.xlsx')#commited in same repository
data.shape
data.isnull().sum()
data.describe()

#Checking For Null Values.
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

#Here we divided the columns into X and Y variables so as to  begin our training and testing operations.
X=data.drop('outcome',axis=1)
Y=data['outcome']
