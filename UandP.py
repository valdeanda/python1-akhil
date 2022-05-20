manager = {}
username = input("Username: ")
password = input("Password: ")
manager[username] = password
check = input("Check Password: ")
if check == manager.get(username):
    print("Correct Password")
else:
    print("Wrong Password")
