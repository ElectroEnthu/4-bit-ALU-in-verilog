from tkinter import *
from boltiot import Bolt, Sms
from tkinter import messagebox
import random
import conf
import time

root = Tk()
root.title('DOOR SECURITY')
root.geometry('1080x1080')
bg = PhotoImage(file = "door.png")
l1 = Label(root, image =bg )
l1.place(x=-90,y=700)
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)

original = random.randint(10000, 99999)
print("password is:",original)

sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

response = sms.send_sms("Passcode is: " + str(original))

code1 = StringVar()
code2 = StringVar()
code3 = StringVar()
code4 = StringVar()
code5 = StringVar()

f1 = Frame(root)
f1.pack()
e1 = Entry(f1, textvar=code1, width=2, font=('arial bold', 19), border=3, bg='lightgreen', fg='black')
e1.pack(side=LEFT, padx=3, pady=5)
e1.focus()
e2 = Entry(f1, textvar=code2, width=2, font=('arial bold', 19), border=3, bg='lightgreen', fg='black')
e2.pack(side=LEFT, padx=3, pady=5)
e3 = Entry(f1, textvar=code3, width=2, font=('arial bold', 19), border=3, bg='lightgreen', fg='black')
e3.pack(side=LEFT, padx=3, pady=5)
e4 = Entry(f1, textvar=code4, width=2, font=('arial bold', 19), border=3, bg='lightgreen', fg='black')
e4.pack(side=LEFT, padx=3, pady=5)
e5 = Entry(f1, textvar=code5, width=2, font=('arial bold', 19), border=3, bg='lightgreen', fg='black')
e5.pack(side=LEFT, padx=3, pady=5)


def displaycode(k):
    dis = 0
    if code1.get() == '':
        dis = 1
    elif code2.get() == '':
        dis = 2
    elif code3.get() == '':
        dis = 3
    elif code4.get() == '':
        dis = 4
    elif code5.get() == '':
        dis = 5

    if dis == 1:
        code1.set(k)
        e2.focus()
    elif dis == 2:
        code2.set(k)
        e3.focus()

    elif dis == 3:
        code3.set(k)
        e4.focus()

    elif dis == 4:
        code4.set(k)
        e5.focus()

    elif dis == 5:
        code5.set(k)


passcode = ''
count = 0
resetcode = ''
flag = 1


def validate():
    global original
    global count, flag
    global passcode
    if flag == 1:
        passcode += str(e1.get()) + str(e2.get()) + str(e3.get()) + str(e4.get()) + str(e5.get())

        print(passcode)
        code1.set('')
        code2.set('')
        code3.set('')
        code4.set('')
        code5.set('')

        if passcode == str(original):
            mybolt.analogWrite("4", "195")

            time.sleep(3)
            mybolt.digitalWrite("4", "LOW")
            messagebox.showinfo('Message!', 'Successfully Door Opened!')
            count = 0
            e1.focus()

        else:
            count += 1
            messagebox.showerror('Warning!', 'Wrong passcode\n{} times remaining'.format(3 - count))
            e1.focus()
            if count == 3:
                enter.config(state=DISABLED)
                flag = 0
                unblock.config(state=NORMAL)
                for i in range(5):
                    mybolt.digitalWrite("1", "HIGH")
                    mybolt.digitalWrite("1", "LOW")
                response1 = sms.send_sms("Unknown Person is Deteced!!")
        passcode = ''


def unblock_system():
    global count, resetcode, flag
    if flag == 0:
        resetcode += str(e1.get()) + str(e2.get()) + str(e3.get()) + str(e4.get()) + str(e5.get())
        print(resetcode)
        if resetcode == str(original):
            enter.config(state=NORMAL)
            unblock.config(state=DISABLED)
            flag = 1
            count = 0

        else:
            messagebox.showerror('Warning!', "Enter Correct Unblock Passcode")
        resetcode = ''


f2 = Frame(root)
f2.pack()

b1 = Button(f2, text='1', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(1))
b1.grid(row=0, column=0, pady=5, padx=5)
b2 = Button(f2, text='2', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(2))
b2.grid(row=0, column=1, pady=5, padx=5)
b3 = Button(f2, text='3', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(3))
b3.grid(row=0, column=2, pady=5, padx=5)
b4 = Button(f2, text='4', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(4))
b4.grid(row=1, column=0, pady=5, padx=5)
b5 = Button(f2, text='5', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(5))
b5.grid(row=1, column=1, pady=5, padx=5)
b6 = Button(f2, text='6', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(6))
b6.grid(row=1, column=2, pady=5, padx=5)
b7 = Button(f2, text='7', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(7))
b7.grid(row=2, column=0, pady=5, padx=5)
b8 = Button(f2, text='8', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(8))
b8.grid(row=2, column=1, pady=5, padx=5)
b9 = Button(f2, text='9', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(9))
b9.grid(row=2, column=2, pady=5, padx=5)
b0 = Button(f2, text='0', width=3, font=('arial bold', 18), border=4, relief=RAISED, bg='black', fg='white',
            command=lambda: displaycode(0))
b0.grid(row=3, column=0, pady=5, padx=5)

enter = Button(f2, text='ENTER', width=8, font=('times new roman', 19, 'bold'), border=4, relief=RAISED, bg='red',
               fg='white', command=lambda: validate())
enter.grid(row=3, column=1, pady=4, padx=5, columnspan=2)

unblock = Button(f2, text='UNBLOCK', state=DISABLED, width=8, font=('times new roman', 16, 'bold'), border=4,
                 relief=RAISED, bg='green', fg='white', command=lambda: unblock_system())
unblock.grid(row=4, column=0, pady=7, padx=5, columnspan=3)

root.mainloop()
