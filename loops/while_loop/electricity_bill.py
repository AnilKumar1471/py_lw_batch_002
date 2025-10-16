choice = input("do you want to calculate electricity bill: ")
while choice == 'y' or choice == "Y":
    print("***Electricity bill menu***")
    print("1.Domestic plan")
    print("2.Commercial plan")
    print("3.Exit")
    option = int( input("Enter your choice: "))
    if option == 1:
        units = int(input("Enter number of units consumed in a month: "))
        if units > 0 and units <=100:
            bill = units * 5
            print("Your electricity bill for domestic plan is: ",  bill)
        elif units > 100 and units <=200:
            bill = (100 * 5) + (units - 100) * 10
            print("Your electricity bill for domestic plan is: ", bill)
        elif units > 200:
            bill = (100 * 5) + (100 * 10) + (units - 200) * 20
            print("Your electricity bill for domestic plan is: ", bill)
        else:
            print("Invalid number of units")
    elif option == 2:
        units = int(input("Enter number of units consumed in a month: "))
        if units > 0 and units <=100:
            bill = units * 10
            print("Your electricity bill for commercial plan is: ", bill)
        elif units > 100 and units <=200:
            bill = (100 * 8) + (units - 100) * 15
            print("Your electricity bill for commercial plan is: ", bill)
        elif units > 200:
            bill = (100 * 8) + (100 * 10) + (units - 200) * 25
            print("Your electricity bill for commercial plan is: ", bill)
        else:
            print("Invalid number of units")
    elif option == 3:
        print("Thank you for using this app")
        break
    else:
        print("Invalid option")
choice = input("do you want to calculate another electricity bill: ")