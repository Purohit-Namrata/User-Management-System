import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import pandas as pd
import csv
import re
import bcrypt

def load_user_data():
    """Load user data from CSV."""
    userdb_path = os.path.join("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System", "userdb.csv")
    if not os.path.exists(userdb_path):
        return pd.DataFrame(columns=['Username', 'Password', 'Email'])
    return pd.read_csv(userdb_path)

def save_user_data(df):
    """Save user data to CSV."""
    userdb_path = os.path.join("C:/Users/BLAUPLUG/Documents/Python_programs/User Management System", "userdb.csv")
    df.to_csv(userdb_path, index=False)

def login():
    def adminlogin():
        def adminpage():
            def viewall():
                df = load_user_data()
                if df.empty:
                    messagebox.showinfo("Users List", "No user found.")
                else:
                    users_info = "\n".join([f"USERNAME: {row['Username']}, EMAIL: {row['Email']}" for _, row in df.iterrows()])
                    messagebox.showinfo("Users List", users_info)

            def deleteacc():
                def deleterow():
                    username = e1.get().strip()
                    if not username:
                        messagebox.showinfo("Error", "Please enter a Username")
                        return
                    
                    df = load_user_data()
                    if username not in df['Username'].values:
                        messagebox.showinfo("Error", "Username not found")
                        return
                    
                    df = df[df['Username'] != username]
                    save_user_data(df)
                    messagebox.showinfo("Success", "Account deleted")
                    
                lbl = tk.Label(root1, text="Enter username to delete account", fg="brown")
                lbl.grid(row=6, column=0)
                e1 = tk.Entry(root1)
                e1.grid(row=6, column=1)
                b1 = tk.Button(root1, text="Delete", command=deleterow, bg="brown", fg="white")
                b1.grid(row=8, column=1)
                
            def logout():
                if messagebox.askyesno("Sure?", "Are you sure you want to logout?"):
                    root1.destroy()
                    messagebox.showinfo("Success", "Admin successfully logged out")
                    login()
            
            root1 = tk.Tk()
            root1.geometry("400x400")
            root1.title("Admin Page")
            root1.configure(bg="orange")
            
            tk.Label(root1, text="Welcome, Admin!", font=("Arial", 16), fg="brown").grid(row=1, column=1)
            tk.Button(root1, text="View all users", command=viewall, fg="white", bg="brown").grid(row=3, column=0)
            tk.Button(root1, text="Delete accounts", command=deleteacc, fg="white", bg="brown").grid(row=3, column=1)
            tk.Button(root1, text="Logout", command=logout, fg="white", bg="brown").grid(row=3, column=2)
            root1.mainloop()

        username = un_entry.get().strip()
        pwd = pwd_entry.get().strip()
        if username == "admin" and pwd == "admin":
            messagebox.showinfo("Admin logged in", "Welcome, Admin!")
            adminpage()
        else:
            messagebox.showinfo("Error", "Invalid username or password")

    def loginpage():
        def uploadimage():
            def upload():
                path = path_entry.get().strip()
                if not path:
                    messagebox.showinfo("Error", "Please enter a path")
                    return

                if not os.path.isfile(path):
                    messagebox.showinfo("Error", "File does not exist")
                    return

                try:
                    im = Image.open(path)
                    im = im.resize((200, 200))
                    img = ImageTk.PhotoImage(im)
                    lab.config(image=img)
                    lab.image = img
                except Exception as e:
                    messagebox.showinfo("Error", f"Failed to load image: {e}")

            lbl = tk.Label(root2, text="Enter path to upload image", fg="brown")
            lbl.grid(row=3, column=1)
            path_entry = tk.Entry(root2, width=20)
            path_entry.grid(row=4, column=1)
            tk.Button(root2, text="Upload", command=upload, bg="brown", fg="white").grid(row=5, column=1)


        def viewprofile():
            def view():
                username = e1.get().strip()
                if not re.match(r"^[A-Za-z\s]+$", username):
                    messagebox.showinfo("Error", "Please enter a valid username")
                    return
                
                df = load_user_data()
                user = df[df['Username'] == username]
                if user.empty:
                    messagebox.showinfo("User Details", "User not found")
                else:
                    messagebox.showinfo("User Details", f"Username: {user['Username'].values[0]}\nEmail: {user['Email'].values[0]}")

            tk.Label(root2, text="Enter username", fg="brown").grid(row=7, column=0)
            e1 = tk.Entry(root2)
            e1.grid(row=8, column=0)
            tk.Button(root2, text="View Profile", bg="brown", fg="white", command=view).grid(row=9, column=1)

        def updateprofile():
            def update():
                selecteditem = t1.get(tk.ACTIVE)
                if selecteditem == "Username":
                    def update_un():
                        oldun = e1.get().strip()
                        newun = e2.get().strip()
                        if not oldun or not newun:
                            messagebox.showinfo("Error", "All fields are required")
                            return

                        df = load_user_data()
                        if oldun not in df['Username'].values:
                            messagebox.showinfo("Error", "Old username not found")
                            return

                        df.loc[df['Username'] == oldun, 'Username'] = newun
                        save_user_data(df)
                        messagebox.showinfo("Success", "Username updated successfully")
                    
                    tk.Label(root2, text="Enter old username and new username", fg="brown").grid(row=10, column=1)
                    e1 = tk.Entry(root2)
                    e1.grid(row=11, column=1)
                    e2 = tk.Entry(root2)
                    e2.grid(row=12, column=1)
                    tk.Button(root2, text="Update Username", fg="white", bg="brown", command=update_un).grid(row=13, column=1)

                    def update_em():
                        oldemail = e1.get().strip()
                        newemail = e2.get().strip()
                        if not oldemail or not newemail:
                            messagebox.showinfo("Error", "All fields are required")
                            return

                        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', oldemail):
                            messagebox.showinfo("Error", "Invalid old email address")
                            return
                        if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', newemail):
                            messagebox.showinfo("Error", "Invalid new email address")
                            return

                        df = load_user_data()
                        if oldemail not in df['Email'].values:
                            messagebox.showinfo("Error", "Old email not found")
                            return

                        df.loc[df['Email'] == oldemail, 'Email'] = newemail
                        save_user_data(df)
                        messagebox.showinfo("Success", "Email updated successfully")

                    tk.Label(root2, text="Enter old email and new email", fg="brown").grid(row=12, column=4)
                    e1 = tk.Entry(root2)
                    e1.grid(row=13, column=4)
                    e2 = tk.Entry(root2)
                    e2.grid(row=14, column=4)
                    tk.Button(root2, text="Update Email", fg="white", bg="brown", command=update_em).grid(row=15, column=4)

            tk.Label(root2, text="What do you want to update?", fg="brown").grid(row=13, column=1)
            t1 = tk.Listbox(root2, height=5, width=10)
            t1.insert(0, "Username")
            t1.insert(1, "Email")
            t1.grid(row=14, column=1)
            tk.Button(root2, text="Update", bg="brown", fg="white", command=update).grid(row=15, column=1)

        def managepwd():
            def changepwd():
                email = e1.get().strip()
                pwd = e2.get().strip()
                if not email or not pwd:
                    messagebox.showinfo("Error", "All fields are required")
                    return

                df = load_user_data()
                if email not in df['Email'].values:
                    messagebox.showinfo("Error", "Email not found")
                    return

                hashed_pwd = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()
                df.loc[df['Email'] == email, 'Password'] = hashed_pwd
                save_user_data(df)
                messagebox.showinfo("Success", "Password changed successfully")


            tk.Label(root2, text="Enter email to change password", fg="brown").grid(row=16, column=1)
            e1 = tk.Entry(root2)
            e1.grid(row=17, column=1)
            tk.Label(root2, text="Enter new password", fg="brown").grid(row=18, column=1)
            e2 = tk.Entry(root2, show="*")
            e2.grid(row=19, column=1)
            tk.Button(root2, text="Change Password", command=changepwd, fg="white", bg="brown").grid(row=20, column=1)

        def deleteacc():
            def delete():
                username = e1.get().strip()
                if not username:
                    messagebox.showinfo("Error", "Username field is required")
                    return
                
                df = load_user_data()
                if username not in df['Username'].values:
                    messagebox.showinfo("Error", "Username not found")
                    return
                
                df = df[df['Username'] != username]
                save_user_data(df)
                messagebox.showinfo("Success", "Account deleted successfully")
                root2.destroy()
                login()

            tk.Label(root2, text="Enter Username", fg="brown").grid(row=21, column=1)
            e1 = tk.Entry(root2)
            e1.grid(row=22, column=1)
            tk.Button(root2, text="Delete", bg="brown", fg="white", command=delete).grid(row=23, column=1)
                
        def logout():
            if messagebox.askyesno("Sure?", "Are you sure you want to logout?"):
                root2.destroy()
                messagebox.showinfo("Success", "User successfully logged out")
                login()

        root2 = tk.Tk()
        root2.geometry("800x800")
        root2.title("Login Page")
        tk.Button(root2, text="Upload Image", command=uploadimage, fg="white", bg="brown").grid(row=2, column=0)
        tk.Button(root2, text="View Profile", width=10, command=viewprofile, fg="white", bg="brown").grid(row=2, column=1)
        tk.Button(root2, text="Update Profile", width=10, command=updateprofile, fg="white", bg="brown").grid(row=2, column=2)
        tk.Button(root2, text="Delete Account", width=10, command=deleteacc, fg="white", bg="brown").grid(row=2, column=3)
        tk.Button(root2, text="Manage Password", width=10, command=managepwd, fg="white", bg="brown").grid(row=2, column=4)
        tk.Button(root2, text="Logout", width=10, command=logout, fg="white", bg="brown").grid(row=2, column=5)
        lab = tk.Label(root2, bg='white')
        lab.grid(row=5, column=5, rowspan=5, columnspan=5, sticky='nsew')
        root2.mainloop()
    
    def userlogin():
        username = un_entry.get().strip()
        pwd = pwd_entry.get().strip()
        
        if not username or not pwd:
            messagebox.showinfo("Error", "All fields are required")
            return
        
        df = load_user_data()
        user = df[df['Username'] == username]
        if user.empty or not bcrypt.checkpw(pwd.encode(), user['Password'].values[0].encode()):
            messagebox.showinfo("Error", "Invalid username or password")
        else:
            messagebox.showinfo("Success", "You are logged in")
            loginpage()
        
    root = tk.Tk()
    root.title("Login Page")
    root.geometry("400x400")
    root.configure(bg="orange")
    tk.Label(root, text="Welcome to login page", fg="brown").grid(row=0, column=1)
    tk.Label(root, text='Username', fg="brown").grid(row=1, column=0)
    un_entry = tk.Entry(root)
    un_entry.grid(row=1, column=1)
    tk.Label(root, text="Password", fg="brown").grid(row=2, column=0)
    pwd_entry = tk.Entry(root, show="*")
    pwd_entry.grid(row=2, column=1)
    tk.Button(root, text="Admin Login", command=adminlogin, fg="white", bg="brown").grid(row=4, column=1)
    tk.Button(root, text="User Login", command=userlogin, fg="white", bg="brown").grid(row=5, column=1)
    root.mainloop()

if __name__ == "__main__":
    login()
