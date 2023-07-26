from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
python=Tk()
python.geometry('1536x864+0+0')
python.resizable(True,True)
python.title("Login Window")
#python.resizable(width=False,height=False)

def log():
    if userentry.get() == '' or passentry.get() == '' :
        messagebox.showerror("ERROR","Please Enter data")
    elif userentry.get() == 'AsmitaHema' and passentry.get() == 'ashemz':
        messagebox.showinfo("SUCCESSFULL","Welcome back Asmita and Hema")
        python.destroy()
        import part2
    else:
        messagebox.showerror("ERROR","INVALID USERNAME OR PASSWORD")
        python.destroy()

def show_password():
    if passentry.cget('show') == '*':
        passentry.config(show='')
    else:
        passentry.config(show='*')


backgroundimage=ImageTk.PhotoImage(file="bg.jpg")
bglabel=Label(python,image=backgroundimage)
bglabel.place(x=0,y=0)

loginFrame=Frame(python,bg='#9ad5dd')
loginFrame.place(x=240,y=180)

logoImage=PhotoImage(file='icon.png')
logolabel=Label(loginFrame,image=logoImage,bg='#9ad5dd')
logolabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameimage=PhotoImage(file="user.png")
usernamelabel=Label(loginFrame,text="Username",font=("times new roman",30,"bold"),image=usernameimage,compound=LEFT,bg='#9ad5dd')
usernamelabel.grid(row=1,column=0,pady=10,padx=20)
userentry=Entry(loginFrame,font=("times new roman",25,"bold"),bd=5)
userentry.grid(row=1,column=1)

passwordimage=PhotoImage(file="pass.png")
passwordlabel=Label(loginFrame,text="Password",font=("times new roman",30,"bold"),image=passwordimage,compound=LEFT,bg='#9ad5dd')
passwordlabel.grid(row=2,column=0,pady=10,padx=20)
passentry=Entry(loginFrame,font=("times new roman",25,"bold"),bd=5,show="*")
passentry.grid(row=2,column=1)

check_button=Checkbutton(loginFrame,text="Show Password",font=("times new roman",15),command=show_password,bg='#9ad5dd')
check_button.grid(row=3,column=1,sticky=W,pady=1)

logbtn=Button(loginFrame,text="LOGIN",font=("times new roman",20,"bold"),width=15,fg='white',bg="darkblue",activebackground="darkblue",activeforeground="white",cursor="hand2",command=log)
logbtn.grid(row=4,column=1,pady=10)

python.mainloop()



