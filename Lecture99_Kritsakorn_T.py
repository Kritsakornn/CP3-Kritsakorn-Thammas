from tkinter import *
import math

def calBmi(evnet):
    height = float(textBoxHeight.get())
    weight = float(textBoxWeight.get())
    bmi = weight / math.pow(height / 100, 2)
    if bmi < 18.50:
        labelResult.configure(text="ผอมไปไอ้ก้างปลาทู!")
    elif bmi >= 18.50 and bmi <= 22.90:
        labelResult.configure(text="ปกติสุข")
    elif bmi >= 23 and bmi <= 24.90:
        labelResult.configure(text="ท้วมแล้วนะ")
    elif bmi >= 25 and bmi <= 29.90:
        labelResult.configure(text="อ้วนจัง")
    else:
        labelResult.configure(text="อ้วนมากก!")



main = Tk()
labelHeight = Label(main,text="ส่วนสูง (Cm)").grid(row=0,column=0)
labelWeight = Label(main,text="นํ้าหนัก (Kg)").grid(row=1,column=0)
textBoxHeight = Entry(main)
textBoxWeight = Entry(main)
textBoxHeight.grid(row=0,column=1)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(main,text="คํานวณ")
calculateButton.bind('<Button-1>', calBmi)
calculateButton.grid(row=2,column=0)
labelResult = Label(main,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
main.mainloop()