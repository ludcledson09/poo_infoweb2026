# Conversor de moeda fictícia para Real (BRL)

def ficticia_para_real(valor_ficticio: float, taxa_cambio: float) -> float:
    """
    Converte um valor da moeda fictícia para Real (BRL).
    
    :param valor_ficticio: Quantia na moeda fictícia.
    :param taxa_cambio: Quantos reais valem 1 unidade da moeda fictícia.
    :return: Valor convertido em reais.
    """
    if valor_ficticio < 0:
        raise ValueError("O valor da moeda fictícia não pode ser negativo.")
    if taxa_cambio <= 0:
        raise ValueError("A taxa de câmbio deve ser maior que zero.")
    
    return round(valor_ficticio * taxa_cambio, 2)


def real_para_ficticia(valor_real: float, taxa_cambio: float) -> float:
    """
    Converte um valor em Real (BRL) para a moeda fictícia.
    
    :param valor_real: Quantia em reais.
    :param taxa_cambio: Quantos reais valem 1 unidade da moeda fictícia.
    :return: Valor convertido na moeda fictícia.
    """
    if valor_real < 0:
        raise ValueError("O valor em reais não pode ser negativo.")
    if taxa_cambio <= 0:
        raise ValueError("A taxa de câmbio deve ser maior que zero.")
    
    return round(valor_real / taxa_cambio, 2)


# Exemplo de uso
if __name__ == "__main__":
    # Definindo a taxa fictícia: 1 BRO = 3.75 BRL
    TAXA_CAMBIO = 3.75

    try:
        valor_bro = 100  # 100 unidades fictícias
        valor_em_reais = ficticia_para_real(valor_bro, TAXA_CAMBIO)
        print(f"{valor_bro} BRO = R$ {valor_em_reais}")

        valor_brl = 50  # 50 reais
        valor_em_bro = real_para_ficticia(valor_brl, TAXA_CAMBIO)
        print(f"R$ {valor_brl} = {valor_em_bro} BRO")

    except ValueError as e:
        print(f"Erro: {e}")