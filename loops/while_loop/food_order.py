choice = input("do you want to order food: ")
while choice == 'y' or choice == 'Y':
    print("***Food Menu***")
    print("1.veg thali")
    print("2.non veg thali")
    print("3.chinese")
    print("4.exit")
    option = int(input("enter your choice: "))
    if option == 1:
        parcels1 = int(input("enter number of parcels: "))
        amount1 = parcels1 * 150
    elif option == 2:
        parcels2 = int(input("enter number of parcels: "))
        amount2 = parcels2 * 200
        
    elif option == 3:
        parcels3 = int(input("enter number of  parcels: "))
        amount3 =  parcels3 * 250
    elif option == 4:
        name = input("enter your name: ")
        address = input("enter your address: ")
        print("*****Thank you for using food ordering app*****")
        print("***your order placed successfully***")
        print("your name is", name)
        print("your address is", address)
        parcels = parcels1 + parcels2 + parcels3
        print("Your total parcels: ", parcels)
        print("total amount of veg thali: ", amount1)
        print("total amount of non veg thali: ", amount2)
        print("total amount of chinese: ", amount3)
        Total_amount = amount1 + amount2 + amount3
        print("Total amount is", Total_amount)
        break
    else:
        print("invalid option")
choice = input("do you want to order again another option: ")