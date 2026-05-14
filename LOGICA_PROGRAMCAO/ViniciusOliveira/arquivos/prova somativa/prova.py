# exercico 1
nome = str(input("qual seu nome de operador? \n"))
turno = str(input("de qual turno voce pertence? A B ou C \n"))
print(f"operador {nome} registrado no turno {turno}. Bom trabalho!!")

# exercico 2
peças = int(input("qual a quantidade de peças produzidas em 1 Hora? \n "))
total_produzido = peças * 8
print(f"a quantidade de peças produzidas no turno completo foi {total_produzido}. obrigado pelo trabalho! \n")

# exercico 3
pressão = float(input("qual a medida da pressão em bar: \n"))
PSI = pressão * 14.5
print(f"o valor da pressão em PSI foi de:{PSI}")

# exercico 4
v1 = int(input("qual a qualidade dessa peça? (de 0 a 10) \n"))
v2 = int(input("qual a qualidade dessa peça? (de 0 a 10) \n"))
v3 = int(input("qual a qualidade dessa peça? (de 0 a 10) \n"))
qualidade = v1 + v2 + v3 /3
print(f" a qualidade dessa proução foi de: {qualidade}")

# exercicio 5
temperatura = int(input("Qual temperatura você deseja calcular:\n"))
if temperatura <= 40:
    print ("SUA CARGA ESTÁ BAIXA")
elif 40<= temperatura <= 70:
    print("SUA TEMPERATURA ESTA DENTRO DO IDEAL")
elif temperatura > 70:
    print ("SUA TEMPERATURA ESTÁ ACIMA DO IDEAL")
else:
    print("Desligando o sitema")

# exercicio 6
lotes = str(input("digite qual lotes deseja: \n"))
if lotes == "A":
    print("sua escolha foi o lote de alimetos")
elif lotes == "E":
    print("sua escolha foi o lote de eletronicos")
else:
    print("Desconhecido")

# exercico 7 
sensor = str(input("qual a condição da porta? \n"))
botão = str(input(" qual a condição do botão de emergencia? \n"))
if sensor == "fechada" or botão == "desligado":
    print("tudo dentro dos requisitos")
else:
    print("desligando maquina por segurança")

# exercicio 8
produzidas = int(input("qul a quantidade de peças produzidas? \n"))
defeito = int(input("qual a quantidade de peças defeituosas? \n"))
total_feito = defeito * 0.05
if total_feito < defeito:
    print("revisar processos")
elif total_feito > defeito:
    print("processos otimizados")
else:
    print("fechando local de trabalho")

# exercicio 9 
peça = float(input("qual a medida da sua peça \n"))
if peça <9.8:
    print("abaixo do esperado")
elif peça > 9.8 or peça <10.2:
    print("dentro da tolerancia")
elif peça >10.2:
    print("sua peça esta acima do desejado")
else:
    print("agradeço pela compreenção e solicitação de serviço")

#  exercico 10
for num in range (10,0 ,-1):
    print(num)
print("prensa Ativada")

#  exercico 11
peso = 0 
while True:
    caixa = int(input("digite o peso da caixa: \n"))
    if peso == 0:        
        break
    peso += caixa  
    print(f" o peso acumulado foi {peso}")