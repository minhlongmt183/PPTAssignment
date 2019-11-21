import math
def func(x): 
    return x*x-math.sin(math.pi*x)
   

def bisection(a,b): 
    if func(a)*func(b) > 0:
        return
    
    print("{}   {}    {}".format('n', 'x','f'))
    
    i = 0
    while(i <= 5):
      c = (a + b) / 2 
      if func(a)*func(c) < 0:
        b = c                  
      elif func(b)*func(c) < 0:
        a = c         
      #print(i,"\t",round(c,4), "\t", round(func(c),4))
      print('{}  {}  {}'.format(i,round(c,6),round(func(c),6)))
      i = i+1
     
# Driver code 
# Initial values assumed 
a = 1/2
b = 2
bisection(a, b) 
