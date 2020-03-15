from tkinter import *

root = Tk()
root.title("images")

root.iconbitmap('DN_Logo.ico')

button_quit = Button(root, text ="Exit Program", command=root.quit)

button_quit.pack()

root.mainloop()

