from tkinter import *

janela = Tk()

janela.config(background='#DEB882')
janela.minsize(width=400, height=200)
janela.maxsize(width=400, height=200)

janela.grid_rowconfigure(0,weight=1)
janela.grid_rowconfigure(1,weight=1)
janela.grid_rowconfigure(2,weight=1)
janela.grid_rowconfigure(3,weight=1)
janela.grid_rowconfigure(4,weight=1)
janela.grid_rowconfigure(5,weight=1)
janela.grid_rowconfigure(6,weight=1)
janela.grid_rowconfigure(7,weight=1)
janela.grid_rowconfigure(8,weight=1)

janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)
janela.grid_columnconfigure(3,weight=1)
janela.grid_columnconfigure(4,weight=1)


def IMC():
    try:
        (Resul['text']) = round(float(pesoV.get()) / (float(alturaV.get()) * float(alturaV.get())),2)
    except:
        Resul['text'] = "Valor Invalido"

#    if pesoV.get().isdigit() and alturaV.get().isdigit():
#        Resul['text'] = float(pesoV.get()) / (float(alturaV.get()) * float(alturaV.get()))
#    else:
#        Resul['text'] = "Valor Invalido" (ERRO: considera "." como texto)

peso = Label(janela,text='Peso:',font='Arial 20',background='#B38B6D')
altura = Label(janela,text='Altura:',font='Arial 20',background='#B38B6D')
pesoV = Entry(janela,font='Arial 20')
alturaV = Entry(janela,font='Arial 20')
IMC = Button(janela,text='IMC',font='Arial 20',command=IMC,background='#B38B6D')
Resul = Label(janela,font='Arial 20',background='#DEB882')
blo1 = Label(janela,font='Arial 20',background='#B38B6D')

peso.grid(row=1,column=1,sticky=NSEW)
pesoV.grid(row=1,column=3,sticky=NSEW)
altura.grid(row=3,column=1,sticky=NSEW)
alturaV.grid(row=3,column=3,stick=NSEW)
IMC.grid(row=5,column=3,sticky=NSEW)
Resul.grid(row=7,column=3,sticky=NSEW)
blo1.grid(row=5,column=1,sticky=NSEW)

janela.mainloop()