from tkinter import *

root = Tk()
def myClick():
    myLabel = Label(root, text="I clicked it")
    myLabel.pack()

myButton = Button(root, text="Click me!", command = myClick, fg="blue", bg="#ffd3b6")
myButton.pack()

root.mainloop()