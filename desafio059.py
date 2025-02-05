result = False
while result != True:
    num1 = int(input("Informe o primeiro valor: "))
    num2 = int(input("Informe o segundo valor: "))
    opcao = int(input("Escolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do programa\n"))
    if opcao == 1:
        soma = num1 + num2
        print(f"A soma de {num1} e {num2} é: {soma}")
        result = True
    elif opcao == 2:
        mult = num1 * num2
        print(f"{num1} multiplicado por {num2} é: {mult}")
        result = True
    elif opcao == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que {num2}")
            result = True
        elif num1 == num2:
            print("Os números são iguais.")
            result = True
        else:
            print(f"O número {num2} é maior que {num1}")
            result = True
    elif opcao == 4:
        print("Okay!")
    elif opcao == 5:
        print("Bye bye!")
        result = True
    else:
        print(f"Opção inválida. Voltando para o começo.")
print("Fim.")