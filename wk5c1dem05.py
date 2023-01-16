https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
import locale as l
INTEREST_RATE = 0.04
def balanceAndInterest(principle, numYears):
    balance = principle*((1+INTEREST_RATE)**numYears)
    interestEarned = balance - principle
    return (balance, interestEarned)
def getInput(msg):
    while True:
        try:
            prin = input(msg)
            nYears = input()
        except:
            print("\t...Enter principle, then press \'Enter\', then number of years....\n")
            continue
        else:
            break
    return (prin, nYears)
def main():
    l.setlocale(l.LC_MONETARY, '')
    principle, nYears = getInput("Enter deposit amount and number of years? ")
    balance, intEarned = balanceAndInterest(principle, nYears)
    print("Balance:={0:>10s}\nInterest Earned:={1:>10s}".format(l.currency(balance, True), \
                                                                      l.currency(intEarned, True)))
##---------------------------------------------------------------------------------
main()
