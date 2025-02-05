import random
num = random.randint(0, 10)
tries = 0
chute = 999
while chute != num:
    chute = int(input("Escolha um número de 0 a 10: "))
    if chute != num:
        print("Você errou. Tente de novo!")
        tries += 1
    else:
        print(f"Você Acertou! Mas foram precisas {tries} tentativas!")