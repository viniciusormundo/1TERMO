# TKINTER

# componentes Widgts
# tk : tk() #janela
# lb: Label() #rotulo
# bt: Button() #botão 
# et: Entry() #Caixa de texto

# import tkinter as tk
# from tkinter import messagebox

# # 1. Criar a janela principal 
# janela = tk.Tk()
# janela.title("Minha primeira janela GUI")
# janela.geometry("400x200") #Largura x altura
# janela.configure(bg="#551d54")
 
# # 2 criar a funçao do botao (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("sucesso!", "voce clicou no botão")

# # 3 Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-vindo a nossa aula de tkinter",bg="#551d54", font=("Arial", 14, "bold"))
# btn_clique = tk.Button(janela, text="Clique Aqui", font=("arial", 11), bg="#551d54", fg="white", command=mostrar_mensagem)
# bnt_close = tk.Button(janela, text="Fechar", font=("Aril", 14, "bold"), bg="#380b35", fg="white" , command=janela.destroy)


# # 4 Posicionar os composnentes
# lbl_titulo.pack(pady=20)
# btn_clique.pack(pady=10)
# bnt_close.pack(pady= 5)


# #5 rodar loop da interface 
# janela.mainloop()

# import tkinter as tk
# from tkinter import messagebox

# def saudar_usuario():
#     #. get() serve para buscar o texto que vamos digitar

#     nome = campo_nome.get()

#     if nome =="":
#         messagebox.showwarning("aviso","por favor digite seu nome! :)")
#     else:
#         messagebox.showinfo("saudações alunos", f"ola {nome}! seja bem-vindo ao mundo das interfaces graficas")

# #config da janela
# app = tk.Tk()
# app.title = ("Exemplo")
# app.geometry("350x200")

# #componentes
# lbl_introducao = tk.Label(app, text="digite seu nome abaixo")
# lbl_introducao.pack(pady=5)

# campo_nome = tk.Entry(app, font=("arial", 12))
# campo_nome.pack(pady =5)

# bnt_enviar = tk.Button(app, text="Enviar",command=saudar_usuario)
# bnt_enviar.pack(pady=15)

# app.mainloop()

import tkinter as tk
from tkinter import messagebox
 
def calcular_media():
        nota1 = float(calculo1.get())
        nota2 = float(calculo2.get())
        nota3 = float(calculo3.get())
 
        media = (nota1 + nota2 + nota3) / 3
 
        if media >= 5:
            situacao = "Aprovado ✓"
        else:
            situacao = "Reprovado ✗"
        messagebox.showinfo("Resultado", f"Média: {media:.2f}\nSituação: {situacao}")
 
#config da janela
calculador_media = tk.Tk()
calculador_media.title = ("Calculadora de Média")
calculador_media.geometry("550x400")
calculador_media.configure(bg="#1b1b1b")

titulo = tk.Label(calculador_media, text="Calculadora de Média", font=("Arial", 14, "bold"), bg="#1b1b1b", fg="white")
titulo.pack(pady=10)

calculo1 = tk.Entry(calculador_media, font=("Arial", 12))
calculo1.pack(pady=5)

formataçao1 = tk.Label(calculador_media, text="Digite a sua primeira média abaixo: ", bg="#1b1b1b", fg="white")
formataçao1.pack(pady=5)


calculo2 = tk.Entry(calculador_media, font=("Arial", 12))
calculo2.pack(pady=5)

formataçao2 = tk.Label(calculador_media, text="Digite a sua segunda média abaixo: ", bg="#1b1b1b", fg="white")
formataçao2.pack(pady=5)

calculo3 = tk.Entry(calculador_media, font=("Arial", 12))
calculo3.pack(pady=5)

formataçao3 = tk.Label(calculador_media, text="Digite a sua terceira média abaixo: ", bg="#1b1b1b", fg="white")
formataçao3.pack(pady=5)


botao = tk.Button(calculador_media, text="Calcular Média", bg="#064a04", fg="white", command=calcular_media)
botao.pack(pady=15)

calculador_media.mainloop()