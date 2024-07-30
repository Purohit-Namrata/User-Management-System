import tkinter as tk
from tkinter import messagebox
import pymysql
        

def login():
    def adminlogin():
        def adminpage():
            
            def viewall():
                con=pymysql.connect(host='localhost',user='root',password='ROOT123')
                cursor=con.cursor()
                
                cursor.execute("SELECT * FROM User")
                result = cursor.fetchall()
                if result:
                    for x in result:
                        messagebox.showinfo("All users","Username:"+result[0]+"Password"+result[1]+"Email"+result[2]+"\n")
            
            def deleteacc():
                lbl=tk.Label(root1,text="Enter username to delete account")
                lbl.grid(row=5,column=0)
                e1=tk.Entry(root1)
                e1.grid(row=6,column=1)
                un=e1.get()
                con=pymysql.connect(host="localhost",user="root",password="Root123")
                cursor=con.cursor()
                cursor.execute("Delete from User where Username="+un)
                messagebox.showinfo("Success","Account deleted")
                lbl.delete()
                e1.delete()

            def logout():
                answer=messagebox.askyesno("Sure?","Are you sure you want to logout?")
                if answer:
                    root1.destroy()
                    messagebox.showinfo("Success","User successfully logged out")
                    login()
                else:
                    adminpage()
            
            root1=tk.Tk()
            root1.geometry("400x400")
            root1.title("Admin page")
            root1.configure(bg="orange")
            l1=tk.Label(root1, text="Welcome, Admin!",font=10)
            l1.grid(row=1,column=1)
            b1=tk.Button(root1, text="View all users",command=viewall)
            b1.grid(row=3,column=0)
            b2=tk.Button(root1,text="Delete accounts",command=deleteacc)
            b2.grid(row=3,column=1)
            b3=tk.Button(root1, text="Logout",command=logout)
            b3.grid(row=3,column=2)
            root1.mainloop()

        con=pymysql.connect(host='localhost',user='root',password='ROOT123')
        cursor=con.cursor()

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
            def viewprofile():
                con=pymysql.connect(host='localhost',user='root',password='ROOT123')
                cursor=con.cursor()
                l1=tk.Label(root2,text="Enter username")
                l1.grid(row=3,column=0)
                e1=tk.Entry(root2)
                e1.grid(row=4,column=0)
                un=e1.get()                
                cursor.execute("SELECT * FROM User where username="+un)
                result = cursor.fetchone()
                if result:
                    for x in result:
                        messagebox.showinfo("All users","Username:"+result[0]+"Password"+result[1]+"Email"+result[2])
                
            def uploadimage():
                pass
            root2=tk.TK()
            root2.geometry("400x400")
            root2.title("Login page")
            b1=tk.Button(root2,text="Upload image",command=uploadimage)
            b1.grid(row=2,column=0)
            b2=tk.Button(root2,text="View Profile",width=10,command=viewprofile)
            b2.grid(row=2,column=1)
            b3=tk.Button(root2,text="Update Profile",width=10)
            b3.grid(row=2,column=2)
            b4=tk.Button(root2, text="Delete account",width=10)
            b4.grid(row=2,column=3)
            b5=tk.Button(root2,text="Manage password",width=10)
            b5.grid(row=2,column=4)
            b6=tk.Button(root2, text="Logout",width=10)
            b6.grid(row=2,column=5)

            root2.mainloop()
    
    def userlogin():
        con=pymysql.connect(host='localhost',user='root',password='ROOT123')
        cursor=con.cursor()

        username=un_entry.get()
        pwd=pwd_entry.get()
        
        if username=="" or pwd=="":
            messagebox.showinfo("Insert status","All fields are required")
        
        else:
            cursor.execute('select %s from User') % username
            dbuser = cursor.fetchone()
            if dbuser == username:
                cursor.execute('select %s from User') % pwd
                dbpass = cursor.fetchone()
                if dbpass == pwd:
                    return "True"
                else:
                    return "Password is incorrect."

            else:
                return "Username is incorrect." 
        messagebox.showinfo("User logged in",f"Welcome,{username}")
        loginpage()

    root=tk.Tk()
    root.title("Login page")
    root.geometry("400x400")
    root.configure(bg="orange")
    l1=tk.Label(root,text="Welcome to login page")
    l1.grid(row=0,column=1)
    un_lbl=tk.Label(root,text='Username')
    un_lbl.grid(row=1,column=0)
    un_entry=tk.Entry(root)
    un_entry.grid(row=1,column=1)

    pwd_lbl=tk.Label(root,text="Password")
    pwd_lbl.grid(row=2,column=0)
    pwd_entry=tk.Entry(root,show="*")
    pwd_entry.grid(row=2,column=1)
    
    b1=tk.Button(root,text="Admin login",command=adminlogin)
    b1.grid(row=3,column=0)
    b2=tk.Button(root,text="User login",command=userlogin)
    b2.grid(row=3,column=1)

    root.mainloop()