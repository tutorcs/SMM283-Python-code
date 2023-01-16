https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#-----------------------------------------------------------------------------
#  Computes the cummulative probabilities of standard normal distribution
#  Uses  an approximation method
import math as m
def n(x):
    b1 = 0.319381530
    b2 = -0.356563782
    b3 = 1.781477937
    b4 = -1.821255978
    b5 = 1.330274429
    p = 0.2316419
    c = 0.39894228
    prob  = 0.0
    if (x >= 0.0):
        t = 1.0/(1.0 + p * x)
        prob = (1.0 - c *  m.exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))

    else:
        t = 1.0 / (1.0 - p * x)
        prob =(c * m.exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))
    return prob
#---------------------------------------------------------------------------
