from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Address data entry form')
window.columnconfigure([0, 1], minsize=100)
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=100)

def sql_connection():
    import mysql.connector
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        database='p18'
    )
    return mydb

font = ('DM Sans', 50)

lbl_name = Label(text='Enter your name: ', font=font, bg='#00008B',fg="White",relief="groove")
lbl_name.grid(column=0, row=0,sticky='nsew')

ent_name = Entry(master=window, font=font, width=15)
ent_name.grid(column=1, row=0, sticky='nsew')

lbl_addr = Label(text='Enter Address:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_addr.grid(column=0, row=1, sticky='news')

ent_addr = Entry(master=window, font=font, width=15)
ent_addr.grid(column=1, row=1, sticky='nsew')

lbl_city = Label(text='Enter City:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_city.grid(column=0, row=2, sticky='news')

ent_city = Entry(master=window, font=font, width=15)
ent_city.grid(column=1, row=2, sticky='nsew')

lbl_state = Label(text='Enter State:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_state.grid(column=0, row=3, sticky='news')

ent_state = Entry(master=window, font=font, width=15)
ent_state.grid(column=1, row=3, sticky='nsew')

lbl_country = Label(text='Enter Country:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_country.grid(column=0, row=4, sticky='news')

ent_country = Entry(master=window, font=font, width=15)
ent_country.grid(column=1, row=4, sticky='nsew')

def button_clicked():
    mydb = sql_connection()

    name = ent_name.get()
    address = ent_addr.get()
    city = ent_city.get()
    state = ent_state.get()
    country = ent_country.get()

    if name == '':
        messagebox.showerror("Error", "Name cannot be empty!")
    else:
        cursor = mydb.cursor()
        cursor.execute(f"insert into address_records values ('{name}','{address}','{city}','{state}','{country}')")
        mydb.commit()
        # lbl.configure(text=f'Hello, {user}')
        btn1.configure(text='Saved!')

btn1 = Button(master=window, text='Save', font=font,
              fg='Indigo', bg='LightBlue', relief="raised",
              command=button_clicked)
btn1.grid(column=1, row=5, sticky='news')
window.mainloop()