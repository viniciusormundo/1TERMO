# # clean code - aula 8
# print("Clean code - aula 08")
# aula = 8
# print(f"estamaos na aula {aula} de Clean code")

# # manipulação de arquivo
# texto = " python "
# print(texto.strip().upper())
# print(texto.strip().lower())

# # escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code.")

# #lendo
# with open("notas.txt", "r")as arquivo:
#      conteudo = arquivo.read()
#      print(conteudo)

# # manipulação
# texto = " Python é muito legal! "
# print(texto.strip().upper())
# print(texto.strip().lower())
# print(texto.strip().capitalize())
# print(texto.strip().title())
# print(texto.strip().replace(" ", "_"))
# print(texto.strip().split())

# executar comandos do sistema
import os ##importa o modulo os para interagir com o sistema operacional

# onde estou
# print(os.getcwd()) 

# # lista arquivos na pasta
# print(os.listdir(".."))
# print(os.listdir("..\\.."))
# print(os.listdir("C:\\"))
# print(os.listdir("C:\\Users"))
# print(os.listdir("C:\\Users\\Public"))

# outros comando uteis
# # criar pasta
# os.mkdir("nova_pasta")
# # renomear pasta
# os.rename("nova_pasta","pasta_renomeada")
# #excluir pasta
# os.rmdir("pasta_renomeada")

# exercicio 1
# Crie um script que mostre o caminho da pasta atual

# # Obtém o diretório atual
# print(os.getcwd())

# # exercicio 2
# #liste os arquivos da pasta atual
# print(os.listdir)

# # exercicio 3

# os.mkdir("projetos")

# os.rename("projetos","meus_projetos")

# os.rmdir("meus_projetos")

# # exercicio 4
# #Crie um arquivo chamado log.txt e ecreva a mensafem log de atividades. depois leia o conteudo do arquivo e exiba na tela.

# with open("log.txt", "w")as arquivo:
#     arquivo.write("log de ativivade")
# with open("log.txt", "r")as arquivos:
#     conteudo = arquivo.read()
#     print(conteudo)

# exemplo 5- exemplo 1
# crie um dicionario com informações sobre uma pessoa e aceese o valor usando uma chave
pessoa = {
    "nome":"Vinicius",
    "idade": 17,
    "cidade": "São Paulo",
}
pessoa2 = {
    "nome": "ana",
    "idade": 42,
    "cidade": "Limeira"
}
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])
print(pessoa2["nome"])
print(pessoa2["idade"])
print(pessoa2["cidade"])

# exercicio 6
with open("desliga.bat", 'w')as desligar:
    desligar.write("shutdows -s -t 3660 -c \desligamento")
    # -s comando para desligar
    # -t tempo definir
    # -a cancelar deligamento
with open("desliga.bat", 'r')as desligar:
    conteudo = desligar.read()
    print(conteudo)

# exercicio 7 criar um aquivo de backup do arquivo "notas.txt" com o nome "notas_backup.txt". O script deve ler o conteudo de "notas.txt" e escrever de novo arquivo

with open("notas.txt", "r") as original:
    conteudo = original.read()
with open("notas_backup.txt", "w") as backup:
    backup.write(conteudo)
print("Backup criado com sucesso!")

# exemplo 8 - exemplo 2
pasta = os.listdir()
for arquivo in pasta:
    if arquivo.endswith(".txt"):
        os.remove(arquivo)
        print(f"Arquivo {arquivo} excluido.")
print("Limpeza de arquivos concluida.")

# execicio 9
    # Ler a temperatura do arquivo
with open("temperatura.txt", "w") as arquivo:
        temperatura = (arquivo.read)

if temperatura > 70:
        print(f"ALERTA! Temperatura alta: {temperatura}°C")
else:
        print(f"Temperatura normal: {temperatura}°C")