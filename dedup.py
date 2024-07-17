from tkinter import *
import tkinter
from PIL import ImageTk, Image 
from main import findandremoveduplicates
window= Tk()
window.title("De-Duplication")
window.geometry("1650x980")
window.configure(bg="beige")
dirname=tkinter.StringVar()
#window.iconbitmap(r'favicon.ico')
lbl=Label(window, text="IMAGE DE-DUPLICATION",fg="teal",bg="pink",font=("Showcard Gothic", 50)).pack(pady=70)
lbl2=Label(window,text="Use me to remove DUPLICATES from ur device",fg="teal",bg="beige",font=("Lucida Sans",35)).pack(padx=50,pady=40)
e= Entry(window,width=60,textvariable = dirname,bd=2,font=("Verdana",15))
#e.configure(highlightcolor= "red")
e.pack(padx= 250)
e.pack(pady=100)
e.focus()
e.insert(0, "Please provide the path of folder...")
e.configure(state=DISABLED)
def onclick(event):
    e.configure(state=NORMAL)
    e.delete(0, END)
    e.unbind('<Button-1>', onclickid)
def submit():
    findandremoveduplicates(dirname.get())
onclickid = e.bind('<Button-1>', onclick)
btn=Button(window,text="DE-DUP",font=("georgia",10),height=1,width=7,bg="teal",fg="white",command=submit).pack(pady=20)
window.mainloop()