https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from time import *
##------------------------------------
def power_(b, n):
    result = 1
    if n < 0:
        b = 1.0/b
        n = -n
        for i in range(n):
            result *= b
        return result
    elif n == 0:
        return result
    elif n == 1:
        result = b
        return result
    else:
        for i in range(n):
            result *= b
        return result
##---------------------------------------------------------
def power(b, n):
    if n < 0:
        b = 1.0/b
        n = -n
        return (b *power(b, n-1)) 
    elif n == 0:
        return 1
    elif n == 1:
        return b
    else:
        return  (b *power(b, n-1))
##----------------------------------------------------------------------
def main():
    start = time()
    r = power(10, 300)
    end = time()
    diff1 = start - end
    print("It took {0:>,.30f} seconds to run function power()".format(diff1))
    start = time()
    r = power_(4, 3)
    end = time()
    diff2 = start - end
    print("It took {0:>,.30f} seconds to run function power_()".format(diff2))
##----------------------------------------------------------------------
main()
        
    
