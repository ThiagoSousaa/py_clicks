import tkinter as tk
from tkinter import colorchooser

janela = tk.Tk()
janela.title('Contador de Clicks')
janela.config(bg='#0a0a0a')
janela.resizable(False, False)
janela.geometry('400x300')
janela.iconphoto (False, tk.PhotoImage(file='408249.png'))

# Configurando tk

numero = 0

def acrescentar():
    global numero
    numero = numero + 1
    contador_click.config(text=numero)

def diminuir():
    global numero
    numero = numero - 1
    contador_click.config(text=numero)

def sair_tk():
    quit()

def cores_bg():
    trocar_cor = colorchooser.askcolor()[1]
    janela.config(bg=trocar_cor)


botao_adicionar = tk.Button(janela, text=('+'), bg='white', font=('Arial', 16, 'bold'), padx=20, command=acrescentar)
botao_adicionar.place(x=175,y=53)

contador_click = tk.Label(janela, text=numero, fg='white', bg='black', font=('Arial', 16, 'bold'))
contador_click.place(x=200, y=95)

botao_diminuir = tk.Button(janela, text=('-'), bg='white', font=('Arial', 16, 'bold'), padx=20, command=diminuir)
botao_diminuir.place(x=177, y=125)

botao_sair = tk.Button(janela, text=('Sair'), fg='red', bg='white', font=('bold', 16, 'bold'), padx=20, command=sair_tk)
botao_sair.place(x=260, y=90)

botao_cores = tk.Button(janela, text=('Cor'), fg='red', bg='white', font=('Arial', 16, ), padx=20, command=cores_bg)
botao_cores.place(x=69, y=90)


janela.mainloop()

