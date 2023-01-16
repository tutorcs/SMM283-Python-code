https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com

sumData = 0.0
##n = 0
while True:   ##make it an infinite loop
    try:
        data = raw_input("Enter a integer number or press \'Enter\' to quit: ")
        if data == "":
          break
        if type(data) != int:
            continue
        sumData += float(data)
       ## n += 1
    except Exception as e:
        print(".....Message: %s " % (e))
        continue

print("Sum: %.4f" % (sumData))
##print("Aver: %.4f" % (sumData/n))
