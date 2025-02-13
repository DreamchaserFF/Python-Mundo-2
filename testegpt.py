frase = str(input("Informe uma frase: "))
reverso = frase.lower().replace(' ', '')  # Remove espaços e converte para minúsculas
eh_palindromo = True  # Suponha que é um palíndromo até provar o contrário

# Verifica se a string é igual ao seu reverso
for i in range(len(reverso) // 2):  # Percorre apenas metade da string
    if reverso[i] != reverso[-(i + 1)]:  # Compara início com final
        eh_palindromo = False
        break

if eh_palindromo:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
