#Escrito por Luan Roberto Nunes em 17/12/2021

import tkinter
import easygui
import random
import threading
import time
import turtle
import pandas
import os
import datetime as dt
from turtle import textinput
from tkinter import messagebox

tur = turtle

pendNome = True
csv_state = False

rodada = 0
agora = dt.datetime.now()
dataatual = f"{agora.day}/{agora.month}/{agora.year} às {agora.hour}:{agora.minute}:{agora.second}"
participantes = []

time.sleep(1)
tur.title("Sistema de Sorteios by Luan Roberto Nunes")
tur.penup()
tur.hideturtle()
#tur.bgpic('caminhodalogo/logo.png') -> INSIRA SUA LOGO AQUI
tur.goto(-70, -220)
tur.write(f"              {agora.day}/{agora.month}/{agora.year}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n2021\n"
          f"\nSISTEMA DE SORTEIOS", font=("Song body", 12,
                                                                                                    "bold"))
tur.goto(0, -300)
tur.shapesize(5, 5)


def abre_csv():
    csv_input = easygui.fileopenbox("Selecione o arquivo CSV")
    try:
        data = pandas.read_csv(csv_input,index_col=1).drop_duplicates()
        for index, row in data.iterrows():
          participantes.append(row["nome"])
          global pendNome
          pendNome = False
        messagebox.showinfo(title="Sucesso!", message="O arquivo foi importado com sucesso!")
    except UnicodeDecodeError:
        messagebox.showerror(title="Formato não suportado", message="Este formato de arquivo não é suportado, "
                                                      "por favor, selecione um arquivo CSV")
        abre_csv()
    except IndexError:
        messagebox.showerror(title="Arquivo não formatado corretamente", message=
                                                                        "O arquivo não está formatado corretamente!"
                                                                        "\n\nSão necessárias pelo menos duas "
                                                                        "colunas separadas por virgula.\n\nPor favor, "
                                                                        "verifique o arquivo de exemplo contido na "
                                                                         "pasta do programa.")
        abre_csv()

    tur.bye()
    root_window()


def selecao_manual():
    global pendNome
    while pendNome == True:
        nome_participante = textinput("Nomes", "Digite o nome de um participante e clique em OK\n"
                                               "Se terminou de informar os nomes, deixe vazio e clique em "
                                               "OK:").upper()
        tur.ht()
        if nome_participante == '' and len(participantes) != 0:
            pendNome = False
            turtle.bye()
            root_window()

        if nome_participante == '' and len(participantes) == 0:
            messagebox.showerror(title="Vazio", message="Você não inseriu nenhum nome")

        if nome_participante != '':
            participantes.append(nome_participante)


def vencedores():
    try:
        with open("Vencedores.txt", "r") as venc_file:
            venc = venc_file.read()
            messagebox.showinfo(title="Vencedores", message=venc)
    except FileNotFoundError:
        messagebox.showerror(title="Nenhum sorteio", message="Nenhum sorteio foi efetuado ainda, realize pelo menos "
                                                             "um e então, tente visualizar os vencedores.")



opcao = tkinter.Label(text="SELECIONE A FUNÇÃO DESEJADA: ", width=50, height=3, font=("Song body", 15, "bold"))
opcao.pack()

bt_manual = tkinter.Button(text="Adição manual de nomes", width=35, height=3, command=selecao_manual, fg="Blue")
bt_manual.pack()

bt_csv = tkinter.Button(text="Adição de nomes por arquivo CSV", width=35, height=3, command=abre_csv, fg="Green")
bt_csv.pack()


