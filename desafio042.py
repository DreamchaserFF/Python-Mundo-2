linha1 = float(input("Informe o cumprimento da primeira linha: "))
linha2 = float(input("Informe o cumprimento da segunda linha: "))
linha3 = float(input("Informe o cumprimento da terceira linha: "))
if (linha2 + linha3) > linha1 and (linha1 + linha3) > linha2 and (linha1 + linha2) > linha3:
    print("As três linhas formam um triangulo.")
    if linha1 == linha2 and linha2 == linha3:
        print(f"Triângulo equilátero.")
    elif linha1 == linha2 or linha1 == linha3 or linha2 == linha3:
        print(f"Triângulo isósceles.")
    else:
        print(f"Triângulo escaleno.")
else:
    print("As três linhas não formam um triangulo.")