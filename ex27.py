nome = str(input('Digite seu nome completo: ')).strip()
separar_nome = nome.split()
print('Seu primeiro nome é: {}'.format(separar_nome[0]))
print('Seu último nome é: {}'.format(separar_nome[-1]))