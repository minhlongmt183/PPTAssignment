import numpy as np

#################################################
#  INPUT:                                       #
#  f là hàm dưới dấu tích phân                  #
#  a và b là các cận dưới và trên,              #
#  n là số đoạn chia.                           #
#   OUTPUT:                                     #
# I là giá trị xấp xỉ của tích phân             #
#################################################

def trapez(f, a, b, n):
    if n <= 0:
        print("khong the tinh tich phan")
        return
    h = (b-a)/n
    I = 