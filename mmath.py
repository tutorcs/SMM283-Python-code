https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
##------------------------------------------------
def factorial_v1(n):  ##header of function factorial
    if n <= 0:
        return 1
    else:
        return n*factorial_v1(n-1)   ##n! = n*[(n-1)!]= n*(n-1)*[(n-2)!]
##------------------------------------------------
def factorial_v2(n):  ##header of function factorial
    result = 1
    for i in range(n, 0, -1):
        result *= i   ##n! = n*[(n-1)!]= n*(n-1)*[(n-2)!]
    return result   

def sqrt(x):
    r = 0.5*x
    tol = 0.00001
    size = int(1/tol)
    for i in range(size):
        r = 0.5 *(r + x/r)
    return r
##-------------------------------------------------
def absolute(x):
    if x < 0:
        return -x
    else:
        return x
##------------------------------------------------
def maximum(a, b):
    m = a
    if a < b:
        m = b
    return m
##-----------------------------------------------
