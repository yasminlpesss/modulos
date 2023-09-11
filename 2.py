from modulos import *
import customtkinter as Tk

def mediaacao():
    n1 = int(nota1.get())
    res = 2023-n1

    if res >= 18:
        label.configure(text=f'Idade: {res} | Maior de idade.')
    else:
        label.configure(text=f'Idade: {res} | Menor de idade.')

Janela = CriarJanela('Janela Principal', '900x400',1)
nota1 = CriarCaixaDeTexto(Janela, 70,20,1,6)
label = CriarLabel(Janela, '', 5,6)

btn1 = CriarBotão(Janela, "Ver maioridade", mediaacao, 3,6,100,30)

Janela.mainloop()