# # exemplo1
# for i in range(1, 11):
#     print(f"\nTabuada do {i}:")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# # exemplo 2, lista de temperatura
# leituras = [70, 75, 82, 92, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRITICO: {temp}ºC deectado adicionar parada de emergencia.")
#         break #o loop para aqui e não lê os proximos valores (85 e 80)
#     print(f"temperatura esta em {temp} ]ºC. operação normal")

# print(f"sistema deligando. aguarde a manutenção")

# # exemplo 3
# materias = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peças in materias:
#     if peças != "metal":
#         print(f"aviso: peça de {peças} detectada. desviando para descarte...")
#         continue # pula o resto do codigo abaixo e vai para a proxima peça
# #este código só roda se a peça for de matal 
# print(f"processo peças de {peças}. Furando e polindo...")
# # este código só rod se a peça for de metal
# print("fim do lote de produção")

# exercico 1

# for numb in range(1,11):
#     if numb == 5:
#         print(f"Falha ao ler o nº {numb} da lista. por motivos de contagem")
#         continue
#     print(numb)      
# print(f"fim da contagem")

# exemplo 4
# from time import sleep
# for i in range(1,11):
#     if i == 5:
#         print(f"falha ao ler o numero {i}")
#         sleep(1.8)
#         continue 
#     print(i)
#     sleep(0.7)
# print("acabou")

# # exercico 2
# cores = str(input("escolha a cor atual do semafaro:\n"))

# from time import sleep

# if  cores == "vermelho":
#         for cores in range(0):
#             print(f"vermelho")
#         sleep(9.0)
    
# elif cores == "amarelo":
#         for cores in range(0):
#             print("amarelo")
#         sleep(8.0)

# elif cores == "verde":
#         for cores in range(0):
#            print ("verde")
#         sleep (10.0)
# else:
#  print("obriado pro esperar")

#  exercico 3
# maquinas = 0
# for i in range(1,6):
#     valor = float(input(f"digte o valor de cada {i} maquina voce deseja saber:\n"))  
#     maquinas += valor
#     print(f"esses foram os resultados das maquinas em kwh {maquinas}")

# exercicio 4
# print("identificando peças defeituosas")
# leitor = [50.1, 49.5, 52.0, 50.0, 48.5, 67.9, 82.0, 33.7, 19.8, 77.9, 100.0]

# for temperatura in leitor:
#     if temperatura > 50.0:
#         print(f"{temperatura} sua temperatura esta OK")

#     elif temperatura < 50.0:
#         print(f"{temperatura} temperatura esta baixa")
        
#     else:
#         ("fim da contagem")

# peso = float(input("qual o peso desse saco?\n"))
# for i in range(1,7):
#       if peso > 50.0: 
#         print(f"{peso} esta acima do recomendado")
#       elif peso < 50.0:
#           print(f"{peso} esta abixo do recoemdado")
#       elif peso == 50.0:
#           print("o peso está dentro do remoendado")
# else:
#     print("o agradeço por usar o sistema")

# exercico 5

