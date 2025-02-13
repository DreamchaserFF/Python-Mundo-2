print("Gerador de PA")
print("-=" * 20)
pTermo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
cont = 1
while cont <= 10:
    print(f"{pTermo} -> ", end="")
    pTermo += razao
    cont += 1
print("fim")