https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
##----------------------------------------
def annualiseRate(r):
    #print("\nI am in the function annualiseRate...")
    return r *12
##----------------------------------------
def annualiseStd(sig):
    ##print("\nI am in the function annualiseStd...")
    return sig*sqrt_(12)
##---------------------------------------
def sqrt_(x):
    ##print("\nI am in the function SQRT...")
    sqrt_x = 0.5*x
    tol = 0.000001
    i = 0
    while i < int(1.0/tol):
        sqrt_x = 0.5*(sqrt_x+x/sqrt_x)
        i += 1
    return sqrt_x
def main():
    ##print("I am at the START of the MAIN!\n")
    while True:
        try:
            rate = input("Enter monthly rate: ")
        except:
            continue
        if type(rate) == float:
            break
    while True:
        try:
            vol = input("Enter monthly volatility: ")
        except:
            continue
        if type(vol) == float:
            break
    rate = annualiseRate(rate)
    vol = annualiseStd(vol)
    print("Annualised rate:= {0:>10.2%}\nAnnualised Std:= {1:>10.2%}\n".format(rate, vol))
    ##print("\nI am NOW at the END of the MAIN!\n")
##----------------------------------------
##call main
main()
