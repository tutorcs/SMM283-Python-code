https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com

def balance(principle, nYears=10, intRate=0.04):
    balance = principle * ((1+intRate)**nYears)
    return balance
def main():
    print('Balance')
    print('~~~~~~~~~~~~')
    print('{0:,.2f}'.format(balance(1000.0, 10)))
    print('{0:,.2f}'.format(balance(1000.0, intRate=0.04, nYears= 10)))
    print('{0:,.2f}'.format(balance(principle=1000.0, intRate=0.04, nYears= 10)))
    print('{0:,.2f}'.format(balance(1000.0)))
    print('~~~~~~~~~~~~')
    print('{0:,.2f}'.format(balance(principle=100.0, intRate=0.08, nYears= 5)))
main()
