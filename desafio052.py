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

'''num = int(input("Informe um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print(f'O numero {num}, foi divisível {total} vezes.')
if total == 2:
    print(f"E por isso ele é primo.")
else:
    print(f"E por isso ele não é primo.")'''