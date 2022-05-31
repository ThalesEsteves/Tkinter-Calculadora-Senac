from tkinter import *

janela = Tk()

janela.grid_rowconfigure(0,weight=1)
janela.grid_rowconfigure(1,weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

janela.config(background='#add8e6')

bloco1 = Button(janela, text='Bt 1',font="Arial 20")
bloco2 = Button(janela, text='Bt 2',font="Arial 20")
bloco3 = Button(janela, text='Bt 3',font="Arial 20")
bloco4 = Button(janela, text='Bt 4',font="Arial 20")
bloco5 = Button(janela, text='Bt 5',font="Arial 20")
bloco6 = Button(janela, text='Bt 6',font="Arial 20")

bloco1.grid(row=0, column=0,sticky=NSEW)
bloco2.grid(row=0, column=1,sticky=NSEW)
bloco3.grid(row=0, column=2,sticky=NSEW)
bloco4.grid(row=1, column=0,sticky=NSEW)
bloco5.grid(row=1, column=1,sticky=NSEW)
bloco6.grid(row=1, column=2,sticky=NSEW)

janela.mainloop()
