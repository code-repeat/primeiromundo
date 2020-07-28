nome_completo = input('Digite seu nome completo: ')
print('TODAS AS LETRAS MAIÚSCULAS: {}'.format(nome_completo.upper()))
print()

print('TODAS AS LETRAS MINÚSCULAS: {}'.format(nome_completo.lower()))
print()

dividir_nome = nome_completo.split()
juntar_nome = ''.join(dividir_nome)

print('QUANTIDADE DE LETRAS: {}'.format(len(juntar_nome)))
print('QUANTIDADE DE LETRAS DO PRIMEIRO NOME: {}'.format(len(dividir_nome[0])))
