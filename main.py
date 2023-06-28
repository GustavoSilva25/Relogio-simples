# Importando as bibliotecas necessários do Tkinter e time
from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()   #Criando uma instância da janela principal
root.title('Relógio digital')

def relogio():   # Função para atualizar o horário exibido
    horario = strftime('%H:%M:%S')
    Label.config(text=horario)
    Label.after(1000, relogio)

Label = Label(root, font=("Pacifico",60), background="#000", foreground=("#66CC00"))
Label.pack(anchor="center")


relogio()

mainloop()# Iniciando o loop principal 