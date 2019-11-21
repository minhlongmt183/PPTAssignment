import math
import numpy as np


    #############################################################
    #INPUT:                                                     #
    # N: so phuong trinh va so an                               #
    # A: ma tran cap Nx(N+1), cot N+1 la vector tu do           #
    #OUTPUT:                                                    #
    # X la vector nghiem                                        #
    #############################################################


def lowersys(N, L):
    Y = [None]*N
    Y[0] = L[0][N] / L[0][0]

    for i in range(1,N):
        sum = 0
        for j in range(i):
            sum = sum + L[i][j]*Y[j]
        Y[i] = (L[i][N] - sum) / L[i][i]
    return Y