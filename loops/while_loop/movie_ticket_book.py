choice = input("do you want book movie tickets: ")
while choice == 'y' or choice == 'Y':
    print("***Movie Ticket Booking***")
    print("1. for 2D")
    print("2. for 3D")
    print("3. for IMAX")
    print("4. for exit")
    option = int(input("enter your choice: "))
    if option == 1:
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        gender = input("enter your gender: ")
        persons = int(input("enter number of persons: "))
        amount = persons * 250
        print("*******************your ticket booked successfully*************************")
        print("your name is", name)
        print("your age is", age)
        print("your gender is", gender)
        print("payment amount is", amount)
    elif option == 2:
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        gender = input("enter your gender: ")
        persons = int(input("enter number of persons: "))
        amount = persons * 500
        print("********************your ticket booked successfully************************")
        print("your name is", name)
        print("your age is", age)
        print("your gender is", gender)
        print("payment amount is", amount)
    elif option == 3:
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        gender = input("enter your gender: ")
        persons = int(input("enter number of persons: "))
        amount = persons * 800
        print("********************your ticket booked successfully************************")
        print("your name is", name)
        print("your age is", age)
        print("your gender is", gender)
        print("payment amount is", amount)
    elif option == 4:
        print("Thank you for using movie ticket booking")
        break
    else:
        print("invalid option")
choice = input("do you want again book movie tickets: ")