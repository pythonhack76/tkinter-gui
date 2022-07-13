from tkinter import *

window = Tk() 
window.geometry("500x500")

myimage = PhotoImage(file='cars_icon.png')
label = Label(window, image=myimage, bg="red")
label.place(x=0, y=0)

window.mainloop() 