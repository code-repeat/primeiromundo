salario_atual = float(input('Informe seu salário atual: '))
tax_acre = 15

novo_salario = salario_atual + (salario_atual * tax_acre / 100)
print(f"Seu salário com acréscimo de {tax_acre}$ é de R${novo_salario}")

