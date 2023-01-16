https://tutorcs.com
WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
MENU = \
"""
        ~~~~~~~~~~~~~~~Portfolio Theory~~~~~~~~~~~~~~~~~~~~~~~
        ** A two-fund seperation problem in finance         **
        ** Selecting from a pool of four assets (A, B, C, D)**
        ** Author: Adrian Euler
        ** School: Cass
        **~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**

                -----------MENU-----------
                   1. Portfolio of A & B   
                   2. Portfolio of A & C
                   3. Portfolio of A & D
                   4. Portfolio of B & C
                   5. Portfolio of B & D
                   6. Portfolio of C & D
                --------------------------

"""
print(MENU)

while True:
    yesNo = raw_input("\t\tWish to make a  choice/new choice (yes/no)? ")
    if lower(yesNo) == "yes":
        while True:
            try:
                choice = input("\t\tEnter your choice: ")
                if choice == 1:
                    print("\t\t...Portfolio of A & B...")
                
                    ##Add more statements..calculations, etc..
                elif choice == 2:
                    print("\t\t...Portfolio of A & C...")
                    ##Add more statements..calculations, etc..
                    break
                elif choice == 3:
                    print("\t\t...Portfolio of A & D...")
                    ##Add more statements..calculations, etc..
                    break
                elif choice == 4:
                    print("\t\t...Portfolio of B & C...")
                    ##Add more statements..calculations, etc..
                    break
                elif choice == 5:
                    print("\t\t...Portfolio of B & D...")
                    ##Add more statements..calculations, etc..
                    break
                elif choice == 6:
                    print("\t\t...Portfolio of C & D...")
                    ##Add more statements..calculations, etc..
                    break
                else:
                    print("\t\t...Ivalid data (1)......")
                    continue
            except Exception:
                ##print("\t\t...Invalid input in this program (2)......")
                continue
    else:
        break



