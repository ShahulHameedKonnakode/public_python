import sqlite3
from tkinter import*
import re
import tkinter.messagebox
from tkinter import ttk
import re



class Database:
    def __init__(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        userid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        username TEXT,
        password TEXT
        );''')
        self.connection.commit()

    def insert_user_data(self,name,email, phone,username, password):
        self.cursor.execute("INSERT INTO users (name,email,phone,username,password)values(?,?,?,?,?)",(name,email,phone,username,password))
        self.connection.commit()
    
    def fetch_user_data(self, userid):
        self.cursor.execute("select * from users where userid=?",(userid,))
        return self.cursor.fetchone()
    
    def update_user_data(self, userid, name, email, phone, username, password):
        self.cursor.execute("update users set name=?,email=?,phone=?,username=?,password=? where userid=?",(name,email,phone,username,password,userid))
        self.connection.commit()

class RegistrationForm:
    def __init__(self,root,db):
        self.root = root
        self.db = db
        self.setup_ui()

    def entry_focus_in(self,event):
        if self.search_entry.get() == "Enter User Id":
            self.search_entry.delete(0,'end')
            self.search_entry.config(fg="grey")
        
    def entry_focus_out(self,event):
        if self.search_entry.get() == "":
            self.search_entry.delete(0,'Enter User Id')
            self.search_entry.config(fg="grey")

    def setup_ui(self):
        self.root.title("Registration Form")
        self.root.geometry("400x850")
        self.root.resizable(False,False)

 
        # Design

        self.heading = Label(root, text= "REGISTRATION FORM", font=("arial", 20, "bold"), fg="#002e62")
        self.heading.place(x=50, y=20)
        self.name_label=Label(self.root,font="arial 11",text="Name:")
        self.name_label.place(x=20,y=100)
        self.name_entry = Entry(self.root,width=28,font= "arial 11")
        self.name_entry.place(x=140,y=100)

        self.email_label=Label(self.root,font="arial 11",text="Email:")
        self.email_label.place(x=20,y=150)
        self.email_entry = Entry(self.root,width=28,font= "arial 11")
        self.email_entry.place(x=140,y=150)

        self.phone_label=Label(self.root,font="arial 11",text="Phone No:")
        self.phone_label.place(x=20,y=200)
        self.phone_entry = Entry(self.root,width=28,font= "arial 11")
        self.phone_entry.place(x=140,y=200)

        self.username_label=Label(self.root,font="arial 11",text="Username:")
        self.username_label.place(x=20,y=250)
        self.username_entry = Entry(self.root,width=28,font= "arial 11")
        self.username_entry.place(x=140,y=250)

        self.password_label=Label(self.root,font="arial 11",text="Password:")
        self.password_label.place(x=20,y=300)
        self.password_entry = Entry(self.root,width=28,font= "arial 11", show="*")
        self.password_entry.place(x=140,y=300)

        button=Button(self.root, text="REGISTER", font="arial 20 bold", width=15, bg="#5a95ff", fg="#fff",bd=0, command=self.register_user)
        button.place(x=60, y=350)

        self.search_entry = Entry(self.root, width=24,font= "arial 11")
        self.search_entry.place(x=20,y=450)
        self.search_entry.insert(0,"Enter User Id",)
        self.search_entry.bind("<FocusIn>",self.entry_focus_in)
        self.search_entry.bind("<FocusOut>",self.entry_focus_out)
        button=Button(self.root, text="Search", font="arial 10 bold", width=10, bg="#eb3443", fg="#fff",bd=0, command=self.search_by_user_id,)
        button.place(x=250, y=450)
    
    # Update Section

    # Design

        self.heading = Label(root, text= "UPDATE DATAS", font=("arial", 15, "bold"), fg="#016327")
        self.heading.place(x=100, y=500)
        # separator = ttk.Separator(root, orient='horizontal')
        # separator.pack(pady=550,fill='x')
        self.update_name_label=Label(self.root,font="arial 11",text="Name:")
        self.update_name_label.place(x=20,y=550)
        self.update_name_entry = Entry(self.root,width=28,font= "arial 11")
        self.update_name_entry.place(x=140,y=550)

        self.update_email_label=Label(self.root,font="arial 11",text="Email:")
        self.update_email_label.place(x=20,y=600)
        self.update_email_entry = Entry(self.root,width=28,font= "arial 11")
        self.update_email_entry.place(x=140,y=600)

        self.update_phone_label=Label(self.root,font="arial 11",text="Phone No:")
        self.update_phone_label.place(x=20,y=650)
        self.update_phone_entry = Entry(self.root,width=28,font= "arial 11")
        self.update_phone_entry.place(x=140,y=650)

        self.update_username_label=Label(self.root,font="arial 11",text="Username:")
        self.update_username_label.place(x=20,y=700)
        self.update_username_entry = Entry(self.root,width=28,font= "arial 11")
        self.update_username_entry.place(x=140,y=700)

        self.update_password_label=Label(self.root,font="arial 11",text="Password:")
        self.update_password_label.place(x=20,y=750)
        self.update_password_entry = Entry(self.root,width=28,font= "arial 11")
        self.update_password_entry.place(x=140,y=750)

        upadate_button=Button(self.root, text="UPDATE", font="arial 12 bold", width=10, bg="#016327", fg="#fff",bd=0, command=self.updation)
        upadate_button.place(x=10, y=800)
        delete_button=Button(self.root, text="DELETE", font="arial 12 bold", width=10, bg="#9e0202", fg="#fff",bd=0, command=self.delete_user)
        delete_button.place(x=280, y=800)

    def reset_field(self):
        self.name_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.phone_entry.delete(0,END)
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)

    def reset_updation_field(self):
        self.update_name_entry.delete(0,END)
        self.update_email_entry.delete(0,END)
        self.update_phone_entry.delete(0,END)
        self.update_username_entry.delete(0,END)
        self.update_password_entry.delete(0,END)
        self.search_entry.delete(0,END)


    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        username =  self.username_entry.get()
        password = self.password_entry.get()
        if self.validation():
            self.db.insert_user_data(name,email, phone,username, password)
            tkinter.messagebox.showinfo("Registered Successfully", f"The user {name} registered Successfully!")
            self.reset_field()
        else:
            tkinter.messagebox.showerror("Error", "All Fields are Mandatory")

         # validation
    def validation(self):
    # Validate name (letters and spaces only)
    name = self.name_entry.get()
    valid_name = r"^[a-zA-Z\s]+$"
    if not re.match(valid_name, name):
        tkinter.messagebox.showwarning("Error", "Invalid Name. Please enter a valid name (letters only).")
        return False

    # Validate email (general email format)
    email = self.email_entry.get()
    valid_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(valid_email, email):
        tkinter.messagebox.showwarning("Error", "Invalid email format. Please enter a valid email.")
        return False

    # Validate phone number (10 digits)
    phone = self.phone_entry.get()
    valid_phone = r"^\d{10}$"
    if not re.match(valid_phone, phone):
        tkinter.messagebox.showwarning("Error", "Invalid Phone Number. Please enter a valid 10-digit phone number.")
        return False

    # Validate username (alphanumeric only)
    username = self.username_entry.get()
    valid_username = r"^[a-zA-Z0-9]+$"
    if not re.match(valid_username, username):
        tkinter.messagebox.showwarning("Error", "Invalid Username. Only alphanumeric characters are allowed.")
        return False

    # Validate password (8+ characters, one letter, one number, one special character)
    password = self.password_entry.get()
    valid_password = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(valid_password, password):
        tkinter.messagebox.showwarning("Error", "Invalid Password. Must be 8+ characters, with at least one letter, one number, and one special character.")
        return False

    return True  # All validations passed





    def search_by_user_id(self):
        userid=self.search_entry.get()
        if userid.isdigit():
            user_data = self.db.fetch_user_data(userid)
            if user_data:
                tkinter.messagebox.showinfo("User Found", f"User found with the ID.{user_data[0]} and Name {user_data[1]}")
                                            
                self.id=user_data[0]
                self.name= user_data[1]
                self.email= user_data[2]
                self.phone= user_data[3]
                self.username= user_data[4]
                self.password=user_data[5]

                self.update_datas()
            else:
                tkinter.messagebox.showwarning("Not Found", "No user found with this ID.")
        else:
            tkinter.messagebox.showerror("Invalid Input", "Please enter a valid user ID.")
    
    def update_datas(self):        
        self.update_name_entry.delete(0, END)
        self.update_name_entry.insert(0, self.name)
        self.update_email_entry.delete(0, END)
        self.update_email_entry.insert(0, self.email)
        self.update_phone_entry.delete(0, END)        
        self.update_phone_entry.insert(0, self.phone)
        self.update_username_entry.delete(0, END)       
        self.update_username_entry.insert(0, self.username)
        self.update_password_entry.delete(0, END)
        self.update_password_entry.insert(0,self.password)
    def updation(self):
        name = self.update_name_entry.get()
        email = self.update_email_entry.get()
        phone = self.update_phone_entry.get()
        username = self.update_username_entry.get()
        password = self.update_password_entry.get()

        if self.validation():
            self.db.update_user_data(self.id, name, email, phone, username, password)
            tkinter.messagebox.showinfo("Success", "User Data updated successfully!")
            self.reset_updation_field()


    def delete_user(self):
        user_id=self.search_entry.get()
        if user_id.isdigit():
            self.db.cursor.execute("Delete from users where userid=?",(user_id,))            
            confirm=tkinter.messagebox.askyesno(title="Warning !", message="Are you sure to delete?!")
            if confirm:
                self.db.connection.commit()
                tkinter.messagebox.showinfo("Success", "User Deleted successfully!")
                self.reset_updation_field()
        else:
            tkinter.messagebox.showerror("Invalid", "Enter a valid id!")

class Menus:
    def __init__(self,root):
        self.menubar=Menu(root)
        root.config(menu=self.menubar)
        self.filemenu=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        
        self.filemenu.add_command(label='Register', command="")
        self.filemenu.add_command(label='Update', command='')
        self.filemenu.add_command(label='Delete')
        self.filemenu.add_command(label='Exit',command=root.destroy)

        self.editmenu=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)

        self.aboutmenu=Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="About",menu=self.aboutmenu)


    
db=Database("registration_datas")
root=Tk()
app = RegistrationForm(root,db)
menus= Menus(root)



root.mainloop()
