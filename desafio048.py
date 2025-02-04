soma = 0
for c in range(3, 500, 3):
    if c % 2 != 0 and c % 3 == 0:
        soma += c
print(f"A soma de todos os numeros impares multiplos de 3 é: {soma}")
