import tkinter as tk
from tkinter import messagebox
import re
import pymysql
import bcrypt
import csv

def register():
    def checkPassword(password):
        upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
        length = len(password)

        if (length < 6):
            pwd_strength_lbl.config(text="Password must be at least 6 characters long!\n")
        else:
            for i in range(0, length):
                if (password[i].isupper()):
                    upperChars += 1
                elif (password[i].islower()):
                    lowerChars += 1
                elif (password[i].isdigit()):
                    digits += 1
                else:
                    specialChars += 1


        if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
            if (length >= 10):
                pwd_strength_lbl.config(text="Password strength: Strong")
            else:
                pwd_strength_lbl.config(text="Password strength: Medium")
        else:
            if (upperChars == 0):
                pwd_strength_lbl1.config(text="Password must contain at least one uppercase character!\n")
            if (lowerChars == 0):
                pwd_strength_lbl2.config(text="Password must contain at least one lowercase character!\n")
            if (specialChars == 0):
                pwd_strength_lbl3.config(text="Password must contain at least one special character!\n")
            if (digits == 0):
                pwd_strength_lbl4.config(text="Password must contain at least one digit!\n")

    def submit():
        info1=un_entry.get()
        if not re.match(r'^[A-Za-z\s]+$',info1):
            messagebox.showinfo("Error","Please enter valid username")
            return
        info2=pwd_entry.get()
        checkPassword(info2)

        info3=email_entry.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not (re.fullmatch(regex, info3)):
            messagebox.showinfo("Error","Please enter a valid email id")
            return

        if(info1=="" or info2=="" or info3==""):
            messagebox.showinfo("Insert status","All fields are required")
            return
        else:
            username=un_entry.get()
            pwd=pwd_entry.get()
            email=email_entry.get()
            
            #hashedpwd = hash(pwd) 
            with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", "r") as file:
                reader=csv.reader(file)
                for row in reader:
                    if username==row[0]:
                        messagebox.showinfo("Error","Username already exist")
                        return
            with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([username, pwd, email])
            messagebox.showinfo("Success", "User added successfully!")
            un_entry.delete(0,tk.END)
            pwd_entry.delete(0,tk.END)
            email_entry.delete(0,tk.END)


    root=tk.Tk()
    root.title("Register page")
    root.geometry("600x600")
    root.configure(bg="orange")
    l1=tk.Label(root, text="Register",font=10,fg="brown")
    l1.grid(row=0,column=1)
    un_lbl=tk.Label(root, text="Username: ",fg="brown")
    un_lbl.grid(row=2,column=0)
    un_entry=tk.Entry(root)
    un_entry.grid(row=2,column=1)

    pwd_lbl=tk.Label(root, text="Password: ",fg="brown")
    pwd_lbl.grid(row=3,column=0)
    pwd_entry=tk.Entry(root,show="*")
    pwd_entry.grid(row=3,column=1)
    pwd_strength_lbl=tk.Label(root,fg="brown")
    pwd_strength_lbl.grid(row=4,column=1)
    pwd_strength_lbl1=tk.Label(root,fg="brown")
    pwd_strength_lbl1.grid(row=5,column=1)
    pwd_strength_lbl2=tk.Label(root,fg="brown")
    pwd_strength_lbl2.grid(row=6,column=1)
    pwd_strength_lbl3=tk.Label(root,fg="brown")
    pwd_strength_lbl3.grid(row=7,column=1)
    pwd_strength_lbl4=tk.Label(root,fg="brown")
    pwd_strength_lbl4.grid(row=8,column=1)

    email_lbl=tk.Label(root, text="Email: ",fg="brown")
    email_lbl.grid(row=9,column=0)
    email_entry=tk.Entry(root)
    email_entry.grid(row=9, column=1)

    submit_btn=tk.Button(root, text="Submit",command=submit,bg="brown",fg="white")
    submit_btn.grid(row=10,column=1)
    root.mainloop()
