from tkinter import *

 #def imprimir():
    #table['text'] = entry1.get()

def somar():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        Resultado['text'] = float(entry1.get()) + float(entry2.get())
    else:
        Resultado['text'] = 'Valor Invalido'
def subtrair():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        Resultado['text'] = float(entry1.get()) - float(entry2.get())
    else:
        Resultado['text'] = 'Valor Invalido'
def multiplicar():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        Resultado['text'] = float(entry1.get()) * float(entry2.get())
    else:
        Resultado['text'] = 'Valor Invalido'
def dividir():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        Resultado['text'] = float(entry1.get()) / float(entry2.get())
    else:
        Resultado['text'] = 'Valor Invalido'


janela = Tk()
janela.geometry('400x200+100+500')
janela.minsize(width=800, height=400)
janela.maxsize(width=800, height=400)
janela.config(background='#FA8072')

label1 = Label(janela, text="Calculo de dois numeros", font= 'Arial 25 bold',background='#FA8072')
label2 = Label(janela, text="Primeiro numero:", font="Arial 15",background='#FA8072')
entry1 = Entry(janela, font="Arial 20")
label3 = Label(janela, text="Segundo numero:", font="Arial 15",background='#FA8072')
entry2 = Entry(janela, font="Arial 20")
button1 = Button(janela, text = "+", font="Arial 25 bold", command=somar)
button2 = Button(janela, text = "-", font="Arial 25 bold", command=subtrair)
button3 = Button(janela, text = "*", font="Arial 25 bold", command=multiplicar)
button4 = Button(janela, text = "/", font="Arial 25 bold", command=dividir)
Resultado = Label(janela, font=" Arial 36",background='#FA8072')
bloco1 = Label(janela,text="-----------------------------------------------------------",foreground="#FA8072",background='#FA8072')
bloco2 = Label(janela,background='#FA8072')
bloco3 = Label(janela,background='#FA8072')
bloco4 = Label(janela,background='#FA8072')
bloco5 = Label(janela,text="-------------------------------------------------------",background='#FA8072')

#label1 = Label(janela, text='Ola mundo', font='Arial 36 bold italic')
#entry1 = Entry(janela, font='Arial 36')
#button1 = Button(janela, text = 'sair', font='Arial 36 bold', command=quit)
#button2 = Button(janela, text = 'imprimir', font='Arial 36 bold', command=imprimir)


#table = Label(janela, text='', font='Arial 36')

label1.pack()
label2.pack()
entry1.pack()
label3.pack()
entry2.pack()
bloco1.pack(side=LEFT)
button1.pack(side=LEFT)
bloco2.pack(side=LEFT)
button2.pack(side=LEFT)
bloco3.pack(side=LEFT)
button3.pack(side=LEFT)
bloco4.pack(side=LEFT)
button4.pack(side=LEFT)
bloco5.pack(side=BOTTOM)
Resultado.pack(side=BOTTOM)

#label1.pack()
#entry1.pack()
#button2.pack()
#button1.pack()
#table.pack()

janela.mainloop()