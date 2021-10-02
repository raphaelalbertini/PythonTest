from tkinter import *

def Cria():
    window2 = Tk()
    window2.mainloop()

window = Tk()

botao = Button(window,text="Cria",command=Cria)
botao.pack()

window.mainloop()


print("loop main")