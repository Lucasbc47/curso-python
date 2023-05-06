import random
import tkinter as tk

class App:
    def __init__(self, root: tk.Tk):

        self.letras = []  
        self.lista_traco = [] 
        self.lista_erro = []
        self.letras_escolhidas = [] 
        self.lista_conferencia = [] 
        self.dificuldade = [] 

        root.title("Forca")
        width = 199
        height = 121
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        DificuldadeLabel=tk.Label(root)
        DificuldadeLabel["fg"] = "#333333"
        DificuldadeLabel["justify"] = "center"
        DificuldadeLabel["text"] = "Escolha dificuldade:"
        DificuldadeLabel.place(x=40,y=10,width=123,height=30)

        EasyButton=tk.Button(root)
        EasyButton["bg"] = "#f0f0f0"
        EasyButton["fg"] = "#000000"
        EasyButton["justify"] = "center"
        EasyButton["text"] = "Fácil"
        EasyButton.place(x=10,y=40,width=70,height=25)
        EasyButton["command"] = self.easy_button_event

        HardButton=tk.Button(root)
        HardButton["bg"] = "#f0f0f0"
        HardButton["fg"] = "#000000"
        HardButton["justify"] = "center"
        HardButton["text"] = "Díficil"
        HardButton.place(x=60,y=70,width=70,height=25)
        HardButton["command"] = self.hard_button_event

        MediumButton=tk.Button(root)
        MediumButton["bg"] = "#f0f0f0"
        MediumButton["fg"] = "#000000"
        MediumButton["justify"] = "center"
        MediumButton["text"] = "Médio"
        MediumButton.place(x=110,y=40,width=70,height=25)
        MediumButton["command"] = self.medium_button_event




        if len(self.dificuldade) == 1:
            
            for indice in range(len(self.get_palavrax())):
                self.letras.append(self.get_palavrax()[indice])
                self.lista_traco.append(" _____ ")
            


            self.interface = tk.Tk()
            self.interface_titulo = tk.Canvas(self.interface) 
            self.interface_titulo.pack(side=tk.TOP) 
            self.interface_forca = tk.Canvas(self.interface,width=400, height=400) 
            self.interface_forca.pack(side=tk.TOP)
            self.interface_texto = tk.Canvas(self.interface,width=400, height=400)
            self.interface_texto.pack(side=tk.TOP)

            self.interface_forca.create_rectangle(10,400,400,390,fill='yellow') 
            self.interface_forca.create_rectangle(10,400,20,30,fill='yellow')
            self.interface_forca.create_rectangle(10, 30, 200, 40, fill='yellow')
            self.interface_forca.create_rectangle(130,40,200,50,fill='red')
            self.interface_forca.create_rectangle(187.5,50,192.5,90,fill='black')
            self.interface_forca.create_oval(160,90,220,145,fill='black')
            self.interface_forca.create_oval(165,95,215,140,fill='white')

            tk.Label(self.interface_titulo,text='Bem Vindo ao Jogo da Forca! ',font=('Arial',12),fg='black').pack()
            tk.Label(self.interface_texto, text=f'Digite sua letra abaixo:\n{self.get_palavrax()}',font=('Arial',12),fg='black').pack()
            self.entrada_dados = tk.StringVar()
            self.caracter = tk.Entry(self.interface_texto, textvariable=self.entrada_dados)
            self.caracter.pack() 


            self.caracter.bind("<Return>", self.forca(self.interface_forca))
            self.caracter_vazio = tk.Label(self.interface_texto, text=self.lista_traco)
            self.caracter_vazio.pack()

            tk.Label(self.interface_texto, text="Letras Erradas:")
            self.caracteres_anteriores = tk.Label(self.interface_texto, text=self.lista_erro)
            self.caracteres_anteriores.pack()

            self.mensagem_final = tk.Label(self.interface_texto, text='')
            self.mensagem_final.pack()
            self.interface.mainloop()


    def get_palavrax(self):
        with open('palavras.txt') as arq:
            leitura = arq.readlines()
            palavra = random.choice(leitura).split("\n")[0].upper()
        return palavra

    def easy_button_event(self):
        self.dificuldade.append(10)
        root.destroy()

    def medium_button_event(self):
        self.dificuldade.append(8)
        root.destroy()

    def hard_button_event(self):
        self.dificuldade.append(6)
        root.destroy()


    def forca(self):
        cabeca_olhos_nariz = self.interface_forca.create_oval
        corpo = self.interface_forca.create_line
        boca = self.interface_forca.create_arc

        try:
            char = self.caracter.get().upper()[0] 
        except IndexError:
            pass
        else:
            try:
                int(char) 
            except ValueError:
                if char not in self.letras_escolhidas:
                    self.letras_escolhidas.append(char) 
                    for indice in range(len(self.letras)): 
                        if char == self.letras[indice]: 
                            self.lista_traco[indice] = self.letras[indice] 
                            self.caracter_vazio['text'] = self.lista_traco
                            self.lista_conferencia.append(char)

                    if char not in self.letras:
                        self.lista_erro.append(char)
                        self.caracteres_anteriores['text'] = self.lista_erro

        self.entrada_dados.set('') 

        if len(self.lista_conferencia) == len(self.letras): 
            self.mensagem_final['text'] = 'Jogo Ganho! Parabéns!'
            self.mensagem_final['fg'] ='green' 
            self.caracter.destroy()
            tk.Button(self.interface,text='Finalizar',font=('Arial',12),fg='red',command=quit).pack()

        if len(self.lista_erro) == self.dificuldade[0]:
            self.mensagem_final['text'] = "Erros máximos atingidos, você perdeu!" 
            self.mensagem_final['fg'] = 'red'
            self.caracter.destroy() 
            tk.Button(self.interface, text='Finalizar', font=('Arial', 12), fg='red', command=quit).pack() 

        if len(self.lista_erro) == 1: 
            cabeca_olhos_nariz(165,95,215,140,fill='gray',outline='black')
        if len(self.lista_erro) == 2: 
            corpo(190, 140, 190, 235)
        if len(self.lista_erro) == 3: 
            corpo(190, 140, 130, 190)
        if len(self.lista_erro) == 4: 
            corpo(198, 140, 258, 198)
        if len(self.lista_erro) == 5: 
            corpo(190, 235, 125, 308)
        if len(self.lista_erro) == 6:
            corpo(198, 235, 258, 300)
        if len(self.lista_erro) == 7: 
            cabeca_olhos_nariz(175, 195, 185, 115, fill='white', outline='black')
        if len(self.lista_erro) == 8: 
            cabeca_olhos_nariz(195, 105, 205, 115, fill='white', outline='black')
        if len(self.lista_erro) == 9:
            cabeca_olhos_nariz(187.5, 117.5, 192.5, 122.5, fill='white', outline='black')
        if len(self.lista_erro) == 10: 
            boca(165, 125, 205, 130, fill='white') 



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
