from modulos import *
import customtkinter as Tk

def mediaacao():
    n1 = int(nota1.get())
    prest = int(prestacao.get())

    res = n1/prest

    if res >= 500:
        label.configure(text=f'parcela: {res} | Usuário não consegue pagar.')
    elif res <500:
        label.configure(text=f'parcela: {res} | Usuário consegue pagar.')

Janela = CriarJanela('Janela Principal', '900x400',1)
nota1 = CriarCaixaDeTexto(Janela, 70,20,1,6)
prestacao = CriarCaixaDeTexto(Janela, 70,20,2,6)
label = CriarLabel(Janela, '', 5,6)

btn1 = CriarBotão(Janela, "Calcular a média", mediaacao, 3,6,100,30)

Janela.mainloop()