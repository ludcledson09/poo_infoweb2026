# Conversor de moeda fictícia para Euro
# Autor: Assistente
# Data: 2026-10-06

from decimal import Decimal, InvalidOperation

# Taxa fictícia: 1 boró = 2.5 EUR
TAXA_BORÓ_PARA_EURO = Decimal("2.5")

def converter_para_euro(valor_boró):
    """
    Converte valor de boró para Euro.
    :param valor_boró: Decimal - valor em boró
    :return: Decimal - valor em Euro
    """
    return valor_boró * TAXA_BORÓ_PARA_EURO

def main():
    print("=== Conversor de boró para Euro ===")
    try:
        entrada = input("Digite o valor em boró: ").strip()
        valor_boró = Decimal(entrada)

        if valor_boró < 0:
            print("Valor não pode ser negativo.")
            return

        valor_euro = converter_para_euro(valor_boró)
        print(f"{valor_boró} BRO equivalem a €{valor_euro:.2f}")

    except InvalidOperation:
        print("Entrada inválida. Digite apenas números.")

if __name__ == "__main__":
    main()