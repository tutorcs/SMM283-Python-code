https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import random as r
import math as m
import locale as l
##---------------------------
def payoff(s, k, iopt):
    ma = maximum(iopt*(s-k), 0)
    return ma
def maximum(a, b):
    ma = a
    if a < b:
        ma = b
    return ma
def main():
    s = []
    l.setlocale(l.LC_ALL, '')
    for i in range(100):
        temp = r.uniform(0.0, 150.0)
        s.append(temp)  ##populate the s list
    s.sort()
    k = m.fsum(s)/len(s)
    print("Strike is the avergae of all prices: > {0:>10s}".format(str(l.currency(k, True))))
    while True:
        try:
            iopt = input("Enter +1 for call, -1 for put: ")
        except:
            continue
        if type(iopt) == int:
            if iopt == 1 or iopt == -1:
                break
        if type(iopt) == float:
            continue
    po = []
    for j in range(100):
        temp = payoff(s[j], k, iopt)
        po.append(temp) ##populate the payoff list
    f = open("optiondata1.xls", "w")
    msg1 = "Spock price\tOption Payoff"
    print(msg1)
    f.write(msg1)
    for k in range(100):
        msg2 = "{0:>10s}\t{1:>10s}".format(str(l.currency(s[k], True)), str(l.currency(po[k], True)))
        print(msg2)
        f.write(msg2)
    f.close()
main()
