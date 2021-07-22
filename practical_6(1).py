"""
Write GUI-based program that implements the tax calculator program shown in Figure 1.
"""
from tkinter import *
def calculate(btn1):
    # Initialize the constants
    TAX_RATE = 0.20
    STANDARD_DEDUCTION = 10000.00
    DEPENDENT_DEDUCTION = 3000.0
    grossIncome = float(gi.get())
    numDependents = int(dep.get())
    # compute the income TAX
    taxableIncome = grossIncome-STANDARD_DEDUCTION-DEPENDENT_DEDUCTION * numDependents
    incomeTax = taxableIncome * TAX_RATE
    # Display the income TAX_RATE
    tt.delete(0, 'end')
    tt.insert(END, str(round(incomeTax, 2)))
#window
window=Tk()
window.title('Tax Calculator')
window.geometry("500x270")
#All Label
lbl=Label(window, text="Gross Income", font=("Helvetica", 10))
lbl.place(x=0, y=0)
gi=Entry(window, text="Gross Income", bd=5)
gi.place(x=150, y=0)
lbl=Label(window, text="Dependence", font=("Helvetica", 10))
lbl.place(x=0, y=50)
dep=Entry(window, text="Dependence", bd=5)
dep.place(x=150, y=50)
lbl=Label(window, text="Total Tax", font=("Helvetica", 10))
lbl.place(x=0, y=200)
tt=Entry(window, text="Total Tax", bd=5)
tt.place(x=150, y=200)
btn1=Button(window, text="Compute")
btn1.bind('<Button-1>', calculate)
btn1.place(x=200, y=125)
window.mainloop()
