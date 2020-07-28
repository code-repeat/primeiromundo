salario = float(input('Digite seu salário: '))
aumento_10 = (salario * 10 / 100) + salario
aumento_15 = (salario * 15 / 100) + salario

if salario < 1250:
    print('Seu salário atual é ............R${}'.format(salario))
    print('Salário com aumento de 15% ..........{:.2f}'.format(aumento_15))

else:
    print('Seu salário atual é ............R${}'.format(salario))
    print('Salário com aumento de 10% ..........{:.2f}'.format(aumento_10))