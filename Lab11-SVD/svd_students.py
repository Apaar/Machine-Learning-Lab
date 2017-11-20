                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           

from scipy import linalg
import numpy as np
Data=np.array([[4.9,3.0,1.4,0.2],
	[4.7,3.2,1.3,0.2],
	[4.6,3.1,1.5,0.2],
	[5.0,3.6,1.4,0.2],
	[5.4,3.9,1.7,0.4],
	[4.6,3.4,1.4,0.3],
	[5.0,3.4,1.5,0.2],
	[4.4,2.9,1.4,0.2],
	[4.9,3.1,1.5,0.1],
	[5.4,3.7,1.5,0.2]])
print(" ")
print("The given Original Matrix is")
print(" ")
print(Data)

[m,n] = Data.shape
print(" ")
print("Original Matrix Shape is")
print(" ")
print("m : ", m,' ',"n : ", n)

U, s, V = np.linalg.svd(Data, full_matrices=True)

print(U, '\n', np.reshape(s, (U.shape[1], V.shape[0])), '\n', V)

#print("Original Matrix is Decomposed into U Sigma and V Transpose as ")
#print(" ")


#Fill the missing code and print the sizes of U matrix, Sigma matrix and V Tranpose matrix






