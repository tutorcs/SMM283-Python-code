https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import math as m
import locale as l

def d1(s, k, r, q, sig, tau):
    dTemp = (m.log(s/k) + (r-q+0.5*m.pow(sig, 2))*tau)/(sig*m.sqrt(tau))
    return dTemp
def d2(s, k, r, q, sig, tau):
    dTemp = (m.log(s/k) + (r-q-0.5*m.pow(sig, 2))*tau)/(sig*m.sqrt(tau))
    return dTemp
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
        prob = (1.0 - c *  m.exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))

    else:
        t = 1.0 / (1.0 - p * x)
        prob =(c * m.exp(-x * x/2.0) * t * (t *(t * (t * (t * b5 + b4) + b3) + b2) + b1))
    return prob
#---------------------------------------------------------------------------
def bscall(s, k, r, q, sig, tau):
    d1_ = d1(s, k, r, q, sig, tau)
    d2_ = d2(s, k, r, q, sig, tau)
    tempVal = s*m.exp(-q*tau)*n(d1_)- k*m.exp(-r*tau)*n(d2_)
    return tempVal
def bsput(s, k, r, q, sig, tau):
    d1_ = d1(s, k, r, q, sig, tau)
    d2_ = d2(s, k, r, q, sig, tau)
    tempVal = -s*m.exp(-q*tau)*n(-d1_)+ k*m.exp(-r*tau)*n(-d2_)
    return tempVal
##------------------------------------------------------------------------------
def main():
    l.setlocale(l.LC_MONETARY, '')
    s = 100.0
    k = 95.0
    r = 0.08
    q = 0.03
    sig = 0.21
    tau = 0.5
    tempVal = d1(s, k, r, q, sig, tau)
    print("d1            :={0:>10.4f}".format(tempVal))
    tempVal = d2(s, k, r, q, sig, tau)
    print("d2            :={0:>10.4f}".format(tempVal))
    tempVal = bscall(s, k, r, q, sig, tau)
    print("call val      :={0:>10s}".format(l.currency(tempVal, True)))
    tempVal = bsput(s, k, r, q, sig, tau)
    print("put val       :={0:>10s}".format(l.currency(tempVal, True)))
##-------------------------------------------------------------------------------
main()


