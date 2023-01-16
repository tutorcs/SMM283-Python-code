https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from locale import *
##---------------------------------------------------------------------------
def balance(principle, nYears, iRate=0.04):
    balance = principle*((1+iRate)**nYears)
    return (balance)
def interestEarned(principle, nYears, iRate=0.04):
    iEarned = balance(principle, nYears, iRate) - principle
    return (iEarned)
##------------------------------------------------------------------------------------------------------------------
def main():
    setlocale(LC_ALL, '')  
    print("Balance         := {0:>10s}".format(currency(balance(1000, 1), True)))
    print("Interest Earned := {0:>10s}".format(currency(interestEarned(10000, 1), True)))
    print("Balance         := {0:>10s}".format(currency(balance(1000, 1, 0.08), True)))
    print("Interest Earned := {0:>10s}".format(currency(interestEarned(1000, 1, 0.08), True)))
    print("Balance         := {0:>10s}".format(currency(balance(iRate=0.08, principle=1000, nYears=1), True)))
    print("Interest Earned := {0:>10s}".format(currency(interestEarned(principle=1000, nYears=1, iRate=0.08), True)))
##------------------------------------------------------------------------------------------------------------------
main()
