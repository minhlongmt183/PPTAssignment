import math
import numpy as np


    #############################################################
    #INPUT:                                                     #
    # N: so phuong trinh va so an                               #
    # A: ma tran cap Nx(N+1), cot N+1 la vector tu do           #
    #OUTPUT:                                                    #
    # X la vector nghiem                                        #
    #############################################################



def uppersys(N,A):
    X = [None]*N
    for i in reversed(range(N)):
        sum = 0
        for j in range(i+1 ,N):
            sum = sum + A[i][j]*X[j]
        X[i] = (A[i][N] - sum) / A[i][i]
    return X