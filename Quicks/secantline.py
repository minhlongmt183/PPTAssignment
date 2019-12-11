import math
def func(x):    #khoi tao f(x)
    return x*x-math.sin(math.pi*x)
    #ex:  x^2 - sin(pi*x)

def secantline(a,b): 
    if func(a)*func(b) > 0:     #neu f(a)*f(b) > 0 thi ket thuc chuong trinh
        return

    print("{}     {}      {}".format('n', 'x','f'))

    i = 0
    while(i <= 5):      #tinh den x5
      c = a - (b-a)*func(a)/(func(b)-func(a))
      if func(a)*func(c) < 0:
        b = c           #neu f(a)*f(c) < 0 thi thay b = c   
      elif func(b)*func(c) < 0:
        a = c           #neu f(b)*f(c) < 0 thi thay a = c  
      #print(i,"\t",round(c,4), "\t", round(func(c),4))
      print('{}  {}  {}'.format(i,round(c,6),round(func(c),6)))
      i = i+1

# Driver code 
# Initial values assumed 
a = 1/2     #khoang li do la [1/2; 2]
b = 2       #
secantline(a, b)
