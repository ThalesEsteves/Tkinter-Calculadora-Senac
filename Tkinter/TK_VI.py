from tkinter import *

janela = Tk()

def entrada(valor):
    contas['text'] += valor

def saida():
    resul= eval(contas['text'])
    contas['text'] = str(resul)

def limpar():
    contas['text'] = ''

def deletar():


janela.configure(background='#F7F7F7')

janela.grid_rowconfigure(0,weight=1)
janela.grid_rowconfigure(1,weight=1)
janela.grid_rowconfigure(2,weight=1)
janela.grid_rowconfigure(3,weight=1)
janela.grid_rowconfigure(4,weight=1)
janela.grid_rowconfigure(5,weight=1)
janela.grid_rowconfigure(6,weight=1)
janela.grid_rowconfigure(7,weight=1)


janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)
janela.grid_columnconfigure(3,weight=1)


B1 = Button(janela,text='1',font='Arial 25',command=lambda: entrada('1'))
B2 = Button(janela,text='2',font='Arial 25',command= lambda: entrada('2'))
B3 = Button(janela,text='3',font='Arial 25',command= lambda: entrada('3'))
B4 = Button(janela,text='4',font='Arial 25',command= lambda: entrada('4'))
B5 = Button(janela,text='5',font='Arial 25',command= lambda: entrada('5'))
B6 = Button(janela,text='6',font='Arial 25',command= lambda: entrada('6'))
B7 = Button(janela,text='7',font='Arial 25',command= lambda: entrada('7'))
B8 = Button(janela,text='8',font='Arial 25',command= lambda: entrada('8'))
B9 = Button(janela,text='9',font='Arial 25',command= lambda: entrada('9'))
B0 = Button(janela,text='0',font='Arial 25',command= lambda: entrada('0'))
Bsoma = Button(janela,text='+',font='Arial 25',background='#DCDCDC',command=lambda: entrada('+'))
Bsub = Button(janela,text='-',font='Arial 25',background='#DCDCDC',command=lambda: entrada('-'))
Bdivi = Button(janela,text='/',font='Arial 25',background='#DCDCDC',command=lambda: entrada('/'))
Bvezes = Button(janela,text='X',font='Arial 25',background='#DCDCDC',command=lambda: entrada('*'))
Bigual = Button(janela,text='=',font='Arial 25',background='#808080',command=saida)
Del = Button(janela,text='«',font='Arial 25',background='#DCDCDC',command=lambda: entrada(''))
C = Button(janela,text='C',font='Arial 25',background='#DCDCDC',command=limpar)
vir = Button(janela,text=',',font="Arial 25",background='#DCDCDC',command=lambda: entrada(','))
parenE = Button(janela,text='(',font='Arial 25',background='#DCDCDC',command=lambda: entrada('('))
parenD = Button(janela,text=')',font='Arial 25',background='#DCDCDC',command=lambda: entrada(')'))
contas = Label(janela,font='Arial 25',background='#F7F7F7')
resul = Label(janela,font='Arial 25',background='#F7F7F7')

B1.grid(row=6,column=0,sticky=NSEW)
B2.grid(row=6,column=1,sticky=NSEW)
B3.grid(row=6,column=2,sticky=NSEW)
B4.grid(row=5,column=0,sticky=NSEW)
B5.grid(row=5,column=1,sticky=NSEW)
B6.grid(row=5,column=2,sticky=NSEW)
B7.grid(row=4,column=0,sticky=NSEW)
B8.grid(row=4,column=1,sticky=NSEW)
B9.grid(row=4,column=2,sticky=NSEW)
B0.grid(row=7,column=1,sticky=NSEW)
Bsoma.grid(row=6,column=3,sticky=NSEW)
Bsub.grid(row=5,column=3,sticky=NSEW)
Bvezes.grid(row=4,column=3,sticky=NSEW)
Bdivi.grid(row=3,column=3,sticky=NSEW)
Bigual.grid(row=7,column=3,sticky=NSEW)
Del.grid(row=7,column=2,sticky=NSEW)
C.grid(row=3,column=0,sticky=NSEW)
vir.grid(row=7,column=0,sticky=NSEW)
parenE.grid(row=3,column=1,sticky=NSEW)
parenD.grid(row=3,column=2,sticky=NSEW)
contas.grid(row=0,column=0, columnspan=4,sticky=NSEW)
resul.grid(row=1,column=0, columnspan=4,sticky=NSEW)

janela.mainloop()