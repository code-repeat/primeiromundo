velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO')
    calc_multa = (velocidade - 80) * 7
    print('valor da multa............R${}'.format(calc_multa))
else:
    print('Continue dirigindo com atenção.')