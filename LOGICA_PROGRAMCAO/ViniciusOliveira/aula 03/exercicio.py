# calculando as notas do semestre
# duas notas somativas para encerrar o semestre

# exemplo 1
print("Notas do 1º Semestre")
nota1 = int(input("qual sua primeira nota? \n"))
nota2 = int(input("qual sua segunda nota? \n"))
nota3 = int(input("qual sua terceira nota? \n"))
notafinal = (nota1 + nota2 + nota3) / 3
print(" sua nota do primeiro semestre é \n" , notafinal) 

round(notafinal,2)
# exemplo 2 
print("notas do 2º")
nota11 = int(input("qual sua primeira nota? \n"))
nota12= int(input("qual sua segunda nota? \n"))
nota13 = int(input("qual sua terceira nota? \n"))
notafinal2 = (nota1 + nota2 + nota3) / 3
print(" sua nota do segundo semestre é \n" , notafinal2)
round(notafinal2,2)

# exemplo 3
def boas_vindas(nome, cargo):
    print(f"Olá, {nome}! Você é o novo {cargo}.")
boas_vindas("Vinicius","Desenvolvedora")
boas_vindas("bruno", "Gerente")

# exemplos 4
def configurar_conexao(servidor,porta=8080):
    print(f"Conectando a {servidor} na porta {porta}...")
configurar_conexao("192.168.1.1")              #usar a porta 8080
configurar_conexao("10.0.0.1" , 3000)          #usar a porta 3000 