https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#A simple  Python program
##START
s = float(0.0) ##stock price, starting at 0.0
k =  float(raw_input("Enter option's strike price: "))
##k = float(70.0) ##option exercise price
fileName = "myData1.xls"
myFile = open(fileName, "w")
myFile.write("Stock Price\tCall Payout\n")
for i in range(10):
    cpo = max(s-k, 0)
    myFile.write(str(s) + '\t' + str(cpo) + '\n')
    s = s + 10.0   
myFile.close()
##END
