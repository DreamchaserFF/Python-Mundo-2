cont = 0
num = int(input("Informe um número: "))
proximo = num - 1
cont = proximo
fatorial = num * proximo
print(f"{num}! = {num}x{proximo}", end="")
while cont != 1:
    proximo = proximo - 1
    cont = proximo
    print(f"x{proximo}", end="")
    fatorial = fatorial * proximo
print(f"={fatorial}")   
