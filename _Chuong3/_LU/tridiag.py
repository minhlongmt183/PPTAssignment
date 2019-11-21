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
    u[1] = A[1]
    v[1] = B[1]
    l[1] = C[1]/u[1]
    y[1] = D[1]

    for i in range(1, N-1):
        u[i] = A[i] - l[i-1]*v[i-1]
        v[i] = B[i]
        l[i] = C[i] / u[i]
        y[i] = D[i] -l[i-1]*y[i-1]

    u[N-1] = A[N-1] - l[N-2]*v[N-2]
    y[N-1] = D[N-1] - l[N-2]*y[N-2]
    X[N-1] = y[N-1]/u[N-1]
    for i in range(N-2,-1,-1):
        X[i] = (y[i]-v[i]*x[i+1]) / u[i]

