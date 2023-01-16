https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import math as m
import locale as l
from normsdist import n
def d(s, k, r, q, sig, tau):
    temp = (m.log(s/k)+(r-q+0.5*m.pow(sig, 2))*tau)/(sig*m.sqrt(tau))
    return temp
def bsvalue(s, k, r, q, sig, tau, iopt):
    d1_ = d(s, k, r, q, sig, tau)
    d2_ = d(s, k, r, q, sig, tau) - sig*m.sqrt(tau)
    temp = iopt*(s*m.exp(-q*tau)*n(iopt*d1_)-k*m.exp(-r*tau)*n(iopt*d2_))
    return temp
##--------------------------------------------------------------------------
def main():
    l.setlocale(l.LC_ALL, '')
    s = 100.0
    k = 95.0
    r = 0.08
    q = 0.03
    sig = 0.21
    tau = 0.5
    temp = bsvalue(s, k, r, q, sig, tau, +1)
    print("call value:={0:>10s}".format(l.currency(temp, True)))
    temp = bsvalue(s, k, r, q, sig, tau, -1)
    print("put value :={0:>10s}".format(l.currency(temp, True)))

##--------------------------------------------------------------------------
main()##call main
