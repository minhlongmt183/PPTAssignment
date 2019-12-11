import numpy as np
#########################################################
# INPUT:                                                #
# x và y là các vector chứa các giá trị đối số và       #
#  của hàm.                                             #
# OUTPUT:                                               #
#   a,b,c,d là các vector của hệ số spline              #
#########################################################

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



def nspline(x,y):
    N = min(np.size(x), np.size(y))
    h = np.zeros(N)

    for i in range(N-1):
        h[i] = x[i+1] - x[i]
    
    A = np.zeros(N)
    B = np.zeros(N-1)
    C = np.zeros(N-1)
    D = np.zeros(N)

    A[0]    = 1
    A[N-1]  = 1
    B[1]    = 0
    C[N-2]  = 0

    for i in range(1, N-1):
        A[i] = 2*(h[i-1] + h[i])
        B[i] = h[i]
        C[i-1] = h[i-1]
    D[0] = 0
    D[N-1] = 0
    for i in range(1,N-1):
        D[i] = 3*(y[i+1] - y[i])/h[i] - 3 *(y[i] - y[i-1])/h[i-1]
    
    c = np.zeros(N)

    c = tridiag(N,A,B,C,D)
    a = np.zeros(N-1)
    b = np.zeros(N-1)
    d = np.zeros(N-1)

    for i in range(N-1):
        a[i] = y[i]
        b[i] = (y[i+1] -y[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
        d[i] = (c[i+1] - c[i])/3/h[i]
    
    return (a,b,c,d)


def InputMatrix(M, N, Matrix):
    M = int(input("Nhap cap ma tran M:"))
    N = int(input("Nhap cap ma tran N:"))
    #input matrx from user:
    print("nhap he so ma tran [ " + str(M) + " x " + str(N)+" ]")

    Matrix = []
    for i in range(M):
        a = []
        for j in range(N):
            print("input element [ " + str(i) + "," + str(j)+" ]")
            a.append(int(input()))
        Matrix.append(a)
    return (M,N,Matrix)
    

if __name__ == "__main__":
    # print("nhap ma tran A")
    # Ma = 0
    # Na = 0
    # A = []
    # (Ma, Na, A) = InputMatrix(Ma, Na, A)
    # print()
    # print("nhap ma tran B")
    # Mb = 0
    # Nb = 0
    # B = []
    # (Mb, Nb, B) = InputMatrix(Mb, Nb, B)

    # alpha = float(input("nhap alpha: "))
    # beta = float(input("nhap beta: "))
    X = np.array([0,1,2,3])
    Y = np.array([1,2,4,8])
    

    (a,b,c,d) = nspline(X,Y)

    print("ham so")
    for i in range(np.size(a)):
        print("{0:.2f} + {1:.2f}(x-{4:.2f}) + {2:.2f}(x-{4:.2f})^2 + {3:.2f}(x-{4:.2f})^3".format(a[i], b[i], c[i], d[i], X[i]))
