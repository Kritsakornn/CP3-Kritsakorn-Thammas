def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">> "))
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * 7 / 100)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

login = login()
if login == True:
    showMenu()
    UserSelected = menuSelect()
    if UserSelected == 1:
        totalPrice = int(input("Price (THB): "))
        print(vatCalculate(totalPrice))
    elif UserSelected == 2:
        print(priceCalculate())
elif login == False:
    print("Wrong password or username.")



