from tkinter import * 
from pygame import mixer

import random 

mixer.init()
mixer.music.load("song.mp3")
mixer.music.play(-1)

def escolha_dificuldade():
    Label(interface_dificuldade, text='Escolha sua dificuldade abaixo:', font=('Arial',12), 
          fg='black').pack() 
    Button(interface_dificuldade, text="Fácil - 10 erros permitidos", font=('Arial', 12), 
           fg='black', command=escolha_dificuldade_facil).pack() 
    Button(interface_dificuldade, text="Médio - 8 erros permitidos", font=('Arial', 12), 
           fg='black', command=escolha_dificuldade_medio).pack() 
    Button(interface_dificuldade, text="Dificil - 6 erros permitidos", font=('Arial', 12), 
           fg='black', command=escolha_dificuldade_dificil).pack() 

def escolha_dificuldade_facil():
    dificuldade.append(10)
    interface_dificuldade.destroy()

def escolha_dificuldade_medio():
    dificuldade.append(8)
    interface_dificuldade.destroy()

def escolha_dificuldade_dificil():
    dificuldade.append(6)
    interface_dificuldade.destroy()

def forca(event):
    cabeca_olhos_nariz = interface_forca.create_oval
    corpo = interface_forca.create_line
    boca = interface_forca.create_arc

    try:
        char = caracter.get().upper()[0] 
    except IndexError:
        pass
    else:
        try:
            int(char) 
        except ValueError:
            if char not in letras_escolhidas:
                letras_escolhidas.append(char) 
                for indice in range(len(letras)): 
                    if char == letras[indice]: 
                        lista_traco[indice] = letras[indice] 
                        caracter_vazio['text'] = lista_traco
                        lista_conferencia.append(char)

                if char not in letras:
                    lista_erro.append(char)
                    caracteres_anteriores['text'] = lista_erro

    entrada_dados.set('') 

    if len(lista_conferencia) == len(letras): 
        mensagem_final['text'] = 'Jogo Ganho! Parabéns!'
        mensagem_final['fg'] ='green' 
        caracter.destroy()
        Button(interface,text='Finalizar',font=('Arial',12),fg='red',command=quit).pack()

    if len(lista_erro) == dificuldade[0]:
        mensagem_final['text'] = "Erros máximos atingidos, você perdeu!" 
        mensagem_final['fg'] = 'red'
        caracter.destroy() 
        Button(interface, text='Finalizar', font=('Arial', 12), fg='red', command=quit).pack() 

    if len(lista_erro) == 1: 
        cabeca_olhos_nariz(165,95,215,140,fill='gray',outline='black')
    if len(lista_erro) == 2: 
        corpo(190, 140, 190, 235)
    if len(lista_erro) == 3: 
        corpo(190, 140, 130, 190)
    if len(lista_erro) == 4: 
        corpo(198, 140, 258, 198)
    if len(lista_erro) == 5: 
        corpo(190, 235, 125, 308)
    if len(lista_erro) == 6:
        corpo(198, 235, 258, 300)
    if len(lista_erro) == 7: 
        cabeca_olhos_nariz(175, 195, 185, 115, fill='white', outline='black')
    if len(lista_erro) == 8: 
        cabeca_olhos_nariz(195, 105, 205, 115, fill='white', outline='black')
    if len(lista_erro) == 9:
        cabeca_olhos_nariz(187.5, 117.5, 192.5, 122.5, fill='white', outline='black')
    if len(lista_erro) == 10: 
        boca(165, 125, 205, 130, fill='white') 

def quit(): 
    global interface_dificuldade
    interface.destroy() 
    interface_dificuldade = Tk() 
    escolha_dificuldade() 
    interface_dificuldade.mainloop() 


with open('palavras.txt') as arq:
    leitura = arq.readlines()
    palavra = random.choice(leitura).split("\n")[0].upper()


letras = []  
lista_traco = [] 
lista_erro = []
letras_escolhidas = [] 
lista_conferencia = [] 
dificuldade = [] 

for indice in range(len(palavra)):
    letras.append(palavra[indice])
    lista_traco.append(" _____ ")


interface_dificuldade = Tk() 
escolha_dificuldade() 
interface_dificuldade.mainloop() 

if len(dificuldade) == 1:
    interface = Tk()
    interface_titulo = Canvas(interface) 
    interface_titulo.pack(side=TOP) 
    interface_forca = Canvas(interface,width=400, height=400) 
    interface_forca.pack(side=TOP)
    interface_texto = Canvas(interface,width=400, height=400)
    interface_texto.pack(side=TOP)

    interface_forca.create_rectangle(10,400,400,390,fill='yellow') 
    interface_forca.create_rectangle(10,400,20,30,fill='yellow')
    interface_forca.create_rectangle(10, 30, 200, 40, fill='yellow')
    interface_forca.create_rectangle(130,40,200,50,fill='red')
    interface_forca.create_rectangle(187.5,50,192.5,90,fill='black')
    interface_forca.create_oval(160,90,220,145,fill='black')
    interface_forca.create_oval(165,95,215,140,fill='white')

    Label(interface_titulo,text='Bem Vindo ao Jogo da Forca! ',font=('Arial',12),fg='black').pack()
    Label(interface_texto, text=f'Digite sua letra abaixo:\n{palavra}',font=('Arial',12),fg='black').pack()
    entrada_dados = StringVar()
    caracter = Entry(interface_texto, textvariable=entrada_dados)
    caracter.pack() 


    caracter.bind("<Return>", forca)
    caracter_vazio = Label(interface_texto, text=lista_traco)
    caracter_vazio.pack()

    Label(interface_texto, text="Letras Erradas:")
    caracteres_anteriores = Label(interface_texto, text=lista_erro)
    caracteres_anteriores.pack()

    mensagem_final = Label(interface_texto, text='')
    mensagem_final.pack()
    interface.mainloop()

