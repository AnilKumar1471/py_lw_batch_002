choice = input("do you want to calculate water bill: ")
while choice == 'y' or choice == "Y":
    print("***water bill menu***")
    print("1.water plan 1")
    print("2.water plan 2")
    print("3.Exit")
    option = int( input("Enter your choice: "))
    if option == 1:
        water_cans = int(input("Enter number of water cans used in a month: "))
        if water_cans > 0 and water_cans <=15:
            bill = water_cans * 20
            print("Your water bill for plant 1 is: ",  bill)
        elif water_cans > 15 and water_cans <=30:
            bill = (15 * 20) + (water_cans - 15) * 25
            print("Your water bill for plant 1 is: ", bill)
        elif water_cans > 30:
            bill = (15 * 20) + (15 * 25) + (water_cans - 30) * 30
            print("Your water bill for plant 1 is: ", bill)
        else:
            print("Invalid number of water cans")
    elif option == 2:
        water_cans = int(input("Enter number of water cans used in a month: "))
        if water_cans > 0 and water_cans <=10:
            bill = water_cans * 15
            print("Your water bill for plant 2 is: ", bill)
        elif water_cans > 10 and water_cans <=25:
            bill = (10 * 15) + (water_cans - 10) * 25
            print("Your water bill for plant 2 is: ", bill)
        elif water_cans > 25:
            bill = (10 * 15) + (15 * 25) + (water_cans - 25) * 35
            print("Your water bill for plant 2 is: ", bill)
        else:
            print("Invalid number of water cans")
    elif option == 3:
        print("Thank you for using this app")
        break
    else:
        print("Invalid option")
choice = input("do you want to calculate another water bill: ")