https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from random import *

w1 = []
w2 = []
pret = []
pvol = []
##inputs..validated too
##''''''''''''''''''''''

##pupulate the arrays
for i in range(100):
    temp = uniform(0.1, 1.0)
    w1.append(temp)
    temp = 1- temp
    w2.append(temp)

##calculations


##display
for k in range(100):
    print("{0:>10.2%}{1:>10.2%}{2:>10.2%}".format(w1[k], w2[k], w1[k]+w2[k]))


    
    
