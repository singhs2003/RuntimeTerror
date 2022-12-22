!/usr/bin/env python
"""
	
******************************************** PATIENT MONITORING SYSTEM *********************************************                                                                                                                       
                                                                                                                       
HHHHHHHHH     HHHHHHHHH                                 AAA               lllllll                                      
H:::::::H     H:::::::H                                A:::A              l:::::l                                      
H:::::::H     H:::::::H                               A:::::A             l:::::l                                      
HH::::::H     H::::::HH                              A:::::::A            l:::::l                                      
  H:::::H     H:::::H      eeeeeeeeeeee             A:::::::::A            l::::l    ggggggggg   ggggg   ooooooooooo   
  H:::::H     H:::::H    ee::::::::::::ee          A:::::A:::::A           l::::l   g:::::::::ggg::::g oo:::::::::::oo 
  H::::::HHHHH::::::H   e::::::eeeee:::::ee       A:::::A A:::::A          l::::l  g:::::::::::::::::go:::::::::::::::o
  H:::::::::::::::::H  e::::::e     e:::::e      A:::::A   A:::::A         l::::l g::::::ggggg::::::ggo:::::ooooo:::::o
  H:::::::::::::::::H  e:::::::eeeee::::::e     A:::::A     A:::::A        l::::l g:::::g     g:::::g o::::o     o::::o
  H::::::HHHHH::::::H  e:::::::::::::::::e     A:::::AAAAAAAAA:::::A       l::::l g:::::g     g:::::g o::::o     o::::o
  H:::::H     H:::::H  e::::::eeeeeeeeeee     A:::::::::::::::::::::A      l::::l g:::::g     g:::::g o::::o     o::::o
  H:::::H     H:::::H  e:::::::e             A:::::AAAAAAAAAAAAA:::::A     l::::l g::::::g    g:::::g o::::o     o::::o
HH::::::H     H::::::HHe::::::::e           A:::::A             A:::::A   l::::::lg:::::::ggggg:::::g o:::::ooooo:::::o
H:::::::H     H:::::::H e::::::::eeeeeeee  A:::::A               A:::::A  l::::::l g::::::::::::::::g o:::::::::::::::o
H:::::::H     H:::::::H  ee:::::::::::::e A:::::A                 A:::::A l::::::l  gg::::::::::::::g  oo:::::::::::oo 
HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeeeAAAAAAA                   AAAAAAAllllllll    gggggggg::::::g    ooooooooooo   
                                                                                              g:::::g                  
                                                                                  gggggg      g:::::g                  
                                                                                  g:::::gg   gg:::::g                  
                                                                                   g::::::ggg:::::::g                  
                                                                                    gg:::::::::::::g                   
                                                                                      ggg::::::ggg                     
                                                                                         gggggg                        
                                                                                         
***********************************************************************************************************************************
Machine learning algortihm to read data from patient and monitor them constantly and if the stats are in the danger zone 
it return a value 1 which will be deocoded and immediately conveyed to doctor and staff on duty.
************************************************************************************************************************************

##############################################################     PATIENT MONITORING SYSTEM     #######################################################################
#MADE BY :SAKSHAM SINGH, MAIT , 2nd Yr.
#        :ISHAAN SANGWAN, MAIT , 2nd Yr.
#        :DATE: 22/12/22
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                        """ This code cleans the data set we got from kaggle of  1000+ records"""
"""
#importing libraries.
import pandas as pd
import numpy as np

#Importing the dataset
data=pd.read_excel('dataset.xlsx')#commited in same repository
data.shape
data.isnull().sum()
data.describe()

#Checking For Null Values , here we are concerned about cleaning of data.
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
