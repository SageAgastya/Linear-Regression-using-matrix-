import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

class LinearRegression:
#class was not needed at  all, look at the constructor. it is doing nothing..
#but I belong to OOP background so I preferred to use it.
    def __init__(self):
        pass
        #no use of _init_()

    def train(self,X,Y):   #how to train
        param=inv(X.T.dot(X)).dot(X.T).dot(Y)
        return param

    def test(self,X,param): #testing X with best fit slope
        hox=X.dot(param)
        return hox

#main
lr=LinearRegression()   #creating object
data=np.array([
    [2,4],
    [1,1],
    [5,3],
  [10,14],
    [7,3],
    ])
X=data[:,0]
y=data[:,1]
print X
print y
X=X.reshape(len(X),1)
print X
grad=lr.train(X,y)
yp=lr.test(X,grad)
print yp
plt.scatter(X,y)
plt.plot(X,yp,"r")
plt.show()

        
        
