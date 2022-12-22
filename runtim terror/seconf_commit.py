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
it return a value 1 which will be later read and take proper measures to inform the staff
************************************************************************************************************************************
MADE BY :
	SAKSHAM SINGH, MAIT
	ISHAAN SANGWAN, MAIT
	
Date: 	22/12/2022
*******************************************************************************************************************************
	
"""
import first_commt
from sklearn.model_selection import train_test_split  

#to split array or data in train and test part


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)



# to create pipeline output of one step as input in nxt step , diff classificatn models
#from sklearn import preprocessing

from sklearn.preprocessing import StandardScaler

# It standardizes features by subtracting the mean value from the feature and then dividing the result by feature standard deviation.i.e
#values differ in range or are in different units.


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


# grouping of items eclidean distance column in table assume k=3

from sklearn.svm import SVC

# sets plane between two categories so that dist between pts of both categories is max

from sklearn.tree import DecisionTreeClassifier

# classes may not be seperable by a linear line , it decides line by fact that try to maximizes inf ogain we want pure node, calculates entroy
#info gain entropy of prent - entropy of child so higher info gain is favoured and model compares every possible
#to max info gain splits recursively to 

from sklearn.ensemble import RandomForestClassifier

# better than decision tree 

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.pipeline import Pipeline


#  creating a machine learning pipeline for standarising the raw data 


pipeline_lr=Pipeline([('scalar1',StandardScaler()),('lr_classifier',LogisticRegression())])
pipeline_knn=Pipeline([('scalar2',StandardScaler()),('knn_classifier',KNeighborsClassifier())])
pipeline_svc=Pipeline([('scalar3',StandardScaler()),('svc_classifier',SVC())])
pipeline_dt=Pipeline([('dt_classifier',DecisionTreeClassifier())])
pipeline_rf=Pipeline([('rf_classifier',RandomForestClassifier())])
pipeline_gbc=Pipeline([('gbc_classifier',GradientBoostingClassifier())])


# list for pipelines
pipelines=[pipeline_lr,pipeline_knn,pipeline_svc,pipeline_dt,pipeline_rf,pipeline_gbc]


pipelines

# train pipelines
for pipe in pipelines:
    pipe.fit(X_train,Y_train)
    

pipe_dict={0:'LR',1:'KNN',2:'SVC',3:'DT',4:'RF',5:'GBC'}


# pipe_dict 
# Logisticregression,KNeighborsClassifier,SVC,DecisionTreeClassifier,RandomForestClassifier,GradientBoostingClassifier


for i,model in enumerate(pipelines):
    print("{}Test Accuracy:{}".format(pipe_dict[i],model.score(X_test,Y_test)*100))


from sklearn.ensemble import RandomForestClassifier

X=data.drop('outcome',axis=1)
Y=data['outcome']

rf=RandomForestClassifier()


rf.fit(X,Y)


data.columns

