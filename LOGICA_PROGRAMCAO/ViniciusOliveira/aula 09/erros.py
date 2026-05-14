# erros comum
# ZeroDivisionError: divisao por 0
# ValueError: conversao de tipo invalida
# IndexError: acesso a indice fora do limite
# KeyError: acesso a chave inexistente em dicionario

# exemplo de tratamentos de erros
# print("Exemplo de tratamentos de erros")
# try:
#     num1 = int(input("Digite o primeiro numero"))
#     num2 = int(input("Digite o segundo Numero"))
#     resultado = num1 / num2
#     print(f"O resultado da divisão é: {resultado:.2f}")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero")

# except ValueError:
#     print("Erro: entrada invalida. Por favor, digite um numero inteiro.")

# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}") 

# except NameError:
#     print("Erro: variavel não definida")

# if num1 > 100:
#     print("O numero digitado é maior que 100")
#     for i in range(1,6):
#         print(F"{num1} x {i} = {num1 * i}")
#         if num1 * i > 1000:
#             print("O resultado da multiplicação é maior que 1000")
#             try:
#                 pass
#             except Exception as e:
#                 print(f"Ocorreu um erro inesperado; {e}")
# else:
#     print("O numero digitado é menor ou igual a 100")

# # exercicio 1

# print("Calculadora de média")
# numero = int(input("Quantos numeros você deseja? "))
# soma = 0
# try:
#     for i in range(numero):
#         i = int(input(f"Digite o {i}° número: "))
#         soma += i
#     print(f"A média calculada é: {soma/numero:.1f}")

# except ValueError:
#     print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# # exercico 2
# print("Solicitação ao usuario")
# lista = int(input("quantas palavaras você deseja listar"))
# print(lista.split())
# try:
#     for a in range(lista):
#         i = input("quais palavras voce deseja listas")
#         final += i 
#         print(f"as palavras listadas são {final}")
# except ValueError:
#     print("Esse sistema só aceita textos.")

# exercico 3
print("tratamento de erros")
try:
    variavel = int(input("Digite um numero \n"))
    print(f"o resultado desse teste {variavel}")
except ValueError:
    print("Erro: entrada invalida. Por favor, digite um valor numerico.")
    
except ZeroDivisionError:
    print("Erro: Não é possivel reconhecer zero")

