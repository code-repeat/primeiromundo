distancia = float(input('Distância em km: '))
calc1 = distancia * 0.50
calc2 = distancia * 0.45

if distancia <= 200:
    print('Distância percorrida: {}km'.format(distancia))
    print('Preço a pagar: RS{:.2f}'.format(calc1))
else:
    print('Distância percorrida: {}km'.format(distancia))
    print('Preço a pagar: R${:.2f}'.format(calc2))