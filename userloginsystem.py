import tkinter as tk
from tkinter import messagebox

#sample user database (username:password)
users = {
    "admin":"fathma@1234",
    "user1": "pass"
}
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("login success","welcome"+ username)
    else:
        messagebox.showerror("login failed","invalid username or password")

        # create window
root = tk.Tk()
root.title("login system")
root.geometry("300x200")

#username
tk.Label(root, text="username").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

#password

tk.Label(root, text="password").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

#loginbutton
tk.Button(root, text="login", command=login).pack(pady=10)

#run app
root.mainloop()
