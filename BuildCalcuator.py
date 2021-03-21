from tkinter import *
import math
root = Tk()
root.title("Simple Calculator")

e = Entry(root,font=('arial',35,'bold'), width=10, bg='powder blue', bd=30,  borderwidth=15, justify=RIGHT)
e.grid(row=0, column=0, columnspan=5, pady=1)

root.configure(background="powder blue")


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    if math == "addition":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num+float(second_number))
    elif math == "multiplication":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num*float(second_number))
    elif math == "subtraction":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num-float(second_number))
    elif math == "division":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, f_num / float(second_number))
    elif math == "sqrt":
        e.insert(0, f_num**0.5)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


button_1 = Button(root, padx=30, pady=20, bd=4, text="1", font=('arial', 10, 'bold'),bg='#856ff8', command=lambda: button_click(1))
button_2 = Button(root, padx=30, pady=20, bd=4, text='2', font=('arial', 10, 'bold'), bg='#856ff8',  command=lambda: button_click(2))
button_3 = Button(root, padx=30, pady=20, bd=4, text='3', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(3))
button_4 = Button(root,  padx=30, pady=20, bd=4, text='4', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(4))
button_5 = Button(root, padx=30, pady=20, bd=4, text='5', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(5))
button_6 = Button(root, padx=30, pady=20, bd=4, text='6', font=('arial', 10, 'bold'),  bg='#856ff8', command=lambda: button_click(6))
button_7 = Button(root, padx=30, pady=20, bd=4, text='7', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(7))
button_8 = Button(root, padx=30, pady=20, bd=4, text='8', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(8))
button_9 = Button(root, padx=30, pady=20, bd=4, text='9', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(9))
button_0 = Button(root, padx=30, pady=20, bd=4, text='0', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click(0))

button_clear = Button(root, padx=30, pady=20, bd=4, text='C', font=('arial', 10, 'bold'), bg='#856ff8', command=button_clear)
button_add = Button(root,  padx=30, pady=20, bd=4, text='+', font=('arial', 10, 'bold'), bg='#856ff8', command=button_add)
button_equal = Button(root, padx=30, pady=20, bd=4, text='=', font=('arial', 10, 'bold'), bg='#856ff8', command=button_equal)


button_subtract = Button(root, padx=32, pady=20, bd=4, text='-', font=('arial', 10, 'bold'), bg='#856ff8', command=button_subtract)
button_multiply = Button(root, padx=31, pady=20, bd=4, text='*', font=('arial', 10, 'bold'), bg='#856ff8', command=button_multiply)
button_divide = Button(root, padx=32, pady=20, bd=4, text='/', font=('arial', 10, 'bold'), bg='#856ff8', command=button_divide)

button_sqrt =  Button(root, padx=30, pady=20, bd=4, text='√', font=('arial', 10, 'bold'), bg='#856ff8', command=button_sqrt)
button_CE =  Button(root, padx=25, pady=20, bd=4, text='CE', font=('arial', 10, 'bold'), bg='#856ff8')
button_point =  Button(root, padx=30, pady=20, bd=4, text='.', font=('arial', 10, 'bold'), bg='#856ff8',command=lambda: button_click('.'))
button_zero = Button(root, padx=28, pady=20, bd=4, text='00', font=('arial', 10, 'bold'), bg='#856ff8', command=lambda: button_click('00'))

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_sqrt.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=1, column=1)
button_CE.grid(row=1, column=0)
button_point.grid(row=5, column=2)
button_zero.grid(row=5, column=1)
button_add.grid(row=1, column=3)
button_equal.grid(row=5, column=3)

button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
root.mainloop()
