from tkinter import *
import time
import ttkthemes
import pandas
from tkinter import ttk, messagebox, filedialog
import pymysql

window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('keramik')
window.geometry('1500x700+0+0')
window.resizable(False, False)
window.title("Student Management Project - BY ASMITA AND HEMA")

def connect_database():
    def connect():
        global cur, con
        try:
            con = pymysql.connect(host=hostNameEntry.get(), user=userNameEntry.get(), password=passwordNameEntry.get())
            cur = con.cursor()
            messagebox.showinfo('Success', 'Database connection is successful', parent=connectWindow)
        except:
            messagebox.showerror('Error', 'Invalid Details', parent=connectWindow)
        try:
            query1 = 'CREATE DATABASE SMS'
            cur.execute(query1)
            query2 = 'USE SMS'
            cur.execute(query2)
            query3 = 'CREATE TABLE student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50))'
            cur.execute(query3)
        except:
            query = 'USE SMS'
            cur.execute(query)

    addstubtn.config(state=NORMAL)
    searchstubtn.config(state=NORMAL)
    delstubtn.config(state=NORMAL)
    upstubtn.config(state=NORMAL)
    showstubtn.config(state=NORMAL)
    transferstubtn.config(state=NORMAL)
    extbtn.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.title('Database Connection')
    connectWindow.geometry("450x270+700+200")
    connectWindow.resizable(False, False)

    hostNameLabel = Label(connectWindow, text="HOST NAME", font=('arial', 15, 'bold'))
    hostNameLabel.grid(row=0, column=0, padx=20)
    hostNameEntry = Entry(connectWindow, font=('arial', 15, 'bold'), bd=1.5)
    hostNameEntry.grid(row=0, column=1, padx=40, pady=20)

    userNameLabel = Label(connectWindow, text="USER NAME", font=('arial', 15, 'bold'))
    userNameLabel.grid(row=1, column=0, padx=20)
    userNameEntry = Entry(connectWindow, font=('arial', 15, 'bold'), bd=1.5)
    userNameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordNameLabel = Label(connectWindow, text="PASSWORD", font=('arial', 15, 'bold'))
    passwordNameLabel.grid(row=2, column=0, padx=20)
    passwordNameEntry = Entry(connectWindow, font=('arial', 15, 'bold'), bd=1.5,show='*')
    passwordNameEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, column=0, columnspan=2, pady=10)


def delete_student():
    index = studentTbl.focus()
    content = studentTbl.item(index)
    content_id = content['values'][0]
    query = 'DELETE FROM STUDENT WHERE id = %s'
    cur.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted successfully!')
    query = 'SELECT * FROM STUDENT'
    cur.execute(query)
    fetch_data = cur.fetchall()
    studentTbl.delete(*studentTbl.get_children())
    for data in fetch_data:
        studentTbl.insert('', END, values=data)

def show_student():
    query = 'SELECT * FROM STUDENT'
    cur.execute(query)
    fetch_data = cur.fetchall()
    studentTbl.delete(*studentTbl.get_children())
    for data in fetch_data:
        studentTbl.insert('', END, values=data)

