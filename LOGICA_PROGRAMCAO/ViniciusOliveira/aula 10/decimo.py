# projeto cancela automatico
# 1 - pressionar botão, imprimiu o ticket
# cauculat tempo de permanemcia
# pagar ticket
# devovolver na saida
# liberar cancela

# 2 - acesso por TAGs (sem parar, Conect car)
# caucular tempo de permanencia
# gerar pagamneto em fatura
# abrir a cancela

# 3 - erros
# duda
# verificar sinal de tranmissão
# virificar acesso por ticket ou tag ao mesmo tempo
# perdeu o ticket (levantar informações)
# problemas com cancela

valor_por_hora = 12
multa_perda_ticket = 20

print("--- Bem-vindo ao Shopping do Neymar ---")
escolha = input("Qual sua escolha: entrada por TAG ou Ticket?\n ").strip().lower()

if escolha == "tag":
    print("Acesso por TAG detectado. Cancela aberta!")
    tempo = float(input("Quantas horas de permanência? \n"))
    total = tempo * valor_por_hora
    print(f"Valor de R$ {total} será gerado em sua fatura.")
    print("Cancela liberada. Volte sempre! =)")

elif escolha == "ticket":
    print("Ticket impresso. Cancela aberta!")
    tempo = float(input("Quantas horas de permanência?\n "))
  
    perdeu = input("Você está com seu ticket? (sim/não):\n ").strip().lower()
    
    if perdeu == "não":
        total = (tempo * valor_por_hora) + multa_perda_ticket
        print(f"Multa por perda de ticket aplicada (+ R$ {multa_perda_ticket})")
    else:
        total = tempo * valor_por_hora
        
    print(f"Total a pagar:R$ {total}")
    pagamento = input("Qual método de pagamento (Débito/Crédito/Dinheiro)? \n")
    
    print(f"Pagamento em {pagamento} realizado com sucesso.")
    print("Devolva o ticket na saída. Cancela liberada!")
    print("Volte sempre no shopping do Neymar")

else:
    print("Erro: Método de entrada não reconhecido ou problema no sinal.")
    print("Por favor, acione o suporte no botão de ajuda.")