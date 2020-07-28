numero = input('Digite um número entre 0 a 999: ')
separar_digitos = numero.split()
tamanho_digitos = (len(''.join(separar_digitos)))

if tamanho_digitos == 1:
    print('UNIDADE: {}'.format(separar_digitos[0]))
elif tamanho_digitos == 2:
    print('UNIDADE: {}'.format(separar_digitos[0][1]))
    print('DEZENA: {}'.format(separar_digitos[0][0]))
elif tamanho_digitos == 3:
    print('UNIDADE: {}'.format(separar_digitos[0][2]))
    print('DEZENA: {}'.format(separar_digitos[0][1]))
    print('CENTENA: {}'.format(separar_digitos[0][0]))
else:
    print('UNIDADE: {}'.format(separar_digitos[0][3]))
    print('DEZENA: {}'.format(separar_digitos[0][2]))
    print('CENTENA: {}'.format(separar_digitos[0][1]))
    print('MILHAR: {}'.format(separar_digitos[0][0]))