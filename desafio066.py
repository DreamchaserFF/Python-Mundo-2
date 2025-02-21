soma = 0
cont = 0
while True:
    num = int(input("informe um outro número: [999 para sair] "))
    if num == 999:
        break
    soma += num
    cont +=1
print(f"Foram digitados {cont} números e a soma dos números informados foi: {soma}")
print("Fim")