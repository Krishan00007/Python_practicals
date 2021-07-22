"""
Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit 
and degrees Celsius. The interface should have labeled entry fields for these two values. These components 
should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the 
second row. At start-up, the Fahrenheit field should contain 32.0, and the Celsius field should contain 
0.0. The third row in the window contains two command buttons, labeled >>>> and <<<. When the user presses 
the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, 
which should then be output to the Celsius field. The second button should perform the inverse function.
"""
#!/usr/bin/env python3
from tkinter import *
def convert_fahr():
    words = fbtext.get()
    ftemp = float(words)
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp)))
    return
def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
def tocel(fahr):
    return (fahr-32) * 5.0 / 9.0

def tofahr(cel):
    return cel * 9.0 / 5.0 + 32
Convertor = Tk()
Convertor.title('Temperature converter')

fahrlabel = Label(Convertor, text = 'Fahrenheit')
fahrlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

cellabel = Label(Convertor, text = 'Celsius')
cellabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)
fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(Convertor, textvariable=fbtext)
fahrbox.grid(row = 0, column = 1, padx = 5, pady = 5)
cbtext = StringVar()
cbtext.set('')
celbox = Entry(Convertor, textvariable=cbtext)
celbox.grid(row = 1, column = 1, padx = 5, pady = 5)
fgobutton = Button(Convertor, text = 'convert_far to cel', command = convert_fahr)
fgobutton.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = N+S+E+W)
cgobutton = Button(Convertor, text = 'convert_cel to far', command = convert_cel)
cgobutton.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = N+S+E+W)
Convertor.mainloop()
