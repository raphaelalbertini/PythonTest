from tkinter import *

def Cria():
    window2 = Tk()
    botao1 = Button(window2,text="Cria2",command=window.destroy)
    botao1.pack()
    window2.mainloop()

window = Tk()

botao = Button(window,text="Cria",command=Cria)
botao.pack()

window.mainloop()


print("loop main")