https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com

##-----------------------------------------------------
def balance(principle, nYears=1, interestRate = 0.04):
    balance = principle *((1+interestRate)**nYears)
    return balance
##-----------------------------------------------------
def main():
    print("Balance         := {0:>10,.2f}".format(balance(1000, 1, 0.04)))
    print("Balance         := {0:>10,.2f}".format(balance(1000, 1)))
    print("Balance         := {0:>10,.2f}".format(balance(1000)))
    print("Balance         := {0:>10,.2f}".format(balance(1000, 4, 0.08)))
    print("Balance         := {0:>10,.2f}".format(balance(principle=1000, nYears=4, interestRate=0.08)))
    print("Balance         := {0:>10,.2f}".format(balance(nYears=4, principle=1000, interestRate=0.08)))
    print("Balance         := {0:>10,.2f}".format(balance(nYears=4, principle=1000))) 
main()
