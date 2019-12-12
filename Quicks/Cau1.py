import math
import array
def leftEndPoint(a,b,fa,fb):
    return (b-a)*fa/2
def rightEndPoint(a,b,fa,fb):
    return (b-a)*fb/2
def hinhthang(a,b,fa,fb):
    return (b-a)*(fb+fa)/2


# Driver code
# Initial values assumed
Array=[ [0.5, 0.6, 0.9, 1.1, 1.2, 1.3, 1.4],
        [2.65, 2.82, 3.46, 4.0, 4.32, 4.67, 5.05]]
rsLeftEnd=0
rsRightEnd=0
rsHinhThang=0

for i in range (0,5):
    rsLeftEnd=rsLeftEnd+leftEndPoint(Array[0][i],Array[0][i+1],Array[1][i],Array[1][i+1])

for i in range (0,5):
    rsRightEnd=rsRightEnd+rightEndPoint(Array[0][i],Array[0][i+1],Array[1][i],Array[1][i+1])

for i in range (0,5):
    rsHinhThang=rsHinhThang+hinhthang(Array[0][i],Array[0][i+1],Array[1][i],Array[1][i+1])

print("rsLeftEnd = {}".format(rsLeftEnd))
print("rsRightEnd = {}".format(rsRightEnd))
print("rsHinhThang = {}".format(rsHinhThang))