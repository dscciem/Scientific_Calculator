import math
from tkinter import *
from tkinter.messagebox import *


# variables
font = ('Helvetica', 22)


# creating a window
window = Tk()
window.title('Scientific Calculator')
window.geometry('425x505')

# adding textfield
textField = Entry(window, font=font, justify=RIGHT)
textField.pack(side=TOP, pady=20, fill=X, padx=10)

# creating frame for buttons
buttonFrame = Frame(window)
buttonFrame.pack(side=TOP)

# functions

# equals function
def equals():
   ans = textField.get()
   ans = eval(ans)
   textField.delete(0, END)
   textField.insert(0, ans)

# delete function
def delete():
    exp = textField.get()
    exp = exp[0:len(exp)-1]
    textField.delete(0, END)
    textField.insert(0, exp)

# all clear function
def allclear():
    textField.delete(0, END)

# button click function
def btn_click_func(event):
    print("Button clicked")
    button = event.widget
    text = button['text']
    print(text)
    if text == 'x':
        textField.insert(END, '*')

    elif text == '÷':
        textField.insert(END, '/')
    else:
        textField.insert(END, text)

# scientific calculator function
def sccalc(event):
    print("sc button clicked")
    button = event.widget
    text = button['text']
    print(text)
    num = textField.get()
    result = ''

    if text == 'e':
        if num == "":
            result = str(math.e)
        else:
            result = str(math.e*float(num))

    elif text == 'x!':
        print("Calculate factorial")
        result = str(math.factorial(float(num)))

    elif text == 'π':
        print("calculate pi")
        if num == "":
            result = str(math.pi)
        else:
            result = str(float(num)*math.pi)

    elif text == '1/x':
        print("calculate inverse")
        result = str(1/(float(num)))

    elif text == '²√':
        print("Calculate square root")
        result = str(math.sqrt(float(num)))

    elif text == '³√':
        print("calculate cube root")
        result = math.pow(float(num), (1.0/3.0))

    elif text == 'x²':
        print("calculate square")
        result = math.pow(float(num), 2)

    elif text == 'x³':
        print("calculate cube")
        result = math.pow(float(num), 3)

    elif text == 'sin':
        print("calculate sin")
        result = str(math.sin(float(num)))

    elif text == 'cos':
        print("calculate cos")
        result = str(math.cos(float(num)))

    elif text == 'tan':
        print("calculate tan")
        result = str(math.tan(float(num)))

    elif text == 'log':
        print("calculate log")
        result = str(math.log10(float(num)))

    elif text == 'ln':
        print("calculate natural log")
        result = str(math.log(float(num)))

    elif text == 'Deg':
        print("calculate degree")
        result = str(math.degrees(float(num)))

    elif text == 'Rad':
        print("calculate radian")
        result = str(math.radians(float(num)))

    textField.delete(0, END)
    textField.insert(END, result)

# creating buttons from 1 to 9 by using grid
temp = 9
for i in range(0, 3):
    j = 2
    while (j>= 0):
        btn = Button(buttonFrame, text=str(temp), font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
        btn.grid(row=i, column=j)
        temp -= 1
        j -= 1
        btn.bind('<Button-1>', btn_click_func)


delBtn = Button(buttonFrame, text='DEL', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white', command=delete)
delBtn.grid(row=0, column=3)

acBtn = Button(buttonFrame, text='AC', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white', command=allclear)
acBtn.grid(row=0, column=4)

mulBtn = Button(buttonFrame, text='x', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
mulBtn.grid(row=1, column=3)
mulBtn.bind('<Button-1>', btn_click_func)

divBtn = Button(buttonFrame, text='÷', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
divBtn.grid(row=1, column=4)
divBtn.bind('<Button-1>', btn_click_func)

addBtn = Button(buttonFrame, text='+', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
addBtn.grid(row=2, column=3)
addBtn.bind('<Button-1>', btn_click_func)

subBtn = Button(buttonFrame, text='-', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
subBtn.grid(row=2, column=4)
subBtn.bind('<Button-1>', btn_click_func)

zeroBtn = Button(buttonFrame, text='0', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
zeroBtn.grid(row=3, column=0)
zeroBtn.bind('<Button-1>', btn_click_func)

dotBtn = Button(buttonFrame, text='.', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
dotBtn.grid(row=3, column=1)
dotBtn.bind('<Button-1>', btn_click_func)

piBtn = Button(buttonFrame, text='π', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
piBtn.grid(row=3, column=2)
piBtn.bind('<Button-1>', sccalc)

inverseBtn = Button(buttonFrame, text='1/x', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
inverseBtn.grid(row=3, column=3)
inverseBtn.bind('<Button-1>', sccalc)

equalBtn = Button(buttonFrame, text='=', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white', command= lambda: equals())
equalBtn.grid(row=3, column=4)
equalBtn.bind('<Button-1>')

sqrtBtn = Button(buttonFrame, text='x²', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
sqrtBtn.grid(row=4, column=0)
sqrtBtn.bind('<Button-1>', sccalc)

sqrBtn = Button(buttonFrame, text='x³', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
sqrBtn.grid(row=4, column=1)
sqrBtn.bind('<Button-1>', sccalc)

cubeBtn = Button(buttonFrame, text='²√', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
cubeBtn.grid(row=4, column=2)
cubeBtn.bind('<Button-1>', sccalc)

powBtn = Button(buttonFrame, text='³√', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
powBtn.grid(row=4, column=3)
powBtn.bind('<Button-1>', sccalc)

factBtn = Button(buttonFrame, text='x!', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
factBtn.grid(row=4, column=4)
factBtn.bind('<Button-1>', sccalc)

sinBtn = Button(buttonFrame, text='sin', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
sinBtn.grid(row=5, column=0)
sinBtn.bind('<Button-1>', sccalc)

cosBtn = Button(buttonFrame, text='cos', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
cosBtn.grid(row=5, column=1)
cosBtn.bind('<Button-1>', sccalc)

tanBtn = Button(buttonFrame, text='tan', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
tanBtn.grid(row=5, column=2)
tanBtn.bind('<Button-1>', sccalc)

logBtn = Button(buttonFrame, text='log', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
logBtn.grid(row=5, column=3)
logBtn.bind('<Button-1>', sccalc)

lnBtn = Button(buttonFrame, text='ln', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
lnBtn.grid(row=5, column=4)
lnBtn.bind('<Button-1>', sccalc)

bracesopenBtn = Button(buttonFrame, text='(', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
bracesopenBtn.grid(row=6, column=0)
bracesopenBtn.bind('<Button-1>', btn_click_func)

bracescloseBtn = Button(buttonFrame, text=')', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
bracescloseBtn.grid(row=6, column=1)
bracescloseBtn.bind('<Button-1>', btn_click_func)

combinationBtn = Button(buttonFrame, text='Deg', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
combinationBtn.grid(row=6, column=2)
combinationBtn.bind('<Button-1>', sccalc)

permutationBtn = Button(buttonFrame, text='Rad', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
permutationBtn.grid(row=6, column=3)
permutationBtn.bind('<Button-1>', sccalc)

percentBtn = Button(buttonFrame, text='e', font=font, relief='ridge', width=4, activebackground='grey', activeforeground='white')
percentBtn.grid(row=6, column=4)
percentBtn.bind('<Button-1>', sccalc)

window.mainloop()
