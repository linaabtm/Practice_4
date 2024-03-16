import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("600x300")

number_entry = ttk.Entry(width=40)
number_entry.grid(row=0, column=0, columnspan=4, padx=4, pady=4)

def button_click(number):
    current = number_entry.get()
    number_entry.delete(0, tk.END)
    number_entry.insert(0, str(current) + str(number))

def button_add():
    global f_num
    global math
    first_number = number_entry.get()
    math = "addition"
    f_num = int(first_number)
    number_entry.delete(0, tk.END)

def button_subtract():
    global math
    global f_num
    first_number = number_entry.get()
    math = "subtraction"
    f_num = int(first_number)
    number_entry.delete(0, tk.END)

def button_multiply():
    global math
    global f_num
    first_number = number_entry.get()
    math = "multiplication"
    f_num = int(first_number)
    number_entry.delete(0, tk.END)

def button_divide():
    global math
    global f_num
    first_number = number_entry.get()
    math = "division"
    f_num = int(first_number)
    number_entry.delete(0, tk.END)

def button_equal():
    second_number = number_entry.get()
    number_entry.delete(0, tk.END)

    if math == "addition":
        number_entry.insert(0, f_num + int(second_number))

    if math == "multiplication":
        number_entry.insert(0, f_num * int(second_number))

    if math == "division":
        if ZeroDivisionError:
            number_entry.delete(0, tk.END)
            number_entry.insert(0, 'Ошибка (деление на 0)')
        else:
            number_entry.insert(0, f_num / int(second_number))

    if math == "subtraction":
       number_entry.insert(0, f_num - int(second_number))


button_1 = ttk.Button(text="1", command=lambda: button_click(1))
button_2 = ttk.Button(text="2", command=lambda: button_click(2))
button_3 = ttk.Button(text="3", command=lambda: button_click(3))
button_4 = ttk.Button(text="4", command=lambda: button_click(4))
button_5 = ttk.Button(text="5", command=lambda: button_click(5))
button_6 = ttk.Button(text="6", command=lambda: button_click(6))
button_7 = ttk.Button(text="7", command=lambda: button_click(7))
button_8 = ttk.Button(text="8", command=lambda: button_click(8))
button_9 = ttk.Button(text="9", command=lambda: button_click(9))
button_0 = ttk.Button(text="0", command=lambda: button_click(0))
button_clear = ttk.Button(text="C", command=lambda: number_entry.delete(0, tk.END))
button_add = ttk.Button(text="+", command=button_add)
button_equal = ttk.Button(text="=", command=button_equal)
button_subtract = ttk.Button(text="-", command=button_subtract)
button_multiply = ttk.Button(text="*", command=button_multiply)
button_divide = ttk.Button(text="/", command=button_divide)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

root.mainloop()
