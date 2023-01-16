https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import math as m
import locale as lo
import random as r
def isItPrinted(s = []):
    for i in range(100):
        print(s[i])
    return True     

##-----------------------------
def maximum(a, b):
    m = a
    if a < b:
        m = b
    return m
##-----------------------------
def payoff(s, k, iopt):
    po = maximum(iopt*(s-k), 0)
    return po
##--------------------------------------------------------------------------------------------
def main():
    lo.setlocale(lo.LC_ALL, '')
    s = []
    for i in range(100):
        temp = r.uniform(0.0, 150.0)
        s.append(temp)
    s.sort()
    k = m.fsum(s)/len(s)
    print("Strike is worked out as an avergae price |{0:>10s}|".format(lo.currency(k, True)))
##--------------------------------------------------------------------------------------------
    while True:
        try:
            iopt = int(input("Enter +1 for call, -1 for put: "))
        except:
            continue
        if iopt == 1 or iopt == -1:
            break  
    po = []
    for j in range(100):
        temp = payoff(s[j], k, iopt)
        po.append(temp)
##--------------------------------------------------------------------------------------------
##    f = open("optiondata.xls", "w")
##    print("Stock price\tOpption Payoff")
##    f.write("Stock price\tOpption Payoff")
##    for k in range(100):
##        print("{0:>10s}\t{1:>10s}".format(lo.currency(s[k], True), lo.currency(po[k], True)))
##        f.write("{0:>10s}\t{1:>10s}".format(lo.currency(s[k], True), lo.currency(po[k], True)))
##    f.close()

    isItPrinted(s)
##----------------------------------------------------------------------------------------
main()  ##call the main
