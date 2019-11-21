import numpy as np
import math
#-------------------------------------------------
# INPUT: 
# N là cấp của ma trân,
# A là ma trận hệ số cấp N
# OUTPUT:
# L và U là các ma trận tam giác
#-------------------------------------------------


# khoi tao ma tran voi gia tri val cho truoc

def uppersys(N,A):

    X = [None]*N
    for i in reversed(range(N)):
        sum = 0
        for j in range(i+1, N):
            sum = sum + A[i][j]*X[j]
        X[i] = (A[i][N] - sum) / A[i][i]
    return X

def lowersys(N, L):
    Y = [None]*N
    Y[0] = L[0][N] / L[0][0]

    for i in range(1,N):
        sum = 0
        for j in range(i):
            sum = sum + L[i][j]*Y[j]
        Y[i] = (L[i][N] - sum) / L[i][i]
    return Y

def InitMatrix(N, val):
    A = []
    for i in range(N):
        a = []
        for j in range(N):
            a.append(val)
        A.append(a)
    return A

def doolittle(N, A):

    #initial L and U
    L = InitMatrix(N, 0)
    U = InitMatrix(N, 0)

    # set L[i,i] = 1
    for i in range(N):
        L[i][i] = 1

    # set first row of U: U[0,j] = A[0,j]
    for j in range(N):
        U[0][j] = A[0][j]

    if U[0][0] == 0:
        print("khong the phan tich duoc\n")
        return
    
    # i from 2 ---> N-1
    # caculate L[i,0]
    for i in range(1,N):
        L[i][0] = A[i][0] / U[0][0]

    # caculate U[i,j]   
    for i in range(1,N-1):
        for j in range(i,N):
            sum = 0

            for k in range(i):
                sum = sum + L[i][k]*U[k][j]

            U[i][j] = A[i][j] - sum

        if U[i][i] == 0:
            print("khong the phan tich duoc\n")
            return
        
        for j in range(i+1,N):
            sum = 0
            for k in range(i):
                sum = sum + L[j][k]*U[k][i]
            
            L[j][i] =(A[j][i]-sum) / U[i][i]
         
    sum = 0
    for k in range(N-1):
        sum = sum + L[N-1][k]*U[k][N-1]
    
    U[N-1][N-1] = A[N-1][N-1] - sum
    return [L,U]

def InputMatrix(N, Matrix):
    N = int(input("Nhap cap ma tran N:"))
    #input matrx from user:
    print("nhap he so ma tran [ " + str(N) + " x " + str(N)+" ]")

    Matrix = []
    for i in range(N):
        a = []
        for j in range(N):
            print("input element [ " + str(i) + "," + str(j)+" ]")
            a.append(int(input()))
        Matrix.append(a)
    return (N,Matrix)
    
def main():

    N = 0
    A = []

    (N,A) = InputMatrix(N,A)

    # Nhap he so tu do
    B = []
    for i in range(N):
        B.append(int(input("nhap he so tu do cua ma tran: ")))

    [L,U] = doolittle(N, A)

    # them he so tu do vao L
    for i in range(N):
        L[i].append(B[i])

    # giai matran tam giac duoi
    Y = lowersys(N,L)
 
    # them he so tu do vao U
    for i in range(N):
        U[i].append(Y[i])
 
    # giai ma tran tam giac tren 
    X = uppersys(N,U)
   
    # print solution
    print("nghiem he phuong trinh la: ")

    for i in range(N):
        print("X[" + str(i) + "]= " + str(round(X[i], 2)))
    
    return
   



if __name__ == "__main__":
    main()
    
    
    




    



