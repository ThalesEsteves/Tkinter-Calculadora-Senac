from tkinter import *

janela = Tk()

fr1 = Frame(janela,bg='#add8e6')
fr2 = Frame(janela,bg='#add8e6')
fr3 = Frame(janela,bg='#add8e6')

janela.config(background="#add8e6")
janela.grid_rowconfigure(0,weight=1)
janela.grid_rowconfigure(1,weight=1)
janela.grid_rowconfigure(2,weight=1)
janela.grid_rowconfigure(3,weight=1)
janela.grid_rowconfigure(4,weight=1)

janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)

def converter():
    try:
        Rfah['text'] = float(cel.get()) * 1.8 + 32
    except:
        Rfah['text'] = 'Valor Invalido'

temp = Label(janela,text='Conversão',font='Arial 20 bold',background='#add8e6')
cel = Entry(janela,font='Arial 12',background='#add8e6')
Gcel = Label(janela,text='Grau Celsius',font='Arial 20')
Rfah = Label(janela,font='Arial 20',background='#add8e6')
Gfah = Label(janela,text='Grau Fahrenheit',font='Arial 19')
Conv = Button(janela,text='Converter',font='Arial 16',command=converter)
engual = Label(janela,text='=',font='Arial 20',background='#add8e6')
sair = Button(janela,text='Sair',font='Arial 20',command=quit)

fr1.grid()
fr2.grid(sticky=NSEW)
fr3.grid()
temp.grid(row=0,column=1)
cel.grid(row=0,column=0)
Gcel.grid(row=1,column=0)
engual.grid(row=0,column=1)
Rfah.grid(row=0,column=2)
Gfah.grid(row=1,column=2)
sair.grid(row=0,column=1)
Conv.grid(row=1,column=1)

janela.mainloop()
