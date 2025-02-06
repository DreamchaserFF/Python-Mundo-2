soma = 0
continuar = True
cont = 0
num = int(input("Informe um número: "))
menor = num
maior = num
while continuar != False:
    num = int(input("Informe outro número: "))
    soma += num
    cont += 1
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
    escolha = str(input("Deseja continuar? [S/N]")).upper().strip()
    if escolha == "S":
        print("Ok")
    elif escolha == "N":
        media = soma / cont
        print(f"A média dos números informados é: {media}")
        print(f"Foram informados {cont} números.")
        print(f"O maior número informado foi {maior} e o menor foi {menor}")
        continuar = False
    else:
        print("Opção inválida.")