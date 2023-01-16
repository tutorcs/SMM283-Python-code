https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
##
##  A simple bank balance calculator  example
##  Using core Python  capabilities.
##  Author:........
##  School:..........

iBalance = eval(input("Enter initial balance: "))
aIRate = eval(input("Enter annual interest rate (0.0 to 1.0): "))
mIRate = aIRate/12

##Display a table
print("\n{0:<7s}{1:>10s}".format("Month", "Balance"))
print("----------------------------")
for i in range(3, 13, 3):
    balance = iBalance *((1+mIRate)**i)
    print("%-7d%+10.2f" % (i, balance))
    print("{0:<7d}{1:>10.2f}".format(i, balance))
    print(str(i).ljust(7), str(balance).rjust(10))
    print("----------------------------")

