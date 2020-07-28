from math import hypot

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjancente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(cateto_oposto, cateto_adjancente)
print('Valor da hipotenusa: {:.2f}'.format(hipotenusa))

#  hi = (cateto_oposto **  + cateto_adjacente ** 2) ** (1/2)
#  ** (1/2) retorna a raíz quadrada
