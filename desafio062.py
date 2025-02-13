print("Gerador de PA")
print("-=" * 20)
pTermo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
cont = 1
total = 0
novo = 10
while novo != 0:
    total += novo
    while cont <= total:
        print(f"{pTermo} -> ", end="")
        pTermo += razao
        cont += 1
    print("Pausa")
    novo = int(input("Deseja exibir mais quantos termos? "))
print("Fim")