bal = 50000
choice =  input("do you want perform operation: ")
while choice == 'y' or choice == 'Y':
    print('***Bank App Menu***')
    print('1.Deposite')
    print('2.Withdraw')
    print('3.Check Balance')
    print('4.Exit')
    option = int(input("Enter your choice: "))
    if option == 1:
        amount = int(input("Enter amount to deposite: "))
        if amount >0 and amount <=50000:
            bal = bal + amount
            print("Amount Deposited Succesufully")
        else:
            print("Invalid Amount")
    elif option == 2:
        amount = int(input("Enter amount to withdraw : " ))
        if amount > 0 and amount <=bal:
            bal = bal - amount
            print ("Please collect your cash")
        else:
            print("insufficient balance")
            
    elif option == 3:
        print("Available balance is : ", bal)
    elif option == 4:
        print("Thank you for using this app")
        break
    else:
        print("Invalid option")
        
        
choice = input("do you want to perform another operation:")