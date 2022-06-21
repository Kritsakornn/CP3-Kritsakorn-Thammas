systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20, "ข้าวมันไก่พิเศษ": 40,"ข้าวหมกไก่":50}
menuList = []
def showMenu():
    orderNumber = 0
    for menu in systemMenu.keys():
        orderNumber += 1
        print(str(orderNumber)+". "+menu)
def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice += menuList[number][1]
    print(totalPrice)
def userMenu():
    while True:
        menuName = input("Plese Enter Menu : ")
        if (menuName.lower() == "exit"):
            break
        else:
            menuList.append([menuName, systemMenu[menuName]])
showMenu()
userMenu()
showBill()