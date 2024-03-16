from tkinter import *

root = Tk()
#Основной цикл создания виджета (элемента) на экране
#Создание виджета
myLabel = Label(root, text = "Hello World!")
myLabel.grid(column=0, row= 0)
#Разместили виджет на экран
myLabel.pack()
root. mainloop()
