#CONTAGEM REGRESSIVA
'''from time import sleep
for control in range(10,0,-1):
    print(control)
    sleep(1)
print("Ignição.")'''

#CONTAGEM DETERMINADA POR USUARIO
'''i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
for control in range(i, f+1, p):
    print(control)
print("Fim")'''

soma = 0
for c in range(0,4):
    num = int(input("Digite um valor: "))
    soma += num
print(f"O somatório dos valores é: {soma}")
