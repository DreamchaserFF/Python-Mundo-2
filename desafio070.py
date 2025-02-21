total = 0
cont = 0
nome = ""
maisBarato = ""
menorValor = 0
maisDeMil = 0

print("-" * 30)
print("LOJA SUPER BARATÃO")
print("-" * 30)

while True:
    nome = str(input("Nome do produto: "))
    cont += 1
    valor = int(input("Preço: R$"))
    if cont == 1:
        menorValor = valor
        maisBarato = nome
    if valor < menorValor:
        maisBarato = nome
    if valor >= 1000:
        maisDeMil += 1
    total += valor
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if continuar == "N":
        break
    
print(f"O produto de menor valor é {maisBarato}")
print(f"Foram comprados {maisDeMil} produtos de mais de R$1000,00")
print(f"O total da compra é R${total}")