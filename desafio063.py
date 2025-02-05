num = int(input("Informe um numero: "))
num1 = 0
num2 = 1
cont = 0
print(f"{num1}", end="")
while cont < num:
    print(f"->{num2}", end="")
    num1, num2 = num2, num1 + num2 #tem que atualizar os dois numeros ao mesmo tempo
    cont += 1
print(" fim")