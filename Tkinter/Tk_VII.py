from tkinter import *

janela = Tk()

fr1 = Frame(janela,background='blue')
fr2 = Frame(janela,background='white')

lb1 = Label(fr1, text='Label no frame 1',font='Arial 25')
lb2 = Label(fr2,text='Label no frame 2',font='Arial 25')
bt1 = Button(fr1,text='Frame 1',font='Arial 25')
bt2 = Button(fr2,text='Frame 2',font='Arial 25')

fr1.pack()
fr2.pack()
lb1.grid(row=0,column=0)
bt1.grid(row=1,column=1)
lb2.grid(row=0,column=0)
bt2.grid(row=1,column=1)

janela.mainloop()