https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from math import *
from locale import *
from normsdist import *

#---------------------------------------------------------------------------
def bsvalue(s, k, r, q, sig, tau, iopt):
    done = (log(s/k) + (r-q+0.5*pow(sig, 2))*tau)/(sig*sqrt(tau))
    dtwo  = done - sig*sqrt(tau)
    temp = iopt*s*exp(-q*tau)*n(iopt*done) - iopt*k*exp(-r*tau)*n(iopt*dtwo)
    return temp
##---------------------------------------------------------------------------
def main():
    setlocale(LC_ALL, '')
    s = 100.0
    k = 95.0
    r = 0.08
    q = 0.03
    sig = 0.21
    tau = 0.5
    temp = bsvalue(s, k, r, q, sig, tau, +1)
    print("call value~~:= {0:>10s}".format(currency(temp, True)))
    temp = bsvalue(s, k, r, q, sig, tau, -1)
    print("put value~~~:= {0:>10s}".format(currency(temp, True)))
##---------------------------------------------------------------------
main()

    
