import random
from tkinter import *
def gerar_senha():

    caracteres = 'abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890!@#$%&*+-/;<>'

    quant = int(quantidade_en.get())

    for pwd in range(quant):
        senha = ''
        for i in range(quant):
            senha += random.choice(caracteres)
        texto_resposta["text"] = senha

    titulo_senha = nome_senha_en.get() + ':'

    arquivo = open('senha_gerada.txt', 'a')
    arquivo.write(titulo_senha.title())
    arquivo.write("\n")
    arquivo.write(senha)
    arquivo.write("\n")
    arquivo.write("===FIM===")
    arquivo.write("\n")
    arquivo.close()
janela = Tk()
janela.title("Gerador de senhas")
texto = Label(janela, text="Que tal gerar uma senha aleatória e segura?")
texto.grid(column=0, row=0)

quant = Label(janela, text="Quantos caracteres você desejesa? ")
quant.grid(column=0, row=2)

quantidade_en = Entry(janela, width=10)
quantidade_en.grid(column=0, row=3)

nome_senha = Label(janela, text="Deseja inserir um título para sua senha?(deixar em branco caso não)")
nome_senha.grid(column=0, row=4)

nome_senha_en = Entry(janela, width=30)
nome_senha_en.grid(column=0, row=5)

botao = Button(janela, text="Gerar", command=gerar_senha, bg='green', fg='white')
botao.grid(column=0, row=6)

texto2 = Label(janela, text="Sua senha é: ")
texto2.grid(column=0, row=7)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=8)

alerta = Label(janela, text="\n\nAtenção: \nSua senha vai ser salva no diretório do arquivo!")
alerta.grid(column=0, row=9)

criado = Label(janela, text="\n\n\n\nCreated By: João Victor Chacon")
criado.grid(column=0, row=11)

janela.mainloop()