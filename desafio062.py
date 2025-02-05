pTermo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
cont = 0
adicionar = 0
while cont != 10:
    print(f"{pTermo}")
    pTermo += razao
    cont += 1
novo = int(input("Deseja mostrar mais quantos termos? "))
novo = cont + novo
while cont != novo:
    print(f"{pTermo}")
    pTermo += razao
    cont += 1
print(f"Fim")