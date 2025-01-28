maior = 0
menor = 0
for i in range(1 , 5+1):
    peso = float(input(f"Informe o peso da {i}° pessoa em kg: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor  = peso
print(f"O maior peso foi: {maior}")
print(f"O menor peso foi {menor}")
