from tkinter import *
from tkinter import ttk 
from ttkbootstrap import Style
from ttkbootstrap.widgets import Meter
from PIL import ImageTk,Image


style=Style()
window=style.master
window.geometry('1140x650')
window.resizable(False,False)
window.config(bg='#262a36')
window.title('Admin Page')
window.attributes('-alpha', 0.94)
#====================Function====================================
#================================================================
#====================Frame========================================
frame1=Frame(window,bg='#050d1f')
frame1.place(x=0,y=0,width=280,height=900)
img=PhotoImage(file='images/prof.png')

lb=Label(frame1,image=img,bg='#050d1f')
lb.place(x=105,y=30)
lb_=Label(frame1,text='Admin',fg='blue',bg='#050d1f',font = "Verdana 15")
lb_.place(x=80,y=30*3.4)

lb__=Label(frame1,text='Welcome Hospital Management',fg='white',bg='#050d1f',font = "Verdana 10 bold")
lb__.place(x=20,y=30*4.8)

home1=Button(frame1,text='Dashboard',bg='#050d1f',fg='#0ac4fc',font = "Arial 16 bold")
home1.place(x=20,y=30*6.7)
img1=PhotoImage(file='images/h22.png')
lb1=Label(frame1,image=img1,bg='#050d1f')
lb1.place(x=100*1.8,y=30*6.4)

home2=Button(frame1,text='Manage',bg='#050d1f',fg='#0ac4fc',font = "Arial 16 bold")
home2.place(x=20,y=30*9.7-20)
img2=PhotoImage(file='images/an1.png')
lb2=Label(frame1,image=img2,bg='#050d1f')
lb2.place(x=100*1.8,y=30*9.4-24)

home3=Button(frame1,text='About us',bg='#050d1f',fg='#0ac4fc',font = "Arial 16 bold")
home3.place(x=20,y=30*12-20)
img3=PhotoImage(file='images/d.png')
lb3=Label(frame1,image=img3,bg='#050d1f')
lb3.place(x=100*1.8,y=30*12-30)

home4=Button(frame1,text='Exit',bg='#050d1f',fg='#0ac4fc',font = "Arial 14",command=window.destroy)
home4.place(x=20,y=30*19.3)
img4=PhotoImage(file='images/ext1.png')
lb4=Label(frame1,image=img4,bg='#050d1f')
lb4.place(x=100*1.8,y=30*19)
#=================================================================

#=============================window===================
lbe=Label(window,text='Dashboard',bg='#262a36',fg='#9fa4a6',font = "Ubuntu 26")
lbe.place(x=310,y=22)
#======================================================



#====================Search=================
s1=StringVar()
src=Entry(window,fg='white',textvariable=s1,bg='#262a36',font = "Ubuntu 10 bold")
src.place(x=700,y=30,width=300,height=30)
s1.set('Search For something...')

window.mainloop()