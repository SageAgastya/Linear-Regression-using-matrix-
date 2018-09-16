# Linear-Regression-using-matrix-
Linear Regression with matrix transpose and inverse

In this approach, we have used matrix method to know the bias term and the best fit slope.
We know that we can find minimal value of bias term or best fit slope by simply differentiating these terms 
and equating it to zero. From here we will get the value of parameter which will generate minimum value of
least squared error.
After performing the above step and doing some sort of calculations, we can observe that the value of parameter 
generating the best fit slope will be (inverse((X.T)(X)))(X.T)(Y).

X=features
Y=labels
X.T= transpose matrix of X

Consider H(x)= (q.T)*X
where X= feature set matrix
  q.T= transpose of matrix of the parameter(parameter is the best fit slope)
  H(x) = Hypothesis or y_hat  


