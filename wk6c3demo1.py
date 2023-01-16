https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from time import *
##------------------------------------------
def power(b, n):
    result = 1
    if n > 0:
        for i in range(n):
            result *= b
    else:
        if n < 0:
            b = 1.0/b
            n = -n
            for i in range(n):
                result *=  b
    return result
##---------------------------------------------------
#------------------------------------------
def power_(b, n):
    result = 1
    if n > 0:
        result = b*power_(b, n-1)
    else:
        if n < 0:
            b = 1.0/b
            n = -n
            result = b*power_(b, n-1)
    return result
##---------------------------------------------------
def main():
    while True:
        try:
            b, n = input("Enter b: "), input("Enter n: ")
        except:
            continue
        else:
            break

    start = time()
    r = power(b, n)
    end = time()
    d = end - start
    
    start = time()
    r = power_(b, n)
    end = time()
    d = end - start

    print("Power({0}, {1}):= {2}".format(b, n, r))
    print("It took {0:.40f} to execute the code with power()..".format(d))
    print("Power_({0}, {1}):= {2}".format(b, n, r))
    print("It took {0:.40f} to execute the code with power_()..".format(d))
    
##---------------------------------------------------
main()
        
    
    
