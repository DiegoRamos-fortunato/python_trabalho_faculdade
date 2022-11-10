
from tkinter import *
from tkinter import Tk,ttk

#Cores
cor_branca = "#F2F2F0"
cor_laranja = "#F28705"
cor_cinza = "#D9CDBF"
cor_laranjaEscuro = "#A64F03"

#janelas
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=cor_branca)
janela.resizable(width = FALSE,height = FALSE)

# dividindo janelas

frame_cima = Frame(janela,width = 310 , height = 50 , bg=cor_laranja, relief='flat'  )
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width = 310 , height = 250 , bg=cor_laranja, relief='flat'  )
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

#configurando o frame cima
l_nome = Label(frame_cima,text='LOGIN',anchor=NE,font=("Ivy 25"),bg=cor_branca,fg=cor_laranjaEscuro)
l_nome.place(x=5,y=5)

#configurando o frame baxi
l_nome = Label(frame_baixo,text='NOME *',anchor=NW,font=("Ivy 10"),bg=cor_branca,fg=cor_laranjaEscuro)
l_nome.place(x=10,y=20)
e_nome = Entry(frame_baixo,width=25,justify='left',font=("",15),relief='solid')
e_nome.place(x = 14, y = 50)

l_senha = Label(frame_baixo,text='SENHA *',anchor=NW,font=("Ivy 10"),bg=cor_branca,fg=cor_laranjaEscuro)
l_senha.place(x=10,y=95)
e_senha = Entry(frame_baixo,width=25,justify='left',font=("",15),relief='solid')
e_senha.place(x = 14, y = 130)

b_botao= Button(frame_baixo,text='ENTRAR ',width=39,height=2,anchor=NW,font=(' Ivy 8 bold '),bg=cor_branca,fg=cor_laranjaEscuro,relief=RAISED)
b_botao.place(x=15,y=180)


janela.mainloop()

