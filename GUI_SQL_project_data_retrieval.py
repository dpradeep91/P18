from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Address data retrieval form')
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

lbl_name = Label(text='Enter your name to search: ', font=font, bg='#00008B',fg="White",relief="groove")
lbl_name.grid(column=0, row=0,sticky='nsew')

ent_name = Entry(master=window, font=font, width=15)
ent_name.grid(column=1, row=0, sticky='nsew')

lbl_addr = Label(text='Address:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_addr.grid(column=0, row=1, sticky='news')

lbl_city = Label(text='City:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_city.grid(column=0, row=2, sticky='news')

lbl_state = Label(text='State:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_state.grid(column=0, row=3, sticky='news')

lbl_country = Label(text='Country:', font=font, bg='#00008B',fg="White",relief="groove")
lbl_country.grid(column=0, row=4, sticky='news')

def button_clicked():
    mydb = sql_connection()

    name = ent_name.get()

    cursor = mydb.cursor()
    cursor.execute(f"select * from address_records where lower(name) = lower('{name}')")
    rows = len([x for x in cursor])
    if rows > 0:
        cursor.execute(f"select * from address_records where lower(name) = lower('{name}')")

        for x in cursor:
            txt_addr = Label(text=f'{x[1]}', font=font, bg='White', fg="Brown", relief="groove")
            txt_addr.grid(column=1, row=1, sticky='news')

            txt_city = Label(text=f'{x[2]}', font=font, bg='White', fg="Brown", relief="groove")
            txt_city.grid(column=1, row=2, sticky='news')

            txt_state = Label(text=f'{x[3]}', font=font, bg='White', fg="Brown", relief="groove")
            txt_state.grid(column=1, row=3, sticky='news')

            txt_country = Label(text=f'{x[4]}', font=font, bg='White', fg="Brown", relief="groove")
            txt_country.grid(column=1, row=4, sticky='news')

    else:
        messagebox.showerror("Error", "No data found!")

    # lbl.configure(text=f'Hello, {user}')


btn1 = Button(master=window, text='Search', font=font,
              fg='Indigo', bg='LightBlue', relief="raised",
              command=button_clicked)
btn1.grid(column=1, row=5, sticky='news')
window.mainloop()