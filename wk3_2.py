https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
sumData = 0.0
while True:
    try:
        data = raw_input("Enter a number: ")
        if data != "":
            number = float(data)
            sumData += number
        else:
            break
    except:
        break
print("Sum: {0:>10,.2f}".format(sumData))
