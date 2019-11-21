import math
import numpy as np

    #############################################################
    #INPUT:                                                     #
    # N: so phuong trinh va so an                               #
    # A: ma tran cap Nx(N+1), cot N+1 la he so tu do            #
    #OUTPUT:                                                    #
    # X la vector nghiem                                        #
    #############################################################

def Gauss(N,A):

    for j in range(N):
        if A[j][j] == 0:
            flag = 0
            for i in range(j+1,N):
                if A[i][j] != 0:
                    flag = 1
                    for k in range(N+1):
                        temp = A[i][k]
                        A[i][k] = A[j][k]
                        A[j][k] = temp
                    
            
            if flag == 0:
                print("Ma tran suy bien ==> Phuong trinh vo nghiem")
                return
        

        for i in range(j+1, N):
            temp = A[i][j]*A[j][j]
            for k in range(j, N+1):
                A[i][k] = A[i][k]-A[j][k]*temp 
        
        #print matrix
        print("\n\n")
        for i in range(N):
            for j in range(N+1):
                print(A[i][j], end=" ")
            print()

    X = uppersys(N,A)
    return X

def uppersys(N,A):
    X = [None]*N
    for i in reversed(range(N)):
        sum = 0
        for j in range(i+1 ,N):
            sum = sum + A[i][j]*X[j]
        X[i] = (A[i][N] - sum) / A[i][i]
    return X




def main():
    # input N
    R = int(input("Nhap so hang: "))
    C = int(input("Nhap so cot: "))
    
    if (C - R) > 1 :
        print("Phuong trinh vo nghiem")
    elif (C - R) < 1:
        print("phuong trinh vo so nghiem")
    else:
        
        #set N = R
        N = R

        # input matrix
        A = []
        print("Input matrix A[N,N+1]\n")
        for i in range(N):
            a = []
            for j in range(N+1):
                a.append(int(input()))
            A.append(a)
        
            #print matrix
        print("\n A: ")
        for i in range(N):
            for j in range(N+1):
                print(A[i][j], end=" ")
            print()
            
        # call function
        X = []
        X = Gauss(N,A)
        
        print("nghiem phuong trinh")
        print(X)


if __name__ == "__main__":
    main()
    