def root_window():

    root = tkinter.Tk()
    root.title("Sorteio - Execução")
    root.geometry('700x700+500+200')
    root.resizable(True, True)
    root.flag = True
    root.config(background="Gray")

    primeiro = tkinter.Label(root, text='', font=("Song body", 11, "normal"))
    primeiro.place(x=180, y=100, width=350, height=100)

    segundo = tkinter.Label(root, text='', font=("Song body", 11, "bold"))
    segundo['fg'] = 'red'
    segundo.place(x=180, y=200, width=350, height=100)

    terceiro = tkinter.Label(root, text='', font=("Song body", 11, "normal"))
    terceiro.place(x=180, y=300, width=350, height=100)

    destaque = tkinter.Label(root, text='', font=("Song body", 11, "bold"))
    destaque.config(fg= "Yellow", bg="Gray", highlightthickness = 0)
    destaque.place(x=130, y=0, width=500, height=100)

    venc_label = tkinter.Label(root, text='', font=("Song body", 10, "normal"))
    venc_label.config(fg="Yellow", bg="Gray", highlightthickness=0)
    venc_label.place(x=200, y=500, width=300, height=100)

    def rolaTela():
        vencedores = []
        vencedor = ''
        root.flag = True
        v = 0
        while root.flag:
            try:
                i = random.randint(0, len(participantes) - 1)
                primeiro['text'] = segundo['text']
                vencedor = segundo['text'] = terceiro['text']
                terceiro['text'] = participantes[i]
                time.sleep(0.005)
                vencedores.append(vencedor)
            except ValueError:
                messagebox.showerror(title="Entrada", message="Houve uma falha na entrada de dados\nApenas nomes são"
                                                              "aceitos!")

        for ven in range(len(vencedores)-1):
            v+=1
            venc_label['text'] = f"{vencedores[v]}\n"
            destaque['text'] = f"{vencedor} É O(A) VENCEDOR(A)"


        with open("Vencedores.txt", mode="a") as file:
            file.write(f"VENCEDOR DA RODADA {rodada}: {vencedor}  |  {agora.day}/{agora.month}/{agora.year}  \n\n---------------------------------------------------"
                       f"------------------------\n\n")

    def clickInicio():
        destaque['text'] = ""
        global rodada
        t = threading.Thread(target=rolaTela)
        t.start()
        rodada += 1
        rodada_label = tkinter.Label(root, text=f'Rodada {rodada}', font=("Song body", 12, "normal"))
        rodada_label.config(fg="Black", bg="Gray", highlightthickness=0)
        rodada_label.place(x=200, y=400, width=300, height=100)
        if clickInicio and root.flag:
            rodada -=1 ##validando linha

    def clickFim():
        root.flag = False

    def reinicia_rodada():
        global rodada
        rodada = 0
        try:
            with open("vencedores.txt","a") as venc_file:
                venc_file.write("\n\n\n***************** NOVA SÉRIE DE RODADAS *****************\n\n\n ")

        except FileNotFoundError:
            messagebox.showerror(title="Nenhuma rodada", message="Você ainda não iniciou nenhuma rodada, "
                                                                 "para reinicializar as rodadas, é necessário ter"
                                                                 "executado pelo menos uma")
        messagebox.showinfo(title="Nova série", message="Nova série iniciada com sucesso! Basta INICIAR para começar "
                                                        "com a nova série de rodadas")

    def limpa_vencedores():
        limpa = messagebox.askokcancel(title="Limpar vencedores", message="Atenção!\n\nEsta ação irá apagar todo o histórico de "
                                                                  "vencedores, deseja prosseguir?")
        if limpa == True:
            try:
                os.remove("vencedores.txt")
                global rodada
                rodada = 0
                messagebox.showinfo(title="Limpo", message="O histórico de vencedores foi limpo com sucesso!")
            except FileNotFoundError:
                messagebox.showerror(title="Sem vencedores", message="Ainda não existem vencedores!\nO sorteio não"
                                                                     " foi executado")

    def sobre():
        messagebox.showinfo(title="SOBRE", message="Sistema de Sorteios"
                                        "\n\nDesenvolvido por Luan Roberto Nunes\nSoftware Developer & Business Analyst\n"
           "\n\nluanrobertonunes@hotmail.com\n"
       )
    def imprimir():
        imp = messagebox.askyesno(title="Imprimir vencedores", message="Tem certeza que deseja realizar a "
                                                                "impressão dos vencedores?")
        if imp:
            try:
                os.startfile("vencedores.txt", "print")
                messagebox.showinfo(title="Impressão enviada", message="A impressão dos vencedores"
                                                                       " foi enviada com sucesso para a "
                                                                        "impressora padrão!")
            except FileNotFoundError:
                messagebox.showerror(title="Sem vencedores", message="Ainda não existem vencedores!\nO sorteio não"
                                                                     " foi executado")


    btnInicio = tkinter.Button(root, text='INICIAR', command=clickInicio, bg="Green")
    btnInicio.place(x=100, y=500, width=80, height=60)

    btnParar = tkinter.Button(root, text='PARAR', command=clickFim, bg="Red")
    btnParar.place(x=500, y=500, width=80, height=60)

    btnVisualizar = tkinter.Button(root, text='VENCEDORES', command=vencedores, bg="Gray", highlightthickness=0)
    btnVisualizar.place(x=10, y=200, width=150, height=60)

    btnReiniciaRodada = tkinter.Button(root, text='REINICIAR RODADAS', command=reinicia_rodada, bg="White",
                                       highlightthickness=0)
    btnReiniciaRodada.place(x=270, y=600, width=150, height=60)

    btnLimpaVencedores = tkinter.Button(root, text='LIMPAR VENCEDORES', command=limpa_vencedores, bg="Orange",
                                        highlightthickness=0)
    btnLimpaVencedores.place(x=540, y=200, width=150, height=60)

    btnSobre = tkinter.Button(root, text='SOBRE', command=sobre, bg="Brown", highlightthickness=0)
    btnSobre.place(x=5, y=5, width=50, height=30)

    btnImprimir = tkinter.Button(root, text='IMPRIMIR VENCEDORES', command=imprimir, bg="Yellow", highlightthickness=0)
    btnImprimir.place(x=10, y=260, width=150, height=60)

    root.mainloop()

    try:
        with open("vencedores.txt", "a") as venc_file:
            venc_file.write("\n\n\n\n")
    except FileNotFoundError:
        messagebox.showerror(title="Nenhuma rodada", message="Você ainda não iniciou nenhuma rodada, "
                                                             "para reinicializar as rodadas, é necessário ter"
                                                             "executado pelo menos uma")

tur.mainloop()




