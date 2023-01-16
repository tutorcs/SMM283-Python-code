https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def maximum(x, y):
    mx = x
    if y > x:
        mx = y
    return mx
def payoff(x, y, iopt):  ##iopt*max(s-k, 0)  where iopt takes two values: 1(call) and -(put)
    po = maximum(iopt(x-y), 0)
    return po
def MAIN():
    s = 120.0
    k = 110.0
    iopt = 1
    print(payoff(s-k, 0.0, iopt))
##invoke the MAIN
MAIN()
