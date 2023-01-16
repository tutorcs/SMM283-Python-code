https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from __future__ import print_function
from random import *
w1 = []
w2 = []
for i in range(100):
    temp = random()
    w1.append(temp)
    x = 1- w1[i]
    w2.append(x)
    print("%10.2f%10.2f%10.2f"% (w1[i], w2[i],  w1[i] + w2[i]))

   
