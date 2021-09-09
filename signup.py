from tkinter import font, ttk,messagebox
from ttkbootstrap import Style
from tkinter import *
import sqlite3
class SignUp:
    def __init__(self,window):
        style=Style()

        window=style.master
        window.config(bg='#262a36')
        window.geometry('1020x610')
        window.resizable(False,False)
        window.attributes('-alpha', 0.92)
        window.title('Signup')
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
        self.v3=StringVar()
        e1=ttk.Entry(window,style='danger.TEntry',textvariable=self.v1,foreground='#9fa4a6',font='bold')
        e1.place(x=100*6.8,y=610/5,width=240)

        e2=ttk.Entry(window,style='danger.TEntry',textvariable=self.v2,foreground='#9fa4a6',font='bold')
        e2.place(x=100*6.8,y=610/3.4,width=240)

        e3=ttk.Entry(window,style='danger.TEntry',textvariable=self.v3,font='bold',foreground='#9fa4a6')
        e3.place(x=100*6.8,y=610/2.6,width=240)
        self.v1.set('Enter Username')
        self.v2.set('Enter password')
        self.v3.set('Enter birthplace for backup')
        #=================================

        #==========Button========
        btn=ttk.Button(window,text='Register',style='info.TButton',command=self.add_user)
        btn.place(x=100*6.8,y=610/2,width=240,height=40)

    def add_user(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.v1.get()=='':
                messagebox.showerror('Error','User name required to be entered!!',parent=window)
            else:
                cur.execute('insert into users (name,password,address) values(?,?,?)',(
                    self.v1.get(),
                    self.v2.get(),
                    self.v3.get()
                    ))
                con.commit()
                messagebox.showinfo('Success','User added successfully!!!',parent=window)
                con.close()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=window)
if __name__ == '__main__':
    window = Tk()
    obj = SignUp(window)
    window.mainloop()