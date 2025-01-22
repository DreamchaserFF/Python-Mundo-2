num = int(input("Informe um número: "))
if num % 2 == 0 or num % 3 == 0:
    print(f"{num} não é um número primo.")
elif num <= 1:
    print(f"{num} não é um número primo.")
elif num <= 3:
    print(f"{num} não é um número primo.")
else:
    for c in range(num - 1, 1, -1):
        if num % c == 0:
            
        print(f"O número {num} não é primo.")
        exit()
        else:
            print(f"O número {num} é primo.")
            exit()