somaIdade = 0
idadeM = 0
senior = ""
mulheres = 0
for pessoa in range(1, 5):
    print(f"{pessoa}ª pessoa:")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    if pessoa == 1 and sexo in "Mm":
        idadeM = idade
        senior = nome
    if sexo in "Mn" and idadeM < idade:
        idadeM = idade
        senior = nome
    if sexo in "Ff" and idade < 20:
        mulheres += 1
    somaIdade += idade
mediaIdade = somaIdade / 4
print(f"A média das idades é {mediaIdade}")
print(f"Temos {mulheres} mulheres com menos de 20 anos.")
print(f"O homem mais velho é {senior} com {idadeM} anos.")