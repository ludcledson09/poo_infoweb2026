try:
    a = int(input("Informe o dividendo"))
    b = int(input("Informe o divisor"))
except Exception as erro:
    print(type(erro))
    print(erro)