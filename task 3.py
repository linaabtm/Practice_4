from tkinter import *

root= Tk()

def myClick():
#Обработчик событий при нажатии кнопки

    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

#Код
myButton = Button(root, text = "Click Me!", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()

root.mainloop()