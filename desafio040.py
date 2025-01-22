nota1 = float(input("Informe a primeira nota de 0 a 10. "))
nota2 = float(input("Informe a segunda nota de 0 a 10. "))
media = (nota1 + nota2) / 2
if 0 > nota1 > 10 or 0 > nota2 > 10:
    print("Informe notas entre 0 e 10.")
else:
    if media < 5.0:
        print(f"Sua média foi de {media}. Reprovado.")
    elif 5.0 < media < 6.9:
        print(f"Sua média foi de {media}. Recuperação.")
    else:
        print(f"Sua média foi de {media}. Aprovado.")