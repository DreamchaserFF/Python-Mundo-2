num = 0
soma = 0
cont = 0
while num != 999:
    if num != 999:
        num = int(input("Informe um numero: "))
        soma += num
        cont += 1
    else:
        print("Numero 999 digitado.")
soma -= 999
print(f"Foram digitados {cont} numeros. A soma dos números informados é {soma}")