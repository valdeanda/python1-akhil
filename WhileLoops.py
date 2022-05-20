stillGoing = True
BankAccounts = {}
while stillGoing:
    print("What would you like to do today?")
    print("1. Sign up for an account")
    print("2. Log into an account")
    print("3. Quit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Choice isn't an integer, try again")
    if choice == 1:
        newUsername = input("Enter a username: ")
        newPassword = input("Enter a password: ")
        BankAccounts[newUsername] = newPassword
    elif choice == 2:
        Username = input("Enter a username: ")
        try:
            Password = BankAccounts.get(Username)
            if input("Enter a password: ") == Password:
                print("Authorized")
            else:
                print("Denied Access, please try again")
        except:
            print("Username isn't recognized, please try again")
    elif choice == 3:
        stillGoing = False
    else:
        print("Choice isn't recognized, please try again")
    print()
