import tkinter as tk
from tkinter import messagebox
import csv
from PIL import ImageTk,Image
import os 
import pandas as pd
import re
from tkinter import PhotoImage,Label


def login():
    def adminlogin():
        def adminpage():
            
            def viewall():
                if os.path.exists("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv"):
                    with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", "r") as file:
                        reader = csv.reader(file)
                        users = [row for row in reader]
                        if users:
                            users_info = "\n".join(["USERNAME: {}, PASSWORD: {}, EMAIL: {}".format(*user) for user in users])
                            messagebox.showinfo("Users List", users_info)
                        else:
                            messagebox.showinfo("Users List", "No user found.")
                else:
                    messagebox.showinfo("Users List", "The user list is empty.")
            
            
            def deleteacc():
                def deleterow():
                    un=e1.get()
                    if un=="":
                        messagebox.showinfo("Error","Please enter Username")
                        return
                    if not re.match(r'^[A-Za-z\s]+$',un):
                        messagebox.showinfo("Error","Please enter a valid username")
                        return
                    
                    df = pd.read_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv')
                    df = df.drop(df[df.Username == un].index)
                    df.to_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv', index=False)
                                    
                    messagebox.showinfo("Success","Account deleted")
                
                lbl=tk.Label(root1,text="Enter username to delete account",fg="Brown")
                lbl.grid(row=6,column=0)
                e1=tk.Entry(root1)
                
                e1.grid(row=6,column=1)
                
                b1=tk.Button(root1,text="Delete",command=deleterow,bg="Brown",fg="White")
                b1.grid(row=8,column=1)
                              
            def logout():
                answer=messagebox.askyesno("Sure?","Are you sure you want to logout?")
                if answer:
                    root1.destroy()
                    messagebox.showinfo("Success","Admin successfully logged out")
                    login()
                else:
                    adminpage()
            
            root1=tk.Tk()
            root1.geometry("400x400")
            root1.title("Admin page")
            root1.configure(bg="orange")
            l1=tk.Label(root1, text="Welcome, Admin!",font=10,fg="Brown")
            l1.grid(row=1,column=1)
            b1=tk.Button(root1, text="View all users",command=viewall,fg="white",bg="brown")
            b1.grid(row=3,column=0)
            b2=tk.Button(root1,text="Delete accounts",command=deleteacc,fg="white",bg="brown")
            b2.grid(row=3,column=1)
            b3=tk.Button(root1, text="Logout",command=logout,fg="white",bg="brown")
            b3.grid(row=3,column=2)
            root1.mainloop()

        username=un_entry.get()
        pwd=pwd_entry.get()
        if username=="" or pwd=="":
            messagebox.showinfo("Insert status","All fields are required")
        
        if username=="admin" and pwd=="admin":
            messagebox.showinfo("Admin logged in ","Welcome, Admin!")
            adminpage()
            
        else:
            messagebox.showinfo("Error","Invalid username or passord")    

    def loginpage():
               
        def uploadimage():
            def upload():
                info1=str(path_entry.get())
                if info1=="":
                    messagebox.showinfo("Error","PLease enter path")
                    return
                frame = tk.Frame(root2, width=200, height=200, bg="white")
                frame.grid(row=5,column=5,pady=20)  # Adjust padding as necessary
                image=Image.open(info1)
                image = image.resize((200, 200), Image.Resampling.LANCZOS)
                photo_image=ImageTk.PhotoImage(image)
                l3=tk.Label(frame,image=photo_image,bd=2,relief="raised")
                l3.pack()
                

            lbl=tk.Label(root2, text="Enter path to upload image",fg="brown")
            lbl.grid(row=3,column=1)
            path_entry=tk.Entry(root2,width=20)
            path_entry.grid(row=4,column=1)
            b1=tk.Button(root2,text="Upload",command=upload,bg="brown",fg="white")
            b1.grid(row=5,column=1)
        
        def viewprofile():
            def view():
                un=e1.get()
                if not re.match(r"^[A-Za-z\s]+$",un):
                    messagebox.showinfo("Error","Please enter valid Username")
                    return
                if os.path.exists("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv"):
                    with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", "r") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            if un in row:
                                messagebox.showinfo("User Details", f"Username: {row[0]}\nPassword: {row[1]}\nEmail: {row[2]}")
                                return                           
                    
            l1=tk.Label(root2,text="Enter username",fg="Brown")
            l1.grid(row=7,column=0)
            e1=tk.Entry(root2)
            e1.grid(row=8,column=0)
            b1=tk.Button(root2,text="View profile",bg="brown",fg="white",command=view)
            b1.grid(row=9,column=1)
            
                    
        def updateprofile():
            def update():
                def update_un():
                    oldun=e1.get()
                    newun=e2.get()
                    if oldun=="" or newun=="":
                        messagebox.showinfo("Error","All fields are required")

                    if not re.match(r"^[A-Za-z\s]+$",oldun):
                        messagebox.showinfo("Error","Please enter valid old username")
                        return
                    if not re.match(r"^[A-Za-z\s]+$",newun):
                        messagebox.showinfo("Error","Please enter valid new username")
                        return
                    
                    df = pd.read_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv") 
                    df['Username'] = df['Username'].replace({oldun: newun}) 
                    df.to_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", index=False) 
               
                    messagebox.showinfo("Success","Username updated succesfully")
               
                selecteditem=t1.get(0)
                if selecteditem=="Username":
                    l1=tk.Label(root2,text="Enter old username and new username ",fg="Brown")
                    l1.grid(row=10,column=1)

                    e1=tk.Entry(root2)
                    e1.grid(row=11,column=1)
                    e2=tk.Entry(root2)
                    e2.grid(row=12,column=1)
                                        
                    updateun_btn=tk.Button(root2,text="Update Username",fg="white",bg="brown",command=update_un)
                    updateun_btn.grid(row=5,column=1)
                     
                def update_em():
                    oldemail=e1.get()
                    newemail=e2.get()
                    if oldemail=="" or newemail=="":
                        messagebox.showinfo("Error","All fields are required")
                    
                    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

                    if not (re.fullmatch(regex, oldemail)):
                        messagebox.showinfo("Error","Please enter a valid old email id")
                        return
                    
                    if not (re.fullmatch(regex, newemail)):
                        messagebox.showinfo("Error","Please enter a valid new email id")
                        return

                    df = pd.read_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv") 
                    df['Username'] = df['Username'].replace({oldemail: newemail}) 
                    df.to_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", index=False) 
               
                    messagebox.showinfo("Success","Email updated succesfully")
    
                selecteditem=t1.get(1)
                if selecteditem=="Email":
                    l1=tk.Label(root2,text="Enter old email and new email ",fg="Brown")
                    l1.grid(row=12,column=4)
                    e1=tk.Entry(root2)
                    e1.grid(row=14,column=4)
                    e2=tk.Entry(root2)
                    e2.grid(row=15,column=4)
                    
                    updateem_btn=tk.Button(root2,text="Update Email",fg="white",bg="brown",command=update_em)
                    updateem_btn.grid(row=16,column=4)
                    
            l4=tk.Label(root2,text="What do you want to update?",fg="Brown")
            l4.grid(row=13,column=1)
            t1=tk.Listbox(root2,height = 5, width = 10,selectmode=tk.MULTIPLE)
            items=("Username","Email")
            t1.insert(0,*items)
            
            t1.grid(row=14,column=1)
            
            b1=tk.Button(root2,text="Update",bg="brown",fg="white",command=update)
            b1.grid(row=15,column=1)
           
        def managepwd():
            def changepwd():
                em=e1.get()
                pwd=e2.get()

                if em=="" or pwd=="":
                    messagebox.showinfo("Error","All fields are required")
                                
                df = pd.read_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv") 
                df.loc[em,"Password"] = pwd            
                df.to_csv("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", index=False) 
                messagebox.showinfo("Success","Password changed successfully")
                
            l1=tk.Label(root2,text="Enter email to change password",fg="Brown")
            l1.grid(row=16,column=1)
            e1=tk.Entry(root2)
            e1.grid(row=17,column=1)

            l2=tk.Label(root2,text="Enter new password",fg="brown")
            l2.grid(row=18,column=1)
            e2=tk.Entry(root2)
            e2.grid(row=19,column=1)
            
            b1=tk.Button(root2,text="Change Password",command=changepwd,fg="white",bg="brown")
            b1.grid(row=20,column=1)
        
        def deleteacc():
            def delete():
                un=e1.get()
                if un=="":
                    messagebox.showinfo("Error","Email field is required")
                if not re.match(r'^[A-Za-z\s]+$',un):
                    messagebox.showinfo("Error","Please enter a valid username")
                    return
                df = pd.read_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv')
                df = df.drop(df[df.Username == un].index)
                df.to_csv('C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv', index=False)
                
                messagebox.showinfo("Success","Account deleted successfully")
                root2.destroy()
                login()
            
            l1=tk.Label(root2,text="Enter Username")
            l1.grid(row=21,column=1)
            e1=tk.Entry(root2)
            e1.grid(row=22,column=1)
            b1=tk.Button(root2,text="delete",bg="brown",fg="white",command=delete)
            b1.grid(row=23,column=1)
                

        def logout():
                answer=messagebox.askyesno("Sure?","Are you sure you want to logout?")
                if answer:
                    root2.destroy()
                    messagebox.showinfo("Success","User successfully logged out")
                    login()
                else:
                    loginpage()
        root2=tk.Tk()
        root2.geometry("800x800")
        root2.title("Login page")
        b1=tk.Button(root2,text="Upload image",command=uploadimage,fg="white",bg="brown")
        b1.grid(row=2,column=0)
        b2=tk.Button(root2,text="View Profile",width=10,command=viewprofile,fg="white",bg="brown")
        b2.grid(row=2,column=1)
        b3=tk.Button(root2,text="Update Profile",width=10,command=updateprofile,fg="white",bg="brown")
        b3.grid(row=2,column=2)
        b4=tk.Button(root2, text="Delete account",width=10,command=deleteacc,fg="white",bg="brown")
        b4.grid(row=2,column=3)
        b5=tk.Button(root2,text="Manage password",width=10,command=managepwd,fg="white",bg="brown")
        b5.grid(row=2,column=4)
        b6=tk.Button(root2, text="Logout",width=10,command=logout,fg="white",bg="brown")
        b6.grid(row=2,column=5)
        root2.mainloop()
    
    def userlogin():
        username=un_entry.get()
        pwd=pwd_entry.get()
        
        if username=="" or pwd=="":
            messagebox.showinfo("Insert status","All fields are required")        
            return
        
        if not re.match(r"^[A-Za-z\s]+",username):
            messagebox.showinfo("Error","Please enter a valid username")
            return
        
        #hashedpwd = hash(pwd) 
        
        with open("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System/userdb.csv", mode='r') as f:
            reader=csv.reader(f)
            for row in reader:
                if username==row[0] and pwd==row[1]:
                    messagebox.showinfo("Success","You are logged in")
                    loginpage()
                
        messagebox.showinfo("Error","Please try again later")
        un_entry.delete(0,tk.END)
        pwd_entry.delete(0,tk.END)

    root=tk.Tk()
    root.title("Login page")
    root.geometry("400x400")
    root.configure(bg="orange")
    l1=tk.Label(root,text="Welcome to login page",fg="brown")
    l1.grid(row=0,column=1)
    un_lbl=tk.Label(root,text='Username',fg="brown")
    un_lbl.grid(row=1,column=0)
    un_entry=tk.Entry(root)
    un_entry.grid(row=1,column=1)

    pwd_lbl=tk.Label(root,text="Password",fg="brown")
    pwd_lbl.grid(row=2,column=0)
    pwd_entry=tk.Entry(root,show="*")
    pwd_entry.grid(row=2,column=1)
    
    b1=tk.Button(root,text="Admin login",command=adminlogin,fg="white",bg="brown")
    b1.grid(row=4,column=1)

    b2=tk.Button(root,text="User login",command=userlogin,fg="white",bg="brown")
    b2.grid(row=5,column=1)

    root.mainloop()
