soma = 0

for c in range(1,7):
    num = int(input(f"informe o {c}° número: "))
    if num % 2 == 0:
        soma += num
print(f"A soma de todos os números pares informados é: {soma}")