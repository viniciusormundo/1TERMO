# # exercicio 1
# print("Registro de Operador")
# operador = input("Digite seu nome")
# turno = input("Digite seu turno")
# print(f"operador {operador} restrado no turno {turno}. Boa jornada")

# # exercicio 2
# print("Cauculo de produção")
# produção_hora = int(input("Digite a quantidade de peças produzidas em 1 hora"))
# produção_turno = produção_hora * 8
# print (f"quantidade de peças produzidas no turno de 8 horas: {produção_turno}")

# # exercicio 3
# print("conversor de Unidade")
# pressao_bar = float(input("Digite a pressão em Bar"))
# pressao_psi = pressao_bar * 14.5
# print(f"Pressão em PSI: {pressao_psi:.2f}")
# print(f"Pressão em PSI {pressao_psi}", round(pressao_psi, 2))

# # exercicio 4
# print("Inspeçaõ de Peças")
# nota1 = float(input("Digite a nta de inspeção 1 (0 a 10)"))
# nota2 = float(input("Digite a noa de inpeção 2 (0 a 10)"))
# nota3 = float(input("Digite a nota da inpeção 3 (0 a 10)"))
# media = (nota1 + nota2 + nota3) /3
# print(f"Media de qualidade da peça: {media:2f}")
# print(f"Media de qualidade da peça:",round(media,2))

# # exercico 5
# print("termostato inteligente")
# temperatura = int(input("digite a temperatura do motor em °C:\n"))
# if temperatura < 40:
#     print ("baixa carga")
# elif 40 <= temperatura <= 70:
#     print("ALERTA: Resfriamento ativo")
# else:
#     print("Normal")

# print("termostato inteligente 2")
# temperatura = int(input("digite a temperatura do motor em °C:\n"))
# if temperatura < 40:
#     print ("baixa carga")
# elif  temperatura > 70:
#     print("ALERTA: Resfriamento ativo")
# else:
#     print("Normal")

# # exercicio 6
# lotes = input("digite qual lotes deseja: \n")
# if lotes == "A":
#     print("alimentos")
# elif lotes("E"):
#     print("eletronicos")
# else:
#     print("Desconhecido")

# lotes = input("digite qual lotes deseja: \n")
# if lotes.startswith ("A"):
#     print("alimentos")
# elif lotes.startswith("E"):
#     print("eletronicos")
# else:
#     print("Desconhecido")


# # exercicio 7
# print("segurança de operação")
# sensor_porta = input("Digite o status do sensor da porta")
# botao_emergencia = input("Digite o status do botão de emergencia (ligando/desligado")
# if sensor_porta == "fechada" and botao_emergencia == "desligado":
#     print("a maquina pode iniciar")
# else:
#     print("a maquina não pode iniciar")

# # exercicio 8
# print("Cauculo de descarte")
# total_peças = int(input("digite o total de peças prduzidas \n"))
# total_defeitos = int(input("digite o total de peças defeituosas \n"))
# descarte = (total_defeitos / total_peças) * 100
# if descarte > 5:
#     print("revisar processo")
# else:
#     print("processo otimizado")
# print(f"descarte percentual: {descarte:.2f}%")

# # exercico 9
# print("validação de medida")
# medida = float(input("digite a medidade da peça em mm"))
# if medida < 9.8:
#     print("A peça está abaixo da tolerancia")
# elif medida > 10.2:
#     print("A peça esta acima da tolerancia")
# else:
#     print("a peça está dentro da tolerancia")

# # exercicio 10
# print("Contagem regressiva de setup")
# for contagem in range (10, 0, -1):
#     print(contagem)
# print("Prensa Ativada!")

# # exercicio 11
# peso = 0 
# while True:
#     caixa = int(input("digite o peso da caixa: \n"))
#     if peso == 0:        
#         break
#     peso += caixa  
#     print(f" o peso acumulado foi {peso}")

# # exercicio 12
# print("multiplas leituras")
# temperaturas = []
# for i in range(1,6):
#     temp = float(input(f"digite a temperatura do sensor em °C"))
#     temperaturas.append(temp)

# print(f"maior temperatura lida: {max(temperaturas):.2f} °C")
# print(f"menor temperatura lida: {min(temperaturas):.2f} °C")
# print(f"soma temperatura lida: {sum(temperaturas):.2f} °C")

# # exercicio 13
# print("Painel de login")
# senha_correta = "admin123"
# tentativas = 3
# while tentativas >0:
#     senha = input("Digite a senha do supervisor")
#     if senha == senha_correta:
#         print("Acesso permitido")
#         break
#     else:
#         tentativas -= 1
#         print(f"Acesso Negado. tentativas restantes:{tentativas}")

# if tentativas == 0:
#     print("painel fechado")

 # exercicio 14
# print("Simulador de estoque")
# estoque = 100
# while True:
#     print("\nmenu")
#     print("1. adicionar itens")
#     print("2. remover itens")
#     print("3. sair")
#     escolha = input("escolha uma opçao (1, 2 , 3) \n")

#     if escolha == 1:
#         quantidade = int(input("digite a quantidade de itens a adicioanar"))
#         estoque += quantidade
#         print(f"estoque atualizado {estoque} itens")
#     elif escolha == "2":
#          quantidade= int(input("digite a quantidade de itens a remover \n"))
#          estoque -= quantidade
#          print(f"estoque atualizado {estoque} itens")
#          if estoque < 10:
#              print("estoque critico")
#     elif escolha == "3":
#         print("saindo do simulador de estoque")
#         break
#     else:
#         print("Opção invalida. tente novamente.")

# # exercicio 15

# print("relatorio de turno")
# total_peça = 5
# peças_aprovadas = 0
# for i in range(1, total_peça + 1):
#     diametro = float(input(f"digite o diametro da peça {i} em mm \n"))
#     if 19.9 <= diametro <= 20.1:
#         peças_aprovadas += 1
# eficiencia = (peças_aprovadas / total_peça) * 100
# print(f"total de peças aprovadas: {peças_aprovadas}")
# print(f"eficiencia do lote: {eficiencia:.2f}%")