# Conversor de moeda fictícia para Libra Esterlina (GBP)

def converter_para_gbp(valor_ficticio, taxa):
    """
    Converte valor de moeda fictícia para GBP.
    :param valor_ficticio: valor na moeda fictícia (float)
    :param taxa: taxa de conversão fictícia (float)
    :return: valor convertido em GBP
    """
    if taxa <= 0:
        raise ValueError("A taxa de conversão deve ser maior que zero.")
    return valor_ficticio * taxa


def main():
    try:
        # Entrada do valor na moeda fictícia
        valor_bro = input("Digite o valor na moeda fictícia: ").strip()
        valor_ficticio = float(valor_bro)

        # Entrada da taxa fictícia (ex: 0.75 significa 1 moeda fictícia = 0.75 GBP)
        taxa_bro = input("Digite a taxa fictícia para GBP: ").strip()
        taxa = float(taxa_bro)

        # Conversão
        valor_gbp = converter_para_gbp(valor_ficticio, taxa)

        # Saída formatada
        print(f"{valor_ficticio:.2f} moedas fictícias equivalem a £{valor_gbp:.2f} GBP.")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()