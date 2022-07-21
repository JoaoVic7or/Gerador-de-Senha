import random
def gerar_senha():

    caracteres = 'abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWYXZ1234567890!@#$%&*+-/;<>'

    quant = int(quantidade_en.get())

    for pwd in range(quant):
        senha = ''
        for i in range(quant):
            senha += random.choice(caracteres)
        texto_resposta["text"] = senha

    arquivo = open('senha_gerada.txt', 'w')
    arquivo.write('Obrigado por utilizar o gerador de senha ;) \n\n')
    arquivo.write('Sua senha é: ')
    arquivo.write(senha)
    arquivo.close()

from tkinter import *


janela = Tk()
janela.title("Gerador de senhas")
texto = Label(janela, text="Que tal gerar uma senha aleatória e segura?")
texto.grid(column=0, row=0)

quant = Label(janela, text="Quantos caracteres você desejesa? ")
quant.grid(column=0, row=2)

quantidade_en = Entry(janela, width=10)
quantidade_en.grid(column=0, row=3)

botao = Button(janela, text="Gerar", command=gerar_senha, bg='green', fg='white')
botao.grid(column=0, row=4)

texto2 = Label(janela, text="Sua senha é: ")
texto2.grid(column=0, row=5)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=6)

alerta = Label(janela, text="\n\nAtenção: \nSua senha vai ser salva no diretório do arquivo!")
alerta.grid(column=0, row=9)

criado = Label(janela, text="\n\n\n\nCreated By: João Victor Chacon")
criado.grid(column=0, row=11)

janela.mainloop()