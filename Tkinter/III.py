from tkinter import *

janela = Tk()
janela.config(background='#808080')

janela.grid_rowconfigure(0,weight=1)

janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=1)
janela.grid_columnconfigure(2,weight=1)
janela.bind('-', lambda event: subtrai())
janela.bind('+',lambda event: soma())

def soma():
    #if int(resul["text"] < 10
    if resul["text"] != 10 :
        #resul["text"] += 1
        resul["text"] = int(resul["text"]) + 1
    else:
        #
        #pass
        resul["text"] = resul["text"]

def subtrai():
    # if int(resul["text"]) > -10 :
    if resul["text"] != -10 :
        resul["text"] = int(resul["text"]) - 1
    else:
        pass

bt1 = Button(janela,text='-',font="Arial 36",background='#d3d3d3', command=subtrai)
bt2 = Button(janela,text='+',font="Arial 36",background='#d3d3d3', command=soma)
resul = Label(janela,text='0',font='Arial 36')

bt1.grid(row=0,column=0,sticky=NSEW)
resul.grid(row=0,column=1,sticky=NSEW)
bt2.grid(row=0,column=2,sticky=NSEW)


janela.mainloop()


