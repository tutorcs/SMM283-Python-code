https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
def factorial(n): ##has function cohesion
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)
##------------------------------   
def sqrt(x):
    sqrt_x = 0.5*x
    tol = 0.000001
    upperLimit = int(1/tol)
    i = 0
    while i < upperLimit:
        sqrt_x = 0.5*(sqrt_x + x/sqrt_x)
        i += 1
    return sqrt_x
####-----------------------------------------
def MAIN():  ##Procedural
    while True:
        try:
            a = input("Enter a number: ")
        except:
            continue
        if type(a) == float or type(a) == int: 
            r = sqrt(float(a))
            print("\tSQRT of {0} is {1}".format(a, r))
            f = factorial(int(a))
            print("\tFACTORIAL, {0}!={1}".format(a, f))
            break
##---------------------------------------
MAIN()  ##CALL THE MAIN....




