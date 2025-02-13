print("TABUADA")
print("-=" * 10)
while True:
    cont = 1
    num = int(input("Deseja a tabuada de qual número? (Número < 0 para sair.) "))
    if num < 0:
        break
    while cont <= 10:
        print(f"{num} x {cont} = {num * cont}")
        cont += 1
    print("-=" * 10)
print("-=" * 10)
print("Programa tabuada encerrado.")