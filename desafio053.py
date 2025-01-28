escolha = str(input("Digite uma frase: "))
frase = escolha.replace(" ", "").lower()
palindromo = True
for i in range(len(frase) // 2):
    if frase[i] != frase[len(frase) - 1 - i]:
        palindromo = False
    else:
        palindromo = True
if palindromo == True:
    print("A frase é um palindromo.")
else:
    print("A frase não é um palindromo.")