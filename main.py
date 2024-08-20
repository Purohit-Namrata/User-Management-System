import tkinter as tk
from register import *
from login import *


root=tk.Tk()
root.title("User Management Sytem")
root.minsize(width=400,height=400)
root.geometry("400x400")
root.configure(bg="Orange")

l1=tk.Label(root, text="User Management System",font=15,fg="Brown")
l1.pack()

b1=tk.Button(root, text="New User? Register here",width=20,height=3,bg='brown',fg='white',command=register)
b1.pack()

b2=tk.Button(root, text="Already a user? Login here",width=20,height=3,bg='brown',fg='white',command=login)
b2.pack()

root.mainloop()
