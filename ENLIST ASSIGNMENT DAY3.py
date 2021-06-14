from tkinter import*
from tkinter import ttk
from typing import Any, Union

window = Tk()
window.title("Registration Screen")
window.geometry('600x600')
window.configure(background = "Blue")

Firstname = Label(window,text = "First Name").grid(row=0,column=0)
Lastname = Label(window,text = "Last Name").grid(row=1,column=0)
Email = Label(window,text = "Email id").grid(row=2,column=0)
Mobile = Label(window,text = "Contact Number").grid(row=3,column=0)
Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)

def clicked():
    res = "Welcome to"+ txt.get()
    Ibl.configure(text = res)
btn = ttk.Button(window,text="Submit").grid(row=4,column=0)
window.mainloop()