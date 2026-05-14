# o laço 'for'(repetiçoes determinadas)
# use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer(como ler 10 sensores ou processar uma lisa de peças).
# exemeplo: relatorio de produção diaria
# imagine que você tem uma meta de produzir 5 lotes e quer numerar cade um:
# # exemplo:
# for lote in range(1, 6):
#     print (f"processando lote numero {lote}...")
#     print ("quantidade verificada. [ok]")
#     print ("produção do dia finalizada")

#     # exemplo 2
#     for carros in range(10):
#         print(f"quantidade de carros {carros}")
#         print("quantidade de carros. [verificando]")

# exercicio 1
# peças = ["engrenagem", "eixo","rolamento", "parafuso"]
# maquinas = ["dobradeira", "soldagem","emplhadeira"]
# for item in peças:
#     print(f"item em estoque: {item}")
#     for maq in maquinas:
#         print(f"maquina que temos {maq}")

# exemplo 4
# for peças in range(1, 10):
#     print(f"peça nº",peças ,"processada com sucesso")
#     print(f"ciclo de produção concluido")

# exeecicio 2
# for bananas in range(11):
#     print(f"quantidade de bananas {bananas}")
# for manga in range(6):
#     print(f"quantidade de manga {manga}")
# for melancia in range(11):
#     print(f"quantidade de melancia {melancia}")
# for abacaxi in range(14):
#     print(f"quantidade de abacaxi {abacaxi}")
# resultado = bananas + manga + melancia + abacaxi
# print(f"o resulatado das frutas é", resultado)

# exercicio 3
# numero = int(input("coloque o valor do numero que deseja operar \n"))
# for valor in range(1,11):
#     print(f"{valor} x {numero}")
#     print(valor*numero)

# exemplos
# temperatura = 11
# while temperatura <30:
#     print(f"temperatura atual{temperatura}ºC sistema operando...")
#     temperatura += 3
# print("ALERTA! temperatura atingiu o limite. Desligamento total")

# opcao = ""
# while opcao != "sair":
#     opcao = input("digite a leitura do sesnsor ou 'sair' para fechar: ").lower()
#     if opcao != "sair":
#         print(f"dado '{opcao}' registro de banco de dados")
# print("sistema finalizado")

filme = ""
while filme != "creed" and "creed ||" and "creed |||":
    filme = input("digite qual filme prefere ").lower()
    if filme != "creed" and "creed ||" and "creed |||":
        print(f"seu filme ", filme)
print("sistema de filme finalizado")
