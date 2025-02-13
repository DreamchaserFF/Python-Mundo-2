import random
num = random.randint(0, 10)
tries = 0
chute = 999
while chute != num:
    tries += 1
    chute = int(input("Adivinhe um número de 0 a 10: "))
    if chute != num:
        if chute < num:
            print(f"Mais. Tente novamente")
        else:
            print(f"Menos. Tente novamente")
    else:
        print(f"Você Acertou! Foram precisas {tries} tentativas!")