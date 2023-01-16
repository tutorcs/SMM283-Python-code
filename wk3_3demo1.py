https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
while True:
    try:
        ##print("\t...Line before the input...")
        rate = float(input("Enter interest rate: [0.0, 1.0]: "))
        ##print("\t...Line after input...")
        ##Use of one-way IF
        ##---------------------------------------------------
        if rate >= 0.0 and rate <= 1.0:
            print("Rate: {0:>.2%}".format(rate))
            ##You may add more statements here...
            break 
        else:
            print("\t...Interest is out of range...")
            ##You may add more statements here...
            continue         
        ##---------------------------------------------------
        
    except:
        print("\t..Ivalid data or operation with data...")
        continue
