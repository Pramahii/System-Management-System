from tkinter import *
from tkinter import messagebox


def login():
    if usernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','Enter the username and password')
    elif usernameEntry.get()=='pandu' and PasswordEntry.get()=='123':
        messagebox.showinfo('Success','WELCOME')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')


window=Tk()

window.geometry('1545x800+0+0')
window.title('Login System for Student Mangement(Sms)')
window.resizable(False,False)

backgroundImage=PhotoImage(file='background .png')
backgroundLabel=Label(window,image=backgroundImage)
backgroundLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='pink')
loginFrame.place(x=590,y=270)
logoImage=PhotoImage(file='group.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)


usernameImage=PhotoImage(file='profile.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,
                    font=('times new roman',15,'bold'),background='pink')
usernameLabel.grid(row=1,column=0,pady=10,padx=10)
usernameEntry=Entry(loginFrame,font=('times new roman',15,'bold'),bd=5,fg='royal blue')
usernameEntry.grid(row=1,column=1,pady=10,padx=10)


PasswordImage=PhotoImage(file='Password.png')
PasswordLabel=Label(loginFrame,image=PasswordImage,text='Password',compound=LEFT,
                    font=('times new roman',15,'bold'),background='pink')
PasswordLabel.grid(row=2,column=0,pady=10,padx=10)
PasswordEntry=Entry(loginFrame,font=('times new roman',15,'bold'),bd=5,fg='royal blue')
PasswordEntry.grid(row=2,column=1,pady=10,padx=10)

LoginButton=Button(loginFrame,text='login',font=('times new roman',15,'bold'),width=5,
                   fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white',
                   cursor='hand2',command=login)
LoginButton.grid(row=3,column=1)


window.mainloop()
