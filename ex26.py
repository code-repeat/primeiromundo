frase = str(input('Digite uma frase: ')).upper().strip()
if 'A' not in frase:
    print('Não foi encontrado a letra A na sua frase')
else:
    print('A letra  A aparece: {} vezes'.format(frase.count('A')))
    print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
    print('A posição em que a letra A aparece pela ultima vez é {}'.format(frase.rfind('A')+1))
