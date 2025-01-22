casa = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos = int(input("Em quantos anos fará o pagamento? "))
prestacao = (casa / anos) / 12
corte = (salario / 100) * 30
if prestacao > corte:
    print(f"A prestação será de R${prestacao}, que é mais de 30% de seu \
salario, que é R${corte}. Emprestimo negado.")
else:
    print(f"A prestação será de R${prestacao}, que é menos de 30% do seu \
salario, que é R${corte}. Emprestimo aprovado.")