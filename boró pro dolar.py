# Conversor de moeda fictícia para dólar
# Autor: Exemplo técnico
# Data: 2026-10-06

def ficticia_para_dolar(valor_ficticio: float, taxa_ficticia_usd: float) -> float:
    """
    Converte um valor de moeda fictícia para dólar (USD).
    
    :param valor_ficticio: Valor na moeda fictícia.
    :param taxa_ficticia_usd: Quantos dólares equivalem a 1 unidade da moeda fictícia.
    :return: Valor convertido em dólares.
    """
    # Validação de entrada
    if not isinstance(valor_ficticio, (int, float)) or not isinstance(taxa_ficticia_usd, (int, float)):
        raise TypeError("Os valores devem ser numéricos.")
    if valor_ficticio < 0:
        raise ValueError("O valor da moeda fictícia não pode ser negativo.")
    if taxa_ficticia_usd <= 0:
        raise ValueError("A taxa de conversão deve ser maior que zero.")

    # Conversão
    return round(valor_ficticio * taxa_ficticia_usd, 2)


# Exemplo de uso
if __name__ == "__main__":
    try:
        # Definindo a taxa fictícia: 1 BRO = 0.75 USD
        taxa = 0.75
        
        # Valor na moeda fictícia
        valor_bro = float(input("Digite o valor em moeda fictícia (BRO): "))
        
        # Conversão
        valor_usd = ficticia_para_dolar(valor_bro, taxa)
        print(f"{valor_bro} BRO equivalem a {valor_usd} USD")
    
    except Exception as e:
        print(f"Erro: {e}")

