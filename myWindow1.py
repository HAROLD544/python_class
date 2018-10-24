#Importar librerias para GUI
from Tkinter import *
import Tkinter
#######################
root = Tkinter.Tk()
root.geometry("400x400")
root.title("mi calculadora")
root.resizable(FALSE,FALSE)
root.configure(background="#17A589")
#######################
display=Entry(root,font=('arial',20,'bold'),width=22,bd=20,insertwidth=10,bg="#A93226",justify="right").place(x=10,y=60)
boton1=button(root,text="1",width=7,height=3).place(x=10,y=60)
root.mainloop()

