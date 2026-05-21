
from datetime import datetime
 
epis_por_setor = {
    "eletrica":            ["Luvas de alta tensão", "Botas dielétricas"],
    "trabalho em altura":  ["Cinturão de segurança", "Talabarte", "Capacete com jugular"],
    "mecanica":            ["Óculos de proteção", "Luvas de vaqueta"],
    "ferramentaria":       ["Protetor auricular", "Óculos de policarbonato", "Sapato de biqueira"],
    "adm":                 ["Apoio de pés (ergonomia)", "Cadeira ajustável NR-17"],
    "operador cnc":        ["Óculos de proteção", "Protetor auricular", "Creme protetor para mãos"]
}
 
def mostrar_epis(setor):
    epis = epis_por_setor.get(setor)
    if epis:
        print("\nEPIs necessários:")
        for epi in epis:
            print(f"  [ ] {epi}")
    else:
        print("\nSetor não encontrado. Verifique o nome digitado.")
 
def brigada_valida(ano):
    ano_atual = datetime.now().year
    if ano < 1990 or ano > ano_atual:
        return False, "Ano inválido."
    if ano_atual - ano <= 2:
        return True, "Treinamento válido."
    return False, "Treinamento vencido — necessita reciclagem."
 
def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Digite apenas s ou n.")
 
def perguntar_ano(pergunta):
    while True:
        try:
            ano = int(input(pergunta))
            return ano
        except ValueError:
            print("Digite apenas o ano com 4 dígitos. Ex: 2023")
 
def main():
    lista_funcionarios = []
 
    print("=" * 50)
    print("       SISTEMA DE GESTÃO SESMT")
    print("=" * 50)
 
    while True:
        print("\nSetores disponíveis: eletrica, mecanica, trabalho em altura, ferramentaria, adm, operador cnc")
 
        nome = input("\nNome do funcionário (ou 'sair' para encerrar): ").strip()
        if nome.lower() == "sair":
            break
 
        setor = input("Setor: ").strip().lower()
        mostrar_epis(setor)
 
        print("\n--- Treinamentos ---")
        tem_nr10 = perguntar_sim_nao("Possui NR-10 ativa?")
        tem_nr35 = perguntar_sim_nao("Possui NR-35 ativa?")
 
        ano_brigada = perguntar_ano("Ano do último treinamento de brigada (ex: 2023): ")
        brigada_ok, mensagem = brigada_valida(ano_brigada)
        print(mensagem)
 
        lista_funcionarios.append({
            "nome":    nome.title(),
            "setor":   setor,
            "nr10":    tem_nr10,
            "nr35":    tem_nr35,
            "brigada": brigada_ok
        })
 
        print(f"\n✓ {nome.title()} cadastrado com sucesso!")
 
    # Relatório final
    total = len(lista_funcionarios)
    if total == 0:
        print("\nNenhum funcionário cadastrado.")
        return
 
    aptos = sum(1 for f in lista_funcionarios if f["nr10"] and f["nr35"] and f["brigada"])
 
    print("\n" + "=" * 50)
    print("         RELATÓRIO FINAL")
    print("=" * 50)
    print(f"  Total cadastrados:    {total}")
    print(f"  Funcionários aptos:   {aptos}")
    print(f"  Com pendências:       {total - aptos}")
    print("=" * 50)
 
    for funcionario in lista_funcionarios:
        status_nr10    = "✓" if funcionario["nr10"]    else "✗"
        status_nr35    = "✓" if funcionario["nr35"]    else "✗"
        status_brigada = "✓" if funcionario["brigada"] else "✗"
        print(f"\n  {funcionario['nome']} ({funcionario['setor']})")
        print(f"    NR-10: {status_nr10}  |  NR-35: {status_nr35}  |  Brigada: {status_brigada}")
 
if __name__ == "__main__":
    main()