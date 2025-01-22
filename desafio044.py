preco = float(input("Informe o valor do produto: "))
opcao = int(input('''Escolha a forma de pagamento: 
1 para a vista no dinheiro.
2 para a vista no cartão.
3 para 2x no cartão.
4 para 3x ou mais: '''))
if opcao == 1:
    print(f"O valor a ser pago será {preco - ((preco / 100) * 10)}")
elif opcao == 2:
    print(f"O valor a ser pago será {preco - ((preco / 100) * 5)}")
elif opcao == 3:
    print(f"O valor a ser pago será {preco}")
elif opcao == 4:
    print(f"O valor a ser pago será {preco +((preco / 100) * 20)}")
else:
    print(f"Escolha uma opção válida.")