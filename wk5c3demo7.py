https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
from locale import *
##---------------------------------------------------------------------------
def balance(principle, nYears, iRate):
    balance = principle*((1+iRate)**nYears)
    return (balance)
def interestEarned(principle, nYears, iRate):
    iEarned = balance(principle, nYears, iRate) - principle
    return (iEarned)
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
    bval = balance(principle, nYears, 0.04)
    iearned = interestEarned(principle, nYears, 0.04)
    print("Balance         := {0:>10s}".format(currency(bval, True)))
    print("Interest Earned := {0:>10s}".format(currency(iearned, True)))
##---------------------------------------------------------------------------
main()
