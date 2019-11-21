import math 
MAX = 100


def Cholesky(matrix, N): 
  
    B = [[0 for x in range(N + 1)]  
                for y in range(N + 1)]
  
    for i in range(N):  
        for j in range(i + 1):  
            sum1 = 0
  
            #tính đường chéo
            if (j == i):  
                for k in range(j): 
                    sum1 += pow(B[j][k], 2)
                B[j][j] = int(math.sqrt(matrix[j][j] - sum1))
            else: 
                  
               #sử dụng L[j][j] tính L[i][j]
                for k in range(j): 
                    sum1 += (B[i][k] *B[j][k]); 
                if(B[j][j] > 0): 
                    B[i][j] = int((matrix[i][j] - sum1) / B[j][j]) 
  
  #in kết quả 
    print("Ma tran duoi\t\t\tMa tran tren") 
    for i in range(N):  
          
        # Lower
        for j in range(N): 
            print(B[i][j], end = "\t") 
        print("", end = "\t") 
          
        #upper 
        for j in range(N): 
            print(B[j][i], end = "\t")
        print("") 
  
N=3
matrix = [[4, 12, -16], 
          [12, 37, -43], 
          [-16, -43, 98]]; 
Cholesky(matrix, N)

