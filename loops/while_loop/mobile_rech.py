mobile = int(input("Enter mobile number: "))
choice = input("do you want to recharge mobile: ")
while choice ==  'y' or choice =="Y":
    print("***Recharge Menu***")
    print("1.Full Talktime")
    print("2.Top Up")
    print("3.Data pack")
    print("4.Exit")
    option = int(input("Enter your choice: "))
    if option == 1:
        amount = int(input("Enter amount to recharge:"))
        if amount >= 100:
            print("Your mobile", mobile, "is recharge with full talktime of", amount, "rupees successfully")
        else:
            print("invalid amount for full talktime recharge")
    elif option == 2:
        amount = int(input("ENter amount to recharge: "))
        if amount >= 10:
            print("Your mobile", mobile, "is recharge with top up of", amount, "rupees successfully")
        else:
            print("invalid amount for top up recharge")
    elif option == 3:
        amount = int(input("Enter amount to recharge: "))
        if amount >=50:
            print("Your mobile", mobile, "is recharge with data pack of", amount, "rupees successfully")
        else:
            print("invalid amount for data pack recharge")
            
    elif option == 4:
        print("Thank you for using this app")
        break
    else:
        print("Invalid option")
choice = input("do you want to recharge again  another option : ")