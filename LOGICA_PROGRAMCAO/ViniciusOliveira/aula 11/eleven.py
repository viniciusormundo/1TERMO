
# def nome ():
#     nome = input("diga seu nome:\n").upper()
#     return nome
# print(f"Olá, {nome()}!")

def valores():
    print("Digite três valores:")
    a = int(input("digite o primeiro valor: \n"))
    b = int(input("digite o segundo valor: \n"))
    c = int(input("digite o segundo valor: \n"))
    return a, b, c
print(f"O maior valor é {max(valores())}")
#reutilizando funçoes
# nome()
# valores()

def calcular_dobro(numero):
    return numero * 2
# como usar:resultado = caucular_dobro
print(calcular_dobro(5))