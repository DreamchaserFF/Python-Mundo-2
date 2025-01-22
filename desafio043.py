peso = float(input("Informe o seu peso em Kg: "))
altura = float(input("Informe a sua altura em m: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Seu imc é de {imc:.2f}, você está abaixo do peso.")
elif imc < 25:
    print(f"Seu imc é de {imc:.2f}, você está com o peso ideal.")
elif imc < 30:
    print(f"Seu imc é de {imc:.2f}, você está sobrepeso.")
elif imc < 40:
    print(f"Seu imc é de {imc:.2f}. Você está obeso.")
else:
    print(f"Seu imc é de {imc:.2f}. Você está morbidamente obeso.")
