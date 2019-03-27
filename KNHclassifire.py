from sklearn import datasets #import datasets from sklearn

iris= datasets.load_iris() #getting data set iris flower
#print (iris)

data=iris.data#data- faatuers 150*4 2d array
target=iris.target##lables 

#print(data)
#print(target)

import numpy as np

train_data=np.delete(data,[0,50,100],axis=0)#delete 1 51 and 100 datas(use axis because 2d array)
#print(train_data)

train_target=np.delete(target,[0,50,100])#not use axis becaue 1d array
#print(train_target)

from sklearn.neighbors import KNeighborsClassifier #import KNN calssifier

clsfr= KNeighborsClassifier()#loading the KNN to clasf

clsfr.fit(train_data , train_target)#training the KNN model

test_data=data[[0,50,100]]
test_target=target[[0,50,100]]

result=clsfr.predict(test_data)

print("Predicted Result is: " , result)
print("Actual Result is: " , test_target )

#print(test_data)
#print(test_target)
