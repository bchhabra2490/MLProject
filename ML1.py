from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour

data=loadtxt('ex1data1.txt',delimiter=",")

scatter(data[:,0],data[:,1],marker='o',c='b')
title("profits distribution")
xlabel("Population of City in 10,000s")
ylabel('Profit in $10,0000s')
show()

X=data[:,0]
y=data[:,1]

m=y.size

it=ones(shape=(m,2))
it[:,1]=X

theta=zeros(shape=(2,1))

iterations=1500
alpha=0.01

def compute_cost(X,y,theta):
	m=y.size
	predictions=X.dot(theta).flatten()

	sqErrors=(predictions-y)**2
	J=(1.0/(2*m))*sqError.sum()
	return J
def gradient_descent(X,y,theta,alpha,num_iters):
	m=y.size
	J_history=zeros(shape=(num_iters,1))

	for i in range(num_iters):
		predictions=X.dot(theta).flatten()

		errors_x1=(predictions-y)*X[:,0]
		errors_x2=(predictions-y)*X[:,1]

		theta[0][0]=theta[0][0]-alpha*(1.0/m)*errors_x1.sum()
		theta[1][0]=theta[1][0]-alpha*(1.0/m)*errors_x2.sum()

		J_history[i,0]=compute_cost(X,y,theta)
	return theta, J_history	