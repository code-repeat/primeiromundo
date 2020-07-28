r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segundaa reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com as medidas {}, {} e {} é possível criar um retângulo'.format(r1, r2, r3))
else:
    print('Não foi possível criar um triângulo')
