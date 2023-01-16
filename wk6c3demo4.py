https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
####-----------------------------------0-
##def power(b, n):
##    result  = 1
##    if n == 0:
##        return result
##    if n == 1:
##        result = b
##        return result
##    if n > 1:
##        for i in range(n):
##            result *= b
##        return result
####--------------------------------
##def power(b, n):
##    result  = 1
##    if n > 0:
##        for i in range(n):
##            result *= b
##    return result
####-------------------------------
##def power(b, n):
##    result  = 1
##    for i in range(n):
##        result *= b
##    return result
####-------------------------------
import time as clock
def power(b, n):
    result  = 1
    if n >= 0:
        for i in range(n):
            result *= b         
    else:
        b = 1.0/b
        n = -n
        for i in range(n):
            result *= b
    return result
##--------------------------------
def power_(b, n):
    result  = 1
    if n >= 0:
        result = b*power(b, n-1)         
    else:
        b = 1.0/b
        n = -n
        for i in range(n):
            result = b*power(b, n-1) 
    return result
##--------------------------------
def main():
    start = clock.time()
    print(start)
    for i in range(1000000):
        ''
    r = power(3, 5)
    end = clock.time()
    print(end)
    print("{0:.40f}".format(end - start))
    start = clock.time()
    print(start)
    for i in range(1000000):
        ''
    r = power_(3, 5)
    end = clock.time()
    print(end)
    print("{0:.40f}".format(end - start))
main()
    
        
        
