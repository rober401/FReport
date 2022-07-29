try:
    import tkinter
    from tkinter import *
    import os
    import PyPDF2
    import time
    import tkinter.messagebox
    from PIL import ImageTk, Image
    import tkinter as tk
except:
    print("Import error... run error solver FPsolve.py")


top = tk.Tk()

top.title('Fast Report')
top.geometry('400x400')
top.resizable(width=False, height=False)
top.configure(bg="light blue")

Createreport_title = tk.Label(top, text='Fast Report', font='times 30', bg='light blue')
Createreport_title.pack()

Full_name = tk.Label(top, text="Full Name", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Full_name.place(x=5, y=60)

Phone_Number = tk.Label(top, text="Phone_Number", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Phone_Number.place(x=5, y=90)

Email = tk.Label(top, text="Email", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Email.place(x=5, y=120)

Age = tk.Label(top, text="Age", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Age.place(x=5, y=150)

Gender = tk.Label(top, text="Gender", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Gender.place(x=5, y=180)

Area_code = tk.Label(top, text="Area_code", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Area_code.place(x=5, y=210)

Address = tk.Label(top, text="Address", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Address.place(x=5, y=240)

Extra = tk.Label(top, text="Extra info", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Extra.place(x=5, y=270)

Notes = tk.Label(top, text="Notes", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Notes.place(x=5, y=300)


FN = Entry(top, bd=5)
FN.place(x=140, y=60)

PN = Entry(top, bd=5)
PN.place(x=140, y=90)

E = Entry(top, bd=5)
E.place(x=140, y=120)

A = Entry(top, bd=5)
A.place(x=140, y=150)

G = Entry(top, bd=5)
G.place(x=140, y=180)

AC = Entry(top, bd=5)
AC.place(x=140, y=210)

AD = Entry(top, bd=5)
AD.place(x=140, y=240)

Ext = Entry(top, bd=5)
Ext.place(x=140, y=270)

N = Entry(top, bd=5)
N.place(x=140, y=300)


Filename = tk.Label(top, text="Filename", font="times 15", bg='light blue', borderwidth=2, relief="groove")
Filename.place(x=5, y=368)

Filen = Entry(top, bd=5)
Filen.place(x=140, y=368)




def close():
    f = open(f"{Filen.get()}.txt", "w")
    f.write(f"""Fullname: {FN.get()}
Phone Number: {PN.get()}
Email:        {E.get()}
Age:          {A.get()}
Gender:       {G.get()}
Area code:    {AC.get()}
Address:      {AD.get()}
Extra info:   {Ext.get()}
Notes:        {N.get()}
""")
    f.close()
    quit()


# Save & Quit Button
SQbtn = tk.Button(top, text="Save & Quit", command=lambda: (close()))
SQbtn.place(x=320, y=368)

top.mainloop()
