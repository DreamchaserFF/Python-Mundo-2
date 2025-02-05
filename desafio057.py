sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input(f"Informe um sexo: [M/F]: ")).upper()
    if sexo != "F" and sexo != "M":
        print("Opção invalida.")
print("Obrigado")