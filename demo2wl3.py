https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#--------------------------------------------------------
rate = input("Enter interest rate (0.0 to 1.0): ")
print(rate)
##------------------------------------------------------

while True:
    try:
        rate = input("Enter interest rate (0.0 to 1.0): ")
        if rate >=0.0 and rate <= 1.0:
            break
        else:
            print("\tOut of range..re-try!")
            continue
    except Exception as e:
        ##print("\tThe %s" % (e))
        print((e))
        continue
print(rate)
