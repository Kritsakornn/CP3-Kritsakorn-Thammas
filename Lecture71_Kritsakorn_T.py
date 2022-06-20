menuList = []
menupriceList = []
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        menupriceList.append(menuPrice)
def showBill():
    totalPrice = 0
    print("------My Food------")
    for number in range(len(menuList)):
        print(menuList[number],menupriceList[number])
        totalPrice += menupriceList[number]
    print("TotalPrice =",totalPrice,"THB")


showBill()
