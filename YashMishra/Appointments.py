from tkinter import *

root = Tk()
root.title("Appointment")
root.iconbitmap('c:/Project/Logo1.ico')
root.configure(background="#f0c2e0")
root.geometry("500x500")
 
lable0 = Label(root, text="MEDICARE HOSPITAL", font=('Helvetica', 30, 'bold', 'underline') ,bg="#f0c2e0", fg="purple")
lable0.place(x=40, y=0)


lable1 = Label(root, text="APPOINTMENT",font=('Helvetica', 16, 'bold') ,bg="#f0c2e0", fg="purple")
lable1.place(x=170, y=100)


lable2 = Label(root, text="Patient ID",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable2.place(x=50, y=160)

entry1 = Entry(root, width=46)
entry1.place(x=160, y=160)

lable3 = Label(root, text="Doctor ID",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable3.place(x=50, y=190)

entry2 = Entry(root, width=46)
entry2.place(x=160, y=190)

lable4 = Label(root, text="Appt.nt No.",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable4.place(x=50, y=220)

entry3 = Entry(root, width=46)
entry3.place(x=160, y=220)

lable5 = Label(root, text="Appt.nt Time",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable5.place(x=50, y=250)

entry4 = Entry(root, width=46)
entry4.place(x=160, y=250)

lable6 = Label(root, text="Appt.nt Date",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable6.place(x=50, y=280)

entry5 = Entry(root, width=46)
entry5.place(x=160, y=280)

lable6 = Label(root, text="Sickness",font=('Helvetica', 12) ,bg="#f0c2e0", fg="purple")
lable6.place(x=50, y=310)

entry5 = Entry(root, width=46)
entry5.place(x=160, y=310, height=75)

Button1 = Button(root, text="Fix Appointment",height=2, width=18, bg="#f0c2e0", fg="purple")
Button1.place(x=32, y=430)

Button2 = Button(root, text="Delete",height=2, width=18, bg="#f0c2e0", fg="purple")
Button2.place(x=182, y=430)

Button3 = Button(root, text="All Appointments",height=2, width=18, bg="#f0c2e0", fg="purple")
Button3.place(x=332, y=430)




root.mainloop()