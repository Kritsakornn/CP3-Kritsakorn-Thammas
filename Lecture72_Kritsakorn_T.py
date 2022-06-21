menuListandPrice = []
while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuListandPrice.append([menuName,menuPrice])
def showBill():
    print("------My Food------")
    for number in range(len(menuListandPrice)):
        print(menuListandPrice[number][0],end=" ")
        print(menuListandPrice[number][1])


showBill()
