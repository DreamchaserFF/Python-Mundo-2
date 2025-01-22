ano = int(input("Informe o ano de nascimento do atleta. "))
idade = 2024 - ano
if idade <= 9:
    print(f"O atleta tem {idade} anos. Atleta mirim.")
elif idade <= 14:
    print(f"O atleta tem {idade} anos. Atleta infantil.")
elif idade <= 19:
    print(f"O atleta tem {idade} anos. Atleta junior.")
elif idade <= 20:
    print(f"O atleta tem {idade} anos. Atleta sênior")
else:
    print(f"O atleta tem {idade} anos. Atleta master.")