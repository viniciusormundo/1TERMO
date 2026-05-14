from datetime import datetime

def verificar_epi(setor_escolhido):
    """
    Mapeamento de EPIs por setor utilizando dicionário para melhor performance.
    """
    setores_map = {
        "elétrica": ["Luvas de alta tensão", "Botas dielétricas"],
        "eletrica": ["Luvas de alta tensão", "Botas dielétricas"],
        "trabalho em altura": ["Cinturão de segurança", "Talabarte", "Capacete com jugular"],
        "mecânica": ["Óculos de proteção", "Luvas de vaqueta"],
        "mecanica": ["Óculos de proteção", "Luvas de vaqueta"],
        "ferramentaria": ["Protetor auricular", "Óculos de policarbonato", "Sapato de biqueira"],
        "adm": ["Apoio de pés (Ergonomia)", "Cadeira ajustável NR-17"],
        "operador cnc": ["Óculos de proteção", "Protetor auricular", "Creme protetor para mãos"]
    }
    
    setor_limpo = setor_escolhido.strip().lower()
    
    print("\n" + "-"*50)
    print(f" LISTAGEM DE EPIS - SETOR: {setor_limpo.upper()}")
    print("-"*50)
    
    epis = setores_map.get(setor_limpo)
    
    if epis:
        for item in epis:
            print(f" [ ] {item}")
    else:
        print(" [!] Setor nao localizado no PGR. Verifique a base de dados.")
    print("-"*50)

def verificar_validade_brigada(ano_treinamento):
    """Valida se o treinamento de brigadista esta dentro do prazo de 2 anos."""
    try:
        ano_atual = datetime.now().year
        if not (1990 <= ano_treinamento <= ano_atual):
            return False, "ERRO: Ano digitado fora do intervalo logico."
        
        diferenca = ano_atual - ano_treinamento
        
        if diferenca <= 2:
            return True, "STATUS: Treinamento Valido."
        else:
            return False, "STATUS: Treinamento Vencido (Necessita Reciclagem)."
    except Exception:
        return False, "ERRO: Falha ao processar data."

def sistema_sesmt():
    lista_funcionarios = []
    
    # Cabecalho Principal
    print("="*60)
    print(f"{'SISTEMA DE GESTAO SESMT':^60}")
    print(f"{'Controle de Normas Regulamentadoras':^60}")
    print("="*60)
    
    while True:
        nome_input = input("\nNome do Funcionario (ou 'sair'): ").strip()
        if nome_input.lower() == 'sair': 
            break
        
        nome = nome_input.title()
            
        print("\nSetores: Eletrica, Mecanica, Trabalho em Altura, Ferramentaria, ADM, Operador CNC")
        setor = input("Setor de atuacao: ")
        verificar_epi(setor)
        
        # Validacao de Treinamentos
        print("\n--- CHECKLIST DE TREINAMENTOS ---")
        nr10 = input("Possui NR-10 ativa? (S/N): ").strip().lower() == 's'
        nr35 = input("Possui NR-35 ativa? (S/N): ").strip().lower() == 's'
        
        # Loop para garantir entrada numerica do ano
        while True:
            try:
                ano_brigada = int(input("Ano do ultimo treinamento de Brigada: ex(2023)"))
                break
            except ValueError:
                print(">>> Entrada invalida. Digite apenas o ano com 4 digitos.")

        brigada_ok, msg_brigada = verificar_validade_brigada(ano_brigada)
        print(f"{msg_brigada}")

        lista_funcionarios.append({
            "nome": nome,
            "setor": setor,
            "nr10": nr10,
            "nr35": nr35,
            "brigada": brigada_ok
        })
        
    # --- RELATORIO FINAL DE CONFORMIDADE ---
    total = len(lista_funcionarios)
    if total > 0:
        aprovados = sum(1 for f in lista_funcionarios if f["nr10"] and f["nr35"] and f["brigada"])
        
        print("\n" + "╔" + "═"*58 + "╗")
        print(f"║{'RESUMO GERAL DE CONFORMIDADE':^58}║")
        print("╠" + "═"*58 + "╣")
        print(f"║  Total de Funcionarios Cadastrados: {total:<21}║")
        print(f"║  Funcionarios 100% Aptos:           {aprovados:<21}║")
        print(f"║  Funcionarios com Pendencias:       {total - aprovados:<21}║")
        print("╚" + "═"*58 + "╝")
    else:
        print("\nNenhum dado foi registrado.")

if __name__ == "__main__":
    sistema_sesmt()