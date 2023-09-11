from modulos import *
import customtkinter as Tk

def mediaacao():
    n1 = int(nota1.get())
    n2 = int(nota2.get())

    res = (n1+n2)/2

    if res >= 6:
        label.configure(text=f'Média: {res} | Aluno aprovado.')
    elif res <6:
        label.configure(text=f'Média: {res} | Aluno reprovado.')

Janela = CriarJanela('Janela Principal', '900x400',1)
nota1 = CriarCaixaDeTexto(Janela, 70,20,1,6)
nota2 = CriarCaixaDeTexto(Janela, 70,20,2,6)
label = CriarLabel(Janela, '', 5,6)

btn1 = CriarBotão(Janela, "Calcular a média", mediaacao, 3,6,100,30)

Janela.mainloop()