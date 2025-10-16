choice = input("do you want booking bus ticket: ")
while choice == 'y' or choice == 'Y':
    print("***bus ticket booking***")
    print("1. for ac")
    print("2. for non ac")
    print("3. for sleeper")
    print("4. for exit")
    option = int(input("enter your choice: "))
    if option  == 1:
        persons1 = int(input("enter number of persons:"))
        amount1 = persons1 * 1000
    elif option == 2:
        persons2 = int(input("enter number of persons: "))
        amount2 = persons2 * 800
    elif option == 3:
        persons3 = int(input("enter number of persons: "))
        amount3 = persons3 * 500
    elif option == 4:
        print("Thank you  for using bus ticket booking")
        name = input("enter your name: ")
        age = int(input("enter your age: "))
        gender = input("enter your gender: ")
        print("***your ticket booked successfully***")
        print("your name is", name)
        print("your age is", age)
        print(" your gender is", gender)
        amount = amount1 + amount2 + amount3
        print("payment amount is", amount)
        break
    else:
        print("invalid option")
choice = input("do you want again booking bus ticket")
    