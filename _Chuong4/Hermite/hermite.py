import math
import numpy as np


#############################################################################
# INPUT:                                                                    #
#  x, y, z là các vector chứa các giá trị của đối số , của hàm và           #
#  đạo hàm của nó                                                           #
# OUTPUT:                                                                   #
# P là mảng 2n chiều chứa hệ số của đa thức Hermite                         #
# H(x) = P(1) + P(2)(x-x(1)) + ,,,,,, + (x-x(n-1))^2(x-x(n))                #                                                                   
#############################################################################


def InitMatrix(m,n, val = 0):
    A = []
    for i in range(m):
        a = []
        for j in range(n):
            a.append(val)
        A.append(a)
    return A





def hermite(x,y,z):
    n = len(x)
    xx = InitMatrix(2*n,1)
    Q = InitMatrix(2*n, 2*n)
    for i in range(n):
        xx[2*i-1] = x[i]
        xx[2*i] = x[i]
        Q[2*i -1][0] = y[i]
        Q[2*i][0] = y[i]

    Q[2*i][2] = z[i]
    if i > 1:
        Q[2*i-1][2] = (Q[2*i-1][1] - Q[2*i-2][1]) / (xx[i]-xx[i-j+1])
    
    for j in range(3, 2*n):
        for i in range(j, 2*n):
            Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (xx[i]-xx[i-j+1])
    
    P = InitMatrix(2*n, 1)
    for i in range(2*n):
        P(i) = Q[i][i]
    return