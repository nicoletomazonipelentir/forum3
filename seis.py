# 6 - Desenvolva um programa que monte uma tabela de símbolos, em que cada símbolo possa se apresentar com um comprimento arbitrário. Construa procedimentos para ordená-los alfabeticamente, para pesquisar um símbolo específico na tabela, para incluir um elemento adicional, associar atributos a um determinado símbolo, etc.

import json

#função que le os simbolos
def le_simbolos(arquivo):
    """Lê símbolos de um arquivo e armazena em uma lista de dicionários."""
    tabela = []
    try:
        with open(arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(',')
                if len(partes) == 3:
                    simbolo, tipo, escopo = partes
                    tabela.append({"simbolo": simbolo.strip(), "tipo": tipo.strip(), "escopo": escopo.strip()})
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
    return tabela

#função que ordena a tabela
def ordenar_tabela(tabela):
    """Ordena a tabela alfabeticamente pelo nome do símbolo."""
    return sorted(tabela, key=lambda x: x["simbolo"])

#função que pesquisa
def pesquisar_simbolo(tabela, nome):
    """Pesquisa um símbolo na tabela e retorna seus atributos."""
    for simbolo in tabela:
        if simbolo["simbolo"].lower() == nome.lower():
            return simbolo
    return None

#função de adicioonar simbolo a tabela
def adicionar_simbolo(tabela):
    """Permite que o usuário adicione um novo símbolo à tabela."""
    while True:
        nome = input("\nDigite o nome do novo símbolo (ou ENTER para sair): ").strip()
        if nome == "":
            break 

        if pesquisar_simbolo(tabela, nome):
            print(f"Erro: Símbolo '{nome}' já existe na tabela.")
            continue

        tipo = input("Digite o tipo do símbolo (ex: variável, constante, função): ").strip()
        escopo = input("Digite o escopo do símbolo (ex: global, local): ").strip()

        tabela.append({"simbolo": nome, "tipo": tipo, "escopo": escopo})
        print(f"Símbolo '{nome}' adicionado com sucesso!")
        
#função que printa a tabela
def exibir_tabela(tabela):
    tabela=ordenar_tabela(tabela)
    """Exibe a tabela de símbolos formatada."""
    print("\nTabela de Símbolos:")
    print("-" * 40)
    print(f"{'Símbolo':<15} {'Tipo':<15} {'Escopo':<10}")
    print("-" * 40)
    for simbolo in tabela:
        print(f"{simbolo['simbolo']:<15} {simbolo['tipo']:<15} {simbolo['escopo']:<10}")
    print("-" * 40)

#função que salva no json
def salvar_tabela_em_arquivo(tabela, arquivo):
    """Salva a tabela de símbolos em um arquivo JSON."""
    with open(arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(tabela, arquivo, indent=4)
    print(f"Tabela salva!")

#main
def main():
    arquivo = "simbolos.txt"
    tabela = le_simbolos(arquivo)

    print("Tabela original:")
    exibir_tabela(tabela)

    tabela = ordenar_tabela(tabela)
    print("\nTabela ordenada:")
    exibir_tabela(tabela)

    nome_busca = input("Digite um símbolo para pesquisar (ou ENTER para pular): ").strip()
    if nome_busca:
        resultado = pesquisar_simbolo(tabela, nome_busca)
        if resultado:
            print(f"Encontrado: {resultado}")
        else:
            print("Símbolo não encontrado.")

    # permite ao usuário adicionar novos símbolos
    adicionar_simbolo(tabela)

    # mostra tabela atualizada
    exibir_tabela(tabela)

    # salvar tabela em arquivo JSON
    salvar_tabela_em_arquivo(tabela, "tabela_simbolos.json")

if __name__ == "__main__":
    main()
