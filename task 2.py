from tkinter import *

root= Tk()
#Основной цикл создания виджета (элемента) на экране
#Создание виджета
myLabel = Label(root, text = "Hello World!")
myLabel.grid(column=0, row= 0)
myLabel1 = Label(root, text = "My name is Lisichenko Natalya")
myLabel1.grid(column=1, row= 1)
#Разместили виджет на экран


root. mainloop()
