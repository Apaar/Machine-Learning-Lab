import numpy as np
def Gauss(A, b):
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in xrange(n-1):
        print A
        print b
        for row in xrange(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in xrange(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print 'RESULTS AFTER GUASSIAN ELIMINATION'
    print '--------------------------------------'
    print A
    print b
    x = np.zeros(n)
    #print 'before',x
    k = n-1
    x[k] = b[k]/A[k,k]
    #print 'b value is ',b[k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x


def partial(A, b):
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in xrange(n-1):
        print A
        print b
        max = A[pivot_row:,pivot_row].argmax()
        if max+pivot_row != pivot_row :
            temp = A[[pivot_row ,max+pivot_row ]]
            A[[pivot_row ,max+pivot_row ]] = A[[max+pivot_row , pivot_row ]]
            A[[max+pivot_row , pivot_row ]] = temp
            temp = b[[pivot_row ,max+pivot_row ]]
            b[[pivot_row ,max+pivot_row ]] = b[[max+pivot_row , pivot_row ]]
            b[[max+pivot_row , pivot_row ]] = temp

        for row in xrange(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in xrange(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print 'RESULTS AFTER GUASSIAN ELIMINATION'
    print '--------------------------------------'
    print A
    print b
    x = np.zeros(n)
    #print 'before',x
    k = n-1
    x[k] = b[k]/A[k,k]
    #print 'b value is ',b[k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x
    

if __name__ == "__main__":
    '''
    A = np.array([[2.,1.,-1.],[-3.,-1.,2.],[-2.,1.,2.]])
    b =  np.array([[8.],[-11.],[-3.]])
    
    A = np.array([[2.,1.,-1.],[2.,1.,-1.],[2.,1.,-1.]])
    b =  np.array([[8.],[8.],[7.]])
    '''

    A = np.array([[0.02,0.01,0.,0.],[1.,2.,1.,0.],[0.,1.,2.,1.],[0.,0.,100.,200.]])
    b =  np.array([[0.02],[1.],[4.],[800.]])
    print Gauss(A,b)
    A = np.array([[0.02,0.01,0.,0.],[1.,2.,1.,0.],[0.,1.,2.,1.],[0.,0.,100.,200.]])
    b =  np.array([[0.02],[1.],[4.],[800.]])
    print partial(A,b)
    # Take matrix A
    # Take Matrix b