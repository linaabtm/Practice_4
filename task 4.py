from tkinter import *

root= Tk()

e = Entry(root, width=50, bg='blue', fg = "white", borderwidth = 5)
e.pack()
e.insert(0, "Enter Your Name: ")
def myClick():
#Обработчик событий при нажатии кнопки
    hello="Hello "+e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

#Код
myButton = Button(root, text = "Enter your name", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()

root.mainloop()