# 7 - Desenvolva um procedimento para pesquisa em tabelas de conteúdo fixo, como as de palavras reservadas e similares.
import json

#função le o arquivo
def le_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            tabela = [linha.strip() for linha in arquivo if linha.strip()]
        return sorted(tabela)  # Ordena a tabela
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return []
#pesquisa
def pesquisar_palavra(tabela, palavra):
    return palavra in tabela

#mostra
def exibir_tabela(tabela):
    print("\nTabela de Palavras Reservadas:")
    for palavra in tabela:
        print(f" - {palavra}")
    print("-" * 40)

#salva em json
def salva_json(tabela, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(tabela, arquivo, indent=4)
    print(f"Tabela salva no arquivo '{nome_arquivo}'.")

def main():
    nome_arquivo = "palavras_reservadas.txt"
    tabela = le_arquivo(nome_arquivo)

    if not tabela:
        return

    exibir_tabela(tabela)

    palavra = input("Digite uma palavra para pesquisar (ou ENTER para sair): ").strip()
    if palavra:
        if pesquisar_palavra(tabela, palavra):
            print(f"'{palavra}' é uma palavra reservada.")
        else:
            print(f"'{palavra}' não é uma palavra reservada.")

    salva_json(tabela, "tabela_palavras_reservadas.json")

if __name__ == "__main__":
    main()
