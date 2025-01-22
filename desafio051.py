pTermo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
nTermo = (pTermo + (10) * razao)
for c in range(pTermo,nTermo,razao):
    print(f"{c}")
