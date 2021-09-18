import os
def menu():
    print("          MEANU:               ")
    print("         1)Addition            ")
    print("         2)subtraction         ")
    print("         3)multiplication      ")
    print("         4)divide.             ")
    print("         5)Exit                ")
menu()

loop = 1
while loop == 1:

    ch = int(input("Please select the option :"))
    if ch == 1:
        print("Please Enter Two number for addition: ")
        x = int(input("enter 1St no plz:-"))
        y = int(input("enter 2St no plz:-"))
        def plus(x, y):
         z = x + y
         print("add of two no is ", z)
        plus(x, y)
        input("press any key to Clear........")
        os.system('cls')
        menu()
    elif ch == 2:
        print("Please Enter Two number for subtraction ")
        x = int(input("enter 1St no plz:-"))
        y = int(input("enter 2St no plz:-"))
        def su(x, y):
            z = x - y
            print("subtraction of two no is ", z)
        su(x, y)
        input("press any key to Clear........")
        os.system('cls')
        menu()
    elif ch == 3:
        print("Please Enter Two number for multiplication  ")
        x = int(input("enter 1St no plz:-"))
        y = int(input("enter 2St no plz:-"))
        def mul(x, y):
            z = x * y
            print("multiplication of two no is ", z)
        mul(x, y)
        input("press any key to Clear........")
        os.system('cls')
        menu()
    elif ch == 4:
        print("Please Enter Two number for divide:   ")
        x = int(input("enter 1St no plz:-"))
        y = int(input("enter 2St no plz:-"))
        def div(x, y):
            z = x / y
            print("divide of two no is ", z)
        div(x, y)
        input("press any key to Clear........")
        os.system('cls')
        menu()
    elif ch == 5:
        loop = 0
        print("Thank So Much !")
        input("press any key to Exit........")
        os.system('cls')
    else:
        print("Enter R8 no betwwen 1 to 5!")
        input("press any key to Clear........")
        os.system('cls')
        menu()