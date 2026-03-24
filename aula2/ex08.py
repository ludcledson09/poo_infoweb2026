s=input("digite uma frase")
for k in range(len(s)):
    s = s[1:] + s[0]
    print(s)