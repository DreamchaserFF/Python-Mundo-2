decimal = int(input("Informe um numero inteiro: "))
opcao = int(input('''Agora escolha a base de conversão. 
1 para binario.
2 para octal. 
3 para hexadecimal. '''))
if opcao == 1:
    print(f"O numero {decimal} convertido para binario é {bin(decimal)[2:]}")
elif opcao == 2:
    print(f"O numero {decimal} convertido para octal é {oct(decimal)[2:]}")
elif opcao == 3:
    print(f"O numero {decimal} convertido para hexadecimal é {hex(decimal)[2:]}")
else:
    print(f"Escolha uma opção válida.")