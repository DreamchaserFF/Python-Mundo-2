continuar = True
soma = cont = 0 #Iguala tudo a zero
while continuar != False:
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input("Deseja continuar? [S/N]").upper().strip()[0]
    if continuar == "N":
        continuar = False
print(f"A média dos números informados foi {soma / cont}")
print(f"O maior número informado foi {maior} e o menor foi {menor}")
print("Fim")
