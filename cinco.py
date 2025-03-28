# 5 - Conversão Numérica - Desenvolva no programa uma conversão numérica de entrada e saída de dados que efetuem a leitura de dados escritos em diversas bases numéricas e armazenem na memória os valores convertidos, denotados em uma notação padrão (decimal). Faça o mesmo para a saída de dados, escolhendo a base e o formato de saída (númerop de dígitos a imprimir, posição do sinal, etc.)

#função que le os numeros
def ler_numeros_de_arquivo(nome_arquivo):
    numeros = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                partes = linha.strip().split()
                if len(partes) == 2:
                    numero, base = partes
                    try:
                        base = int(base)
                        numeros.append({"numero": numero, "base": base})
                    except ValueError:
                        print(f"Erro: Base inválida na linha '{linha.strip()}'")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    return numeros

#função que converte pra decimal
def converter_para_decimal(numero, base):
    try:
        return int(numero, base)
    except ValueError:
        print(f"Erro: '{numero}' não é um número válido na base {base}.")
        return None
        
#função que formata
def formatar_saida(numero, base_destino, num_digitos=0, incluir_sinal=False):
    if base_destino == 2:
        resultado = bin(numero)[2:]
    elif base_destino == 8:
        resultado = oct(numero)[2:]
    elif base_destino == 16:
        resultado = hex(numero)[2:].upper()
    else:
        resultado = str(numero)

    # Ajusta o número de dígitos
    if num_digitos > 0:
        resultado = resultado.zfill(num_digitos)

    # Adiciona o sinal
    if incluir_sinal and numero <= 0:
        resultado = "-" + resultado

    return resultado
    
#main
def main():
    nome_arquivo = "numeros.txt"
    numeros = ler_numeros_de_arquivo(nome_arquivo)

    print("Conversões para decimal:")

    # armazenar os valores convertidos
    memoria = []

    for item in numeros:
        numero, base = item["numero"], item["base"]
        decimal = converter_para_decimal(numero, base)
        if decimal is not None:
            item["decimal"] = decimal  # Adiciona a conversão ao dicionário
            memoria.append(item)  # Salva na memória
            print(f"{numero} (base {base}) -> {decimal} (decimal)")

    #saída formatada
    print("\nSaídas formatadas:")
    for item in memoria:
        valor = item["decimal"]
        print(f"Decimal: {formatar_saida(valor, 10)}")
        print(f"Binário: {formatar_saida(valor, 2, num_digitos=8, incluir_sinal=True)}")
        print(f"Octal: {formatar_saida(valor, 8, num_digitos=5)}")
        print(f"Hexadecimal: {formatar_saida(valor, 16, num_digitos=4)}")
        print("-" * 30)

    # valores na memoria
    print("\nValores armazenados na memória:")
    print(memoria)

if __name__ == "__main__":
    main()
