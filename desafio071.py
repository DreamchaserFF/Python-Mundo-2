'''print("=" * 30)
print("CAIXA ELETRONICO")
print("=" * 30)

aSacar = 0
controle = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while True:
    aSacar = int(input("Que valor você quer sacar? R$"))
    while aSacar >= 50:
        controle = aSacar - 50
        aSacar = controle
        nota50 += 1
        if aSacar < 50:
            break
    if nota50 > 0:
        print(f"{nota50} notas de R$50")
    while aSacar >= 20:
        controle = aSacar - 20
        aSacar = controle
        nota20 += 1
        if aSacar < 20:
            break
    if nota20 > 0:
        print(f"{nota20} notas de R$20")
    while aSacar >= 10:
        controle = aSacar - 10
        aSacar = controle
        nota10 += 1
        if aSacar < 10:
            break
    if nota10 > 0:
        print(f"{nota10} notas de R$10")
    while aSacar >= 1:
        controle = aSacar - 1
        aSacar = controle
        nota1 += 1
        if aSacar < 1:
            break
    if nota1 > 0:
        print(f"{nota1} notas de R$1")
    break

print("=" * 30)
print("Volte Sempre ao nosso banco.")'''

print("=" * 30)
print("CAIXA ELETRONICO")
print("=" * 30)

valor = int(input("Qual valor quer sacar? R$"))
total = valor
cedula = 50
numCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        numCedula += 1
    else:
        if numCedula > 0:
            print(f"Total de {numCedula} cedulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        numCedula = 0

        if total == 0:
            break
