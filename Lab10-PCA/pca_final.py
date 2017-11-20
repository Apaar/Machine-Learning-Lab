

from scipy import linalg
import numpy as np

import functools

import numpy.linalg as linalg


Data=np.array([[4.9,3.0,1.4,0.2],
	[4.7,3.2,1.3,0.2],
	[4.6,3.1,1.5,0.2],
	[5.0,3.6,1.4,0.2],
	[5.4,3.9,1.7,0.4],
	[4.6,3.4,1.4,0.3],
	[5.0,3.4,1.5,0.2],
	[4.4,2.9,1.4,0.2],
	[4.9,3.1,1.5,0.1],
	[5.4,3.7,1.5,0.2]]).transpose()

covariance = np.cov(Data)
eigen_values, eigen_vectors = linalg.eig(covariance)


print(eigen_values, eigen_vectors)


# find the covarience matrix using np.cov(x) module





#find the eigen vectors of the covarience matrix






#after finding the eigen vectors(Principal components) which will be 4 since 4 original dimentions we have
#put them in decreasing order and make a threshold to have how many principal components are required 





