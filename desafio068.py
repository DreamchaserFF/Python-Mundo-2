from random import randint
print("=-" * 10)
print("Vamos jogar par ou ímpar")
print("=-" * 10)
cont = 0
while True:
    player = int(input("Diga um valor: "))
    escolha = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
    cpu = randint(0,10)
    soma = player + cpu
    if escolha == "P" and soma % 2 == 0:
        print(f"Você jogou {player} e o computador jogou {cpu}. Total de {soma}. Par Vence.")
        print(f"Você venceu!")
        print("=-" * 10)
        cont += 1
    elif escolha == "I" and soma % 2 != 0:
        print(f"Você jogou {player} e o computador jogou {cpu}. Total de {soma}. Ímpar Vence.")
        print(f"Você venceu!")
        print("=-" * 10)
        cont += 1
    elif escolha == "P" and soma % 2 != 0:
        print(f"Você jogou {player} e o computador jogou {cpu}. Total de {soma}. Ímpar Vence.")
        print(f"Você Perdeu!")
        print("=-" * 10)
        print(f"Game Over! Você venceu {cont}")
        break
    elif escolha == "I" and soma % 2 == 0:
        print(f"Você jogou {player} e o computador jogou {cpu}. Total de {soma}. Par Vence.")
        print(f"Você Perdeu!")
        print("=-" * 10)
        print(f"Game Over! Você venceu {cont} vezes")
        break
    else:
        print(f"Opção Inválida")
