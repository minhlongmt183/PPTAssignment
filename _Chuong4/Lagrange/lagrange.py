import math
import numpy as np


#############################################################################
# INPUT:                                                                    #
#  x, y: các vector chứa các giá trị đối số  và của hàm                     #
#  xx là giá trị của đối số                                                 #
# OUTPUT:                                                                   #
# yx là giá trị xấp xỉ của hàm tại xx                                       #                                                                   
#############################################################################


def lagrange(x,y,xx):
    N = min(len(x), len(y))
    for i in range(N):
        if xx == x[i]:
            yx = y[i]
        
        omega = 1
        for i in range(N):
            omega = omega*(xx - x[i])
        D = []
        for k in range(N):
            D[k] = 1
            for i in range(N):
                if i-k < 1e-6:
                    D[k] = D[k]*(xx-x[k])
        yx = 0
        for k in range(N):
            yx = yx + y[k]/D[k]
        yx = yx * omega
    