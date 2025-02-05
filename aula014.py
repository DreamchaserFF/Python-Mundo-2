'''for c in range(1, 10):
    print(c)
print(f"Fim")'''

'''c = 1
while c < 10:
    print(c)
    c += 1
print(f"Fim")'''

'''r = "S"
while r == "S":
    n = int(input(f"Digite um valor: "))
    r = str(input(f"Quer continuar? [S/N]: ")).upper()
print("Fim")'''

n = 1
par = 0
impar = 0
while n != 0:
    n = int(input(f"Digite um numero: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Houveram {par} números pares.")
print(f"Houveram {impar} números impares.")
print("Fim")
