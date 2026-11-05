class Mamifero:
    pass
class Gato(Mamifero) :
    pass

x = Gato()
print(type(x))
print(type(x) == Mamifero)
print(type(x) == Gato)
print(isinstance(x, Mamifero))
print(isinstance(x, Gato))