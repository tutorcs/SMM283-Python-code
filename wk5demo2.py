https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import math as m
import locale as l
from normsdist import n

def d(s, k, r, q, sig, tau):
    dTemp = (m.log(s/k) + (r-q+0.5*m.pow(sig, 2))*tau)/(sig*m.sqrt(tau))
    return dTemp
#---------------------------------------------------------------------------
def bsval(s, k, r, q, sig, tau, iopt):
    d1 = d(s, k, r, q, sig, tau)
    d2 = d(s, k, r, q, sig, tau) - sig*m.sqrt(tau)
    tempVal = iopt*(s*m.exp(-q*tau)*n(iopt*d1)- k*m.exp(-r*tau)*n(iopt*d2))
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
    tempVal = d(s, k, r, q, sig, tau)
    print("d1            :={0:>10.4f}".format(tempVal))
    tempVal = d(s, k, r, q, sig, tau)-sig*m.sqrt(tau)
    print("d2            :={0:>10.4f}".format(tempVal))
    iopt = 1
    tempVal = bsval(s, k, r, q, sig, tau, iopt)
    print("call val      :={0:>10s}".format(l.currency(tempVal, True)))
    iopt = -1
    tempVal = bsval(s, k, r, q, sig, tau, iopt)
    print("put val       :={0:>10s}".format(l.currency(tempVal, True)))
##-------------------------------------------------------------------------------
main()


