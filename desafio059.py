result = False    
num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
while result != True:
    opcao = int(input("Escolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do programa\n"))
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é: {soma}")
    elif opcao == 2:
        mult = num1 * num2
        print(f"{num1} multiplicado por {num2} é: {mult}")
    elif opcao == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que {num2}")
        elif num1 == num2:
            print("Os números são iguais.")
        else:
            print(f"O número {num2} é maior que {num1}")
    elif opcao == 4:
        num1 = int(input("Informe o primeiro valor: "))
        num2 = int(input("Informe o segundo valor: "))
    elif opcao == 5:
        print("Bye bye!")
        result = True
    else:
        print(f"Opção inválida. Voltando para o começo.")
    print("=-=" * 10)
print("Fim.")