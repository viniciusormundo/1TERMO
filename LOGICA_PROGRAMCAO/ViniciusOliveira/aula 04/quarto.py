# #logica, exemplo 1
# print("expressões lógicas")
# idade = int(input("digite sua idade:"))

# if idade >= 18:
#     print("você é maior, mas já pode votar")
#     print("pode tirar carta de motorista.")
# elif idade >= 16:
#     print("você ainda não é maior, mas ja pode votar.")
# else:
#     print("você é menor de idade")


# # if "se" a condição for verdadeira. 
# # elif "senão, se" (usado para multiplas condiões)
# # else: "senão"(executa se nenhuma das anteriores for verdadeira)


# # exemplo 2

# print("escolha sua modalidade")
# print("Opção 1: TI")
# print("opção 2: Humanas")
# print("opção 3 exatas")
# modalidade = int(input("Digite sua opção de modalidade por números"))
# if modalidade == 1:
#     print("voce escolheu TI")
# elif modalidade == 2:
#     print(" voce escolheu Humanas")
# else: 
#     print("você escolheu Exatas")

# # exemplo 3
# print("Categoria de Série e Filmes")
# print("Escolha uma caegoria")
# print("Série = S")
# print("Filme = F")
# categoria = input("Digite sua categoria ")
# if categoria == "S":
#     print("Sua escolha foi para Séries ")
# elif categoria == "F":
#   print("Sua escolha foi para Filmes ")
# else:
#     print("Você não esolheu nenhuma opção ")

## exemplo 4
# print("Calculadora com condições")
# print("Escolha como quer calcular")
# print("1 = Soma")
# print("2 = Subtração")
# print("3 = Multiplicação")
# print("4 = Divisão")
# calculadora = float(input("Digite sua opção para caucular \n"))
# if calculadora == 1:
#    print("1 = Você escolheu soma") 
#    soma1 = int(input("Digite o primeiro valor \n "))
#    soma2 = int(input("Digite o segundo valor \n "))
#    print(soma1+soma2)
# elif calculadora == 2:
#     print("2 = Você escolheu Subtração")
#     sub1 =int(input(" digite o primeiro valor pra subtrair \n"))
#     sub2 = int(input("digite o segundo valor pra subtrair \n"))
#     print(sub1-sub2)
# elif calculadora == 3:
#    print("3 você escolheu multiplicação")
#    mult1 = int(input(" digite o operador \n"))
#    mult2 = int(input(" digite o multiplicador \n"))
#    print(mult1*mult2)

# elif calculadora == 4:
#    print("4 você escolheu divisão ")
#    div1 = int(input(" digite o operador \n"))
#    div2 = int(input(" digite o divisor \n"))
#    print(div1*div2)

# # exercicio 1
# print("calculo de notas")
# nota1 = int(input("Digite a primeira nota \n"))
# nota2 = int(input("Digite a segunda nota \n "))
# media = (nota1 + nota2) / 2

# if media >= 50:
#    print("aprovado")
# else:
#    print("reprovado")

# # exercicio 2

# cores = int(input("qual cor esta o semafaro \n"))

# if cores == 1:
#  print ("vermelho")

# elif cores == 2:
#  print("amarelo")

# elif cores == 3:
#  print ("verde")

# else:
#  print("somente essas cores")

# # exercicio 3
# produto1 = int(input("qual produto deseja? \n"))
# if produto1 == 1:
#     qtde = int(input("quantos sapatos você deseja?\n"))
#     valor1= float(input("qual o valor do seu sapato? \n"))
#     valorfinal = valor1 - (valor1/ 5) 
#     print("o valor do sapato com desconto é", valorfinal)

# elif produto2 == 2:
#     produto2 = int(input("quantas roupas você deseja?\n"))
#     produto2 = float(input("qual o valor da sua roupa? \n"))
#     valorfinal2 = valor2 - (valor2 / 5) 
#     print("o valor da roupa com desconto é", valorfinal2)

# elif produto3 == 3:
#     valor3 = produto3
#     print("perfumes")
#     print("o valor de desconto é 3%")
#     valor3 = produto3
#     produto3 = int(input("quantas perfume você deseja?\n"))
#     produto3 = float(input("qual o valor da sua perfume? \n"))
#     valorfinal3 = valor3 - (valor3 / 5) 
#     print("o valor do perfume com desconto é", valorfinal3)

# else:
#     print("você não escolheu nenhum produto")
#     print("obrigado por comprar em nossa loja")



# exercico 4
# nota = int(input("qual o valor da sua nota? \n"))
# if nota >=70:
#     print("aprovado")
#     print("seu resultado final foi", nota)
# elif nota >=50:
#     print("recuperação")
#     print("seu resultado final foi", nota)
# elif nota <=50:
#     print("reprovado")
#     print("seu resultado final foi", nota)
# else:
#     print("Obrigado por usar o sistema")