num = soma = cont = 0
num999 = False
num = int(input("Informe um numero [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Informe um numero: "))
print("Numero 999 digitado.")
print(f"Foram digitados {cont} numeros. A soma dos números informados é {soma}")
