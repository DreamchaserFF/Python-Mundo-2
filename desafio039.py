ano = int(input("Informe o ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    tempo = 18 - idade
    if tempo == 1:
        print(f"O recruta precisará se alistar daqui a {tempo} ano.")
    else:
        print(f"O recruta precisará se alistar daqui a {tempo} anos.")
elif idade > 18:
    tempo = idade - 18
    if tempo == 1:
        print(f"O recruta deveria ter se alistado a {tempo} ano.")
    else:
        print(f"O recruta deveria ter se alistado a {tempo} anos.")
else:
    print(f"O recruta precisa se alistar esse ano.")