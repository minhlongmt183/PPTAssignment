# Phương pháp lặp đơn

############################################
# INPUT:
# g là biểu thức của hàm lặp g(x)
# x0 là giá trị lặp ban đầu
# eps là sai số cho trước
# N là số lần lặp tối đa

# OUTPUT:
# Giá trị nghiệm x
############################################

import math
# Gán x0, eps, N
x0 = 0.75
eps = 10**-4
N = 100

# Gán biểu thức g
def g(x):
    return (5*x**3 + 3)/20 # VD: g(x) = (5x^3 + 3)/20

def fixedPoint(func, x0, eps, N):
    for i in range(0, N):
        x = func(x0)
        if abs(x - x0) < eps: # |x - x0| < eps, thoả điều kiện sai số => dừng
            return x
        x0 = x
    return "Loi. Khong thanh cong sau {} lan lap".format(N)

print("Nghiem: x =", fixedPoint(g, x0, eps, N))