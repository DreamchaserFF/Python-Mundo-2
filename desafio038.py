num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
if num1 > num2:
    print(f"O primeiro valor é maior.")
elif num1 < num2:
    print(f"O segundo valor é maior.")
else:
    print(f"Não existe valor maior, os dois são iguais.")