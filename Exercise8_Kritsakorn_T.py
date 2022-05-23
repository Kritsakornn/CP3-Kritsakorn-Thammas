username = input("Username : ")
password = input("Password : ")

if username == "Kritsakorn" and password == "123456789":
    print("Login success")
    print("Welcome to the dev store")
    print("-----Choose your goods-----")
    print("1. Chicken 300THB")
    print("2. Meat 200THB")
    print("3. Tomato 50THB")
    userSelected = int(input("Type the number : "))
    total_of_goods = int(input("How many do you want to buy? : "))
    chicken_price = 300
    meat_price = 200
    tomato_price = 50
    if userSelected == 1:
        price = chicken_price * total_of_goods
        print("you have to pay " + str(price) + "THB")
    elif userSelected == 2:
        price = meat_price * total_of_goods
        print("you have to pay " + str(price) + "THB")
    elif userSelected == 3:
        price = tomato_price * total_of_goods
        print("you have to pay " + str(price) + "THB")