def search_student():
    def search_data():
        query7 = 'SELECT * FROM STUDENT WHERE id = %s or name = %s or mobile = %s or email = %s or address = %s or gender = %s or dob = %s'
        cur.execute(query7, (
        idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(),
        DOBEntry.get()))
        studentTbl.delete(*studentTbl.get_children())
        fetch_data = cur.fetchall()
        for data in fetch_data:
            studentTbl.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title("Search_Student")
    search_window.resizable(False, False)
    search_window.grab_set()
    idLabel = Label(search_window, text="Id", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(search_window, text="Name", font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    phoneLabel = Label(search_window, text="Phone", font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    phoneEntry.grid(row=2, column=1, padx=10, pady=15)

    emailLabel = Label(search_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    emailEntry.grid(row=3, column=1, padx=10, pady=15)

    addressLabel = Label(search_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    addressEntry.grid(row=4, column=1, padx=10, pady=15)

    genderLabel = Label(search_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    genderEntry.grid(row=5, column=1, padx=10, pady=15)

    DOBLabel = Label(search_window, text="DOB", font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(search_window, font=('roman', 15, 'bold'), width=20)
    DOBEntry.grid(row=6, column=1, padx=10, pady=15)

    search_student_button = Button(search_window, text="SEARCH STUDENT", command=search_data)
    search_student_button.grid(row=7, column=0, columnspan=2)


def add_student():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or DOBEntry.get() == '':
            messagebox.showerror('Error', 'All Fields are required', parent=add_window)
        else:
            currentdate = time.strftime('%d/%m/%Y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query4 = 'INSERT INTO STUDENT VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cur.execute(query4, (
                idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                genderEntry.get(), DOBEntry.get(), currentdate, currenttime))
                con.commit()
                result = messagebox.askyesno('Confirm', 'Do you want to clean the form?', parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    phoneEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    DOBEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id cannot be repeated', parent=add_window)
                return
            query5 = 'SELECT * FROM STUDENT'
            cur.execute(query5)
            fetch_data = cur.fetchall()
            studentTbl.delete(*studentTbl.get_children())

            for data in fetch_data:
                datalist = list(data)
                studentTbl.insert('', END, values=datalist)

    add_window = Toplevel()
    add_window.resizable(False, False)
    add_window.grab_set()
    idLabel = Label(add_window, text="Id", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(add_window, text="Name", font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    phoneLabel = Label(add_window, text="Phone", font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    phoneEntry.grid(row=2, column=1, padx=10, pady=15)

    emailLabel = Label(add_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    emailEntry.grid(row=3, column=1, padx=10, pady=15)

    addressLabel = Label(add_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    addressEntry.grid(row=4, column=1, padx=10, pady=15)

    genderLabel = Label(add_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    genderEntry.grid(row=5, column=1, padx=10, pady=15)

    DOBLabel = Label(add_window, text="DOB", font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(add_window, font=('roman', 15, 'bold'), width=20)
    DOBEntry.grid(row=6, column=1, padx=10, pady=15)

    add_student_button = Button(add_window, text="ADD STUDENT", command=add_data)
    add_student_button.grid(row=7, column=0, columnspan=2)


def transfer_data():
    url = filedialog.asksaveasfile(defaultextension='.csv')
    indexing = studentTbl.get_children()
    newList = []
    for index in indexing:
        content = studentTbl.item(index)
        datalist = content['values']
        newList.append(datalist)
    table = pandas.DataFrame(newList,
                             columns=['ID', 'NAME', 'PHONE', 'EMAIL', 'ADDRESS', 'GENDER', 'DOB', 'DATE', 'TIME'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')

def update_student():
    def update_data():
        query = 'UPDATE STUDENT SET name = %s, mobile = %s, email = %s, address = %s, gender = %s, dob = %s, date = %s, time = %s where id = %s'
        cur.execute(query, (
        nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), DOBEntry.get(),
        date, crntime, idEntry.get()))
        con.commit()
        messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully!', parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title("Update_Student")
    update_window.resizable(False, False)
    update_window.grab_set()
    idLabel = Label(update_window, text="Id", font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(update_window, text="Name", font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    phoneLabel = Label(update_window, text="Phone", font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    phoneEntry.grid(row=2, column=1, padx=10, pady=15)

    emailLabel = Label(update_window, text="Email", font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    emailEntry.grid(row=3, column=1, padx=10, pady=15)

    addressLabel = Label(update_window, text="Address", font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    addressEntry.grid(row=4, column=1, padx=10, pady=15)

    genderLabel = Label(update_window, text="Gender", font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    genderEntry.grid(row=5, column=1, padx=10, pady=15)

    DOBLabel = Label(update_window, text="DOB", font=('times new roman', 20, 'bold'))
    DOBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(update_window, font=('roman', 15, 'bold'), width=20)
    DOBEntry.grid(row=6, column=1, padx=10, pady=15)

    update_student_button = ttk.Button(update_window, text="UPDATE STUDENT", command=update_data)
    update_student_button.grid(row=7, column=0, columnspan=2)

    indexing = studentTbl.focus()
    content = studentTbl.item(indexing)
    listdata = content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    phoneEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    addressEntry.insert(0, listdata[4])
    genderEntry.insert(0, listdata[5])
    DOBEntry.insert(0, listdata[6])

def clock():
    global date, crntime
    date = time.strftime('%d/%m/%Y')
    crntime = time.strftime('%H:%M:%S')
    data_timelbl.config(text=f'   Date: {date}\nTime: {crntime}')
    data_timelbl.after(1000, clock)

count = 0
text = ''

def slide():
    global text, count
    if count == len(t):
        count = 0
        text = ''

    text = text + t[count]
    slideLbl.config(text=text)
    count += 1
    slideLbl.after(200, slide)

def exit():
    ex=messagebox.askyesno("CONFIRM","Do you want to exit ?")
    if ex:
        window.destroy()
    else:
        pass

data_timelbl = Label(window, text='h', font=("times new roman", 17, "bold"))
data_timelbl.place(x=10, y=10)
clock()

t = "STUDENT MANAGEMENT SYSTEM"
slideLbl = Label(window, text=t, font=('arial', 25, "bold"), width=40,fg="darkblue")
slideLbl.place(x=300, y=20)
slide()

conntBtn = ttk.Button(window, text="Connect to Database", command=connect_database)
conntBtn.place(x=1110, y=30)

lftframe = Label(window)
lftframe.place(x=40, y=65, width=400, height=680)

logoimg = PhotoImage(file='leftframeicon.png')
logolbl = Label(lftframe, image=logoimg)
logolbl.grid(row=0, column=0)

addstubtn = ttk.Button(lftframe, text="ADD STUDENT", width=25, state=DISABLED, command=add_student)
addstubtn.grid(row=1, column=0, pady=20)

searchstubtn = ttk.Button(lftframe, text="SEARCH STUDENT", width=25, state=DISABLED, command=search_student)
searchstubtn.grid(row=2, column=0, pady=20)

delstubtn = ttk.Button(lftframe, text="DEL STUDENT", width=25, state=DISABLED, command=delete_student)
delstubtn.grid(row=3, column=0, pady=20)

upstubtn = ttk.Button(lftframe, text="UPDATE STUDENT INFO", width=25, state=DISABLED, command=update_student)
upstubtn.grid(row=4, column=0, pady=20)

showstubtn = ttk.Button(lftframe, text="SHOW STUDENT INFO", width=25, state=DISABLED, command=show_student)
showstubtn.grid(row=5, column=0, pady=20)

transferstubtn = ttk.Button(lftframe, text="TRANSFER DATA", width=25, state=DISABLED, command=transfer_data)
transferstubtn.grid(row=6, column=0, pady=20)

extbtn = ttk.Button(lftframe, text="EXIT", width=25, command=exit)
extbtn.grid(row=7, column=0, pady=20)

rightframe = Label(window)
rightframe.place(x=230, y=130, width=1200, height=500)

scrollX = Scrollbar(rightframe, orient=HORIZONTAL)
scrollY = Scrollbar(rightframe, orient=VERTICAL)

studentTbl = ttk.Treeview(rightframe, columns=(
'ID', 'NAME', 'MOBILE', 'EMAIL', 'ADDRESS', 'GENDER', 'DOB', 'ENTRY DATE', 'ENTRY TIME'),
                          xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
scrollX.config(command=studentTbl.xview)
scrollY.config(command=studentTbl.yview)

scrollX.pack(side=BOTTOM, fill=X)
scrollY.pack(side=RIGHT, fill=Y)
studentTbl.pack(fill=BOTH, expand=1)

studentTbl.heading('ID', text='I.D')
studentTbl.heading('NAME', text='NAME')
studentTbl.heading('MOBILE', text='MOBILE NO')
studentTbl.heading('EMAIL', text='EMAIL')
studentTbl.heading('ADDRESS', text='ADDRESS')
studentTbl.heading('GENDER', text='GENDER')
studentTbl.heading('DOB', text='DATE_OF_BIRTH')
studentTbl.heading('ENTRY DATE', text='ENTRY DATE')
studentTbl.heading('ENTRY TIME', text='ENTRY TIME')

studentTbl.column('ID', width=200, anchor=CENTER)
studentTbl.column('NAME', width=200, anchor=CENTER)
studentTbl.column('MOBILE', width=200, anchor=CENTER)
studentTbl.column('EMAIL', width=200, anchor=CENTER)
studentTbl.column('ADDRESS', width=200, anchor=CENTER)
studentTbl.column('GENDER', width=200, anchor=CENTER)
studentTbl.column('DOB', width=200, anchor=CENTER)
studentTbl.column('ENTRY DATE', width=200, anchor=CENTER)
studentTbl.column('ENTRY TIME', width=200, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview', rowheight=35, font=('arial', 10, 'bold'), foreground='black', background='silver', )
style.configure('Treeview.Heading', font=('arial', 12, 'bold'))
studentTbl.config(show='headings')
window.mainloop()