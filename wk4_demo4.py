https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
## A program computing the call and put option prices
## using the Black-Scholes model.
## Various user-defined functions are used.
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## Author: Adrian Euler
## Achool: Cass Business School
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## c(s, k, r, q, sig, tau) = +1*(s*exp(-q*tau)*n(d1) - k*exp(-r*tau)*n(d2))
## p(s, k, r, q, sig, tau) = -1*(s*exp(-q*tau)*n(d1) - k*exp(-r*tau)*n(d2))
## ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## d1(s, k, r, q, sig, tau) = (log(s/k) + (r-q+0.5*pow(sig, 2))*tau)/(sig*sqrt(tau))
## d2 = d1 - sig*sqrt(tau)
##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import math as m
from normsdist import n
def d1(s, k, r, q, sig, tau):
    dOne = (m.log(s/k) + (r-q+0.5*m.pow(sig, 2))*tau)/(sig*m.sqrt(tau))
    return dOne
def d2(s, k, r, q, sig, tau):
    dTwo = d1(s, k, r, q, sig, tau) - sig*m.sqrt(tau)
    return dTwo

def bscall(s, k, r, q, sig, tau):
    dOne = d1(s, k, r, q, sig, tau)
    dTwo = d2(s, k, r,q, sig, tau) 
    c = s*m.exp(-q*tau)*n(dOne) - k*m.exp(-r*tau)*n(dTwo)
    return c
def bsput(s, k, r, q, sig, tau):
    dOne = d1(s, k, r, q, sig, tau)
    dTwo = d2(s, k, r,q, sig, tau) 
    p = -s*m.exp(-q*tau)*n(dOne) + k*m.exp(-r*tau)*n(dTwo)
    return p
##--------------------------------------------------------------------------
def main():
    MENU = \
    """
     
    """
    s = 100.0
    k = 95.0
    r = 0.08
    q = 0.00
    sig = 0.21
    tau = 0.5
    cval = bscall(s, k, r, q, sig, tau)
    pval = bsput(s, k, r, q, sig, tau)
    print(cval)
    print(pval)
    
main()
