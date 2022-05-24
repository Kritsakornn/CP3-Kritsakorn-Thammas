username = input("Username : ")
password = input("Password : ")
while username != "admin" or password != "1234":
    print("Wrong password or username")
    username = input("Username : ")
    password = input("Password : ")
print("Done.")
