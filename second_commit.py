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


Machine learning algortihm to read data from patient , and  monitor them constantly and if the stats are in the danger zone or some abnormality is witnessed ,
it return a value 1 which will be later read , and communicated to staff so they can take proper measures to inform the staff

************************************************************************************************************************************

MADE BY :
	SAKSHAM SINGH, MAIT
	ISHAAN SANGWAN, MAIT
	
Date: 	22/12/2022
*******************************************************************************************************************************
	
"""
#to split array or data in train and test part
from sklearn.model_selection import train_test_split  
#declaring variables for the same
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)



#from sklearn importing different models which will power the the algorithm and then we will check them for accuracy.

# It standardizes features by subtracting the mean value from the feature and then dividing the result by feature standard deviation.i.e
#values differ in range or are in different units.
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
#For creating pipeline
from sklearn.pipeline import Pipeline


#  creating a machine learning pipeline for standarising the raw data , we are doing for all models to test them seperately for accuracy.


pipeline_lr=Pipeline([('scalar1',StandardScaler()),('lr_classifier',LogisticRegression())])
pipeline_knn=Pipeline([('scalar2',StandardScaler()),('knn_classifier',KNeighborsClassifier())])
pipeline_svc=Pipeline([('scalar3',StandardScaler()),('svc_classifier',SVC())])
pipeline_dt=Pipeline([('dt_classifier',DecisionTreeClassifier())])
pipeline_rf=Pipeline([('rf_classifier',RandomForestClassifier())])
pipeline_gbc=Pipeline([('gbc_classifier',GradientBoostingClassifier())])


# list of pipelines
pipelines=[pipeline_lr,pipeline_knn,pipeline_svc,pipeline_dt,pipeline_rf,pipeline_gbc]

# train pipelines
for pipe in pipelines:
    pipe.fit(X_train,Y_train)
    
# pipe_dict 
# Logisticregression,KNeighborsClassifier,SVC,DecisionTreeClassifier,RandomForestClassifier,GradientBoostingClassifier
pipe_dict={0:'LR',1:'KNN',2:'SVC',3:'DT',4:'RF',5:'GBC'}

for i,model in enumerate(pipelines):
    print("{}Test Accuracy:{}".format(pipe_dict[i],model.score(X_test,Y_test)*100))
#Now we have got our accuracy of all models we compared and found RandomForestClassifier to best suit our model.

#So now train it over whole data
from sklearn.ensemble import RandomForestClassifier

X=data.drop('outcome',axis=1)
Y=data['outcome']

rf=RandomForestClassifier()
rf.fit(X,Y)


