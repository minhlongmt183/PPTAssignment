import math
import numpy as np


#############################################################################
# INPUT:                                                                    #
#  N: số phương trình và số ẩn                                              #
#  A: các phần tử thuộc đường chéo chính                                    #
#  B và C là các vector chưa các phan tử nằm trên và dưới đường chéo chính  #
# OUTPUT:                                                                   #
# X là vector nghiệm                                                        #                                                                   
#############################################################################


def tridiag(N, A, B, C, D):
    u = np.zeros(N)
    l = np.zeros(N)
    v = np.zeros(N)
    y = np.zeros(N)
    X = np.zeros(N)

    u[0] = A[0]
    v[0] = B[0]
    l[0] = C[0]/u[0]
    y[0] = D[0]

    for i in range(1, N-1):
        u[i] = A[i] - l[i-1]*v[i-1]
        v[i] = B[i]
        l[i] = C[i] / u[i]
        y[i] = D[i] -l[i-1]*y[i-1]

    u[N-1] = A[N-1] - l[N-2]*v[N-2]
    y[N-1] = D[N-1] - l[N-2]*y[N-2]
    X[N-1] = y[N-1]/u[N-1]
    for i in range(N-2,-1,-1):
        X[i] = (y[i]-v[i]*X[i+1]) / u[i]
    return X


if __name__ == "__main__":
    A = np.array([2,3,5,3])
    B = np.array([3,9,2])
    C = np.array([6,2,4])
    D = np.array([21,69,34,22])
    N = 4

    X = tridiag(N,A,B,C,D)
    print(X)

