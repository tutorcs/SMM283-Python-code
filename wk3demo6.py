https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
##def factorial(n):
##        result = 1
##	if n == 1 or n == 0:
##            return result
##	for i in range(n, 0, -1):
##		result = result * i
##	return result
def factorial(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n*factorial(n-1)
def sqrt(x):
    tol = 0.00001
    sqrt_x = float(x)/2.0
    upperLimit = int(1/tol)
    for i in range(upperLimit+1):
        sqrt_x = 0.5*(sqrt_x + x/sqrt_x)
    return sqrt_x
def MAIN():
    while True:
        try:
            x = input("Enter an integer number: ")
            if type(x) != int:
                print("\t..Re-try...please!")
                continue
            else:
                break
        except Exception as e:
            print("\t..Re-try!")
            continue
    res = factorial(x)
    print(res)
##------------------------------------------------
MAIN()
    
