def saudacao(nome):
    return f"Olá, {nome}!"
mensagem = saudacao ("Vinicius")
print(mensagem)

nome = input("seu nome:")
idade = int(input("sua idade"))
print(f" seu{nome} tem {idade} anos.")

# os dois resultados são praticamente o mesmo, porem o DEF ele usa o RETURN
# para completar sua estrutura
# Ja o print usa o F como formar pra chamar e reconhecer a variavel

