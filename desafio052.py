num = int(input("Informe um número: "))
if num <= 1:
    print(f"{num} não é um número primo.")
elif num <= 3:
     print(f"{num} é um número primo.")
elif num % 2 == 0 or num % 3 == 0:
    print(f"{num} Não é um numero primo.")
else:
    primo = True
    for c in range(5, int(num ** 0.5) + 1, 2):
        if num % c == 0:
            primo = False
            print(f"O número {num} não é primo.")
            break
    if primo:
            print(f"O número {num} é primo.")
    else:
         print(f"O numero {num} não é primo.")