total = 0
cont = 0
nome = ""
maisBarato = ""
menorValor = 0
print("-" * 30)
print("LOJA SUPER BARATÃO")
print("-" * 30)
nome = str(input("Nome do produto: "))
valor = int(input("Preço: R$"))
menorValor = valor
maisBarato = nome
if valor >= 1000:
    cont += 1
total += valor
continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
while continuar != "N":
    while True:
        nome = str(input("Nome do produto: "))
        valor = int(input("Preço: R$"))
        if valor < menorValor:
            maisBarato = nome
        if valor >= 1000:
            cont += 1
        total += valor
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
        if continuar == "N":
            break
print(f"O produto de menor valor é {maisBarato}")
print(f"Foram comprados {cont} produtos de mais de R$1000,00")
print(f"O total da compra é R${total}")