https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
MENU =\
'''
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 Author: Adrian Euler...
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 School: Cass Business School
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                 
       ~~~~~~~~~~~~~~~~~~Portfolio Theory~~~~~~~~~~~~
       A two-fund seperation problem.
       Portfolios of two assets drawn out of a pool
       of 4 assets (A, B, C, D)
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

       ----------MENU----------------
          1. Portfolio of A and B
          2. Portfolio of A and C
          3. Portfolio of A and D
          4. Portfolio of B and C
          5. Portfolio of B and D
          6. Portfolio of C and D
       -----------------------------
'''
print(MENU)
while True:
    try:
        choice = input("\tEnter your choice from MENU: ")
        choice = int(choice)
        if type(choice) == int and choice == 1:
            print("\t\tPortfolio of A and B...")
            ##Can add more statements
            break
        elif type(choice) == int and choice == 2:
            print("\t\tPortfolio of A and C...")
            ##Can add more statements
            break
        elif choice == 3:
            print("\t\tPortfolio of A and D...")
            ##Can add more statements
            break
        elif choice == 4:
            print("\t\tPortfolio of B and C...")
            ##Can add more statements
            break
        elif choice == 5:
            print("\t\tPortfolio of B and D...")
            ##Can add more statements
            break
        elif choice == 6:
            print("\t\tPortfolio of C and D...")
            ##Can add more statements
            break
        else:
            print("\t\tNot in the menu... (1)")
            ##Can add more statements
            continue
    except:
        print("\t\tNot in the menu...(2)")
        continue
    
