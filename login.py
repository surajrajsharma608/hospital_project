from tkinter import font, ttk,messagebox
from ttkbootstrap import Style
from tkinter import *
import sqlite3
import os


class Login:
    def __init__(self,window):

        style=Style()

        window=style.master
        window.config(bg='#262a36')
        window.geometry('1020x610')
        window.resizable(False,False)
        window.attributes('-alpha', 0.92)
        window.title('Login')
        img1=PhotoImage(file='images/hh1.png')
        lb=Label(window,image=img1,bg='#262a36')
        lb.place(x=100,y=610/2.5)
        txt=Label(text='Hospital Management',fg='white',font='Terminal 18 bold',bg='#262a36')
        txt.place(x=100*2,y=610/2.4)

        sep=ttk.Separator(window, orient='horizontal')
        sep.place(x=100*3.5,y=610/2)

        sep2=ttk.Separator(window, orient='vertical')
        sep2.place(x=100*6,y=610/6.9,height=390)

        #==========Entry==================
        self.v1=StringVar()
        self.v2=StringVar()
        e1=ttk.Entry(window,style='info.TEntry',textvariable=self.v1,foreground='#9fa4a6')
        e1.place(x=100*6.8,y=610/5,width=240)

        e2=ttk.Entry(window,style='info.TEntry',textvariable=self.v2,foreground='#9fa4a6')
        e2.place(x=100*6.8,y=610/3.4,width=240)
        self.v1.set('Enter Username')
        self.v2.set('Enter password')
        #=================================

        #==========Button========
        btn=ttk.Button(window,text='Login',style='success.TButton',command=self.login)
        btn.place(x=100*6.8,y=610/2.3,width=240,height=40)

        forg=Button(window,text='Forgot Password',fg='white',font='normal 13 bold',bg='#262a36')
        forg.place(x=100*7.1,y=610/1.8)
    
    def login(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.v1.get()=='' or self.v2.get()=='':
                messagebox.showerror('Error','Please enter Employee ID and Password!!!',parent=window)
            else:
                cur.execute('select name from users where name=? AND password=?',(self.v1.get(),self.v2.get()))
                user = cur.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid username and passwod\nPlease try again with valid credintials!!!!',parent=window)
                else:
                    if user[0]==self.v1.get():
                        window.destroy()
                        os.system('python admin.py')
                    # else:
                    #     self.root.destroy()
                    #     os.system('python bill.py')

        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=window)

if __name__ == '__main__':
    window = Tk()
    obj = Login(window)
    window.mainloop()