https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from random import *

w1 = []
w2 = []

##Populate the two arrays
for i in range(100):
    temp = uniform(0.0, 1.0)
    w1.append(temp)
    temp = 1.0 - temp
    w2.append(temp)

##Display arrays
for j in range(100):
    print("{0:10.2%}{1:10.2%}{2:10.2%}".format(w1[j], w2[j], w1[j] + w2[j]))
        
