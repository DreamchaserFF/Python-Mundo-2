maior18 = 0
homens = 0
mulheres = 0
mocas = 0
sexo = ""
while True:
    print("-" * 30)
    print("   CADASTRE UMA PESSOA   ")
    print("-" * 30)
    idade = int(input("Idade: "))
    if idade >= 18:
        maior18 += 1
    sexo = str(input("Sexo: [M/F] ")).strip().upper()
    while sexo != "M" and sexo != "F":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade <= 20:
        mocas += 1
    escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while escolha != "N" and escolha != "S":
        print("Escolha inválida.")
        escolha = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if escolha == "N":
            break
    if escolha == "N":
        break
print(f"Foram informadas {maior18} pessoas com maiores de 18 anos.")
print(f"Foram cadastrados {homens} homens.")
print(f"Foram cadastradas {mocas} mulheres com menos de 20 anos.")