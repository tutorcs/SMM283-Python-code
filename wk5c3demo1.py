https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from math import *
from locale import *
def d1(s, k, r, q, sig, tau):
    temp = (log(s/k) + (r-q+0.5*pow(sig, 2))*tau)/(sig*sqrt(tau))
    return temp
def d2(s, k, r, q, sig, tau):
    temp = (log(s/k) + (r-q-0.5*pow(sig, 2))*tau)/(sig*sqrt(tau))
    return temp
##def d2_(s, k, r, q, sig, tau):
##    temp = d1(s, k, r, q, sig, tau) - sig*sqrt(tau)
##    return temp
#-----------------------------------------------------------------------------
#  Computes the cummulative probabilities of standard normal distribution
#  Uses  an approximation method
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
        prob = (1.0 - c *  exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))

    else:
        t = 1.0 / (1.0 - p * x)
        prob =(c * exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))
    return prob
#---------------------------------------------------------------------------
def bscall(s, k, r, q, sig, tau):
    done = d1(s, k, r, q, sig, tau)
    dtwo  = d2(s, k, r, q, sig, tau)
    temp = s*exp(-q*tau)*n(done) - k*exp(-r*tau)*n(dtwo)
    return temp
def bsput(s, k, r, q, sig, tau):
    done = d1(s, k, r, q, sig, tau)
    dtwo  = d2(s, k, r, q, sig, tau)
    temp = -s*exp(-q*tau)*n(-done) + k*exp(-r*tau)*n(-dtwo)
    return temp
def main():
    setlocale(LC_ALL, '')
    s = 100.0
    k = 95.0
    r = 0.08
    q = 0.03
    sig = 0.21
    tau = 0.5
    temp = d1(s, k, r, q, sig, tau)
    print("d1~~~~~~~~~~:= {0:>10.2f}".format(temp))
    temp = d2(s, k, r, q, sig, tau)
    print("d2~~~~~~~~~~:= {0:>10.2f}".format(temp))
    temp = bscall(s, k, r, q, sig, tau)
    print("call value~~:= {0:>10s}".format(currency(temp, True)))
    temp = bsput(s, k, r, q, sig, tau)
    print("put value~~~:= {0:>10s}".format(currency(temp, True)))
##---------------------------------------------------------------------
main()
    
