# calculo de idade, com nome, curso, data de nascimento e apresentar a idade no final

nome = str(input("me fale seu nome? \n"))
curso = str(input("qual curso voce esta fazendo? \n"))
nascimento = int(input("que ano vc nasceu? \n"))
ano = int(input("em qual anos estamos? \n"))

idade = ano - nascimento 
print(f"vc atualmente tem {idade} anos")

# exercicio 3
# gorgeta do garçon, calcule a gorgeta de 10% do valor da conta

valor = float(input("qual o valor da conta? \n"))
totaldaconta = float(valor / 10) 
print(f"o valor da gorgeta é:" ,totaldaconta)
print(f" o valor da conta com a gorgeta é", valor + totaldaconta )

# exerciocio 4

numero = int(input("coloque seu numero \n"))
print("antessesor é: \n", numero-1)
print("sucessor é: \n" , numero+1)

# exercicio 5
# criar um algoritimo que caucula a venda de um livro e apresente um desconto fixo de 5%

livro = int(input("quantos livros você deseja?\n"))
preço = float(input("qual o valo do seu livro? \n"))
totalvalor = preço - (preço / 5) 
print("o valor do livro com desconto é", totalvalor)









