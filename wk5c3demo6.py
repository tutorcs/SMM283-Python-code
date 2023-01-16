https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from locale import *
INTEREST_RATE = 0.04
##---------------------------------------------------------------------------
def balanceAndInterest(principle, nYears):
    balance = principle*((1+INTEREST_RATE)**nYears)
    interestEarned = balance - principle
    return (balance, interestEarned)
##---------------------------------------------------------------------------
def main():
    setlocale(LC_ALL, '')
    while True:
        try:
            principle = input("Enter deposit amount: ")
        except:
            continue
        if principle < 0.0:
            continue
        else:
            break
    while True:
        try:
            nYears = input("Enter number of years: ")
        except:
            continue
        if nYears < 0:
            continue
        else:
            break
    balance, interestEarned = balanceAndInterest(principle, nYears)
    print("Balance         := {0:>10s}".format(currency(balance, True)))
    print("Interest Earned := {0:>10s}".format(currency(interestEarned, True)))
##---------------------------------------------------------------------------
main()
