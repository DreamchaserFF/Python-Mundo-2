nasc = []
for i in range(1, 7+1):
    ano = int(input(f"Informe o ano de nascimento da {i}° pessoa: "))
    idade = 2025 - ano
    nasc.append(idade)
for i in range(7):
    if nasc[i] >= 21:
        print(f"A pessoa {i + 1} tem {nasc[i]} anos e é maior de idade")
    else:
        print(f"A pessoa {i + 1} tem {nasc[i]} anos e é menor de idade.")
