from forex_python.converter import CurrencyRates
from forex_python.converter import CurrencyCodes
from tkinter import *

c = CurrencyRates() 
c_symbol = CurrencyCodes()

def currency_exchange(event):
    currency1 = str(textBoxCurrency1.get())
    currency2 = str(textBoxCurrency2.get())
    userAmount = int(textBoxAmount.get())
    
    convert_rate = round(c.convert(currency1,currency2,userAmount),2)
    labelResultCurrency.configure(text=str(convert_rate) + c_symbol.get_symbol(currency2))

def rate_currency(event):
    rate_user_input = str(textBoxRateUser.get())
    rate_show = round(c.get_rate('USD',rate_user_input),2)

    labelResultRate.configure(text=str(rate_show) + c_symbol.get_symbol(rate_user_input))


main = Tk()
main.title("Currency Exchange and currency rates")

labelCurrency1 = Label(main,text="สกุลเงินของท่าน : ").grid(row=0,column=0)
labelCurrency2 = Label(main,text="สกุลเงินที่ต้องการแปลง : ").grid(row=1,column=0)
labelAmount = Label(main,text="จํานวนเงินของท่าน : ").grid(row=2,column=0)

textBoxCurrency1 = Entry(main)
textBoxCurrency2 = Entry(main)
textBoxAmount = Entry(main)

textBoxCurrency1.grid(row=0,column=1)
textBoxCurrency2.grid(row=1,column=1)
textBoxAmount.grid(row=2,column=1)

calculateButtonCurrency = Button(main,text="แปลงสกุลเงิน")
calculateButtonCurrency.bind('<Button-1>',currency_exchange)
calculateButtonCurrency.grid(row=3,column=0)

labelResultCurrency = Label(main,text="ผลลัพธ์")
labelResultCurrency.grid(row=3,column=1)

labelListCurrencyUSD = Label(main,text="อัตราเงินในสกุลต่างๆต่อ 1 USD").grid(row=4,column=0)
labelRateUser = Label(main,text="อัตราสถุลที่ต้องการรู้ : ").grid(row=5,column=0)

textBoxRateUser = Entry(main)
textBoxRateUser.grid(row=5,column=1)

calculateButtonRate = Button(main,text="แสดงอัตราเงิน")
calculateButtonRate.bind('<Button-1>',rate_currency)
calculateButtonRate.grid(row=6,column=0)

labelResultRate = Label(main,text="ผลลัพธ์")
labelResultRate.grid(row=6,column=1)

main.mainloop()

