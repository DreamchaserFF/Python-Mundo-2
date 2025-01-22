soma = 0
for c in range(1,6+1):
    int(input(f"informe o {c}° número: "))
    if c % 2 == 0:
        soma += c
print(f"A soma de todos os números pares informados é: {soma}")