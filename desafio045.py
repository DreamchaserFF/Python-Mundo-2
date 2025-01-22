import random
from time import sleep
cpu = random.randint(1,3)
if cpu == 1:
    cpuPlay = "Pedra"
elif cpu == 2:
    cpuPlay = "Papel"
else:
    cpuPlay = "Tesoura"
player = int(input('''Escolha: 
1 para Pedra.
2 Para Papel
3 para Tesoura
'''))
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po!")
if player == 1:
    playerPlay = "Pedra"
elif player == 2:
    playerPlay = "Papel"
elif player == 3:
    playerPlay = "Tesoura"
else:
    print(f"Opção inválida.")
    exit()

if player == 1 and cpu == 2:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você perdeu.")
elif player == 2 and cpu == 3:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você perdeu.")
elif player == 3 and cpu == 1:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você perdeu.")
elif player == 1 and cpu == 3:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você venceu!")
elif player == 2 and cpu == 1:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você venceu!")
elif player == 3 and cpu == 2:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Você venceu!")
else:
    print(f"Você escolheu {playerPlay}, o computador escolheu {cpuPlay}. Empate.")



